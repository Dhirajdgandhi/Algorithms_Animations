import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       canvas = tk.Canvas(self, width=400, height=400, bg='white', bd=2)

       canvas.create_rectangle(175, 25, 225, 75) #Parent
       canvas.create_text(200, 40, text="Boy: 50")
       canvas.create_text(200, 60, text="Girl: 50")
       canvas.create_text(290, 50, text="height > 165cm?")


       canvas.create_line(200, 75, 150, 100, fill='blue')
       canvas.create_line(200, 75, 250, 100, fill='blue')

       canvas.create_text(247, 83, text="No")
       canvas.create_text(153, 83, text="Yes")
       """
       canvas.create_rectangle(125, 100, 175, 150) #Child 1
       canvas.create_rectangle(225, 100, 275, 150) #Child 2

       canvas.create_text(250, 115, text="Boy: 10")
       canvas.create_text(250, 135, text="Girl: 40")


       canvas.create_text(150, 115, text="Boy: 40")
       canvas.create_text(150, 135, text="Girl: 10")

       canvas.create_line(150, 150, 100, 175, fill='blue')
       canvas.create_line(150, 150, 200, 175, fill='blue')

       canvas.create_text(340, 125, text="weight > 65kg?")

       canvas.create_text(196, 160, text="No")
       canvas.create_text(104, 160, text="Yes")

       canvas.create_rectangle(75, 175, 125, 225) #Grandchild 1
       canvas.create_rectangle(175, 175, 225, 225) #Grandchild 2

       canvas.create_text(200, 190, text="Boy: 5")
       canvas.create_text(200, 215, text="Girl: 7")


       canvas.create_text(100, 190, text="Boy: 35")
       canvas.create_text(100, 215, text="Girl: 3")
       """


       canvas.pack(side="top", expand=False)

       #label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       canvas = tk.Canvas(self, width=400, height=400, bg='white', bd=2)


       canvas.create_rectangle(175, 25, 225, 75) #Parent
       canvas.create_text(200, 40, text="Boy: 50")
       canvas.create_text(200, 60, text="Girl: 50")
       canvas.create_text(290, 50, text="height > 165cm?")


       canvas.create_line(200, 75, 150, 100, fill='blue')
       canvas.create_line(200, 75, 250, 100, fill='blue')

       canvas.create_text(247, 83, text="No")
       canvas.create_text(153, 83, text="Yes")

       canvas.create_rectangle(125, 100, 175, 150) #Child 1
       canvas.create_rectangle(225, 100, 275, 150) #Child 2

       canvas.create_text(250, 115, text="Boy: 10")
       canvas.create_text(250, 135, text="Girl: 40")


       canvas.create_text(150, 115, text="Boy: 40")
       canvas.create_text(150, 135, text="Girl: 10")

       canvas.create_line(150, 150, 100, 175, fill='blue')
       canvas.create_line(150, 150, 200, 175, fill='blue')

       canvas.create_text(340, 125, text="weight > 65kg?")

       canvas.create_text(196, 160, text="No")
       canvas.create_text(104, 160, text="Yes")
       """
       canvas.create_rectangle(75, 175, 125, 225) #Grandchild 1
       canvas.create_rectangle(175, 175, 225, 225) #Grandchild 2

       canvas.create_text(200, 190, text="Boy: 5")
       canvas.create_text(200, 215, text="Girl: 7")


       canvas.create_text(100, 190, text="Boy: 35")
       canvas.create_text(100, 215, text="Girl: 3")
       """


       canvas.pack(side="top", expand=False)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       canvas = tk.Canvas(self, width=400, height=400, bg='white', bd=2)

       canvas.create_rectangle(175, 25, 225, 75)  # Parent
       canvas.create_text(200, 40, text="Boy: 50")
       canvas.create_text(200, 60, text="Girl: 50")
       canvas.create_text(290, 50, text="height > 165cm?")

       canvas.create_line(200, 75, 150, 100, fill='blue')
       canvas.create_line(200, 75, 250, 100, fill='blue')

       canvas.create_text(247, 83, text="No")
       canvas.create_text(153, 83, text="Yes")

       canvas.create_rectangle(125, 100, 175, 150)  # Child 1
       canvas.create_rectangle(225, 100, 275, 150)  # Child 2

       canvas.create_text(250, 115, text="Boy: 10")
       canvas.create_text(250, 135, text="Girl: 40")

       canvas.create_text(150, 115, text="Boy: 40")
       canvas.create_text(150, 135, text="Girl: 10")

       canvas.create_line(150, 150, 100, 175, fill='blue')
       canvas.create_line(150, 150, 200, 175, fill='blue')

       canvas.create_text(340, 125, text="weight > 65kg?")

       canvas.create_text(196, 160, text="No")
       canvas.create_text(104, 160, text="Yes")

       canvas.create_rectangle(75, 175, 125, 225) #Grandchild 1
       canvas.create_rectangle(175, 175, 225, 225) #Grandchild 2

       canvas.create_text(200, 190, text="Boy: 5")
       canvas.create_text(200, 215, text="Girl: 7")


       canvas.create_text(100, 190, text="Boy: 35")
       canvas.create_text(100, 215, text="Girl: 3")


       canvas.pack(side="top", expand=False)


""" HERE BEGINS RANDOM FOREST """
""" HERE BEGINS RANDOM FOREST """
""" HERE BEGINS RANDOM FOREST """
""" HERE BEGINS RANDOM FOREST """
""" HERE BEGINS RANDOM FOREST """

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       canvas = tk.Canvas(self, width=600, height=600, bg='white', bd=2)

       canvas.create_rectangle(100, 20, 120, 40) #Parent

       canvas.create_line(110, 40, 90, 55, fill='blue')
       canvas.create_line(110, 40, 130, 55, fill='blue')

       canvas.create_rectangle(80, 55, 100, 75) #Child 1
       canvas.create_rectangle(120, 55, 140, 75) #Child 2

       canvas.create_line(90, 75, 70, 90, fill='blue')
       canvas.create_line(90, 75, 110, 90, fill='blue')

       canvas.create_rectangle(60, 90, 80, 110) #Grandchild 1
       canvas.create_rectangle(100, 90, 120, 110) #Grandchild 2


       canvas.create_text(100, 125, text="Predict Boy")

       canvas.pack(side="top", expand=False)

       #label.pack(side="top", fill="both", expand=True)

class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       canvas = tk.Canvas(self, width=600, height=600, bg='white', bd=2)

       canvas.create_rectangle(100, 20, 120, 40)  # Parent

       canvas.create_line(110, 40, 90, 55, fill='blue')
       canvas.create_line(110, 40, 130, 55, fill='blue')

       canvas.create_rectangle(80, 55, 100, 75)  # Child 1
       canvas.create_rectangle(120, 55, 140, 75)  # Child 2

       canvas.create_line(90, 75, 70, 90, fill='blue')
       canvas.create_line(90, 75, 110, 90, fill='blue')

       canvas.create_rectangle(60, 90, 80, 110)  # Grandchild 1
       canvas.create_rectangle(100, 90, 120, 110)  # Grandchild 2

       canvas.create_text(100, 125, text="Predict Boy")

       """ NEXT TREE """
       """ NEXT TREE """

       canvas.create_rectangle(200, 20, 220, 40)  # Parent

       canvas.create_line(210, 40, 190, 55, fill='blue')
       canvas.create_line(210, 40, 230, 55, fill='blue')

       canvas.create_rectangle(180, 55, 200, 75)  # Child 1
       canvas.create_rectangle(220, 55, 240, 75)  # Child 2

       canvas.create_line(190, 75, 170, 90, fill='blue')
       canvas.create_line(190, 75, 210, 90, fill='blue')

       canvas.create_rectangle(160, 90, 180, 110)  # Grandchild 1
       canvas.create_rectangle(200, 90, 220, 110)  # Grandchild 2

       canvas.create_text(200, 125, text="Predict Boy")

       canvas.pack(side="top", expand=False)

class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       canvas = tk.Canvas(self, width=600, height=600, bg='white', bd=2)

       canvas.create_rectangle(100, 20, 120, 40)  # Parent

       canvas.create_line(110, 40, 90, 55, fill='blue')
       canvas.create_line(110, 40, 130, 55, fill='blue')

       canvas.create_rectangle(80, 55, 100, 75)  # Child 1
       canvas.create_rectangle(120, 55, 140, 75)  # Child 2

       canvas.create_line(90, 75, 70, 90, fill='blue')
       canvas.create_line(90, 75, 110, 90, fill='blue')

       canvas.create_rectangle(60, 90, 80, 110)  # Grandchild 1
       canvas.create_rectangle(100, 90, 120, 110)  # Grandchild 2

       canvas.create_text(100, 125, text="Predict Boy")

       """ NEXT TREE """
       """ NEXT TREE """

       canvas.create_rectangle(200, 20, 220, 40)  # Parent

       canvas.create_line(210, 40, 190, 55, fill='blue')
       canvas.create_line(210, 40, 230, 55, fill='blue')

       canvas.create_rectangle(180, 55, 200, 75)  # Child 1
       canvas.create_rectangle(220, 55, 240, 75)  # Child 2

       canvas.create_line(190, 75, 170, 90, fill='blue')
       canvas.create_line(190, 75, 210, 90, fill='blue')

       canvas.create_rectangle(160, 90, 180, 110)  # Grandchild 1
       canvas.create_rectangle(200, 90, 220, 110)  # Grandchild 2

       canvas.create_text(200, 125, text="Predict Boy")

       """ NEXT TREE """
       """ NEXT TREE """

       canvas.create_rectangle(200, 160, 220, 180)  # Parent

       canvas.create_line(210, 180, 190, 195, fill='blue')
       canvas.create_line(210, 180, 230, 195, fill='blue')

       canvas.create_rectangle(180, 195, 200, 215)  # Child 1
       canvas.create_rectangle(220, 195, 240, 215)  # Child 2

       canvas.create_line(190, 215, 170, 230, fill='blue')
       canvas.create_line(190, 215, 210, 230, fill='blue')

       canvas.create_rectangle(160, 230, 180, 250)  # Grandchild 1
       canvas.create_rectangle(200, 230, 220, 250)  # Grandchild 2

       canvas.create_text(200, 265, text="Predict Boy")

       """ NEXT TREE """
       """ NEXT TREE """

       canvas.create_rectangle(100, 160, 120, 180)  # Parent

       canvas.create_line(110, 180, 90, 195, fill='blue')
       canvas.create_line(110, 180, 130, 195, fill='blue')

       canvas.create_rectangle(80, 195, 100, 215)  # Child 1
       canvas.create_rectangle(120, 195, 140, 215)  # Child 2

       canvas.create_line(90, 215, 70, 230, fill='blue')
       canvas.create_line(90, 215, 110, 230, fill='blue')

       canvas.create_rectangle(60, 230, 80, 250)  # Grandchild 1
       canvas.create_rectangle(100, 230, 120, 250)  # Grandchild 2

       canvas.create_text(100, 265, text="Predict Girl")

       canvas.create_text(150, 290, text=".")
       canvas.create_text(150, 300, text=".")
       canvas.create_text(150, 310, text=".")
       canvas.create_text(150, 320, text=".")
       canvas.create_text(150, 330, text=".")
       canvas.create_text(150, 340, text=".")

       """ NEXT TREE """
       """ NEXT TREE """

       canvas.create_rectangle(100, 360, 120, 380)  # Parent

       canvas.create_line(110, 380, 90, 395, fill='blue')
       canvas.create_line(110, 380, 130, 395, fill='blue')

       canvas.create_rectangle(80, 395, 100, 415)  # Child 1
       canvas.create_rectangle(120, 395, 140, 415)  # Child 2

       canvas.create_line(90, 415, 70, 430, fill='blue')
       canvas.create_line(90, 415, 110, 430, fill='blue')

       canvas.create_rectangle(60, 430, 80, 450)  # Grandchild 1
       canvas.create_rectangle(100, 430, 120, 450)  # Grandchild 2

       canvas.create_text(100, 465, text="Predict Boy")

       canvas.create_rectangle(40, 10, 270, 500)
       canvas.create_line(270, 260, 310, 260, fill='blue', arrow=tk.LAST)
       canvas.create_text(390, 260, text="Random Forest: BOY")


       canvas.pack(side="top", expand=False)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
     tk.Frame.__init__(self, *args, **kwargs)
     p1 = Page1(self)
     p2 = Page2(self)
     p3 = Page3(self)
     p4 = Page4(self)
     p5 = Page5(self)
     p6 = Page6(self)

     buttonframe = tk.Frame(self)
     container = tk.Frame(self)
     buttonframe.pack(side="top", fill="x", expand=False)
     container.pack(side="top", fill="both", expand=True)

     p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
     p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
     p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

     p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
     p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
     p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

     b1 = tk.Button(buttonframe, text="Tree 1", command=p1.lift)
     b2 = tk.Button(buttonframe, text="Tree 2", command=p2.lift)
     b3 = tk.Button(buttonframe, text="Tree 3", command=p3.lift)

     b4 = tk.Button(buttonframe, text="Random Forest 1", command=p4.lift)
     b5 = tk.Button(buttonframe, text="Random Forest 2", command=p5.lift)
     b6 = tk.Button(buttonframe, text="Random Forest 3", command=p6.lift)

     b1.pack(side="left")
     b2.pack(side="left")
     b3.pack(side="left")
     b4.pack(side="left")
     b5.pack(side="left")
     b6.pack(side="left")

     p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("650x650")
    root.mainloop()