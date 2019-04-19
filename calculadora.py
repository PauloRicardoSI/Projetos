#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:23:33 2019

@author: paulo
"""
from tkinter import *

class Python_Calculadora:
    def __init__(self, corpo):
        self.frame = Frame(corpo)
        self.frame.grid()
        self.dados = Entry(corpo, width=64)
        self.dados.grid(row=1, column=0)
        botoes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "C"]
        r = 1
        c = 0
        for click in botoes:
            calc = lambda x = click:self.calcular(x)
            self.botao = Button(self.frame, text = click, width = 13, command = calc)
            self.botao.grid(row=r, column=c)
            c +=1
            if c > 3:
                c = 0
                r += 1
        
    def calcular(self, valor):
        
        if valor == "=":
            numeros = "123456789.+-*/"
            if self.dados.get()[0] not in numeros:
                self.dados.insert(self.dados.insert(END, "Operação Inválida"))
                
            try:
                total = eval(self.dados.get())
                self.dados.insert(END, "=" + str(total)) 
            except:
                self.dados.insert(END, "Erro")
                
        elif valor == "C":
            self.dados.delete(0,END)
                
        else:
            if "=" in self.dados.get():
                self.dados.delete(0,END)
            self.dados.insert(END, valor)      

root = Tk()
root.title("Calculadora")
Python_Calculadora(root)
root.mainloop()
