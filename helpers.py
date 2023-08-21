image_helper= """
Image:
    source: "logo.png"
    pos_hint :{"center_x":0.5, "center_y": 0.9}
    size_hint_x : None
    width : 300
"""
username_helper= """
MDTextField:
    hint_text: "UserID"
    pos_hint :{"center_x":0.5, "center_y": 0.6}
    size_hint_x : None
    width : 300
    icon_right : "android"
"""
password_helper= """
MDTextField:
    hint_text: "Password"
    pos_hint :{"center_x":0.5, "center_y": 0.4}
    size_hint_x : None
    width : 300
    password: True
    helper_text : "or forgot password"
    helper_text_mode : "on_focus"
    icon_right :"android"
"""
ResetPassword = '''
BoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None 
    height: "120dp"
    

    MDTextField:
        hint_text: "New Password"
        id: new_password
        size_hint_x : .9

    MDTextField:
        hint_text: "Comfirm Password"
        id:comfirm_password
        size_hint_x : .9

'''

historyselection = '''
BoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "New Password"
        id: new_password

    MDTextField:
        hint_text: "Comfirm Password"
        id:comfirm_password

'''

toolbar_helper = """
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


<Pro>:
    name: "pro"
    MDNavigationLayout:

        MDScreenManager:
            id: nav_bar
            MDScreen:
                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["dots-vertical",lambda x:app.dot_vert(x)]]
                ScreenManager:
                    id: screen_manager
                    Screen:
                        name:"dashboard"

                        
                    Screen:
                        name:"profile"
                        
            
                    
                    Screen:
                        name:"courseregistration"
                        

                    Screen:
                        name:"carryover"
                         
                        
                    Screen:
                        name:"registercourses"
                         
                             
                    Screen:
                        name:"coursehistory1"
                         

                    
                    Screen:
                        name:"result1"
                    
                    Screen:
                        name:"coursehistory2"
                        MDLabel:
                            text:"coursehistory2"
                    
                    Screen:
                        name:"result2"
                        MDLabel:
                            text:"result2"
                         


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerItem:
                    icon: "speedometer"
                    text_right_color: "#4a4939"
                    text: "Dashboard"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "dashboard"  

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "account"
                    text: "Profile"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "profile"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "book"
                    text: "Course Registration"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "courseregistration"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "book"
                    text: "CarryOver Courses"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "carryover"
                
                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "book"
                    text: "Registered Courses"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "registercourses"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "book"
                    text: "Course History"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "coursehistory1"
                
                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "chart-bar"
                    text: "Result"
                    on_release:
                        nav_drawer.set_state("close")
                        screen_manager.current = "result1"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    icon: "logout"
                    text: "Logout"

                 
                        
"""