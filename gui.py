import tkinter as tk
from tkinter import *
import connect
from connect import cur

#creating a window
win = tk.Tk()

#window setup
width = 960
height = 720
bgcolor = "white"

win.title("Venture Union Pawnshops")
win.geometry(f"{width}x{height}")
win.configure(bg=bgcolor)
win.resizable(False,False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#item appraisal page
itemFrame = Frame(win)
itemFrame.configure(bg=bgcolor)

itemFrameA = Frame(itemFrame)
itemFrameA.configure(bg=bgcolor)

#title
title = tk.Label(itemFrameA, text="Item Registry", bg=bgcolor, fg="black", font="Times 32")
title.grid(column=1,row=0)

#search
searchLabel = tk.Label(itemFrameA, text="Search item: ", bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid")
searchLabel.grid(column=0,row=1)

searchBar = tk.Entry(itemFrameA, width=60, font="Times 18")
searchBar.grid(column=1,row=1)

def search():        
    cur.execute(f"SELECT * FROM item WHERE description LIKE '%{searchBar.get()}%'")
    
    rows = cur.fetchall()
    
    for r in rows:
        itemNum = tk.Label(b, text="Item#", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
        itemNum.grid(column=0,row=0)
        category = tk.Label(b, text="Category", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=20)
        category.grid(column=1,row=0)
        description = tk.Label(b, text="Description", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=50)
        description.grid(column=2,row=0)
        risk = tk.Label(b, text="Risk Level", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
        risk.grid(column=3,row=0)
        amount = tk.Label(b, text="Amount", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
        amount.grid(column=4,row=0)
    

searchButton = tk.Button(itemFrameA, text="Search", font="Times 18", bg=bgcolor, fg="black",command=search)
searchButton.grid(column=2,row=1)

itemFrameB = Frame(itemFrame)
itemFrameB.configure(bg=bgcolor)

#search results
LitemNum = tk.Label(itemFrameB, text="Item#", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
LitemNum.grid(column=0,row=0)
Lcategory = tk.Label(itemFrameB, text="Category", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=20)
Lcategory.grid(column=1,row=0)
Ldescription = tk.Label(itemFrameB, text="Description", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=50)
Ldescription.grid(column=2,row=0)
Lrisk = tk.Label(itemFrameB, text="Risk Level", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
Lrisk.grid(column=3,row=0)
Lamount = tk.Label(itemFrameB, text="Amount", bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
Lamount.grid(column=4,row=0)

#back

def goBack():
    itemFrame.grid_remove()
    f.grid()

back = tk.Button(itemFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

itemFrameA.grid()
itemFrameB.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Customer Registry page
regCustomerFrame = Frame(win)
regCustomerFrame.configure(bg=bgcolor)

regCustomerFrameA = Frame(regCustomerFrame)
regCustomerFrameA.configure(bg=bgcolor)
regCustomerFrameB = Frame(regCustomerFrame)
regCustomerFrameB.configure(bg=bgcolor)

#labels
LcustomerID = tk.Label(regCustomerFrameB, text="Customer ID", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
LlastName = tk.Label(regCustomerFrameB, text="Last Name", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
LgivenName = tk.Label(regCustomerFrameB, text="Given Name", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
LmiddleInitial = tk.Label(regCustomerFrameB, text="MI", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
Laddress = tk.Label(regCustomerFrameB, text="Address", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
Lcity = tk.Label(regCustomerFrameB, text="City", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
Lmobile = tk.Label(regCustomerFrameB, text="Mobile", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
Llandline = tk.Label(regCustomerFrameB, text="Landline", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
LpostalCode = tk.Label(regCustomerFrameB, text="Postal Code", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
LbirthDate = tk.Label(regCustomerFrameB, text="Birth Date", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
Lage = tk.Label(regCustomerFrameB, text="Age", bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#New customer page
newCustomerFrameA = Frame(win)
newCustomerFrameA.configure(bg=bgcolor)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#functions
def item_appraisal():
    f.grid_remove()
    itemFrame.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#main frame
f = Frame(win)

#title label
blank = tk.Label(f, text="             ", bg=bgcolor, font="Times 32",width=13)
title = tk.Label(f, text="VENTURE UNION", bg=bgcolor, fg="black", font="Times 32")
blank.grid(column=0,row=0)
title.grid(column=1,row=0)

#item appraisal
itemAppraisalButton = tk.Button(f, text="Find an Item", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
itemAppraisalButton.grid(column=1,row=1)

#loan computation and releasing
findCustomer = tk.Button(f, text="Find a Customer", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
findCustomer.grid(column=1,row=2)

newCustomer = tk.Button(f, text="Register a Customer", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
newCustomer.grid(column=1,row=3)

#inventory management
inventoryTag = tk.Button(f, text="Create an Inventory Tag", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
newCustomer.grid(column=1,row=4)

#business processes
payment = tk.Button(f, text="Process a Payment", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
payment.grid(column=1,row=5)

extend = tk.Button(f, text="Extend a Loan", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
extend.grid(column=1,row=6)

expire = tk.Button(f, text="Report Expired Inventory", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
expire.grid(column=1,row=7)

f.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Mainloop = neverending loop, only ends on close
win.mainloop()