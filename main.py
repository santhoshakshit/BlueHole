import os
from subprocess import call
import eel
from engine.features import *
from engine.Translator import *
from engine.command import *

eel.init("www")

subprocess.call([r'device.bat'])
playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True ) 

            