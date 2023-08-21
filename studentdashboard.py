from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineListItem


Window.size = (350,580)

kv = Builder.load_file("student.kv")

class Student (Screen):
    pass

class IconListItem(OneLineListItem):
    icon = StringProperty()

class Portal (MDApp):
    def build(self):
        return  Student()
    
    def table (self):
        self.registrationdatatables2 = MDDataTable(
            #padding_x = 50,
            size_hint=(0.3,0.5),
            pos_hint= {"center_x": .5, "center_y": .3},
            check = True,
            column_data=[
                ("S/N.", dp(30)),
                ("Course Code", dp(30)),
                ("Course Title", dp(30),),
                ("Lecturer", dp(30)),
                ("Course Unit", dp(30)),
            ],)
    
    def call_login1(self):
        registrationdatatables = MDDataTable(
            #padding_x = 50,
            pos_hint= {"center_x": .5, "center_y": .1},
            check = True,
            column_data=[
                ("S/N.", dp(30)),
                ("Course Code", dp(30)),
                ("Course Title", dp(60),),
                ("Lecturer", dp(30)),
                ("Course Unit", dp(30)),
            ],)
        self.root.get_screen("dashboard").add_widet(registrationdatatables)
        
    
    def dropdown_session (self):
        session = ["2019/2020","2020/2021","2021/22","2022/2023"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": i,
                "on_release": lambda x=i: self.session_set_item(x),
            } for i in session]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.history_session_dropdown,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def session_set_item(self, text__item):
        self.root.ids.history_session_dropdown.text = text__item
        self.menu.dismiss()

    def dropdown_semester (self):
        semester = ["first semster","second semester"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": i,
                "on_release": lambda x=i: self.semester_set_item(x),
            } for i in semester]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.history_semester_dropdown,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def semester_set_item(self, text__item):
        self.root.ids.history_semester_dropdown.text = text__item
        self.menu.dismiss()

    def dot_vert(self,instance):
        self.menu_list = [
            {"viewclass":"OneLineListItem",
             "text":"Profile",
             "on_release":lambda x = "Profile":self.test1()},

            {"viewclass":"OneLineListItem",
             "text":"Logout",
             "on_release":lambda x = "Logout":self.test2()}
        ]

        self.menu = MDDropdownMenu(
            items = self.menu_list,
            width_mult = 4
        )
        self.menu.caller = instance
        self.menu.open()


    def test1(self):
        print("hello")
        #self.root.screen_manager.current = "profile"
        self.menu.dismiss()
    
    def test2(self):
        print("hi")
        self.menu.dismiss()
    
    def test3(self):
        self.root.ids.namevalue.text = "name"
        print("hi")



if __name__ == "__main__":
    Portal().run()
