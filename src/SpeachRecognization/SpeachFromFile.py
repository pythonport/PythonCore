'''
Created on Feb 25, 2021

@author: admin
'''
import speech_recognition as sr

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    #audio = sr.