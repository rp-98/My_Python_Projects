import  time
import  winsound
from win10toast import  ToastNotifier
def timer(message, minutes):
    #window notification
    notificator=ToastNotifier()
    #notification details
    notificator.show_toast("Alarm",f"Alarm will go off in {minutes}",duration=50)
    time.sleep(minutes*60) # pause
    winsound.Beep(frequency=2500,duration=1000) #alarm sound
    notificator.show_toast(f"Alarm",message,duration=50)
if __name__=='__main__':
    message='Hi ravi'
    minutes=1
    timer(message,minutes)
