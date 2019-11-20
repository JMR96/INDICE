from tkinter import *

prog = Tk()

prog.title("CALCULAR IMC")

lbNome = Label(prog, text="Nome Completo")
lbNome.place(x=25, y=20)

lbEnd = Label(prog, text="Endereço Completo")
lbEnd.place(x=25, y=45)

lbAlt = Label(prog, text="Altura (0.00)")
lbAlt.place(x=25, y=70)

lbPeso = Label(prog, text="Peso (kg)")
lbPeso.place(x=25, y=95)

entNome = Entry(prog, width=70)
entNome.place(x=150, y=20)

entEnd = Entry(prog, width=70)
entEnd.place(x=150, y=45)

entAlt = Entry(prog, width=70)
entAlt.place(x=150, y=70)

entPeso = Entry(prog, width=70)
entPeso.place(x=150, y=95)

def bt_click_calc():
    if(str(entAlt.get()).isascii() and str(entPeso.get()).isnumeric()):
        Alt = float(entAlt.get())
        Peso = int(entPeso.get())
        IMC = float(Peso / (Alt * Alt))
        lbResulN["text"] = round(IMC, 2)
        if IMC < 17:
            lbResulSit["text"] = "Muito Abaixo do Peso"
            lbResulSit.config(bg="yellow")
            lbResulN.config(bg="yellow")
        elif IMC < 18.5:
            lbResulSit["text"] = "Abaixo do Peso"
            lbResulSit.config(bg="yellow")
            lbResulN.config(bg="yellow")
        elif IMC < 25:
            lbResulSit["text"] = "Peso Normal"
            lbResulSit.config(bg="green")
            lbResulN.config(bg="green")
        elif IMC < 30:
            lbResulSit["text"] = "Acima do Peso"
            lbResulSit.config(bg="cyan")
            lbResulN.config(bg="cyan")
        elif IMC < 35:
            lbResulSit["text"] = "Obesidade I"
            lbResulSit.config(bg="magenta")
            lbResulN.config(bg="magenta")
        elif IMC < 40:
            lbResulSit["text"] = "Obesidade II (severa)"
            lbResulSit.config(bg="magenta")
            lbResulN.config(bg="magenta")
        elif IMC >= 40:
            lbResulSit["text"] = "Obesidade III (mórbida)"
            lbResulSit.config(bg="red")
            lbResulN.config(bg="red")
        else:
            lbResulSit["text"] = "Situação"
    else:
        lbResulN["text"] = "Digite os valores de Altura e Peso corretamente."

def bt_click_reini():
    entNome.delete(0, END)

    entEnd.delete(0, END)

    entAlt.delete(0, END)

    entPeso.delete(0, END)

    lbResulN.config(text="IMC", bg="gray")

    lbResulSit.config(text="SITUAÇÃO", bg="gray")


def bt_click_sair():
    prog.quit()



btCalc = Button(prog, width=15, text="CALCULAR", command=bt_click_calc)
btCalc.place(x=30, y=300)

btSair = Button(prog, width=15, text="SAIR", command=bt_click_sair)
btSair.place(x=480, y=300)

btReini = Button(prog, width=15, text="REINICIAR", command=bt_click_reini)
btReini.place(x=255, y=300)

lbResulN = Label(prog, text="IMC", width=11, height=5, bg="gray", font="arial 20 bold")
lbResulN.place(x=390, y=130)

lbResulSit = Label(prog, text="SITUAÇÃO", width=20, height=5, bg="gray", font="arial 20 bold")
lbResulSit.place(x=20, y=130)


prog.geometry("600x350+350+100")

prog.mainloop()