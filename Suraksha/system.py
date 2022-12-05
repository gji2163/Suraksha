from win32process import GetWindowThreadProcessId
from psutil import Process
from win32gui import GetWindowText, GetForegroundWindow
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from datetime import datetime
from os import system,listdir
from os.path import basename,dirname
from sys import executable

cred = credentials.Certificate('SysLock.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://remote-f2ce1-default-rtdb.firebaseio.com/'
    }
)

while True:
    fg = GetForegroundWindow()
    x = GetWindowText(fg)
    main = db.reference('/SysLock/')
    with open(dirname(executable)+'\\DeviceId.txt') as f:
        ref = main.child(f.read())
        f.close()
    Curr = ref.get()['Curr']
    for i in main.get()['Blacklist']:
        if i in Curr[0]:
            system("taskkill /im "+Process(GetWindowThreadProcessId(fg)[-1]).name()+" /f")
            #p('audio.mp3')
            #system("shutdown \s \t 1")
            break
    if Curr[0]!=x:
        ref.update({
            Curr[1]+' to '+datetime.now().strftime("%d-%m-%Y %H:%M:%S"):Curr[0],
            'Curr':[x,datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
            })
    if ref.get()['vid']=="true":
        pass    
    sleep(5)


