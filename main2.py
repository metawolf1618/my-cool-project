from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class SoundPlayer(BoxLayout):

    def play_sound(self):
        sound = SoundLoader.load('tupac.mp3')
        if sound:
            sound.volume = 0.1
            sound.play()

class MyApp(App):
    def build(self):
        return  SoundPlayer() 


MyApp().run()                                                      
                                                   
       
        
    


