import tkinter as tk
from tkinter import *
import connect
from connect import cur

#creating a window
win = tk.Tk()

f = Frame(win)
f.configure(bg="white")

#window setup
width = 960
height = 720

win.title("Venture Union Pawnshops")
win.geometry(f"{width}x{height}")
win.configure(bg="white")
win.resizable(True,False)

customerIDVal = 1

#functions    
def item_appraisal():
    f.grid_remove()
    
    a = Frame(win)
    a.configure(bg="white")
    
    #title
    title = tk.Label(a, text="Item Registry", bg="white", fg="black", font="Times 32")
    title.grid(column=1,row=0)
    
    #search
    searchLabel = tk.Label(a, text="Search item: ", bg="white", fg="black", font="Times 18", borderwidth=1,relief="solid")
    searchLabel.grid(column=0,row=1)

    searchBar = tk.Entry(a, width=60, font="Times 18")
    searchBar.grid(column=1,row=1)

    def search():        
        #cur.execute(f"SELECT * FROM item WHERE description LIKE '%{searchBar.get()}%'")
        
        cur.close()

    searchButton = tk.Button(a, text="Search", font="Times 18", bg="white", fg="black",command=search)
    searchButton.grid(column=2,row=1)
    
    b = Frame(win)
    b.configure(bg="white")
    
    #search results
    itemNum = tk.Label(b, text="Item#", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
    itemNum.grid(column=0,row=0)
    category = tk.Label(b, text="Category", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid", width=20)
    category.grid(column=1,row=0)
    description = tk.Label(b, text="Description", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid", width=50)
    description.grid(column=2,row=0)
    risk = tk.Label(b, text="Risk Level", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
    risk.grid(column=3,row=0)
    amount = tk.Label(b, text="Amount", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
    amount.grid(column=4,row=0)
    
    #back
    
    def goBack():
        a.grid_remove()
        b.grid_remove()
        f.grid()
    
    back = tk.Button(a, text="Go Back", font="Times 18", bg="white", fg="black",command=goBack)
    back.grid(column=2,row=0)
    
    a.grid(column=0,row=0)
    b.grid(column=0,row=1)
    
def regCustomer():
    f.grid_remove()
    
    a = Frame(win)
    a.configure(bg="white")
    
    b = Frame(win)
    b.configure(bg = "white")
    
    #title
    blank = tk.Label(f, text="             ", bg="white", font="Times 32",width=13)
    title = tk.Label(a, text="Customer Information", bg="white", fg="black", font="Times 32")
    blank.grid(column=0,row=0)
    title.grid(column=1,row=0)
    
    #search
    searchLabel = tk.Label(a, text="Search item: ", bg="white", fg="black", font="Times 18", borderwidth=1,relief="solid")
    searchLabel.grid(column=0,row=1)

    searchBar = tk.Entry(a, width=60, font="Times 18")
    searchBar.grid(column=1,row=1)

    def search():        
        #cur.execute(f"SELECT * FROM item WHERE description LIKE '%{searchBar.get()}%'")
        
        cur.close()

    searchButton = tk.Button(a, text="Search", font="Times 18", bg="white", fg="black",command=search)
    searchButton.grid(column=2,row=1)
    
    b = Frame(win)
    b.configure(bg="white")
    
    #labels
    LcustomerID = tk.Label(b, text="Customer ID: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=0,row=0)
    LlastName = tk.Label(b, text="Last Name: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=1,row=0)
    LgivenName = tk.Label(b, text="Given Name: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=2,row=0)
    LmiddleInitial = tk.Label(b, text="Middle Initial: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=3,row=0)
    Laddress = tk.Label(b, text="Address: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=4,row=0)
    Lcity = tk.Label(b, text="City: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=5,row=0)
    Lmobile = tk.Label(b, text="Mobile: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=6,row=0)
    Llandline = tk.Label(b, text="Landline: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=7,row=0)
    LpostalCode = tk.Label(b, text="Postal Code: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=8,row=0)
    LbirthDate = tk.Label(b, text="Birth Date: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=9,row=0)
    Lage = tk.Label(b, text="Age: ", bg="white", fg="black", font="Times 12")
    LcustomerID.grid(column=10,row=0)
    
    customerID = tk.Label(b, text=customerIDVal, width=10, font="Times 12")
    
    #entry fields    
    lastName = tk.Entry(b, width=10, font="Times 12")
    givenName = tk.Entry(b, width=10, font="Times 12")
    middleInitial = tk.Entry(b, width=10, font="Times 12")
    address = tk.Entry(b, width=10, font="Times 12")
    city = tk.Entry(b, width=10, font="Times 12")
    mobile = tk.Entry(b, width=10, font="Times 12")
    landline = tk.Entry(b, width=10, font="Times 12")
    postalCode = tk.Entry(b, width=10, font="Times 12")
    birthDate = tk.Entry(b, width=10, font="Times 12")
    age = tk.Entry(b, width=10, font="Times 12")
    
    #back    
    def goBack():
        a.grid_remove()
        f.grid()
    
    back = tk.Button(a, text="Go Back", font="Times 18", bg="white", fg="black",command=goBack)
    back.grid(column=2,row=0)
    
    a.grid(column=0,row=0)
    
    

#title label
blank = tk.Label(f, text="             ", bg="white", font="Times 32",width=13)
title = tk.Label(f, text="VENTURE UNION", bg="white", fg="black", font="Times 32")
blank.grid(column=0,row=0)
title.grid(column=1,row=0)

#item appraisal
itemAppraisalButton = tk.Button(f, text="Find an Item", font="Times 18", bg="white", fg="black",command=item_appraisal)
itemAppraisalButton.grid(column=1,row=1)

#loan computation and releasing
newCustomer = tk.Button(f, text="Find a Customer", font="Times 18", bg="white", fg="black",command=regCustomer)
newCustomer.grid(column=1,row=2)

#inventory management
inventoryTag = tk.Button(f, text="Create an Inventory Tag", font="Times 18", bg="white", fg="black",command=item_appraisal)
newCustomer.grid(column=1,row=3)

#business processes
payment = tk.Button(f, text="Process a Payment", font="Times 18", bg="white", fg="black",command=item_appraisal)
payment.grid(column=1,row=4)

extend = tk.Button(f, text="Extend a Loan", font="Times 18", bg="white", fg="black",command=item_appraisal)
extend.grid(column=1,row=5)

expire = tk.Button(f, text="Report Expired Inventory", font="Times 18", bg="white", fg="black",command=item_appraisal)
expire.grid(column=1,row=6)

f.grid(column=0,row=0)

#Mainloop = neverending loop, only ends on close
win.mainloop()