import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.dropdown import DropDown
from kivymd.uix.menu import MDDropdownMenu


class DEMO(FloatLayout):

    def main_(self):
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": "Arabic",
                "on_release": lambda x="Arabic": self.test1()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Chinese",
                "on_release": lambda y="Chinese": self.test2()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "English",
                "on_release": lambda p="English": self.test3()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Hindi",
                "on_release": lambda q="Hindi": self.test4()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Kannada",
                "on_release": lambda w="Kannada": self.test5()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Malayalam",
                "on_release": lambda r="Malayalam": self.test6()
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.menu_,
            items=self.menu_list,
            width_mult=4
        )
        self.menu.open()
    def test1(self):
        print("Arabic txt")
    def test2(self):
        print("Chinese txt")
    def test3(self):
        print("English txt")
    def test4(self):
        print("Hindi txt")
    def test5(self):
        print("Kannada txt")
    def test6(self):
        print("Malayalam txt")
    Builder.load_file("sample.kv")


class Main(MDApp):
    def build(self):
        return DEMO()


Main().run()
