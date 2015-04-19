from flask import Flask, render_template, request, redirect, url_for
import time
import re
from random import randint
import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
#print voice
#engine.setProperty('gender', 'male')
# for voice in voices:
#     if voice.gender == "male":
#         engine.setProperty('voice', voice.id)
#         print "yes!"
#         break
engine.setProperty('voice',u'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
engine.say("Yeahyeah! First of all, this folly is gorgeous, well, my answer to your question is autocatalysis")

# engine.runAndWait()
# # for voice in voices:
# # 	print voice.gender
# #engine = pyttsx.init()
for voice in voices:
	#voices = engine.getProperty('voices')
	engine.setProperty('voice', voice.id)
	print voice.id
# 	engine.say("this folly is gorgeous")
engine.runAndWait()
	