from datetime import datetime, timedelta
import tkinter, tkinter.messagebox
from tkinter import StringVar
import time
import threading

# Global variable to control Pomodoro Functions
status = 0
attempts = 0
objective = ""
breaktime = False

def main():
    # Define current time (currently no use, for future functionality use)
    ctime = datetime.now()
# Hardcoded wrappers for key Pomodoro timings
def pomoblock():
    global breaktime
    breaktime = False
    settimer(25, 0)
def breakblock():
    global breaktime
    breaktime = True
    settimer(5, 0)
def debugblock():
    global breaktime
    breaktime = False
    settimer(0, 10)
# Wrapper for custom timing
def customblock():
    # Get timing input by user
    time = entry.get()
    # Ensure that timing is a valid integer
    try:
        int(time)
    except ValueError:
        return
    # Convert string input to integer
    time = int(time)
    # Set timer
    settimer(time,0)
# Main function for setting timer
def settimer(m, s):
    # Utilises global status variable to check for previous alarms
    global status
    status += 1
    if status == 1:
        # Delta can take hours, minutes, seconds
        delta = timedelta(minutes=m, seconds=s)
        target = datetime.now() + delta
        # Format target into string
        targetf = target.strftime('%H:%M:%S')
        # Set GUI display labels
        displaydefault()
        displaytarget(targetf)
        # Multithreading to assign runtimer to separate thread, preventing main thread from locking up
        runtimerthread = threading.Thread(target=runtimer, args=[target])
        runtimerthread.start()
    else:
        displayerror()

def runtimer(target):
    # Continues polling current time in one second interval to check if alarm criteria met. Could set up differing intervals to further reduce CPU load in the future.
    global status
    global breaktime
    while datetime.now() < target:
        if status >= 1:
            time.sleep(1)
        else:
            displaydefault()
            break
    else:
        # Prompts user that time is up
        # use toast() if you want to show toast notifications on Windows 10 instead of a message box
        finmessagebox()
        if attempts > 0 and breaktime == False:
            objmessagebox()
        status = 0
        return

def stop():
    # Stop timer running through adjusting global status (runtimer constantly monitors global status)
    global status
    status = 0
    displayreset()

def customobj():
    # Get objective from user
    obj = tentry.get()
    # Draw out relevant global variables
    global objective
    global attempts
    # If objectives are the same
    if obj == objective:
        displayobjective()
    else:
        objective = obj
        attempts = 1
        displayobjective()

# GUI DESIGN COMMENCES BELOW
# Creates tkinter window
window = tkinter.Tk()
window.geometry("700x400")
window.title("Tomado - A Pomodoro Timer")

# Main Pomodoro Button creation
pomo_b = tkinter.Button(window, text="Start Pomodoro (25 mins)!", command=pomoblock, font=(None, 12))
break_b = tkinter.Button(window, text="Take a break (5 mins) :)", command=breakblock, font=(None, 12))
stop_b = tkinter.Button(window, text="Stop timer", command=stop, font=(None, 12))

# Custom Time Section
label = tkinter.Label(window, text="Input custom time in minutes:", font=(None, 12))
entry = tkinter.Entry(font=(None, 12))
customtime_b = tkinter.Button(window, text="Submit Custom Time", command=customblock, font=(None, 12))

# Required setup of string variables in order to amend labels
endtime = StringVar()
endtime.set(' ')
ttarget = tkinter.Label(window, textvariable = endtime, font=(None, 15))

statuslabel = StringVar()
statuslabel.set('Welcome to Tomado')
slabel = tkinter.Label(window, textvariable = statuslabel, font=(None, 20))

# Optional Target Section
tlabel = tkinter.Label(text="Do you have something you wish to focus on?", font=(None, 12))
tentry = tkinter.Entry(font=(None, 12))
customobj_b = tkinter.Button(window, text="Submit Focus Statement", command=customobj, font=(None, 12))
obj_string = StringVar()
obj_string.set(' ')
target_l = tkinter.Label(window, textvariable = obj_string, font=(None, 15))

# Pack items
# Welcome and status display
slabel.pack()
# Fixed Pomodoro section
pomo_b.pack()
break_b.pack()
stop_b.pack()
# Custom Pomodoro section
label.pack()
entry.pack()
customtime_b.pack()
# Custom Objectives section
tlabel.pack()
tentry.pack()
customobj_b.pack()
# Label display section
ttarget.pack()
# Objective display section
target_l.pack()

# Function calls to amend display labels
def displaytarget(targetf):
    endtime.set(f'Time to end is {targetf}')
def displayreset():
    endtime.set(' ')
def displaydefault():
    statuslabel.set('Welcome to Tomado')
def displayerror():
    statuslabel.set('Only one timer can run. You might want to stop the current timer.')
def displayobjective():
    global objective
    global attempts
    obj_string.set(f'Your objective is set as {objective}.\n This is your {attempts} attempt')
def blankobjective():
    obj_string.set(" ")

# Function calls to amend message boxes
def finmessagebox():
    tkinter.messagebox.showinfo("Timer complete", "You have completed your session!")
    displayreset()
def objmessagebox():
    global objective
    global attempts
    msg = tkinter.messagebox.askyesno(f"Objectives", f"Did you accomplish {objective}?")
    if msg == True:
        attempts = 0
        objective = ""
        blankobjective()
    else:
        attempts += 1
        displayobjective()

# Prevents tkinter window from closing
window.mainloop()

# Call to run main function
main()
