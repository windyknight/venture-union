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
    win.geometry(f"{width}x{height}")
    f.grid()

back = tk.Button(itemFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

itemFrameA.grid()
itemFrameB.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Customer Registry page
regCustomerFrame = Frame(win)
regCustomerFrame.configure(bg=bgcolor)

#subframes
regCustomerFrameA = Frame(regCustomerFrame)
regCustomerFrameA.configure(bg=bgcolor)
regCustomerFrameB = Frame(regCustomerFrame)
regCustomerFrameB.configure(bg=bgcolor)

#for A
#title
title = tk.Label(regCustomerFrameA, text="Customer Registry", bg=bgcolor, fg="black", font="Times 32")
title.grid(column=1,row=0)

#search
searchLabel = tk.Label(regCustomerFrameA, text="Search item: ", bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid")
searchLabel.grid(column=0,row=1)

searchBar = tk.Entry(regCustomerFrameA, width=60, font="Times 18")
searchBar.grid(column=1,row=1)

def search():        
    cur.execute(f"SELECT * FROM item WHERE description LIKE '%{searchBar.get()}%'")
    
    rows = cur.fetchall()
    
    i = 0
    for r in rows:
        customerID = tk.Label(regCustomerFrameB, text=r[0], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        customerID.grid(column=i,row=i)
        lastName = tk.Label(regCustomerFrameB, text=r[1], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        lastName.grid(column=i+1,row=i)
        givenName = tk.Label(regCustomerFrameB, text=r[2], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        givenName.grid(column=i+2,row=i)
        middleInitial = tk.Label(regCustomerFrameB, text=r[3], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        middleInitial.grid(column=i+3,row=i)
        address = tk.Label(regCustomerFrameB, text=r[4], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        address.grid(column=i+4,row=i)
        city = tk.Label(regCustomerFrameB, text=r[5], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        city.grid(column=i+5,row=i)
        mobile = tk.Label(regCustomerFrameB, text=r[6], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        mobile.grid(column=i+6,row=i)
        landline = tk.Label(regCustomerFrameB, text=r[7], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        landline.grid(column=i+7,row=i)
        postalCode = tk.Label(regCustomerFrameB, text=r[8], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        postalCode.grid(column=i+8,row=i)
        birthDate = tk.Label(regCustomerFrameB, text=r[9], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        birthDate.grid(column=i+9,row=i)
        age = tk.Label(regCustomerFrameB, text=r[10], bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid")
        age.grid(column=i+10,row=i)
        i+=1
    

searchButton = tk.Button(regCustomerFrameA, text="Search", font="Times 18", bg=bgcolor, fg="black",command=search)
searchButton.grid(column=2,row=1)

#labels
customerAttributes = ["Customer ID", "Last Name", "Given Name", "MI", "Address", "City", "Mobile", "Landline", "Postal Code", "Birth Date", "Age"]
attributeWidths = [10,10,10,5,25,10,10,10,10,10,5]

i = 0
for a in customerAttributes:
    label = tk.Label(regCustomerFrameB, text=a, bg="white", fg="black", font="Times 12", borderwidth=1,relief="solid",width=attributeWidths[i])
    label.grid(column=i,row=0)
    i+=1
    
#back
def goBack():
    regCustomerFrame.grid_remove()
    win.geometry(f"{width}x{height}")
    f.grid()

back = tk.Button(regCustomerFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

regCustomerFrameA.grid()
regCustomerFrameB.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#New customer page
newCustomerFrameA = Frame(win)
newCustomerFrameA.configure(bg=bgcolor)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#functions
def item_appraisal():
    f.grid_remove()
    win.geometry(f"{width}x{height}")
    itemFrame.grid()
    
def customer_registry():
    f.grid_remove()
    win.geometry("1080x720")
    regCustomerFrame.grid()    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#main frame
f = Frame(win)
f.configure(bg=bgcolor)

#title label
blank = tk.Label(f, text="             ", bg=bgcolor, font="Times 32",width=13)
title = tk.Label(f, text="VENTURE UNION", bg=bgcolor, fg="black", font="Times 32")
blank.grid(column=0,row=0)
title.grid(column=1,row=0)

#item appraisal
itemAppraisalButton = tk.Button(f, text="Find an Item", font="Times 18", bg=bgcolor, fg="black",command=item_appraisal)
itemAppraisalButton.grid(column=1,row=1)

#loan computation and releasing
findCustomer = tk.Button(f, text="Find a Customer", font="Times 18", bg=bgcolor, fg="black",command=customer_registry)
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