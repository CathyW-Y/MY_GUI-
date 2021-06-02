# author: Catherine Wang
# email: mifwang@clarku.edu
# Cs120
import csv
from tkinter import *
from csv import reader
from collections import OrderedDict
from typing_extensions import SupportsIndex


#create a dictionary
mydict = {}
with open('20192.csv', mode = 'r') as inp:
    reader = csv.reader(inp)
    mydict = {rows[1]:rows[2] for rows in reader}
sorted_dict = OrderedDict(sorted(mydict.items()), key = lambda t: t[0])


#class GUI 
class MY_GUI():

    def __init__(self, init_window_name):
        """ A constructor class
        """
        self.init_window_name = init_window_name 
        self.init_window_name.title("Predict your happiness level based on your nationality")
        self.init_window_name.geometry('1000x1000')

    def set_init_window(self):
        """ Interace features/interactive buttons/listbox
        """ 
        #selection reaction display 
        self.var1 = StringVar() #initialize a variable to receive instruction
        #self.var1 = '' 
        self.l = Label(bg='green', font=('Arial', 30), width=50, height=10, textvariable=self.var1)
        self.l.pack()

        #button 
        self.b1 = Button(text = "select your country", width=20, height=3, padx=40, pady=20, command=self.print_selection)
        self.b1.pack()

        #initialize list box 
        sb = Scrollbar()
        self.my_listbox = Listbox(yscrollcommand = sb.set)
        self.my_listbox.pack(fill = BOTH, expand=True, padx=100)
        self.my_listbox.bind('<<ListboxSelect>>') #, self.callback)

        #insert the name of countries into listbox
        for i in sorted_dict:
            if i != 'key':
                self.my_listbox.insert(END, i)
        
    
    def print_selection(self):
        """print prediction based on selected country 
        """
        #get the index of the selected item
        value = self.my_listbox.curselection()[0]

        #retrieve the corresponding value from dictionary using index
        s = self.my_listbox.get(value)

        #differentiate response based on score:
        #if score is around 2 ~ 3:
        if float(sorted_dict[s]) >= 2.853 and float(sorted_dict[s]) <= 3.836:
             result = """Unfortunately, based on world happiness report(2019), \nyour country scored very low.\n"""
             prediction = "\nYour have a minimum chance at being happy."
        
        #if score is around 3 ~ 4:
        if float(sorted_dict[s]) > 3.835 and float(sorted_dict[s]) <= 4.819:
            result = """Unfortunately, based on world happiness report(2019), \nyour country scored relatively low. \n"""
            prediction = "\nYou have a scarce chance at being happy."
        
        #if score is around 4 ~ 5:
        if float(sorted_dict[s]) > 4.819 and float(sorted_dict[s]) <= 5.802:
            result = """Congratulation! Based on world happiness report(2019), \nyour country scored in the middle.\n"""
            prediction = "\nYou have a chance at being happy."
        
        #if score is around 5 ~ 6:
        if float(sorted_dict[s]) > 5.802 and float(sorted_dict[s]) <= 6.785:
            result = """Congratulation! Based on world happiness report(2019), \nyour country scored relatively high.\n"""
            prediction = "\nYou have many chances at being happy."
        
        #if score is around 6 ~ 7:
        if float(sorted_dict[s]) > 6.785 and float(sorted_dict[s]) <= 7.769:
            result = """Congratulation! Based on world happiness report(2019), \nyour country scored very high.\n"""
            prediction = "\nYou have an abundance of chances at being happy."

        #finalize response
        response = result + prediction+ "\n" + s + """'s score: """ + str(sorted_dict[s])

        self.var1.set(response)
    
    


#run MY_GUI()
def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    #
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()



#main function:
if __name__ == "__main__":
    gui_start()
    







