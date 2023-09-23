from tkinter import *
#calculadora
root = Tk()
root.title("minha calculadora")
root.geometry("488x355")
root.minsize(408, 355)
root.maxsize(408, 355)

numero1 = ' '
divisao = False
multiplica = False
adicao = False
subtracao = False

root.configure(background="#1E2551")

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg="white", bg="#a7a28f", font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2,
)

def botaoClick(num):
    e.insert(END, num)

def botaoDivisao():
    global numero1
    global divisao
    divisao = True
    numero1 = e.get()
    e.delete(0, END)

def botaoMultiplica():
    global numero1
    global multiplica
    multiplica = True
    numero1 = e.get()
    e.delete(0, END)

def botaoSubtracao():
    global numero1
    global subtracao
    subtracao = True
    numero1 = e.get()
    e.delete(0, END)

def botaoAdicao():
    global numero1
    global adicao
    adicao = True
    numero1 = e.get()
    e.delete(0, END)

def botaoLimpa():
    e.delete(0, END)

def botaoIgual():
    global adicao
    global subtracao
    global divisao
    global multiplica
    numero2 = e.get()
    e.delete(0, END)
    
    try:
        if adicao == True:
            resultado = int(numero1) + int(numero2)
        elif subtracao == True:
            resultado = int(numero1) - int(numero2)
        elif multiplica == True:
            resultado = int(numero1) * int(numero2)
        elif divisao == True:
            if numero2 == '0':
                e.insert(0, "Erro: Divisão por zero")
                return
            resultado = int(numero1) / int(numero2)
        e.insert(0, resultado)
        
        # Reinicializa as variáveis de operação
        adicao = False
        subtracao = False
        divisao = False
        multiplica = False
    except ValueError:
        e.insert(0, "Erro: Entrada inválida")

divide = Button(
    root,
    text='÷',
    pady=20,
    padx=39,
    command= botaoDivisao,
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
divide.grid(row=0, column=4)

adicao = Button(
    root,
    text='+',
    pady=20,
    padx=39,
    command= botaoAdicao,
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
adicao.grid(row=1, column=4)

subtracao = Button(
    root,
    text=' -',
    pady=20,
    padx=39,
    command= botaoSubtracao,
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
subtracao.grid(row=2, column=4)

multiplica = Button(
    root,
    text='X',
    pady=20,
    padx=38,
    command= botaoMultiplica,
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
multiplica.grid(row=3, column=4)

limpa = Button(
    root,
    text='C',
    pady=20,
    padx=40,
    command= botaoDivisao,
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
limpa.grid(row=4, column=4)

igual = Button(
    root,
    text='=',
    pady=20,
    padx=40,
    command= botaoIgual,
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
igual.grid(row=4, column=3)



um = Button(root,
    text='1',
    pady=20,
    padx=40,
    command= lambda: botaoClick(1),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
um.grid(row=1, column=1)

dois = Button(
    root,
    text='2',
    pady=20,
    padx=40,
    command= lambda: botaoClick(2),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
dois.grid(row=1, column=2)

tres = Button(
    root,
    text='3',
    pady=20,
    padx=40,
    command= lambda: botaoClick(3),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
tres.grid(row=1, column=3)

quatro = Button(
    root,
    text='4',
    pady=20,
    padx=40,
    command= lambda: botaoClick(4),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(
    root,
    text='5',
    pady=20,
    padx=40,
    command= lambda: botaoClick(5),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
cinco.grid(row=2, column=2)

seis = Button(
    root,
    text='6',
    pady=20,
    padx=40,
    command= lambda: botaoClick(6),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
seis.grid(row=2, column=3)

sete = Button(
    root,
    text='7',
    pady=20,
    padx=40,
    command= lambda: botaoClick(7),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
sete.grid(row=3, column=1)

oito = Button(
    root,
    text='8',
    pady=20,
    padx=40,
    command= lambda: botaoClick(8),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
oito.grid(row=3, column=2)

nove = Button(
    root,
    text='9',
    pady=20,
    padx=40,
    command= lambda: botaoClick(9),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
nove.grid(row=3, column=3)

zero = Button(
    root,
    text='0',
    pady=20,
    padx=91,
    command= lambda: botaoClick(0),
    fg='black',
    activeforeground='blue',
    relief=FLAT,
    font=('futura',12,'bold')
)
zero.grid(row=4,column=1, columnspan=2)

root.mainloop()