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
    master1.title('Nova Janela')
    master1.geometry(('323x700+500+153'))

    

# Importações de imagens:
# Imagem pricipal:
Imagem_Pricipal = PhotoImage(file='imagens/Tela_inicial.png') # Importando a imagem em uma variavel
#  Imagem do botão ENTRAR:
# Imagem_Botao_Entrar = PhotoImage(file='imagens/Botao_Entrar.png')

# Criação da Label
TelaPricipal = Label(master,image=Imagem_Pricipal) # Criando label para imagem pricipal
TelaPricipal.pack()

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
Entrada_Nome = Entry(master, bd=2 , font=('calibre', 13), justify=CENTER)
Entrada_Nome.place(width=201, height=24, x=59, y=357,)

# # config Caixa de Email
Entrada_email = Entry(master, bd=2, font=('calibre', 13), justify=CENTER)
Entrada_email.place(width=197, height=26, x=62, y=412)

# Config Caixa de entrada senha.
Entrada_Senha = Entry(master, bd=2, font=('calibre', 15), justify=CENTER,show='*')
Entrada_Senha.place(width=201, height=23, x=60, y=480)

#config Botao
botao_entrar = Button(master,text='ENTRAR',font=('calibre',17),background='#C0C0C0',justify=CENTER,command=Nova_janela)
botao_entrar.place(width=213, height=34, x=54, y=530)

master.mainloop()