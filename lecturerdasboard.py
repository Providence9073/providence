from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty,ObjectProperty
from kivymd.uix.list import OneLineListItem
#from kivymd.utils  import S

Window.size = (350,580)

kv = Builder.load_file("lecturer.kv")

class Lecturer (Screen):
    """name = ObjectProperty(None)
    mail = ObjectProperty(None)"""
    pass

class IconListItem(OneLineListItem):
    icon = StringProperty()

class Portal (MDApp):
    def build(self):
        return  Lecturer()
    
    def play(self):
        self.root.ids.namevalue.text = "name"
        self.root.ids.matricnumber.text = "name"
        self.root.ids.programmevalue.text = "name"
        self.root.ids.departmentvalue.text = "name"
        self.root.ids.facultyvalue.text = "name"

     
        registrationdatatables = MDDataTable(
            #padding_x = 50,
            pos_hint_x= 0.5,
            pos_hint_y = None,
            height = "20dp",
            check = True,
            column_data=[
                ("S/N.", dp(30)),
                ("Course Code", dp(30)),
                ("Course Title", dp(60),),
                ("Lecturer", dp(30)),
                ("Course Unit", dp(30)),
            ],)
        self.root.ids.table.add_widget(registrationdatatables)
    
    def coursecode_field (self):
        session = ["2019/2020","2020/2021","2021/22","2022/2023"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": i,
                "on_release": lambda x=i: self.course_set_item(x),
            } for i in session]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.coursecodefield,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def course_set_item(self, text__item):
        self.root.ids.coursecodefield.text = text__item
        self.menu.dismiss()

    def name_field (self):
        session = ["2019/2020","2020/2021","2021/22","2022/2023"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": i,
                "on_release": lambda x=i: self.name_set_item(x),
            } for i in session]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.namefield,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def name_set_item(self, text__item):
        self.root.ids.namefield.text = text__item
        self.menu.dismiss()
    
    def grade_field (self):
        session = ["A","B","C","D","E","F"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(56),
                "text": i,
                "on_release": lambda x=i: self.grade_set_item(x),
            } for i in session]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.gradefield,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def grade_set_item(self, text__item):
        self.root.ids.gradefield.text = text__item
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
    
if __name__ == "__main__":
    Portal().run()