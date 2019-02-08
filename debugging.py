import kivy

from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from random import getrandbits

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')

class MainPanel(GridLayout):
    def __init__(self, **kwargs):

        super(MainPanel, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 6
        

        self.add_widget(Label(text="BUG #1"))

        self.bug1 = Switch(active=False)
        self.add_widget(self.bug1)

        self.add_widget(Label(text="BUG #2"))

        self.bug2 = Switch(active=False)
        self.add_widget(self.bug2)   

        self.add_widget(Label(text="BUG #3"))

        self.bug3 = Switch(active=True)
        self.add_widget(self.bug3)   

        self.add_widget(Label(text="BUG #4"))

        self.bug4 = Switch(active=False)
        self.add_widget(self.bug4)   

        self.add_widget(Label(text="BUG #5"))

        self.bug5 = Switch(active=False)
        self.add_widget(self.bug5)   

        self.add_widget(Label(text="BUG #6"))

        self.bug6 = Switch(active=False)
        self.add_widget(self.bug6)  
          
                
        def switch1_callback(switchObject, switchValue):
        
            choice = bool(getrandbits(1))
            if choice == 1:
                self.bug3.active = bool(getrandbits(1))
                self.bug4.active = bool(getrandbits(1))
            else:
            
                self.bug4.active = bool(getrandbits(1))
                self.bug5.active = bool(getrandbits(1))
                self.bug6.active = bool(getrandbits(1))
                
                
        def switch2_callback(switchObject, switchValue):
        
            self.bug4.active = bool(getrandbits(1))
            self.bug5.active = bool(getrandbits(1))

                   
        def switch3_callback(switchObject, switchValue):
            
            self.bug1.active = bool(getrandbits(1))

                   
        def switch4_callback(switchObject, switchValue):
        
            self.bug5.active = bool(getrandbits(1))

                
        def switch5_callback(switchObject, switchValue):
        
            self.bug3.active = bool(getrandbits(1))
                
        def switch6_callback(switchObject, switchValue):
            
            self.bug2.active = bool(getrandbits(1))
                
                              
        self.bug1.bind(active=switch1_callback)
        self.bug2.bind(active=switch2_callback)
        self.bug3.bind(active=switch3_callback)
        self.bug4.bind(active=switch4_callback)
        self.bug5.bind(active=switch5_callback)
        self.bug6.bind(active=switch6_callback)        


          
class MainApplication(App):
    def build(self):
        return MainPanel()

if __name__ == '__main__':

     MainApplication().run()
