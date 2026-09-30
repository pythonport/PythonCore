import json
import os
from datetime import datetime

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineRightIconListItem, IconRightWidget
from kivymd.uix.pickers import MDTimePicker
from plyer import notification

# Global sound object reference
sound = None

KV = '''
MDBoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Automatic School Bell"
        right_action_items: [["plus", lambda x: app.show_time_picker()]]

    MDBoxLayout:
        orientation: 'vertical'
        padding: "16dp"
        spacing: "12dp"

        MDLabel:
            id: current_time_label
            text: "00:00:00"
            font_style: "H3"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: "Scheduled Bells"
            font_style: "Subtitle1"
            size_hint_y: None
            height: self.texture_size[1]

        ScrollView:
            MDList:
                id: schedule_list
'''

class BellApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.schedule_file = "bell_schedule.json"
        self.schedules = self.load_schedules()
        return Builder.load_string(KV)

    def on_start(self):
        # Update UI clock every 1 second
        Clock.schedule_interval(self.update_clock, 1)
        # Check if bell needs to ring every 1 second
        Clock.schedule_interval(self.check_bell_trigger, 1)
        self.refresh_list_ui()

    def update_clock(self, dt):
        now = datetime.now().strftime("%I:%M:%S %p")
        self.root.ids.current_time_label.text = now

    def check_bell_trigger(self, dt):
        now_time = datetime.now().strftime("%H:%M")
        now_seconds = datetime.now().second

        # Check at the start of the minute (second 00)
        if now_seconds == 0:
            for item in self.schedules:
                if item["time"] == now_time and item["enabled"]:
                    self.ring_bell(item["label"])

    def ring_bell(self, label):
        global sound
        print(f"🔔 [RINGING BELL]: {label}")

        # --- Platform Specific Audio Handling ---
        if platform == 'android':
            try:
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Context = autoclass('android.content.Context')
                AudioManager = autoclass('android.media.AudioManager')

                activity = PythonActivity.mActivity
                audio_manager = activity.getSystemService(Context.AUDIO_SERVICE)
                audio_manager.setMode(AudioManager.MODE_NORMAL)
                audio_manager.setSpeakerphoneOn(True)
                
                max_vol = audio_manager.getStreamMaxVolume(AudioManager.STREAM_MUSIC)
                audio_manager.setStreamVolume(AudioManager.STREAM_MUSIC, max_vol, 0)
            except Exception as e:
                print(f"Android Audio Manager Error: {e}")

        # --- Load & Play Audio ---
        if sound:
            sound.stop()
            
        sound = SoundLoader.load('bell_sound.mp3')
        if sound:
            sound.volume = 1.0
            sound.play()
        else:
            print("⚠️ Sound Error: 'bell_sound.mp3' not found in root folder.")

        # --- System Notification ---
        try:
            notification.notify(
                title="School Bell Alarm",
                message=f"Time for: {label}",
                app_name="School Bell App",
                timeout=5
            )
        except Exception as e:
            print(f"Notification error: {e}")

    # --- Schedule Storage & UI Management ---

    def load_schedules(self):
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, "r") as f:
                return json.load(f)
        return [
            {"time": "08:00", "label": "Morning Assembly", "enabled": True},
            {"time": "10:30", "label": "Recess Break", "enabled": True},
            {"time": "15:00", "label": "School Dismissal", "enabled": True}
        ]

    def save_schedules(self):
        with open(self.schedule_file, "w") as f:
            json.dump(self.schedules, f, indent=4)

    def refresh_list_ui(self):
        list_container = self.root.ids.schedule_list
        list_container.clear_widgets()

        for idx, item in enumerate(self.schedules):
            formatted_time = datetime.strptime(item["time"], "%H:%M").strftime("%I:%M %p")
            
            list_item = TwoLineRightIconListItem(
                text=formatted_time,
                secondary_text=item["label"]
            )
            
            trash_icon = IconRightWidget(
                icon="delete",
                on_release=lambda x, i=idx: self.delete_schedule(i)
            )
            list_item.add_widget(trash_icon)
            list_container.add_widget(list_item)

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_time_selected)
        time_dialog.open()

    def on_time_selected(self, instance, time_obj):
        time_str = time_obj.strftime("%H:%M")
        new_entry = {
            "time": time_str,
            "label": f"Period {len(self.schedules) + 1}",
            "enabled": True
        }
        self.schedules.append(new_entry)
        self.schedules.sort(key=lambda x: x["time"])
        self.save_schedules()
        self.refresh_list_ui()

    def delete_schedule(self, index):
        del self.schedules[index]
        self.save_schedules()
        self.refresh_list_ui()

if __name__ == "__main__":
    BellApp().run()