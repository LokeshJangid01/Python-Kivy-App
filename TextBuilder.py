from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from helper import user_helper
from helper import user_helper1



class DemoText(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        scr = Screen()
        btn_flate = MDRectangleFlatButton(text="Log in", pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                          on_release=self.fun)


        self.user_1 = Builder.load_string(user_helper)
        self.user_2 = Builder.load_string(user_helper1)
        scr.add_widget(self.user_1)
        scr.add_widget(self.user_2)
        scr.add_widget(btn_flate)
        return scr

    def on_start(self):
        self.fps_monitor_start()

    def fun(self,obj):
        print(self.user_1.text )
        print(self.user_2.text)
        try:

            f = open("data2.txt", "a")
            f.write(self.user_1.text)
            f.write("\n")
            f.write(self.user_2.text)
            f.close()
        except:
            print("oops mistake")

DemoText().run()