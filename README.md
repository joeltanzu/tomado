# Tomado - A Pomodoro Timer
Tomado is a Pomodoro Timer written in Python, utilising Tkinter as its GUI. Tomado offers the option to track tasks, as well as the option to utilise custom timings in minute increments.

## Getting Started
Libraries utilised are all standard libraries. There is no requirement to download additional libraries to run the script. Any Python intepreter, regardless of OS platform, should be able to run Tomado. 

### Usage
Double click the script to run it. The GUI window should appear.

Starting any Pomodoro Timer causes the application to add a time delta to the current computer time, which the application uses to monitor if the target time has been reached. The application polls the computer at one second intervals, hence the margin of error is up to one second. The timer also checks for and prevents multiple timers from being set.

Stopping the Pomodoro Timer will reset the timer back to its original state. 

Custom time allows the user to input their own timings that they wish to utilise. The application will reject any non-integer inputs.

The focus input box allows the user to submit a focus statement as a rudimentary task tracker. After each Pomodoro or custom time session, the application will check with the user if the focus objectives have been met. If objectives are not met, the application will continue to track the number of attempts utilised to accomplish the task. If objectives are met, the number of attempts will be reset.

## Why this?
* It's a lightweight application that takes up minimal resources
* No internet connection required
* No user data tracked
* Source code is open source for you to edit and reference as necessary

## Authors
* Tan Zu Wei, Joel
