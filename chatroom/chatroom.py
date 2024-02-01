from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk , Image
import backend
# Display
def window(windowName):
    windowName.title("Chat Room")
    windowName.geometry("1000x600")
    windowName.minsize(800 , 500)
    windowName.resizable(0 , 0)
    iconImage = ImageTk.PhotoImage(Image.open("icon.png"))
    windowName.iconphoto(False , iconImage)
# I create settingKey and contact1WindowKey and contact2WindowKey for open and close Window
settingKey = False
contact1WindowKey = False
contact2WindowKey = False
connection = backend.check_connection()
backend.create_table_users(connection)
backend.create_table_chat_contact1(connection)
backend.create_table_chat_contact2(connection)
# Register
def signup():
    mainWindow.withdraw()
    registerWindow = Toplevel(mainWindow)
    window(registerWindow)
    key = {"nameKey" : False ,
            "lastNameKey" : False ,
            "userNameKey" : False ,
            "passwordKey" : False ,
            "passwordAgainKey" : False ,
    }
    def submit():
        connection = backend.check_connection()
        nameGet = nameEntry.get()
        if nameGet.isspace() or not nameGet:
            key["nameKey"] = False
            nameError = customtkinter.CTkLabel(master= registerWindow , text= "Please enter your name." , text_color= "#e54c38" , bg_color= "#d7d7d7")
            nameError.place(x=310 , y=185)
        else:
            key["nameKey"] = True
            nameTrue = customtkinter.CTkLabel(master= registerWindow , text= "                                                        " , bg_color= "#d7d7d7")
            nameTrue.place(x=310 , y=185)
        lastNameGet = lastNameEntry.get()
        if lastNameGet.isspace() or not lastNameGet:
            key["lastNameKey"] = False
            lastNameError = customtkinter.CTkLabel(master= registerWindow , text= "Please enter your Lastname." , text_color= "#e54c38" , bg_color= "#d7d7d7")
            lastNameError.place(x=310 , y=255)
        else:
            key["lastNameKey"] = True
            lastNameTrue = customtkinter.CTkLabel(master= registerWindow , text= "                                                        " , bg_color= "#d7d7d7")
            lastNameTrue.place(x=310 , y=255)
        userNameGet = userNameEntry.get()
        usernameCheck = backend.username_check(connection , userNameGet)
        if usernameCheck:
            key["userNameKey"] = False
            userNameError = customtkinter.CTkLabel(master= registerWindow , text= "This username is already taken.                                                                          " , text_color= "#e54c38" , bg_color= "#d7d7d7")
            userNameError.place(x=310 , y=325)
        elif userNameGet.isspace() or not userNameGet.isidentifier() or len(userNameGet) <= 5 or not userNameGet:
            key["userNameKey"] = False
            userNameError = customtkinter.CTkLabel(master= registerWindow , text= "You can use a-z , 0-9 and underscores. Minimum lenght is 5 characters." , text_color= "#e54c38" , bg_color= "#d7d7d7")
            userNameError.place(x=310 , y=325)
        else:
            key["userNameKey"] = True
            userNameTrue = customtkinter.CTkLabel(master= registerWindow , text= "                                                                                                                                       " , bg_color= "#d7d7d7")
            userNameTrue.place(x=310 , y=325)
        passwordGet = passwordEntry.get()
        if passwordGet.isspace() or not passwordGet.isidentifier() or len(passwordGet) <= 8 or len(passwordGet) >= 16 or not passwordGet or passwordGet.islower() or passwordGet.isupper():
            key["passwordKey"] = False
            passwordError = customtkinter.CTkLabel(master= registerWindow , text= "You can use a-z , 0-9 and underscores. The lenght between 8 to 16." , text_color= "#e54c38" , bg_color= "#d7d7d7")
            passwordError.place(x=310 , y=395)
        else:
            key["passwordKey"] = True
            passwordTrue = customtkinter.CTkLabel(master= registerWindow , text= "                                                                                                                                       " , bg_color= "#d7d7d7")
            passwordTrue.place(x=310 , y=395)
        passwordAgainGet = passwordAgainEntry.get()
        if passwordAgainGet != passwordGet:
            key["passwordAgainKey"] = False
            passwordAgainError = customtkinter.CTkLabel(master= registerWindow , text= "Password is not the same" , text_color= "#e54c38" , bg_color= "#d7d7d7")
            passwordAgainError.place(x=310 , y=465)
        else:
            key["passwordAgainKey"] = True
            passwordAgainTrue = customtkinter.CTkLabel(master= registerWindow , text= "                                                        " , bg_color= "#d7d7d7")
            passwordAgainTrue.place(x=310 , y=465)
        if key["nameKey"] == True and key["lastNameKey"] == True and key["userNameKey"] == True and key["passwordKey"] == True and key["passwordAgainKey"] == True:
            backend.insert_into_users(connection , nameGet , lastNameGet , userNameGet , passwordGet)
            registerWindow.destroy()
            mainWindow.deiconify()
            messagebox.showinfo("Notice" , "Your registration was successful.")
    def registerBack():
        registerWindow.destroy()
        mainWindow.deiconify()
    # Buttoms And Entry And Photos
    registerBgImage = ImageTk.PhotoImage(Image.open("register_bg.png"))
    registerBg = Label(registerWindow , image=registerBgImage).pack()
    nameEntry = customtkinter.CTkEntry(master= registerWindow , width= 400 , height= 40 , placeholder_text= "Name" , corner_radius= 8 ,bg_color= "#d7d7d7")
    nameEntry.place(x=302 , y=145)
    lastNameEntry = customtkinter.CTkEntry(master= registerWindow , width= 400 , height= 40 , placeholder_text= "Lastname" , corner_radius= 8 ,bg_color= "#d7d7d7")
    lastNameEntry.place(x=302 , y=215)
    userNameEntry = customtkinter.CTkEntry(master= registerWindow , width= 400 , height= 40 , placeholder_text= "Username" , corner_radius= 8 ,bg_color= "#d7d7d7")
    userNameEntry.place(x=302 , y=285)
    passwordEntry = customtkinter.CTkEntry(master= registerWindow , width= 400 , height= 40 , placeholder_text= "Password" , corner_radius= 8 ,bg_color= "#d7d7d7" , show= "●")
    passwordEntry.place(x=302 , y=355)
    passwordAgainEntry = customtkinter.CTkEntry(master= registerWindow , width= 400 , height= 40 , placeholder_text= "Re-enter the password" , corner_radius= 8 ,bg_color= "#d7d7d7" , show= "●")
    passwordAgainEntry.place(x=302 , y=425)
    submitButtom = customtkinter.CTkButton(master= registerWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Submit" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= submit).place(x=313 , y=500)
    registerBackButtom = customtkinter.CTkButton(master= registerWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Back" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= registerBack).place(x=513 , y=500)
    registerWindow.mainloop()
# Login
def signin():
    connection = backend.check_connection()
    signinKey = {
        "emailKey" : True ,
        "ageKey" : True ,
        "genderKey" : True ,
        "countryKey" : True ,
        "cityKey" : True ,
        "phoneNumberKey" : True ,
            }
    mainWindow.withdraw()
    loginWindow = Toplevel(mainWindow)
    window(loginWindow)
    loginKey = False
    def login():
        global contact1WindowKey , contact2WindowKey , loginKey
        userNameLogin = userNameLoginEntry.get()
        passwordLogin = passwordLoginEntry.get()
        loginResult = backend.check_login(connection , userNameLogin , passwordLogin)
        if loginResult:
            loginKey = True
            loginWindow.destroy()
            # Logout
            def logoutContact1Window():
                if contact1WindowKey == True:
                    contact1Window.destroy()
                    mainWindow.deiconify()
            # Settings
            def settings():
                global settingKey
                # I use userDetails because when I open settingsWindow I need to new information of user
                connection = backend.check_connection()
                userDetails = backend.check_login(connection , userNameLogin , passwordLogin)
                def cancel():
                    global settingKey
                    settingKey = False
                    settingsWindow.destroy()
                def save():
                    global settingKey
                    connection = backend.check_connection()
                    emailGet = emailEntry.get()
                    if emailGet.isspace() or "@gmail.com" not in emailGet and emailGet != "":
                        signinKey["emailKey"] = False
                        emailError = customtkinter.CTkLabel(master= settingsWindow , text= "Your email is wrong." , text_color= "#e54c38" , bg_color= "#d7d7d7")
                        emailError.place(x= 313 , y= 335)
                    else:
                        signinKey["emailKey"] = True
                        emailTrue = customtkinter.CTkLabel(master= settingsWindow , text= "                                                                                                                                       " , bg_color= "#d7d7d7")
                        emailTrue.place(x= 313 , y= 335)
                    ageGet = ageEntry.get()
                    if ageGet.isspace():
                        signinKey["ageKey"] = False
                    else:
                        signinKey["ageKey"] = True
                    genderGet = radioButtonVariable.get()
                    if genderGet == 1:
                        signinKey["genderKey"] = True
                        genderGet = "Men"
                    elif genderGet == 2:
                        signinKey["genderKey"] = True
                        genderGet = "Female"
                    else:
                        signinKey["genderKey"] = False
                    countryGet = countryEntry.get()
                    if countryGet.isspace():
                        signinKey["countryKey"] = False
                    else:
                        signinKey["countryKey"] = True
                    cityGet = cityEntry.get()
                    if cityGet.isspace() :
                        signinKey["cityKey"] = False
                    else:
                        signinKey["cityKey"] = True
                    phoneNumberGet = phoneNumberEntry.get()
                    if phoneNumberGet.isspace():
                        signinKey["phoneNumberKey"] = False
                    else:
                        signinKey["phoneNumberKey"] = True
                    if signinKey["emailKey"] == True and signinKey["ageKey"] == True and signinKey["countryKey"] == True and signinKey["cityKey"] == True and signinKey["phoneNumberKey"] == True:
                        backend.update_user_information(connection , emailGet , ageGet , genderGet , countryGet , cityGet , phoneNumberGet , userNameLogin , passwordLogin)
                    if signinKey["emailKey"] == True:
                        settingKey = False
                        settingsWindow.destroy()
                        messagebox.showinfo("Notice" , "Successful.")
                if settingKey == False:
                    settingKey = True
                    settingsWindow = Toplevel(mainWindow)
                    settingsBgImage = ImageTk.PhotoImage(Image.open("setting.png"))
                    settingsBg = customtkinter.CTkLabel(master= settingsWindow , image= settingsBgImage , text= "").pack()
                    userProfileImage = ImageTk.PhotoImage(Image.open("user_profile.png"))
                    userProfile = customtkinter.CTkLabel(master= settingsWindow , image= userProfileImage , bg_color= "#d7d7d7" , text= "").place(x=430 , y= 80)
                    nameProfile = userDetails[0][1]
                    lastNameProfile = userDetails[0][2]
                    genderProfile = userDetails[0][7]
                nameFrame = customtkinter.CTkFrame(master= settingsWindow , width= 198 , height= 40 , corner_radius= 8 , bg_color= "#d7d7d7" , fg_color= "#343638").place(x= 301, y= 250)
                nameProfileLabel = customtkinter.CTkLabel(master= settingsWindow , text= nameProfile , bg_color= "#343638" , font= ("Calibri" , 15) , text_color= "#9e9e8f")
                nameProfileLabel.place(x= 309 , y= 255)
                lastNameFrame = customtkinter.CTkFrame(master= settingsWindow , width= 198 , height= 40 , corner_radius= 8 , bg_color= "#d7d7d7" , fg_color= "#343638").place(x= 503, y= 250)
                lastNameProfileLabel = customtkinter.CTkLabel(master= settingsWindow, text= lastNameProfile , bg_color= "#343638" , font= ("Calibri" , 15) , text_color= "#9e9e8f")
                lastNameProfileLabel.place(x= 511 , y= 255)
                emailEntry = customtkinter.CTkEntry(master= settingsWindow , width= 402 , height= 40 , placeholder_text= "Email" , corner_radius= 8 ,bg_color= "#d7d7d7")
                emailEntry.place(x=300 , y=295)
                if userDetails[0][5] != "":
                    emailEntry.insert(0 , userDetails[0][5])
                ageEntry = customtkinter.CTkEntry(master= settingsWindow , width= 198 , height= 40 , placeholder_text= "Age" , corner_radius= 8 ,bg_color= "#d7d7d7")
                ageEntry.place(x=300 , y=365)
                if userDetails[0][6] != "":
                    ageEntry.insert(0 , userDetails[0][6])
                genderFrame = customtkinter.CTkFrame(master= settingsWindow , width= 198 , height= 40 , corner_radius= 8 , bg_color= "#d7d7d7" , fg_color= "#343638").place(x= 503, y= 365)
                genderLabel = customtkinter.CTkLabel(master= settingsWindow , text= "Gender:" , bg_color= "#343638" , font= ("Calibri" , 15) , text_color= "#9e9e8f")
                genderLabel.place(x= 510 , y= 370)
                radioButtonVariable = IntVar()
                maleRadioButton = customtkinter.CTkRadioButton(master= settingsWindow , text= "Male" , bg_color= "#343638" , radiobutton_height= 12 , radiobutton_width= 12 , font= ("Calibri" , 14) , text_color= "#9e9e8f" , variable= radioButtonVariable , value= 1)
                maleRadioButton.place(x= 570 , y= 375)
                femaleRadioButton = customtkinter.CTkRadioButton(master= settingsWindow , width= 20 , text= "Female" , bg_color= "#343638" , radiobutton_height= 12 , radiobutton_width= 12 , font= ("Calibri" , 14) , text_color= "#9e9e8f" , variable= radioButtonVariable , value= 2)
                femaleRadioButton.place(x= 628 , y= 375)
                countryEntry = customtkinter.CTkEntry(master= settingsWindow , width= 198 , height= 40 , placeholder_text= "Country" , corner_radius= 8 ,bg_color= "#d7d7d7")
                countryEntry.place(x=300 , y=415)
                if userDetails[0][8] != "":
                    countryEntry.insert(0 , userDetails[0][8])
                cityEntry = customtkinter.CTkEntry(master= settingsWindow , width= 198 , height= 40 , placeholder_text= "City" , corner_radius= 8 ,bg_color= "#d7d7d7")
                cityEntry.place(x=504 , y=415)
                if userDetails[0][9] != "":
                    cityEntry.insert(0 , userDetails[0][9])
                phoneNumberEntry = customtkinter.CTkEntry(master= settingsWindow , width= 402 , height= 40 , placeholder_text= "Phone number" , corner_radius= 8 ,bg_color= "#d7d7d7")
                phoneNumberEntry.place(x=300 , y=465)
                if userDetails[0][10] != "":
                    phoneNumberEntry.insert(0 , userDetails[0][10])
                saveButtom = customtkinter.CTkButton(master= settingsWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Save" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= save).place(x=313 , y=520)
                cancelButtom = customtkinter.CTkButton(master= settingsWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Cancel" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= cancel).place(x=513 , y=520)
                settingsWindow.mainloop()
            # Contact 2
            def contact2():
                global contact1WindowKey , contact2WindowKey
                def sendContact2():
                    userInformation = backend.check_login(connection , userNameLogin , passwordLogin)
                    userId = userInformation[0][0]
                    send = " you : " + typeBox.get()
                    chatBoxContact2.insert(END , "\n" + send)
                    user = send.lower()
                    if user == " you : hello":
                        contactChat = " \n" + "John Williams : Hi there, how can I help?"
                        chatBoxContact2.insert(END , contactChat)
                    elif  user == " you : hi" or user == " you : hii" or user == " you : hiiii":
                        contactChat = " \n" + "John Williams : Hi there, what can I do for you?"
                        chatBoxContact2.insert(END , contactChat)
                    elif user == " you : how are you" or user == " you : how are you?":
                        contactChat = " \n" + "John Williams : fine! and you?"
                        chatBoxContact2.insert(END , contactChat)
                    elif user == " you : fine" or user == " you : i am good" or user == " you : i am doing good":
                        contactChat = " \n" + "John Williams : Great! how can I help you."
                        chatBoxContact2.insert(END , contactChat)
                    elif user == " you : thanks" or user == " you : thank you" or user == " you : now its my time":
                        contactChat = " \n" + "John Williams : My pleasure!"
                        chatBoxContact2.insert(END , contactChat)
                    elif user == " you : where are you from" or user == " you : where are you from?":
                        contactChat = " \n" + "John Williams : I'm from Chatroom"
                        chatBoxContact2.insert(END , contactChat)
                    elif user == " you : how old are you" or user == " you : how old are you?":
                        contactChat = " \n" + "John Williams : I don't now"
                        chatBoxContact2.insert(END , contactChat)
                    elif user == " you : goodbye" or user == " you : bye" or user == " you : see you later":
                        contactChat = " \n" + "John Williams : Have a nice day!"
                        chatBoxContact2.insert(END , contactChat)
                    else:
                        contactChat = " \n" + "John Williams : Sorry! I didn't understand thet"
                        chatBoxContact2.insert(END , contactChat)
                    backend.insert_into_chat2(connection , user , contactChat , userId)
                    typeBox.delete(0 , END)
                def logoutContact2Window():
                    if contact2WindowKey == True:
                        contact2Window.destroy()
                        mainWindow.deiconify()
                def openContact1():
                    global contact1WindowKey , contact2WindowKey
                    contact1WindowKey = True
                    contact2WindowKey = False
                    contact1Window.deiconify()
                    contact2Window.destroy()
                contact2WindowKey = True
                contact1WindowKey = False
                contact2Window = Toplevel(mainWindow)
                contact1Window.withdraw()
                window(contact2Window)
                chatBgImage = ImageTk.PhotoImage(Image.open("chat_bg.png"))
                chatBg = Label(contact2Window , image= chatBgImage).pack()
                settingButton = customtkinter.CTkButton(master= contact2Window , width= 30 , height= 30 , corner_radius= 100 ,text= "⚙️" , fg_color= "#699bfe" , bg_color= "white" , hover_color= "#3078ff" , command= settings)
                settingButton.place(x= 100 , y= 550)
                logoutButton = customtkinter.CTkButton(master= contact2Window , width= 30 , height= 30 , corner_radius= 100 ,text= "Log out" , fg_color= "#699bfe" , bg_color= "white" , hover_color= "#3078ff" , command= logoutContact2Window)
                logoutButton.place(x= 20 , y= 550)
                chatBoxContact2 = Listbox(master= contact2Window , width= 65 , height= 20 , bg= "#DFDFDF" , font= ("Times" , 14))
                chatBoxContact2.place(x= 388 , y= 75)
                scrollbarContact2 = Scrollbar(master= contact2Window)
                scrollbarContact2.place(x= 980 , y= 270)
                chatBoxContact2.configure(yscrollcommand= scrollbarContact2.set)
                scrollbarContact2.configure(command= chatBoxContact2.yview)
                typeBox = customtkinter.CTkEntry(master= contact2Window , width= 500 , height= 45 , placeholder_text= "Type..." , corner_radius= 20 ,bg_color= "#dfe3e6")
                typeBox.place(x= 410 , y= 540)
                sendButton = customtkinter.CTkButton(master= contact2Window , width= 30 , height= 45 , corner_radius= 100 ,text= "➤" , fg_color= "#699bfe" , bg_color= "#dfe3e6" , hover_color= "#3078ff" , command= sendContact2)
                sendButton.place(x= 915 , y= 540)
                contacts2Profile = ImageTk.PhotoImage(Image.open("contacts2_profile.png"))
                contacts2 = customtkinter.CTkButton(master= contact2Window , width= 385 , height= 78 , corner_radius= 5 ,text= "   John Williams" , font= ("Calibri" , 20) , fg_color= "#b7b7b7" , hover_color= "#b7b7b7" , text_color= "Black" , image= contacts2Profile , compound= "left")
                contacts2.place(x= 3 , y= 80)
                contacts1Profile = ImageTk.PhotoImage(Image.open("contacts1_profile.png"))
                contacts1 = customtkinter.CTkButton(master= contact2Window , width= 385 , height= 78 , corner_radius= 5 ,text= "    Martin Brown" , font= ("Calibri" , 20) , fg_color= "#e7e7e7" , hover_color= "#b7b7b7" , text_color= "Black" , image= contacts1Profile , compound= "left" , command= openContact1)
                contacts1.place(x= 3 , y= 0)
                contacts2Profile = ImageTk.PhotoImage(Image.open("contacts2_profile.png"))
                contactHeaderProfile2 = customtkinter.CTkLabel(master= contact2Window , image= contacts2Profile , text= "" , bg_color= "#C3C3C3")
                contactHeaderProfile2.place(x= 440 , y= 10)
                contactHeaderProfile2 = customtkinter.CTkLabel(master= contact2Window , text= "John Williams" , bg_color= "#C3C3C3" , font= ("Calibri" , 25) , text_color= "Black")
                contactHeaderProfile2.place(x= 530 , y= 17)
                contactHeaderProfile2 = customtkinter.CTkLabel(master= contact2Window , text= "Online" , bg_color= "#C3C3C3" , font= ("Calibri" , 12) , text_color= "Black")
                contactHeaderProfile2.place(x= 530 , y= 45)
                userInformation = backend.check_login(connection , userNameLogin , passwordLogin)
                userId = userInformation[0][0]
                listTupleChat2 = backend.select_chat_contact2(connection , userId)
                for rowTuple in listTupleChat2:
                    for column in rowTuple:
                        chatBoxContact2.insert(END , column)
                contact2Window.mainloop()
            # Contact 1
            contact1WindowKey = True
            contact1Window = Toplevel(mainWindow)
            window(contact1Window)
            chatBgImage = ImageTk.PhotoImage(Image.open("chat_bg.png"))
            chatBg = Label(contact1Window , image= chatBgImage).pack()
            settingButton = customtkinter.CTkButton(master= contact1Window , width= 30 , height= 30 , corner_radius= 100 ,text= "⚙️" , fg_color= "#699bfe" , bg_color= "white" , hover_color= "#3078ff" , command= settings)
            settingButton.place(x= 100 , y= 550)
            logoutButton = customtkinter.CTkButton(master= contact1Window , width= 30 , height= 30 , corner_radius= 100 ,text= "Log out" , fg_color= "#699bfe" , bg_color= "white" , hover_color= "#3078ff" , command= logoutContact1Window)
            logoutButton.place(x= 20 , y= 550)
            def sendContact1():
                    userInformation = backend.check_login(connection , userNameLogin , passwordLogin)
                    userId = userInformation[0][0]
                    send = " you : " + typeBox.get()
                    chatBoxContact1.insert(END , "\n" + send)
                    user = send.lower()
                    if user == " you : hello":
                        contactChat = " \n" + "Martin Brown : Hi there, how can I help?"
                        chatBoxContact1.insert(END , contactChat)
                    elif  user == " you : hi" or user == " you : hii" or user == " you : hiiii":
                        contactChat = " \n" + "Martin Brown : Hi there, what can I do for you?"
                        chatBoxContact1.insert(END , contactChat)
                    elif user == " you : how are you" or user == " you : how are you?":
                        contactChat = " \n" + "Martin Brown : fine! and you?"
                        chatBoxContact1.insert(END , contactChat)
                    elif user == " you : fine" or user == " you : i am good" or user == " you : i am doing good":
                        contactChat = " \n" + "Martin Brown : Great! how can I help you."
                        chatBoxContact1.insert(END , contactChat)
                    elif user == " you : thanks" or user == " you : thank you" or user == " you : now its my time":
                        contactChat = " \n" + "Martin Brown : My pleasure!"
                        chatBoxContact1.insert(END , contactChat)
                    elif user == " you : where are you from" or user == " you : where are you from?":
                        contactChat = " \n" + "Martin Brown : I'm from Chatroom"
                        chatBoxContact1.insert(END , contactChat)
                    elif user == " you : how old are you" or user == " you : how old are you?":
                        contactChat = " \n" + "Martin Brown : I don't now"
                        chatBoxContact1.insert(END , contactChat)
                    elif user == " you : goodbye" or user == " you : bye" or user == " you : see you later":
                        contactChat = " \n" + "Martin Brown : Have a nice day!"
                        chatBoxContact1.insert(END , contactChat)
                    else:
                        contactChat = " \n" + "Martin Brown : Sorry! I didn't understand thet"
                        chatBoxContact1.insert(END , contactChat)
                    backend.insert_into_chat1(connection , user , contactChat , userId)
                    typeBox.delete(0 , END)
            chatBoxContact1 = Listbox(master= contact1Window , width= 65 , height= 20 , bg= "#DFDFDF" , font= ("Times" , 14))
            chatBoxContact1.place(x= 388 , y= 75)
            scrollbarContact1 = Scrollbar(master= contact1Window)
            scrollbarContact1.place(x= 980 , y= 270)
            chatBoxContact1.configure(yscrollcommand= scrollbarContact1.set)
            scrollbarContact1.configure(command= chatBoxContact1.yview)
            typeBox = customtkinter.CTkEntry(master= contact1Window , width= 500 , height= 45 , placeholder_text= "Type..." , corner_radius= 20 ,bg_color= "#dfe3e6")
            typeBox.place(x= 410 , y= 540)
            sendButton = customtkinter.CTkButton(master= contact1Window , width= 30 , height= 45 , corner_radius= 100 ,text= "➤" , fg_color= "#699bfe" , bg_color= "#dfe3e6" , hover_color= "#3078ff" , command= sendContact1)
            sendButton.place(x= 915 , y= 540)
            contacts1Profile = ImageTk.PhotoImage(Image.open("contacts1_profile.png"))
            contacts1 = customtkinter.CTkButton(master= contact1Window , width= 385 , height= 78 , corner_radius= 5 ,text= "    Martin Brown" , font= ("Calibri" , 20) , fg_color= "#b7b7b7" , hover_color= "#b7b7b7" , text_color= "Black" , image= contacts1Profile , compound= "left")
            contacts1.place(x= 3 , y= 0)
            contacts2Profile = ImageTk.PhotoImage(Image.open("contacts2_profile.png"))
            contacts2 = customtkinter.CTkButton(master= contact1Window , width= 385 , height= 78 , corner_radius= 5 ,text= "   John Williams" , font= ("Calibri" , 20) , fg_color= "#e7e7e7" , hover_color= "#b7b7b7" , text_color= "Black" , image= contacts2Profile , compound= "left" , command= contact2)
            contacts2.place(x= 3 , y= 80)
            contacts1Profile = ImageTk.PhotoImage(Image.open("contacts1_profile.png"))
            contactHeaderProfile1 = customtkinter.CTkLabel(master= contact1Window , image= contacts1Profile , text= "" , bg_color= "#C3C3C3")
            contactHeaderProfile1.place(x= 440 , y= 10)
            contactHeaderProfile1 = customtkinter.CTkLabel(master= contact1Window , text= "Martin Brown" , bg_color= "#C3C3C3" , font= ("Calibri" , 25) , text_color= "Black")
            contactHeaderProfile1.place(x= 530 , y= 17)
            contactHeaderProfile1 = customtkinter.CTkLabel(master= contact1Window , text= "Online" , bg_color= "#C3C3C3" , font= ("Calibri" , 12) , text_color= "Black")
            contactHeaderProfile1.place(x= 530 , y= 45)
            userInformation = backend.check_login(connection , userNameLogin , passwordLogin)
            userId = userInformation[0][0]
            listTupleChat1 = backend.select_chat_contact1(connection , userId)
            for rowTuple in listTupleChat1:
                for column in rowTuple:
                    chatBoxContact1.insert(END , column)
            contact1Window.mainloop()
        else:
            loginKey = False
            loginError = customtkinter.CTkLabel(master= loginWindow , text= "Your username or password is incorrect." , text_color= "#e54c38" , bg_color= "#d7d7d7")
            loginError.place(x=310 , y=335)
    def loginBack():
        loginWindow.destroy()
        mainWindow.deiconify()
    # Buttoms And Entry And Photos
    loginBgImage = ImageTk.PhotoImage(Image.open("login_bg.png"))
    loginBg = Label(loginWindow , image=loginBgImage).pack()
    userNameLoginEntry = customtkinter.CTkEntry(master= loginWindow , width= 400 , height= 40 , placeholder_text= "Username" , corner_radius= 8 ,bg_color= "#d7d7d7")
    userNameLoginEntry.place(x=302 , y=235)
    passwordLoginEntry = customtkinter.CTkEntry(master= loginWindow , width= 400 , height= 40 , placeholder_text= "Password" , corner_radius= 8 ,bg_color= "#d7d7d7" , show= "●")
    passwordLoginEntry.place(x=302 , y=290)
    loginButtom = customtkinter.CTkButton(master= loginWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Login" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= login).place(x=313 , y=377)
    loginBackButtom = customtkinter.CTkButton(master= loginWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Back" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= loginBack).place(x=513 , y=377)
    loginWindow.mainloop()
# Welcome Page
mainWindow = Tk()
window(mainWindow)
mainBgImage = ImageTk.PhotoImage(Image.open("main_bg.png"))
mainBg = Label(mainWindow , image=mainBgImage).pack()
signinButtom = customtkinter.CTkButton(master= mainWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Sign in" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= signin).place(x=320 , y=375)
signupButtom = customtkinter.CTkButton(master= mainWindow , width= 180 , height= 30 , corner_radius= 8 , text_color= "black" , bg_color= "#d7d7d7" , fg_color= "#699bfe" , text= "Sign up" , hover_color= "#3078ff" , font= ("Calibri" , 18) , command= signup).place(x=510 , y=375)
mainWindow.mainloop()