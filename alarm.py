from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
import datetime
import time
import sys
import geocoder


def alarm(set_alarm):#the alarm will ring when the value of the loop matches with the user inputed value
    toast=ToastNotifier()
    while True:#an infinite loop is being run here
        time.sleep(1)#increase time by 1 second
        date=datetime.datetime.now()#gives current time
        now=date.strftime("%H:%M:%S")#gives current time in hour minute and second format)
        print(now)
        if now==set_alarm:#statement to check when now matches user inputed value
            print("Alarm Clock")
            toast.show_toast("Alarm Clock",duration=1)#duration of alarm
            playsound("freedompp.mp3")#deciding which mp3 to play
            sys.exit()

def getvalue():
    set_alarm=f"{hour.get()}:{min.get()}:{sec.get()}"#to get hour,min,sec values
   
    alarm(set_alarm)#calling alarm function



def getexit():# to exit the program
     sys.exit()

def getTime():
    rootE=Tk()
    rootE.geometry("250x150")
     
    def destroy_widget():
            rootE.destroy()
    submit4=Button(rootE,text="Destroy",bg="honeydew",width=15,command=destroy_widget).place(x=0,y=120) 
    label=Label(rootE,font=("Courier",30,"bold"),bg="turquoise",fg="white",bd=30)
    label.place(x=0,y=0)
    
    
    def digitalclock():
        text_input=time.strftime("%H:%M:%S")
        label.config(text=text_input)
        label.after(200,digitalclock)
    digitalclock()   
    rootE.mainloop()
  
root=Tk()
root.title("ALARM CLOCK")
root.geometry("300x350")#widget size
info=Label(root,text="Rise And Shine").place(x=60)#packs the text in the xth coardinate
set_time=Label(root,text="Set Time User",relief="solid",font=("Cambria",10,"bold")).place(x=2,y=30)#<font=(family,size,weight,slant,underline,overstrike)
hour=StringVar()
min=StringVar()
sec=StringVar()
def location_calc():
    g=geocoder.ip('me')
   
    set_city=Label(root,text=g.city,relief="solid",font=("Times",15,"bold"),bg="cyan").place(x=50,y=200)
    set_city=Label(root,text=g.country,relief="solid",font=("Times",15,"bold"),bg="cyan").place(x=50,y=230)


hour_E=Entry(root,textvariable=hour,bg="honeydew",width=4).place(x=92,y=30)
min_E=Entry(root,textvariable=min,bg="honeydew2",width=4).place(x=122,y=30)
sec_E=Entry(root,textvariable=sec,bg="azure2",width=4).place(x=152,y=30)
submit=Button(root,text="Set Alarm",bg="linen",width=10,command=getvalue).place(x=50,y=70)
submit1=Button(root,text="Exit program",bg="khaki1", width=15,command=getexit).place(x=40,y=120)
submit2=Button(root,text="Location",bg="honeydew",width=15,command=location_calc).place(x=40,y=170)
submit3=Button(root,text="TIME",bg="honeydew",width=15,command=getTime).place(x=40,y=260)



root.mainloop()


