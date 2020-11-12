#Himma, Nyasia, Sophie

from tkinter import *
import random 
num = 0
root = Tk()

names= ['Himma' ,'Nyasia' ,'Logan' ,'Jonah', 'Aidan','Alex' ,'Nyeema' ,'Zoe','Justin' ,'Phillip','Matthew' 
,'Andrew' ,'Sophie' ,'Jack','Ian','Henry' ,'Angelina' ]

random.shuffle(names)

def pairs():
    global num
    
    for i in range (num):
        
        members= names.pop()
        print(members)
    print("\n")
    
def get_item_values():
    global num
    
    num=int(generator.get())
    
generator= Spinbox(root, from_=1, to=9, width= 30, command= lambda :(get_item_values()))
generator.pack()

m= Button(root, text="click me to create", width=30, command= lambda : (pairs()))
m.pack()
root.mainloop()
