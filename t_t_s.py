
"""
Create a simple text to speech program
@author: Reyhaneh :)

"""

#import nessecery modules
from tkinter import *
import pyttsx3

#create a window
root=Tk()

#set a title for window
root.title("Test_to_speech")

#set the size of the main window
root.geometry("485x225")

#set the smallest size of window

root.maxsize(485,225)

#set the biggest size of window

root.minsize(485,225)

#background color for the main window 
root.config(bg="#99042e")

#make a frame
main_Frame= LabelFrame(root)
#put the frame on the screen
main_Frame.grid(row=0, column=0 , padx = 25 , pady= 25 , ipady=40)

#make a variable 
Text=StringVar()

#make an Input box and set the input into variable
your_text=Entry(main_Frame ,width=38 , textvariable=Text ,bd=3 ,  font ="Calibri 10" ,fg="#99042e")

#put the input box on the screen
your_text.grid(column=0 , row=0 , pady=(40,0) , padx=(10,0) , ipady=10 )

#text to speeech function
def t_t_s():
    global Text
    
    #intilize pyttsx3 properties into the variable
    engine=pyttsx3.init()
    
    #set the rate of the voice
    engine.setProperty('rate', 125) 
    
    #set the voice volume to 1 between 0 and 1 
    engine.setProperty('volume',1.0)
    
    #convert the voice to an mp3 file with the name test
    engine.save_to_file(Text.get(), 'test.mp3')
    
    #get the input and say that 
    engine.say(Text.get())
    
    #play the sound one time and then stop
    engine.runAndWait()
    
#make a button and bind it to t_t_s function    
but=Button(main_Frame ,text="text to speech" , command=t_t_s , font ="Calibri 15 bold" , fg="#ffffff", bg="#99042e" )

#put the button on the screen 
but.grid(column=1 , row=0 , pady=(40,0) , padx=(0,10))


#run and show the gui window 
root.mainloop()
