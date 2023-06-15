import tkinter as tk
from tkinter import *
import posiciona
import time 
import TelaPix


def JanelaSaldo():
    master1 = tk.Tk()
    time.sleep(0.3)
    master1 = tk.Toplevel()
    master1.title('Pybank')
    master1.geometry('323x700+610+153')

        
    #Colar as linhas no código principal. OBS: a instância da classe Tk() deve ser de mesmo nome!
    master1.bind('<Button-1>', posiciona.inicio_place)
    master1.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, master1))
    master1.bind('<Button-2>', lambda arg: posiciona.para_geometry(master1))
    #bordas de janela
    master1.wm_resizable(width=0,height=0)
    #impotaçao nova janela
    #imagem Secudaria
    imagem_secundaria = PhotoImage(file="imagens/Tela_2.png")
    #criaçao da Label
    tela_secundaria = Label(master1,image=imagem_secundaria)
    tela_secundaria.pack()
    saldo = StringVar()
    saldo.set('100,90')
    pix = StringVar()
    pix.set('PIX')
    # CRIAÇAO DE CAIXA DE SAIDA
    # test = Label(master1,text='pix')
    # test.place(width=76, height=30, x=2, y=144)
    #CRIAÇAO DO SEGUNDO SALDO
    test1 = Label(master1,textvariable=saldo,font='verdana  12 bold')
    test1.place(width=90, height=16, x=43, y=164)

    #botao2 = Label(master1,textvariable=pix,font='verdana')
    botao_pix = Button(master1,textvariable=pix,command=TelaPix.Janela_2,font='verdana 7 bold',borderwidth=0)
    botao_pix.place(width=50, height=20, x=20, y=278)
    master1.mainloop()