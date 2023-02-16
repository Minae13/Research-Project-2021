#import widgets used for app
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#initialising window object, creating a class

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1 #column num
        self.window.size_hint = (0.6, 0.7) #this adds margins so sides will be 40 % and top and bottom 30%
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5} #this sets the center 

        self.window.add_widget(Image(source="Yeet.jpg")) #image widget
        self.greeting = Label(
                        text="Cómo te llamas?", 
                        font_size = 18,
                        color = "#00FFCE",
                        ) #label widget and styling shit
        self.window.add_widget(self.greeting) #this adds the widget so if you don't write it the widget won't appear
        self.user = TextInput(
                        multiline=False,
                        padding_y = (20,20), #this makes it 20 x 20 p
                        size_hint = (1, 0.5), #this makes it slimmer #don't forget the ,
                        ) #this is so the input is not multiple lines
        self.window.add_widget(self.user)
        self.button = Button(
                        text="SALUDAR",
                        size_hint = (1,0.5),
                        bold = True,
                        background_color = "00FFCE",
                        #background_normal = "" #backgrounds are usually darker than the og colour this makes it lighter
                        ) 
        self.button.bind(on_press=self.callback) #this is so the button works
        self.window.add_widget(self.button)
        
        #add widgets to window
        return self.window
    
    #this is also so the button works
    def callback(self, instance):
        self.greeting.text = "Hola " + self.user.text + "!"
    
        

#runs the program as soon as the py file is executed
if __name__=="__main__":
    SayHello().run()