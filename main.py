import customtkinter
import loadSave as LS
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("360x400")
app.title("Keypad")

#========
#Keyboard
#========
def CreateKeyboard(Profile):

    keyboard = customtkinter.CTkFrame(Tab.tab(Profile["name"]),width=360,height=360)
    keyboard.pack()
    #screen
    screen = customtkinter.CTkButton(keyboard,width=202,height=58,fg_color='#444444',border_color='#828282',border_width=3,text="Display",state='Disabled')
    screen.grid(row=0,column=0,padx=7,pady=7,columnspan=3)
    #knob
    knob = customtkinter.CTkButton(keyboard,width=62,height=62,fg_color="#444444",border_color="#828282",border_width=3,corner_radius=100,text="",state='Disabled')
    knob.grid(row=0,column=3,padx=3,pady=3)
    #keys
    print(Profile["name"])
    if(Profile["name"]!="Add Profile"):

        print(Profile["keys"])
        for i in Profile["keys"]:
            CreateKey(keyboard,i)


def CreateKey(Frame,keys):
    key = customtkinter.CTkButton(Frame,width=58,height=58,fg_color='#444444',border_color='#828282',border_width=3,text=keys["displayName"])
    key.grid(row=keys["pos"]["row"],column=keys["pos"]["col"],padx=7,pady=7)


#============
#Profile Menu
#============
Tab = customtkinter.CTkTabview(app,)
Profiles = LS.read('./data/keyboard.json')
for Profile in Profiles:
    Tab.add(Profile['name'])
    CreateKeyboard(Profile)
Tab.pack()
app.mainloop()