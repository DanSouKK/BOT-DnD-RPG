#!/usr/bin/env python
#coding=utf-8
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import inspect
from Personagem import *
import Classes

lista_classes = [m[0] for m in inspect.getmembers(Classes, inspect.isclass) if m[1].__module__ == 'Classes']
lista_classes.remove("Class")

personagem = Personagem()

atualizar = False
clear = False
stop = False

class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)

        fileMenu.add_command(label="New", underline=1, command=self.NewChar)
        fileMenu.add_command(label="Load...", underline=1, command=self.LoadChar)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        helpMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=helpMenu)

        helpMenu.add_command(label="Instruções", underline=1, command=self.instr)
        helpMenu.add_command(label="About...", underline=1, command=self.About)

    def NewChar(self):
        global personagem
        personagem = Personagem()

        global clear
        clear = True

    def LoadChar(self):
        char = askopenfilename()
        global personagem
        personagem = load_personagem(char)
        global atualizar
        atualizar = True

    def mensagem(self, title, string):
        tkMessageBox.showinfo(title, string)

    def instr(self):
        string = "Para criar um novo personagem basta preencher os campos e clicar em 'salvar' ou digitar 'enter'."
        string += "\n"
        string += "Apenas o nome, atributos e classes adicionadas são salvos. O life, nível, bba e testes de resistência são calculados automaticamente."
        string += "\n"
        string += "Não preencher tais campos :D"
        string += "\n\n"
        string += "Para carregar um personagem existente basta selecionar a opção 'load...' do menu 'file'."
        string += "\n\n"
        string += "Para adiciona uma classe ao personagem basta clicar em 'Configurar classe' e preencher os campos da nova janela."

        self.mensagem("Instruções", string)

    def About(self):
        string = "O RPG Filler é um programa para automatizar a criação de personagens para o sistema de rpg D&D 3.5."
        string += "\n"
        string += "Para mais informações acessar https://github.com/rodrigondec/RPG-Filler"
        self.mensagem("about", string)

    def quit(self):
        global stop
        stop = True

class Application(Frame):

    def event_salvar_char(self, event):
        self.salvar_char()

    def salvar_char(self):
        if not self.entry_nome.get() or not self.entry_for.get() or not self.entry_dex.get() or not self.entry_con.get() or not self.entry_int.get() or not self.entry_sab.get() or not self.entry_car.get():
            self.mensagem("Erro", "Prencha o campo de nome e de atributos antes de salvar!")
            return
        if  not self.entry_for.get().isdigit() or not self.entry_dex.get().isdigit() or not self.entry_con.get().isdigit() or not self.entry_int.get().isdigit() or not self.entry_sab.get().isdigit() or not self.entry_car.get().isdigit():
            self.mensagem("Erro", "Prencha os campos de atributos com números para salvar!")
            return

        global personagem

        personagem.nome = self.entry_nome.get()
        personagem.atributos['for'] = int(self.entry_for.get())
        personagem.atributos['dex'] = int(self.entry_dex.get())
        personagem.atributos['con'] = int(self.entry_con.get())
        personagem.atributos['int'] = int(self.entry_int.get())
        personagem.atributos['sab'] = int(self.entry_sab.get())
        personagem.atributos['car'] = int(self.entry_car.get())

        personagem.atualizar()
        self.clr()
        self.att()

    def NewClass(self):
        self.t = Toplevel(self)
        self.t.wm_title("Configurar Classe")
        self.t.bind("<Return>", self.event_salvar_classe)

        self.label_lista_classe = Label(self.t, text="Classe: ").grid(row=0)
        self.lista_classes = Listbox(self.t, selectmode=BROWSE)
        self.lista_classes.grid(row=0, column=1)

        for classe in lista_classes:
            self.lista_classes.insert(END, classe)

        self.label_cnivel = Label(self.t, text="Nível: ").grid(row=1, column=0)
        self.entry_cnivel = Entry(self.t)
        self.entry_cnivel.grid(row=1, column=1)

        self.button = Button(self.t)
        self.button["text"] = "Cadastrar",
        self.button["command"] = self.salvar_classe
        self.button.grid(row=2, columnspan=2)

    def event_salvar_classe(self, event):
        self.salvar_classe()

    def salvar_classe(self):
        if not self.entry_cnivel.get() or not self.lista_classes.curselection():
            self.mensagem("Erro", "Selecione a classe e digite o nível da classe")
            return
        if  not self.entry_cnivel.get().isdigit():
            self.mensagem("Erro", "Prencha os campos de atributos com números para salvar!")
            return

        nome_classe = self.lista_classes.get(self.lista_classes.curselection()[0])
        modul = __import__("Classes")
        class_ = getattr(modul, nome_classe)
        classe = class_(int(self.entry_cnivel.get()))
        personagem.set_class(classe)
        self.t.withdraw()
        if personagem.nome:
            self.att()
            self.att_classe()
        else:
            self.att_classe()

    def RmvClass(self):        
        self.t_r = Toplevel(self)
        self.t_r.wm_title("Remover Classe")
        self.t_r.bind("<Return>", self.event_rmv_classe)

        self.label_lista_classe_r = Label(self.t_r, text="Classe: ").grid(row=0)
        self.lista_classes_r = Listbox(self.t_r, selectmode=BROWSE)
        self.lista_classes_r.grid(row=0, column=1)

        for classe in personagem.classes:
            self.lista_classes_r.insert(END, classe)

        self.button_r = Button(self.t_r)
        self.button_r["text"] = "Remover",
        self.button_r["command"] = self.rmv_classe
        self.button_r.grid(row=2, columnspan=2)

    def event_rmv_classe(self, event):
        self.rmv_classe()

    def rmv_classe(self):
        if not self.lista_classes_r.curselection():
            self.mensagem("Erro", "Selecione a classe")
            return
        print personagem
        del personagem.classes[self.lista_classes_r.get(self.lista_classes_r.curselection()[0])]
        print personagem

        self.t_r.withdraw()
        if personagem.nome:
            self.att()
            self.att_classe()
        else:
            self.att_classe()

    def clr(self):
        self.entry_nome.delete(0, END)
        self.entry_for.delete(0, END)
        self.entry_dex.delete(0, END)
        self.entry_con.delete(0, END)
        self.entry_int.delete(0, END)
        self.entry_sab.delete(0, END)
        self.entry_car.delete(0, END)
        
    def att_classe(self):
        global personagem

        string = ""
        counter = 0
        for index in personagem.classes:
            counter += 1
            string += index + " ("+str(personagem.classes[index].nivel)+") "
            if len(personagem.classes) != counter:
                string += "\n"
        self.string_classes.set(string)

        self.string_bba.set(str(personagem.bba))

        self.string_fort.set(str(personagem.fortitude))
        self.string_ref.set(str(personagem.reflexos))
        self.string_von.set(str(personagem.vontade))

    def att(self): 
        self.clr()
        self.att_classe()
        global personagem

        self.entry_nome.insert(0, personagem.nome)  

        self.entry_for.insert(0, str(personagem.atributos['for']))
        self.entry_dex.insert(0, str(personagem.atributos['dex'])) 
        self.entry_con.insert(0, str(personagem.atributos['con'])) 
        self.entry_int.insert(0, str(personagem.atributos['int'])) 
        self.entry_sab.insert(0, str(personagem.atributos['sab'])) 
        self.entry_car.insert(0, str(personagem.atributos['car'])) 

        self.string_life.set(str(personagem.life))
        self.string_lvl.set(str(personagem.nivel))

    def createWidgets(self):
        self.label_nome = Label(self, text="Nome: ").grid(row=0, column=0)
        self.entry_nome = Entry(self, width=17)
        self.entry_nome.grid(row=0, column=1 ,columnspan=3)

        self.label_for = Label(self, text="For: ").grid(row=1, column=0)
        self.entry_for = Entry(self, width=5)
        self.entry_for.grid(row=1, column=1)

        self.label_dex = Label(self, text="Dex: ").grid(row=2, column=0)
        self.entry_dex = Entry(self, width=5)
        self.entry_dex.grid(row=2, column=1)

        self.label_con = Label(self, text="Con: ").grid(row=3, column=0)
        self.entry_con = Entry(self, width=5)
        self.entry_con.grid(row=3, column=1)

        self.label_int = Label(self, text="Int: ").grid(row=1, column=2)
        self.entry_int = Entry(self, width=5)
        self.entry_int.grid(row=1, column=3)

        self.label_sab = Label(self, text="Sab: ").grid(row=2, column=2)
        self.entry_sab = Entry(self, width=5)
        self.entry_sab.grid(row=2, column=3)

        self.label_car = Label(self, text="Car: ").grid(row=3, column=2)
        self.entry_car = Entry(self, width=5)
        self.entry_car.grid(row=3, column=3)

        self.label_lvl = Label(self, text="Nivel: ").grid(row=4, column=0)
        self.string_lvl = StringVar()
        self.entry_lvl = Label(self, textvariable=self.string_lvl, width=5)
        self.entry_lvl.grid(row=4, column=1)

        self.label_life = Label(self, text="Life: ").grid(row=4, column=2)
        self.string_life = StringVar()
        self.entry_life = Label(self, textvariable=self.string_life, width=5)
        self.entry_life.grid(row=4, column=3)

        self.label_classes = Label(self, text="Classes: ").grid(row=5, column=0)
        self.string_classes = StringVar()
        self.entry_classes = Label(self, textvariable=self.string_classes, width=17)
        self.entry_classes.grid(row=5, column=1, columnspan=3)

        self.label_bba = Label(self, text="BBA: ").grid(row=6, column=0)
        self.string_bba = StringVar()
        self.entry_bba = Label(self, textvariable=self.string_bba, width=5)
        self.entry_bba.grid(row=6, column=1)

        self.label_fort = Label(self, text="FORT: ").grid(row=6, column=2)
        self.string_fort = StringVar()
        self.entry_fort = Label(self, textvariable=self.string_fort, width=5)
        self.entry_fort.grid(row=6, column=3)

        self.label_ref = Label(self, text="REF: ").grid(row=7, column=0)
        self.string_ref = StringVar()
        self.entry_ref = Label(self, textvariable=self.string_ref, width=5)
        self.entry_ref.grid(row=7, column=1)

        self.label_von = Label(self, text="VON: ").grid(row=7, column=2)
        self.string_von = StringVar()
        self.entry_von = Label(self, textvariable=self.string_von, width=5)
        self.entry_von.grid(row=7, column=3)

        self.cadastrar_char = Button(self)
        self.cadastrar_char["text"] = "Salvar"
        self.cadastrar_char["command"] = self.salvar_char
        self.cadastrar_char.grid(row=8, column=0, columnspan=4)

        self.remover_classe = Button(self)
        self.remover_classe["text"] = "Remover Classe"
        self.remover_classe["command"] = self.RmvClass
        self.remover_classe.grid(row=9, column=0, columnspan=2)

        self.cadastrar_classe = Button(self)
        self.cadastrar_classe["text"] = "Configurar Classe"
        self.cadastrar_classe["command"] = self.NewClass
        self.cadastrar_classe.grid(row=9, column=2, columnspan=2)

    def mensagem(self, title, string):
        tkMessageBox.showinfo(title, string)

    def event_exit(self, event):
        global stop
        stop = True

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
        menubar = MenuBar(self)
        master.config(menu=menubar)
        master.bind("<Escape>", self.event_exit)
        master.bind("<Return>", self.event_salvar_char)

root = Tk()
root.wm_title("RPG Filler")
# root.resizable(width=False, height=False)
# root.geometry('{}x{}'.format(300, 270))

app = Application(master=root)

while True:
    if atualizar:
        app.att()
        atualizar = False
    if clear:
        app.clr()
        clear = False
    if stop:
        break
    app.update_idletasks()
    app.update()

root.destroy()