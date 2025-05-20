from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel, Label, Listbox, END
import sqlite3
import os
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Downloads\build\assets\frame0")

# Create database table if not exists
def create_table():
    conn = sqlite3.connect('syllabus.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS syllabus (
            subject TEXT PRIMARY KEY,
            pdf_path TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Generic function to open a subject window and list its PDFs
def open_subject_window(subject):
    new_window = Toplevel(window)
    new_window.title(subject)
    new_window.geometry("400x300")
    new_window.configure(bg="#FFFFFF")

    header_canvas = Canvas(
        new_window,
        bg="#FFFFFF",
        height=60,
        width=320,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    header_canvas.pack()
    header_bg_image = PhotoImage(file=relative_to_assets("image_1.png"))
    header_canvas.create_image(200, 30, image=header_bg_image)
    header_canvas.image = header_bg_image

    header_canvas.create_text(
        160, 30,
        text=f"{subject} Syllabus PDFs",
        fill="#FE0000",
        font=("Arial", 9, "bold")
    )

    listbox = Listbox(new_window, width=50)
    listbox.pack(pady=10)

    subject_folder = os.path.join(OUTPUT_PATH, subject) # folder path like syllabus/Computer Engineering
    if os.path.exists(subject_folder):
        for filename in os.listdir(subject_folder):
            if filename.endswith(".pdf"):
                listbox.insert(END, filename)

    def on_select(event):
        selection = listbox.curselection()
        if selection:
            file = listbox.get(selection[0])
            file_path = os.path.abspath(os.path.join(subject_folder, file))
            webbrowser.open_new(file_path)

    listbox.bind("<<ListboxSelect>>", on_select)

# GUI Setup
window = Tk()
window.geometry("700x500")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_text(
    100.0,
    38.0,
    anchor="nw",
    text="COMPUTER ENGINEERING 1ST SEMESTER REVIEWER",
    fill="#FE0000",
    font=("InstrumentSans Regular", 22 * -1)
)

# Images
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(343.0, 160.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(343.0, 278.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(343.0, 395.0, image=image_image_3)

canvas.create_text(129.0, 150.0, anchor="nw", text="COMPUTER ENGINEERING AS DISCIPLINE", fill="#FE0000", font=("IstokWeb Regular", 20 * -1))
canvas.create_text(129.0, 269.0, anchor="nw", text="CHEMISTRY", fill="#FE0000", font=("IstokWeb Regular", 20 * -1))
canvas.create_text(129.0, 380.0, anchor="nw", text="DIFFERENTIAL CALCULUS", fill="#FE0000", font=("IstokWeb Regular", 20 * -1))

# Icons
image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
canvas.create_image(47.0, 49.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
canvas.create_image(76.0, 162.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
canvas.create_image(75.0, 281.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
canvas.create_image(74.0, 395.0, image=image_image_7)

# Buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_subject_window("CHEMISTRY"),
    relief="flat"
)
button_1.place(x=596.6667, y=271.6667, width=18.6667, height=18.6667)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_subject_window("COMPUTER ENGINEERING AS DISCIPLINE"),
    relief="flat"
)
button_2.place(x=596.0, y=152.0, width=18.6667, height=18.6667)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_subject_window("DIFFERENTIAL CALCULUS"),
    relief="flat"
)
button_3.place(x=595.0, y=387.0, width=18.6667, height=18.6667)

window.resizable(False, False)
window.mainloop()
