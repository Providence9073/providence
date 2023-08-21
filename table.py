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
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard

class Table(MDApp):
    def build(self):
        self.dialog =  MDDataTable(
            #padding_x = 50,
            size_hint=(0.3,0.5),
            pos_hint= {"center_x": .5, "center_y": .3},
            check = False,
            column_data=[
                ("S/N.", dp(30)),
                ("Course Code", dp(30)),
                ("Course Title", dp(30),),
                ("Lecturer", dp(30)),
                ("Course Unit", dp(30)),
            ],
            row_data = [
               ("2","CSC124","Software Economics","Prof. Super","8"),
                ("2","CSC124","Software Economics","Prof. Super","8")
                ]
            )
                               

            
        return  self.dialog
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
                ("Course Unit", dp(30))
                ],
                row_data = [
                ("2","CSC124","Software Economics","Prof. Super","8")]
            
            
            
            )
        self.dialog.add_widget(registrationdatatables)
        btn = MDLabel(text="Hi",pos_hint= {"center_x": .5, "center_y": .2},padding_x = 50)


if __name__ == "__main__":
    Table().run()

         