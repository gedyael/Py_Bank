import tkinter as tk
from tkinter import *
import posiciona
import time


def Janela_2():

    time.sleep(0.3)
    master2 = tk.Tk()
    master2.title('Area Pix')
    master2.geometry('323x700+610+153')
    master2.wm_resizable(width=0,height=0)

    master2.bind('<Button-1>', posiciona.inicio_place)
    master2.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, master2))
    master2.bind('<Button-2>', lambda arg: posiciona.para_geometry(master2))

    TerceiraImagem = PhotoImage(file="imagens/Tela_3.png")
    Tela_ter = Label(master2,image=TerceiraImagem)
    Tela_ter.pack()

    #Criaçao dos botoes
    Entradapix= Entry(master2,borderwidth=0,font=('verdana ',12 ), justify=CENTER)
    Entradapix.place(width=195, height=21, x=62, y=337)
    
    Entrada_nome3= Entry(master2,borderwidth=0,font=('verdana ',12 ), justify=CENTER)
    Entrada_nome3.place(width=193, height=21, x=64, y=417)

    Entrada_tipo_pix = Entry(master2,borderwidth=0,font=('verdana ',12 ), justify=CENTER)
    Entrada_tipo_pix.place(width=190, height=19, x=63, y=495)
    master2.mainloop()

