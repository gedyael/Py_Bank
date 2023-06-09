#importaçoes
from tkinter import *
import posiciona
import time 

#iniciando o TK
master = Tk()

# Config pricipais da janela:       
# Título do banco:
master.title('Py_Bank')
# Tamanho da nossa tela:
master.geometry('323x700+610+153')
# Travar o redicionamento da tela:
master.wm_resizable(width=0,height=0)



#funçoes nova janela
def Nova_janela():
    master.destroy()
    time.sleep(0.3)
    master1 = Tk()
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
    saldo.set('0,90')
    
    # CRIAÇAO DE CAIXA DE SAIDA
    # test = Label(master1,text='pix')
    # test.place(width=76, height=30, x=2, y=144)
    #CRIAÇAO DO SEGUNDO SALDO
    test1 = Label(master1,textvariable=saldo,font='verdana  14 bold')
    test1.place(width=54, height=26, x=44, y=159)
    #botao_pix = Button(master1,)
    
    master1.mainloop()




# Importações de imagens:
# Imagem pricipal:
Imagem_Pricipal = PhotoImage(file='imagens/Tela_inicial.png') # Importando a imagem em uma variavel
#  Imagem do botão ENTRAR:
imagem_botao = PhotoImage(file='imagens/Botao.png')

# Criação da Label
TelaPricipal = Label(master,image=Imagem_Pricipal) # Criando label para imagem pricipal
TelaPricipal.pack()

botao_entrar = Label(master,image=imagem_botao)
botao_entrar.pack()


# Criação das entradas:
Entrada_Nome = Entry(master)
Entrada_Senha = Entry(master,show="*")

#Colar as linhas no código principal. OBS: a instância da classe Tk() deve ser de mesmo nome!
master.bind('<Button-1>', posiciona.inicio_place)
master.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, master))
master.bind('<Button-2>', lambda arg: posiciona.para_geometry(master))


''''''
# Botao_Ent = Button(master,image=Imagem_Botao_Entrar,borderwidth=0)
# Config de cada botão:
# Config caixa de entrada nome.
Entrada_Nome= Entry(master, borderwidth=0, font=('Verdana', 10), justify=CENTER)
Entrada_Nome.place(width=201, height=24, x=59, y=357,)

# # config Caixa de Email
Entrada_email = Entry(master, borderwidth=0, font=('Verdana', 10), justify=CENTER)
Entrada_email.place(width=197, height=26, x=62, y=412)

# Config Caixa de entrada senha.
Entrada_Senha = Entry(master, borderwidth=0, font=('Verdana', 10), justify=CENTER,show='*')
Entrada_Senha.place(width=201, height=23, x=60, y=480)

#config Botao
botao_entrar = Button(master,image=imagem_botao,borderwidth=0,command=Nova_janela)
botao_entrar.place(width=198, height=22, x=54, y=532)

master.mainloop()