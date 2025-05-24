from datetime import datetime
from playsound import playsound

alarm=input("Enter alarm you want to set(hours/minute/seconds)in this form -:HHMMSS:\n")
alarm_hour=alarm[0:2]
alarm_minute=alarm[2:4]
alarm_second=alarm[4:6]
alarm_period=alarm[6:8].upper()

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period==current_period:
        if alarm_hour==current_hour:
            if alarm_minute==current_minute:
                if alarm_second==current_second:
                    print("wakey wakey!")
                    playsound("../count down timer/beep.mp3")
                    break