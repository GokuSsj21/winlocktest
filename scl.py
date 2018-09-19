import pyHook
import pythoncom
import win32api
import pymouse
import sys
import os
import winsound
from win32api import GetSystemMetrics
import subprocess
import win32console
import win32gui

print """
=======================================================
|| Program by Ashutosh Tyagi ashutyagi2107@gmail.com ||
=======================================================
"""
f1=open("syslog.log","r")
readf1= f1.readline()
f1.close()
cwd = os.getcwd()
if readf1 == "":
    f2=open("syslog.log","w")
    ps= raw_input("Type Your Password : ")
    f2.write(ps)
    f2.close()
    #dis= raw_input("Add this program to system startup (Y/N)")
    #if dis == "Y" or "y":
        #key ="HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
        #nam = cwd+"\scl.exe"
        #os.system("reg add "+ key +" /v Test /t REG_EXPAND_SZ /d " + nam +" /f")
    print "\n \nYour Password has been saved "
    print "Now you can open this application to Lock your Screen"
    print "\n \n \n          PRESS ENTER "
    zla= input("")
    exit()


password= readf1

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)


res = subprocess.check_output(['tasklist'])


az=GetSystemMetrics(0)/3
bz= GetSystemMetrics(1)/2


pathskin = "start "+cwd+"\skin\\imgflow.exe"
os.system(pathskin)



data = ""
def onclick(event):
    global data
    global password
    global res
    mouse = pymouse.PyMouse()
    a= mouse.position()
    a1= int(a[0])
    a2= int(a[1])
    if 0 < a1 < az and 0 < a2 < bz:
        data=data + "1"
    if az < a1 < (2*az) and 0 < a2 < bz:
        data=data + "2"
    if (2*az) < a1 < (3*az) and 0 < a2 < bz:
        data=data + "3"
    if 0 < a1 < az and bz < a2 < (2*bz):
        data=data + "4"
    if az < a1 < (2*az) and bz < a2 < (2*bz):
        data=data + "5"
    if (2*az) < a1 < (3*az) and bz < a2 < (2*bz):
        data=data + "6"
        
    if data == password:
        print " PC unlocked now "
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        os.system('Taskkill /IM imgflow.exe /F')
        exit()
        return True
    
    if "taskmgr.exe" in res:
        os.system('Taskkill /IM taskmgr.exe /F')
        
    if len(password)== len(data):
        print " Wrong "
        data = ""
        Freq = 2500 # Set Frequency To 2500 Hertz
        Dur = 1000 # Set Duration To 1000 ms == 1 second
        winsound.Beep(Freq,Dur)
    return False



hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.KeyAll = onclick
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()
hm.UnhookMouse()
hm.UnhookKeyboard()



