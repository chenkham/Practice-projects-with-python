import time
from playsound import playsound

Green = "\033[92m"
Reset = "\033[0m"

take_time=int(input("Enter the time in seconds:\n"))
for x in range(take_time,0,-1):
    time_seconds=x % 60
    time_minutes=int(x / 60) % 60
    time_hours=int(x / 3600)
    timer_display=f"{Green}{time_hours:02}:{time_minutes:02}:{time_seconds:02}{Reset}"
    print(f"\r{timer_display}", end='', flush=True)
    time.sleep(1)
print("\ntimes up!")
playsound("beep.mp3")
