
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class MainWindow(Screen):
    pass

class SHSWindow(Screen):
    pass

class CollegeWindow(Screen):
    pass

class GradWindow(Screen):
    pass

class OfficesWindow(Screen):
    pass

class SoEFacultyWindow(Screen):
    pass

class SoEInfo1Window(Screen):
    pass

class SoEInfo2Window(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class Main(MDApp):
    def build (self):
        return kv

Main().run()