import tkinter


class App:
    def __init__(self):

        self.valor = 20

        self.window = tkinter.Tk()
        self.window.title('Game')
        self.window.minsize(width=360, height=640)
        self.window.maxsize(width=360, height=640)

        self.text = tkinter.Label(self.window, text='20', font='Arial 50 ', pady=50)
        self.text.pack()

        self.frame = tkinter.Frame(self.window, bg="white")
        self.frame.pack()

        self.button_plus = tkinter.Button(self.frame, text="Acrescentar", bg='green', width=20, command=self.plus)
        self.button_plus.pack(side='left')

        self.button_down = tkinter.Button(self.frame, text="Diminuir", bg='yellow', width=20, command=self.down)
        self.button_down.pack(side='left')

        self.window.mainloop()

    def plus(self):
        if self.valor < 20:
            self.valor += 1
            self.text.config(text="{}".format(self.valor))

    def down(self):
        if self.valor > 0:
            self.valor -= 1
            self.text.config(text="{}".format(self.valor))


App()
