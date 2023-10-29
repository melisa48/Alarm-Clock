import datetime
import time
import winsound

def convert_to_24_hour_format(time_str):
    time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
    return time_obj.strftime("%H:%M:%S")

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            winsound.Beep(1000, 2000)
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time_input = input("Enter the time for the alarm (HH:MM AM/PM format): ")
    alarm_time_24_hour = convert_to_24_hour_format(alarm_time_input)
    set_alarm(alarm_time_24_hour)
