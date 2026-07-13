'''
Created on Apr 16, 2026

@author: admin
'''
import re
import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# File path
file_path = "69543.TXT"

students = []

# ---------------------------
# 📥 PARSE FILE
# ---------------------------
with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()

    match = re.match(r"(\d{8})\s+[MF]\s+([A-Z\s]+?)\s+.*\s+(PASS|ABST)", line)

    if match:
        roll = match.group(1)
        name = match.group(2).strip()
        result = match.group(3)

        marks_line = lines[i + 1].strip()
        marks_raw = marks_line.split()

        marks = []
        for m in marks_raw:
            if m == "AB":
                marks.append(0)
            else:
                try:
                    marks.append(int(m))
                except:
                    pass

        # Ensure exactly 6 subjects
        while len(marks) < 6:
            marks.append(0)

        total = sum(marks)
        percentage = round(total / 6, 2)

        students.append({
            "Roll": roll,
            "Name": name,
            "Result": result,
            "Sub1": marks[0],
            "Sub2": marks[1],
            "Sub3": marks[2],
            "Sub4": marks[3],
            "Sub5": marks[4],
            "Sub6": marks[5],
            "Total": total,
            "Percentage": percentage
        })

        i += 2
    else:
        i += 1

df = pd.DataFrame(students)

# ---------------------------
# 📊 ANALYSIS
# ---------------------------
topper = df.sort_values(by="Percentage", ascending=False).head(5)

subject_toppers = {}
for sub in ["Sub1", "Sub2", "Sub3", "Sub4", "Sub5", "Sub6"]:
    top = df.loc[df[sub].idxmax()]
    subject_toppers[sub] = (top["Name"], top[sub])

# Stats
total_students = len(df)
passed = len(df[df["Result"] == "PASS"])
absent = len(df[df["Result"] == "ABST"])
avg_percentage = df["Percentage"].mean()

# ---------------------------
# 🎨 TKINTER GUI
# ---------------------------
root = tk.Tk()
root.title("CBSE Result Dashboard")
root.geometry("900x600")

title = tk.Label(root, text="CBSE Class X Result Dashboard", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Summary Frame
frame_summary = tk.Frame(root)
frame_summary.pack(pady=10)

tk.Label(frame_summary, text=f"Total Students: {total_students}", font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Label(frame_summary, text=f"Passed: {passed}", font=("Arial", 12)).grid(row=0, column=1, padx=10)
tk.Label(frame_summary, text=f"Absent: {absent}", font=("Arial", 12)).grid(row=0, column=2, padx=10)
tk.Label(frame_summary, text=f"Average %: {round(avg_percentage,2)}", font=("Arial", 12)).grid(row=0, column=3, padx=10)

# Topper Table
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

cols = ("Roll", "Name", "Percentage")
tree = ttk.Treeview(frame_table, columns=cols, show='headings')

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=150)

for _, row in topper.iterrows():
    tree.insert("", tk.END, values=(row["Roll"], row["Name"], row["Percentage"]))

tree.pack()

# Subject Toppers
frame_sub = tk.Frame(root)
frame_sub.pack(pady=10)

tk.Label(frame_sub, text="Subject-wise Toppers", font=("Arial", 14, "bold")).pack()

for sub, data in subject_toppers.items():
    tk.Label(frame_sub, text=f"{sub}: {data[0]} ({data[1]} marks)").pack()

# ---------------------------
# 📈 CHART FUNCTION
# ---------------------------
def show_chart():
    plt.figure()
    df["Percentage"].plot(kind='hist', bins=10)
    plt.title("Percentage Distribution")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.show()

btn_chart = tk.Button(root, text="Show Performance Chart", command=show_chart)
btn_chart.pack(pady=10)

# ---------------------------
# 💾 SAVE CSV BUTTON
# ---------------------------
def save_csv():
    df.to_csv("cbse_result_analysis.csv", index=False)
    tk.Label(root, text="Saved CSV successfully!", fg="green").pack()

btn_save = tk.Button(root, text="Save CSV", command=save_csv)
btn_save.pack()

root.mainloop()