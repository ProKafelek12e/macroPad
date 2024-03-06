import customtkinter
import loadSave as LS
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("360x480")
app.title("Keypad")
#============
#Profile Menu
#============

#========
#Keyboard
#========
def CreateKeyboard(Profile):
    keyboard = customtkinter.CTkFrame(app,width=360,height=360)
    keyboardJson = LS.read('./data/keyboard.json')
    keyboard.pack()
    #screen
    screen = customtkinter.CTkButton(keyboard,width=202,height=58,fg_color='#444444',border_color='#828282',border_width=3,text="Display")
    screen.grid(row=0,column=0,padx=7,pady=7,columnspan=3)
    #knob
    knob = customtkinter.CTkButton(keyboard,width=62,height=62,fg_color="#444444",border_color="#828282",border_width=3,corner_radius=100,text="")
    knob.grid(row=0,column=3,padx=3,pady=3)
    #keys
    for i in keyboardJson[Profile]['keys']:
        CreateKey(keyboard,i)
def CreateKey(Frame,keys):
    key = customtkinter.CTkButton(Frame,width=58,height=58,fg_color='#444444',border_color='#828282',border_width=3,text=keys["displayName"])
    key.grid(row=keys["pos"]["row"],column=keys["pos"]["col"],padx=7,pady=7)

CreateKeyboard("Profile1")
app.mainloop()