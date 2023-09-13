from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from studentdashboard import Student
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from helpers import ResetPassword
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from lecturerdasboard import Lecturer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from kivymd.uix.card import MDCard

Window.size = (350,580)

cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
UserID = db.collection("LoginDetails").list_documents()
UserIDs = [doc.id for doc in UserID]
#print(UserIDs)

kv =  Builder.load_file("login.kv")

#--------------------------------------------------------------------Screen Manager-----------------------------------
global Portal
global total_unit 
total_unit = []
class Login (Screen):
    
    def login_validation (self):
       
        global username
        self.reset_password_page = Builder.load_string(ResetPassword)
        reset_btn = MDFlatButton(text = "reset", 
                                 on_release = self.reset_dialog 
                                 )
        self.close_btn1 = MDFlatButton(text = "close", 
                                 on_release = self.close_dialog1 )
        
        username = self.ids.usernamevalue.text.replace("/","_")
        if username == "" or self.ids.passwordvalue.text == "" :
            self.dialog = MDDialog(title="Notification", 
                                   text="All fields are required",
                                   #size_hint=(0.5,1),
                                   buttons=[self.close_btn1]
                                   )
            self.dialog.open()

        elif username not in UserIDs:
            self.dialog = MDDialog(title="Notification", 
                                  text="User id not found",
                                   #size_hint=(0.5,1),
                                   buttons=[self.close_btn1]
                                   )
            self.dialog.open()
        
         
        else:
            details = db.collection("LoginDetails").document(username).get().to_dict()
            if details["password"] != self.ids.passwordvalue.text:
                self.dialog = MDDialog(title="Notification", 
                                  text="Pasword not match",
                                   #size_hint=(0.5,1),
                                   buttons=[self.close_btn1]
                                   )
                self.dialog.open()
            else:
                if details["password"] == "students1234" or details["password"] == "lecturer1234":
                    self.dialog = MDDialog(
                    title="Reset Password:",
                    type="custom",
                    content_cls=self.reset_password_page,
                    buttons = [reset_btn],
                    size_hint=(0.9,1))
                    self.dialog.open()

                else:
            
                    if len(username) == 13 :
                 
                         
                        self.manager.current = "student"
                 
                    else:
                         
                        self.manager.current = "lecturer"
            

            
                 
    
    def close_dialog1 (self,obj):
        self.dialog.dismiss()
    
    def reset_dialog (self,obj):
        
        if self.reset_password_page.ids.new_password.text == "" or self.reset_password_page.ids.comfirm_password.text == "" :

            warning_dialog_btn = MDFlatButton(text = "close", 
                                 on_release = self.warning_dialog_btn_func 
                                 )
            self.warning_dialog = MDDialog(
                title= "All fields are required", 
                type="custom",
                 
                buttons = [warning_dialog_btn],
                 
                )
            self.warning_dialog.open()

        elif self.reset_password_page.ids.new_password.text != self.reset_password_page.ids.comfirm_password.text :
    
            warning_dialog_btn = MDFlatButton(text = "close", 
                                 on_release = self.warning_dialog_btn_func 
                                 )
            self.warning_dialog = MDDialog(
                title= "Password not match" , 
                type="custom",
                buttons = [warning_dialog_btn],
                 
                )
            self.warning_dialog.open()
            #db.collection("LoginDetails").document(username).update({"password":self.reset_password_page.ids.new_password.text})
             
        else:
            
            if len(username) == 2 :
                 
                self.dialog.dismiss()
                self.manager.current = "student"
                 
            else:
                self.dialog.dismiss()
                self.manager.current = "lecturer"
            
    
    def warning_dialog_btn_func (self,obl):
        self.warning_dialog.dismiss()

    
    def test3(self):
        Student().ids.namevalue.text = "na"
        print("hi")

        
 

         

class Portal (MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login())
        sm .add_widget(Student())
        sm .add_widget(Lecturer())
        return sm
    
    def dot_vert(self,instance):
        self.menu_list = [
            {"viewclass":"OneLineListItem",
             "text":"Profile",
             "on_release":lambda x = "Profile":Login().test3()},

            {"viewclass":"OneLineListItem",
             "text":"Hide",
             "on_release":lambda x = "Logout":self.std_dashboard()}
        ]

        self.menu = MDDropdownMenu(
            items = self.menu_list,
            width_mult = 4
        )
        self.menu.caller = instance
        self.menu.open()
    
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
            caller=self.root.get_screen("student").ids.history_session_dropdown,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()
    
    def session_set_item(self, text__item):
        self.root.get_screen("student").ids.history_session_dropdown.text = text__item
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
            caller=self.root.get_screen("student").ids.history_semester_dropdown,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def semester_set_item(self, text__item):
        self.root.get_screen("student").ids.history_semester_dropdown.text = text__item
        self.menu.dismiss()


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
            caller=self.root.get_screen("lecturer").ids.coursecodefield,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def course_set_item(self, text__item):
        self.root.get_screen("lecturer").ids.coursecodefield.text = text__item
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
            caller=self.root.get_screen("lecturer").ids.namefield,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def name_set_item(self, text__item):
        self.root.get_screen("lecturer").ids.namefield.text = text__item
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
            caller=self.root.get_screen("lecturer").ids.gradefield,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu.open()

    def grade_set_item(self, text__item):
        self.root.get_screen("lecturer").ids.gradefield.text = text__item
        self.menu.dismiss()

    """def on_start(self):
        Clock.schedule_once(self.std_dashboard,20)""" 
    



    def std_dashboard(self):
        print(username)
        #details = db.collection("profile").document("students").collection(username).document("biodata").get().to_dict()
        details = {"fname": "Muhammed","lname":"TAIRU","tname":"Lolade","programme":"Mathematics","department":"Mathematics and Statitics","faculty":"Natural and Applied Sciences"}
        lname = details['lname']
        fname = details['fname']
        tname = details['tname']
        fullname = f'{lname} {fname} {tname}'
        
        matric = username.replace("/","_")
        self.root.get_screen("student").ids.matricnumber.text = f'Matric Number: {matric}'
        self.root.get_screen("student").ids.namevalue.text = f"Name: {fullname}"
        self.root.get_screen("student").ids.departmentvalue.text = f'Department: {details["department"]}'
        self.root.get_screen("student").ids.programmevalue.text = f'Programme: {details["programme"]}'
        self.root.get_screen("student").ids.facultyvalue.text = f'Faculty: {details["faculty"]}'
        self.table()
        print(username)
        self.menu.dismiss()
         
    def lec_dashboard(self):
        print(username)
        #details = db.collection("profile").document("students").collection(username).document("biodata").get().to_dict()
        details = {"fname": "Muhammed","lname":"TAIRU","tname":"Lolade","programme":"Mathematics","department":"Mathematics and Statitics","faculty":"Natural and Applied Sciences"}
        lname = details['lname']
        fname = details['fname']
        tname = details['tname']
        fullname = f'{lname} {fname} {tname}'
         
        matric = username.replace("/","_")
        self.root.get_screen("lecturer").ids.matricnumber.text = f'Matric Number: {matric}'
        self.root.get_screen("lecturer").ids.namevalue.text = f"Name: {fullname}"
        self.root.get_screen("lecturer").ids.departmentvalue.text = f'Department: {details["department"]}'
        self.root.get_screen("lecturer").ids.programmevalue.text = f'Programme: {details["programme"]}'
        self.root.get_screen("lecturer").ids.facultyvalue.text = f'Faculty: {details["faculty"]}'
        self.table()
        print(username)
        self.menu.dismiss()
        
    
    def table(self):
        list_unit_reg = []
        list_lecturer_reg = []
        list_title_reg = []
        list_status_reg = []
        lis_course_reg=  db.collection("CourseRegistration").list_documents()
        lis_courses_reg = [i.id for i in lis_course_reg ]
        for c in lis_courses_reg:
            output = db.collection("CourseRegistration").document(c).get().to_dict()
            list_unit_reg.append(output["units"])
            list_lecturer_reg.append(output["lecturer"])
            list_title_reg.append(output["title"])
            list_status_reg.append(output["status"])
        
        self.dialog =  MDDataTable(
            #padding_x = 50,
            size_hint=(0.98,0.99),
            pos_hint= {"center_x": .7, "center_y": .5},
            check = True,
            background_color_selected_cell = "e4514f",
            column_data=[
                ("S/N.", dp(30)),
                ("Course Code", dp(30)),
                ("Course Title", dp(60),),
                ("Lecturer", dp(30)),
                ("Course Unit", dp(30)),
                ("Status", dp(30)),
            ],
            row_data=[
                (f'{i + 1}',lis_courses_reg[i],list_title_reg[i],list_lecturer_reg[i],list_unit_reg[i],list_status_reg[i]) for i in range(len(lis_courses_reg))
            ]
            )

        self.dialog.bind(on_row_press = self.on_row_press)
        self.dialog.bind(on_check_press = self.on_check_press)

        label=MDLabel(text=f"total unit: {total_unit}",pos_hint= {"center_x": .8, "center_y": .08})    
        self.bacl = MDCard(
                    #title="Reset Password:",
                    #type="custom",
                    #content_cls=self.dialog,
                    #buttons = [reset_btn],
                    #size_hint=(0.9,1)
                    size_hint=(0.9,0.75),
                    pos_hint= {"center_x": .5, "center_y": .5},
                     
                    )
        #self.bacl.open()
        
        self.bacl.add_widget(self.dialog)
         
        self.root.get_screen("student").ids.screen_manager.get_screen("courseregistration").add_widget(self.bacl)
        self.root.get_screen("student").ids.screen_manager.get_screen("courseregistration").add_widget(label)
    
    
    def on_row_press(self,instance_table,instance_row):
        print(instance_row,instance_table)
    
    
    def on_check_press(self,instance_table,current_row):
         print(current_row)

    
    def results(self):
        list_unit_re = []
        list_grade_re = []
        list_score_re = []
        lis_course_re =  db.collection("Results").list_documents()
        lis_courses_re = [i.id for i in lis_course_re ]
        for c in lis_courses_re:
            output = db.collection("Results").document(c).collection("re").document( username).get().to_dict()
            list_unit_re.append(output["unit"])
            list_grade_re.append(output["grade"])
            list_score_re.append(output["score"])
        
        self.dialogr =  MDDataTable(
            #padding_x = 50,
            size_hint=(0.98,0.99),
            pos_hint= {"center_x": .7, "center_y": .4},
            column_data=[
                ("S/N.", dp(30)),
                ("Course Code", dp(30)),
                ("Course Unit", dp(30)),
                ("Score", dp(30),),
                ("Grade", dp(30)),
                
            ],
            row_data=[
                (f'{i + 1}',lis_courses_re[i],list_unit_re[i],list_score_re[i],list_grade_re[i]) for i in range(len(lis_courses_re))
            ]
            )
        dic_grade = {"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}
        total_point =[]
        list_unit_re_num = []
        for k in range(len(list_unit_re)):
            list_unit_re_num.append(int(list_unit_re[k]))
            total_point.append(int(list_unit_re[k]) * dic_grade[list_grade_re[k]])
        print(list_unit_re_num)
        Cgpa = sum(total_point)/sum(list_unit_re_num)
        print(sum(total_point))
        print(sum(list_unit_re_num))
        label=MDLabel(text=f"GPA: {Cgpa}",pos_hint= {"center_x": .8, "center_y": .08})    
        self.l = MDCard(
                    pos_hint= {"center_x": .5, "center_y": .5},
                     
                    )
        
        
        self.l.add_widget(self.dialogr)
         
        self.root.get_screen("student").ids.screen_manager.get_screen("result2").add_widget(self.l)
        self.root.get_screen("student").ids.screen_manager.get_screen("result2").add_widget(label)

        
    def test3(self):
        self.get_screen("student").ids.namevalue.text = "name"
        self.menu.dismiss()
        print("hi")


    
    
    

if __name__ == "__main__":
    Portal().run()