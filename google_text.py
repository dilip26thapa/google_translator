from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src="English", dest="Nepali"):
    translator = Translator()
    text = translator.translate(text, src=src, dest=dest)
    return text.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='skyblue')
lab_txt = Label(root, text="Translator", font=(
    "Time New Roman", 40, "bold"), bg='aqua', fg='black')
lab_txt.place(x=100, y=50, width=300, height=50)

frame = Frame(root, bg='skyblue').pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=(
    "Time New Roman", 20, "bold"), bg='aqua', fg='black')
lab_txt.place(x=100, y=100, width=300, height=20)

sor_txt = Text(frame, width=30, height=10, font=(
    "Time New Roman", 20, "bold", "italic"), wrap=WORD)
sor_txt.place(x=10, y=130, width=480, height=200)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, values=list_text, state='readonly')
comb_sor.place(x=10, y=350, width=100, height=40)
comb_sor.set("English")

button_change = Button(frame, text="Translate",
                       relief=RAISED, command=data, bg='aqua', fg='black')

button_change.place(x=130, y=350, width=150, height=40)

comb_dest = ttk.Combobox(frame, values=list_text, state='readonly')
comb_dest.place(x=300, y=350, width=100, height=40)
comb_dest.set("English")

lab_txt = Label(root, text="Dest  Text", font=(
    "Time New Roman", 20, "bold"), bg='aqua', fg='black')
lab_txt.place(x=100, y=410, width=300, height=50)

dest_txt = Text(frame, width=30, height=10, font=(
    "Time New Roman", 20, "bold", "italic"), wrap=WORD)
dest_txt.place(x=10, y=470, width=480, height=200)


root.mainloop()
