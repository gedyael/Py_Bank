import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import posiciona
import time
import TelaSaldo

def Janela_2():
    time.sleep(0.3)
    master2 = tk.Tk()
    master2.title('Area Pix')
    master2.geometry('323x700+610+153')
    master2.wm_resizable(width=0,height=0)

    TerceiraImagem = PhotoImage(file="imagens/Tela_3.png")
    Tela_ter = Label(master2,image=TerceiraImagem)
    Tela_ter.pack()
    master2.mainloop()

