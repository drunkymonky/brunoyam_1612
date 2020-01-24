from tkinter import Frame, BOTH, Label, W, Tk, Text, S, N, E, Button, Listbox, END, Scrollbar, LEFT, Y, RIGHT


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Hello")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1,  weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text='Windows')
        lbl.grid(sticky=W, pady=4, padx=5)

        self.area = Listbox(self)
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4,
                  padx=5, sticky=E+W+S+N)

        scroll = Scrollbar(self.area, command=self.area.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.area.config(yscrollcommand=scroll.set)

        cbtn = Button(self, text='Close')
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text='Help')
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text='OK')
        obtn.grid(row=5, column=3)

    def add_item(self, value):
        self.area.insert(END, value)

def main():
    root = Tk()
    root.geometry('350x300+300+300')
    app = Example(root)
    for i in range(40):
        app.add_item('hello')
    root.mainloop()


if __name__ == '__main__':
    main()