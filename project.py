import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

class Population:
    """define a class to deal with the population spreadsheet"""
    
    def __init__(self):
        """read the year, male population, female population and total population from file"""
        self.year = np.loadtxt("PopulationNZ.csv", delimiter = ',', skiprows = 1, usecols = 0)
        self.male = np.loadtxt("PopulationNZ.csv", delimiter = ',', skiprows = 1, usecols = 1)
        self.female = np.loadtxt("PopulationNZ.csv", delimiter = ',', skiprows = 1, usecols = 2)
        self.total = np.loadtxt("PopulationNZ.csv", delimiter = ',', skiprows = 1, usecols = 3)
        
    def plot_growth(self): 
        """Plot the growth of NZ population"""
        axes = plt.axes()
        axes.plot(self.year, self.total, "o-")
        axes.set_xlabel("Time (Year)")
        axes.set_ylabel("PopulationNZ (M)")
        axes.set_title("New Zealand Population Growth")
        axes.grid()
        plt.show()
        
    def plot_by_sex(self):
        """Plot NZ population by sex"""
        axes = plt.axes()
        axes.plot(self.year, self.male, "o-")
        axes.plot(self.year, self.female, "o-", color = "red")
        axes.set_xlabel("Year")
        axes.set_ylabel("PopulationNZ (Million)")
        axes.set_title("New Zealand Population Growth")
        axes.grid()
        plt.show()        

    def pop_search(self):
        """search a particular year and return the population in that year"""
        input_year = E21.get()
        if int(input_year) < 1991 or int(input_year) > 2020:
            T21.delete('1.0', END)
            T21.insert(INSERT, "Wrong number!")
        else:
            for i in range(len(self.year)):
                if  int(self.year[i]) == int(input_year):
                    T21.delete('1.0', END)
                    T21.insert(INSERT, f"Male: {int(self.male[i])}\n")
                    T21.insert(INSERT, f"Female: {int(self.female[i])}\n")
                    T21.insert(INSERT, f"Total: {int(self.total[i])}\n")
                
    def pop_predict(self):
        """predict the population after 2020"""
        coeffs = np.polyfit(self.year, self.total, deg = 1)
        a = coeffs[0]
        b = coeffs[1]
        input_year = E31.get()
        if int(input_year) < 2021:
            T31.delete('1.0', END)
            T31.insert(INSERT, "Wrong number!") 
        else:
            T31.delete('1.0', END)
            T31.insert(INSERT, f"Population will be:\n{round(a * int(input_year) + b)}")
        

class Income:
    """define a class to deal with the income spreadsheet"""
    
    def __init__(self):
        """read the category, NZ income and income of different cities from file"""
        self.cate = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 0, dtype = str)
        self.nz = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 1)
        self.auc = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 2)
        self.tau = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 3)
        self.ham = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 4)
        self.wel = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 5)
        self.chri = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 6)
        self.dun = np.loadtxt("income.csv", delimiter = ',', skiprows = 1, usecols = 7)

    def plot_income(self):
        """plot the income by city"""
        labels = self.cate
        city = C4.get()
        if city == "Auckland":
            data = self.auc
        elif city == "Tauranga":
            data = self.tau
        elif city == "Hamilton":
            data = self.ham
        elif city == "Wellington":
            data = self.wel
        elif city == "Christchurch":
            data = self.chri   
        elif city == "Dunedin":
            data = self.dun
        else:
            data = self.nz        
        fig, ax = plt.subplots()
        ax.barh(labels, data, align = 'center')
        ax.set_title(f'{city} Income Breakdown')
        plt.show()   


pop = Population() #create a Population class
inc = Income() #create a Income class

win = Tk() #create a window
win.title("New Zealand Population System") #set the window title
win.geometry("480x300") #set the window size
win.configure(bg = "green") #set the window background

#canvas does not work if I use grid function to manage the layout
#canvas = Canvas(win, width = 1000, height = 600)
#canvas.pack(expand=YES, fill=BOTH)
#photo = PhotoImage(file="nz.png")
#canvas.create_image(0, 0, image=photo, anchor=NW)



L1 = Label(win, bg = "yellow", text = "Population Charts: ").grid(row = 1, sticky = W) # create a lable

B11 = Button(win, text = "Growth Line", command = pop.plot_growth) #create a button
B11.grid(row = 1, column = 1)

B12 = Button(win, text = "Growth by Sex", command = pop.plot_by_sex) #create a button
B12.grid(row = 1, column = 2, stick = E)

L11 = Label(win, text = "", bg = "green").grid(row = 2, stick = W) #create a label


L2 = Label(win, bg = "yellow", text = "Search Population in Year: \n (Between 1991 and 2020)").grid(row = 3, sticky = W) # create a lable

E21 = Entry(win, width = 5) #create an entry
E21.grid(row = 3, column = 1)

B21 = Button(win, text = "Search", command = pop.pop_search) #create a button
B21.grid(row = 3, column = 2)


T21 = Text(win, width = 25, height = 4, selectforeground = "red") #create a text box
T21.grid(row = 4, column = 1)

L21 = Label(win, text = "", bg = "green").grid(row = 5, stick = W) #create a label

L3 = Label(win, bg = "yellow", text = "Predict Population in Year: \n(after 2020)").grid(row = 6, sticky = W) #create a label

E31 = Entry(win, width = 5) #create an entry
E31.grid(row = 6, column = 1)

B31 = Button(win, text = "Predict", command = pop.pop_predict) #create a button
B31.grid(row = 6, column = 2)

T31 = Text(win, width = 25, height = 2, selectforeground = "red") #create a text box
T31.grid(row = 7, column = 1)

L31 = Label(win, text = "", bg = "green").grid(row = 8, stick = W) #create a label


L4 = Label(win, bg = "yellow", text = "Total Personal Income: ").grid(row = 9, sticky = W) #create a label

C4 = ttk.Combobox(win, width = 10, textvariable = StringVar()) #create a combobox
C4["values"] = ("NewZealand", "Auckland", "Tauranga", "Hamilton", "Wellington", "Christchurch", "Dunedin")
C4.current(0)
C4["state"] = "readonly"
C4.grid(row = 9, column = 1)

B41 = Button(win, text = "View Chart", command = inc.plot_income) #create a button
B41.grid(row = 9, column = 2)

L41 = Label(win, text = "", bg = "green").grid(row = 10, stick = W) #create a label

mainloop()

