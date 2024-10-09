from tkinter import *
import time
import webbrowser as web
import pyautogui as pg


def btn_clicked():
    phone = entry0.get()
    mensagem = str(entry1.get())
    web.open("https://web.whatsapp.com/send?phone=+55"+phone+"&text="+mensagem)
    time.sleep(10)
    pg.press('enter')
    print(mensagem)


window = Tk()

window.geometry("800x700")
window.configure(bg = "#0d230f")
canvas = Canvas(
    window,
    bg = "#0d230f",
    height = 700,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    400.0, 199.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 110.0, y = 164,
    width = 580.0,
    height = 68)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    233.0, 220.5,
    image=background_img)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    400.0, 422.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 110.0, y = 312,
    width = 580.0,
    height = 218)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 100, y = 575,
    width = 600,
    height = 70)

window.resizable(False, False)
window.mainloop()
