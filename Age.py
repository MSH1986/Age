
from gettext import find
from logging import PlaceHolder
from re import S
from tkinter import Place, font
import kivy
from pydoc import text
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import datetime
class Age(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #add widgets to window
        self.window.add_widget(Image(source="age-group.png"))

        #Label
        self.age = Label(
            text="Find out how old you are! \nEnter Your Birth Year Below:",
            font_size = 20,
            color= '#FFFFFF'
            )
        self.window.add_widget(self.age)

        #Input
        self.user = TextInput(
                    multiline=False,
                    font_size = (20),
                    padding_y = (20,20),
                    size_hint = (1,0.5)
                    )
                    
        self.window.add_widget(self.user)

        #Button
        self.button = Button(
            text="Your Age",
            size_hint=(.2, .5),
            bold = True,
            background_color = '#00FFCE'
            #background_normal = ""
            )
        
        self.button.bind (on_press = self.callback)
        self.window.add_widget(self.button)


        #Button Reset
        self.button = Button(
            text="Reset",
            size_hint=(.2, .5),
            bold = True,
            background_color = '#00FFCE'
        
        )
   
        self.button.bind (on_press = self.Reset)
        self.window.add_widget(self.button)
        


        return self.window

    def Reset(self, user):
        self.user.text = ''
        self.age.text="Find out how old you are! \nEnter Your Birth Year Below:"
    

    def callback(self, instance):        
        dy = self.user.text
        try:
            int_dy = int(dy)
            yearnow = datetime.datetime.now().year
            if int_dy < yearnow and int_dy >= 1980:
                Myage = yearnow-int_dy
                self.age.text = "Your Age is " + format(Myage) + " " + "Years Old" 
            else:
                self.age.text = "Please Enter a Number Between The Current Year and 1980"
        except:    
            self.age.text = "You did not enter a valid number"
            self.user.text = ''

if __name__ == "__main__":
    Age().run()
