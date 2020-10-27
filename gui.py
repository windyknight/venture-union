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

#main frame
f = Frame(win)
f.configure(bg=bgcolor)

#buttons
addAnItem = tk.Button(f, text="Add an Item", font="Times 18", bg=bgcolor, fg="black")
findAnItem = tk.Button(f, text="Find an Item", font="Times 18", bg=bgcolor, fg="black")
newCustomer = tk.Button(f, text="Register a Customer", font="Times 18", bg=bgcolor, fg="black")
findCustomer = tk.Button(f, text="Find a Customer", font="Times 18", bg=bgcolor, fg="black")
inventoryTag = tk.Button(f, text="Create an Inventory Tag", font="Times 18", bg=bgcolor, fg="black")
payment = tk.Button(f, text="Process a Payment", font="Times 18", bg=bgcolor, fg="black")
extend = tk.Button(f, text="Extend a Loan", font="Times 18", bg=bgcolor, fg="black")
expire = tk.Button(f, text="Report Expired Inventory", font="Times 18", bg=bgcolor, fg="black")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#addAnItem page                                                                                                                                                                                                                                                                                                                                                                                       
addItemFrame = Frame(win)
addItemFrame.configure(bg=bgcolor)

addItemFrameA = Frame(addItemFrame)
addItemFrameA.configure(bg=bgcolor)
addItemFrameB = Frame(addItemFrameA)
addItemFrameB.configure(bg=bgcolor)

#title
blank1 = tk.Label(addItemFrameA, text="             ", bg=bgcolor, font="Times 32",width=11)
title = tk.Label(addItemFrameA, text="Add to Item Registry", bg=bgcolor, fg="black", font="Times 32")
blank1.grid(column=0,row=0)
title.grid(column=1,row=0)

#labels & entry fields
itemAttributes = ["Item#","Category","Description","Risk Level", "Amount"]
labelWidth = 20
itemDetails = []
itemNum = 0

if str(cur.execute("SELECT COUNT(*) FROM item;")) != "None":
    itemNum = int(cur.execute("SELECT COUNT(*) FROM item;"))

i = 0
for a in itemAttributes:
    label = tk.Label(addItemFrameB, text=a, bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid", width=labelWidth)
    label.grid(column=0,row=i)
    if a == "Item#":
        label2 = tk.Label(addItemFrameB, text=itemNum+1, bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid", width=labelWidth)
        label2.grid(column=1,row=i)
        itemDetails.append(label2)
    else:
        entryField = tk.Entry(addItemFrameB, bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid", width=labelWidth)
        entryField.grid(column=1,row=i)
        itemDetails.append(entryField)
    i+=1

#button

warning = tk.Label(addItemFrameA, text="", bg=bgcolor, fg="red", font="Times 12", width=labelWidth)
def addItemAction():
    #checking for null
    
    if (itemDetails[1].get() == '') or (itemDetails[3].get() == '') or (itemDetails[4].get() == ''):
        message = ""
        if itemDetails[1].get() == '':
            message+="\nPlease provide a category."
            warning.configure(text=message)
        
        if itemDetails[3].get() == '':
            message+="\nPlease select a risk level."
            warning.configure(text=message)
            
        if itemDetails[4].get() == '':
            message+="\nPlease provide an amount."
            warning.configure(text=message)
            
    else:
        warning.configure(text="")
        cur.execute(f"INSERT INTO item VALUES ({itemDetails[0].cget('text')},'{itemDetails[1].get()}','{itemDetails[2].get()}','{itemDetails[3].get()}',{itemDetails[4].get()});")
        for a in itemDetails:
            if a == itemDetails[0]:
                a.configure(text=int(a.cget("text"))+1)
            else:
                a.configure(text="")
                
    findAnItem.configure(state=NORMAL)
    

addItemButton = tk.Button(addItemFrameA, text="Add Item", font="Times 18", bg=bgcolor, fg="black",command=addItemAction)

#back
def goBack():
    addItemFrame.grid_remove()
    f.grid()

back = tk.Button(addItemFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

addItemFrameA.grid(column=0,row=0)
addItemFrameB.grid(column=1,row=1)
addItemButton.grid(column=1,row=2)
warning.grid(column=1,row=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#findAnItem page
findItemFrame = Frame(win)
findItemFrame.configure(bg=bgcolor)

findItemFrameA = Frame(findItemFrame)
findItemFrameA.configure(bg=bgcolor)
findItemFrameB = Frame(findItemFrame)
findItemFrameB.configure(bg=bgcolor)

#title
title = tk.Label(findItemFrameA, text="Item Registry", bg=bgcolor, fg="black", font="Times 32")
title.grid(column=1,row=0)

#search
searchLabel = tk.Label(findItemFrameA, text="Search item: ", bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid")
searchLabel.grid(column=0,row=1)

searchBar = tk.Entry(findItemFrameA, width=60, font="Times 18")
searchBar.grid(column=1,row=1)

def search():        
    cur.execute(f"SELECT * FROM item WHERE description ILIKE '%{searchBar.get()}%'")
    
    rows = cur.fetchall()
    
    i = 1
    for r in rows:
        itemNum = tk.Label(findItemFrameB, text=r[0], bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
        itemNum.grid(column=0,row=i)
        category = tk.Label(findItemFrameB, text=r[1], bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=20)
        category.grid(column=1,row=i)
        description = tk.Label(findItemFrameB, text=r[2], bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=50)
        description.grid(column=2,row=i)
        risk = tk.Label(findItemFrameB, text=r[3], bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
        risk.grid(column=3,row=i)
        amount = tk.Label(findItemFrameB, text=r[4], bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=10)
        amount.grid(column=4,row=i)
        i+=1
    

searchButton = tk.Button(findItemFrameA, text="Search", font="Times 18", bg=bgcolor, fg="black",command=search)
searchButton.grid(column=2,row=1)

findItemFrameB = Frame(findItemFrame)
findItemFrameB.configure(bg=bgcolor)

#search result labels
#itemAttributes found in addAnItem page
#itemAttributes = ["Item#","Category","Description","Risk Level", "Amount"]
itemWidth = [10,20,50,10,10]

i=0
for a in itemAttributes:
    label = tk.Label(findItemFrameB, text=a, bg=bgcolor, fg="black", font="Times 12", borderwidth=1,relief="solid", width=itemWidth[i])
    label.grid(column=i,row=0)
    i+=1

#back
def goBack():
    findItemFrame.grid_remove()
    f.grid()

back = tk.Button(findItemFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

findItemFrameA.grid()
findItemFrameB.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#New customer page
newCustomerFrame = Frame(win)
newCustomerFrame.configure(bg=bgcolor)

newCustomerFrameA = Frame(newCustomerFrame)
newCustomerFrameA.configure(bg=bgcolor)
newCustomerFrameB = Frame(newCustomerFrameA)
newCustomerFrameB.configure(bg=bgcolor)

#title
blank1 = tk.Label(newCustomerFrameA, text="             ", bg=bgcolor, font="Times 32",width=11)
title = tk.Label(newCustomerFrameA, text="Add to Customer Registry", bg=bgcolor, fg="black", font="Times 32")
blank1.grid(column=0,row=0)
title.grid(column=1,row=0)

#labels
customerAttributes = ["Customer ID", "Last Name", "Given Name", "MI", "Address", "City", "Mobile", "Landline", "Postal Code", "Birth Date"]
labelWidth = 20
customerDetails = []
customerIDNum = 0

if str(cur.execute("SELECT COUNT(*) FROM item;")) != "None":
    customerIDNum = int(cur.execute("SELECT COUNT(*) FROM item;"))

i = 0
for a in customerAttributes:
    label = tk.Label(newCustomerFrameB, text=a, bg="white", fg="black", font="Times 18", borderwidth=1,relief="solid",width=labelWidth)
    label.grid(column=0,row=i)
    
    if a == "Customer ID":
        label2 = tk.Label(newCustomerFrameB, text=customerIDNum+1, bg="white", fg="black", font="Times 18", borderwidth=1,relief="solid",width=labelWidth)
        label2.grid(column=1,row=i)
        customerDetails.append(label2)
    else:
        e = tk.Entry(newCustomerFrameB, bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid", width=labelWidth)
        e.grid(column=1,row=i)
        customerDetails.append(e)
    i+=1
    
#button

warning = tk.Label(newCustomerFrameA, text="", bg=bgcolor, fg="red", font="Times 12", width=labelWidth+10)
def addCustomerAction():
    #checking for null
    
    if (customerDetails[1].get() == '') or (customerDetails[2].get() == '') or (customerDetails[4].get() == '') or (customerDetails[5].get() == '') or (customerDetails[8].get() == '') or (customerDetails[9].get() == ''):
        message = ""
        if customerDetails[1].get() == '':
            message+="\nPlease provide your last name."
            warning.configure(text=message)
            
        if customerDetails[2].get() == '':
            message+="\nPlease provide your given name."
            warning.configure(text=message)
        
        if customerDetails[4].get() == '':
            message+="\nPlease select your address."
            warning.configure(text=message)
            
        if customerDetails[5].get() == '':
            message+="\nPlease provide a city."
            warning.configure(text=message)
        
        if customerDetails[8].get() == '':
            message+="\nPlease provide your postal code."
            warning.configure(text=message)
        
        if customerDetails[9].get() == '':
            message+="\nPlease provide your birth date."
            warning.configure(text=message)
    else:
        warning.configure(text="")
        cur.execute(f"INSERT INTO customer VALUES ({customerDetails[0].cget('text')},'{customerDetails[1].get()}','{customerDetails[2].get()}','{customerDetails[3].get()}','{customerDetails[4].get()}','{customerDetails[5].get()}','{customerDetails[6].get()}','{customerDetails[7].get()}',{customerDetails[8].get()},'{customerDetails[9].get()}');")
        
        for a in itemDetails:
            if a == itemDetails[0]:
                a.configure(text=int(a.cget("text"))+1)
            else:
                a.configure(text="")
    
    print("Integrate sql for adCustomerAction() here")

regCustomerButton = tk.Button(newCustomerFrameA, text="Add Customer", font="Times 18", bg=bgcolor, fg="black",command=addCustomerAction)


#back
def goBack():
    newCustomerFrame.grid_remove()
    win.geometry(f"{width}x{height}")
    f.grid()

back = tk.Button(newCustomerFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

newCustomerFrameA.grid(column=0,row=0)
newCustomerFrameB.grid(column=1,row=1)
regCustomerButton.grid(column=1,row=2)
warning.grid(column=1,row=3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Customer Registry page
regCustomerFrame = Frame(win)
regCustomerFrame.configure(bg=bgcolor)

#subframes
regCustomerFrameA = Frame(regCustomerFrame)
regCustomerFrameA.configure(bg=bgcolor)
regCustomerFrameB = Frame(regCustomerFrame)
regCustomerFrameB.configure(bg=bgcolor)

#title
title = tk.Label(regCustomerFrameA, text="Customer Registry", bg=bgcolor, fg="black", font="Times 32")
title.grid(column=1,row=0)

#search
searchLabel = tk.Label(regCustomerFrameA, text="Search item: ", bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid")
searchLabel.grid(column=0,row=1)

searchBar = tk.Entry(regCustomerFrameA, width=60, font="Times 18")
searchBar.grid(column=1,row=1)


def search():
    #erase previous searches
    i=0
    for a in regCustomerFrameB.winfo_children():
        if i < len(customerAttributes):
            i+=1
        else:
            a.destroy()
     
    #create results for current search   
    cur.execute(f"SELECT * FROM customer WHERE last_name ILIKE '%{searchBar.get()}%'")
    
    rows = cur.fetchall()
    
    i = 1
    for r in rows:
        
        customerID = tk.Button(regCustomerFrameB, text=r[0], bg="white", fg="black", font="Times 12", wraplength=225, command=customerInfo)
        customerID.grid(column=0,row=i)
        lastName = tk.Label(regCustomerFrameB, text=r[1], bg="white", fg="black", font="Times 12", wraplength=225)
        lastName.grid(column=1,row=i)
        givenName = tk.Label(regCustomerFrameB, text=r[2], bg="white", fg="black", font="Times 12", wraplength=225)
        givenName.grid(column=2,row=i)
        middleInitial = tk.Label(regCustomerFrameB, text=r[3], bg="white", fg="black", font="Times 12", wraplength=225)
        middleInitial.grid(column=3,row=i)
        address = tk.Label(regCustomerFrameB, text=r[4], bg="white", fg="black", font="Times 12", wraplength=225)
        address.grid(column=4,row=i)
        city = tk.Label(regCustomerFrameB, text=r[5], bg="white", fg="black", font="Times 12", wraplength=225)
        city.grid(column=5,row=i)
        mobile = tk.Label(regCustomerFrameB, text=r[6], bg="white", fg="black", font="Times 12", wraplength=225)
        mobile.grid(column=6,row=i)
        landline = tk.Label(regCustomerFrameB, text=r[7], bg="white", fg="black", font="Times 12", wraplength=225)
        landline.grid(column=7,row=i)
        postalCode = tk.Label(regCustomerFrameB, text=r[8], bg="white", fg="black", font="Times 12", wraplength=225)
        postalCode.grid(column=8,row=i)
        birthDate = tk.Label(regCustomerFrameB, text=r[9], bg="white", fg="black", font="Times 12", wraplength=225)
        birthDate.grid(column=9,row=i)
        i+=1
    

searchButton = tk.Button(regCustomerFrameA, text="Search", font="Times 18", bg=bgcolor, fg="black",command=search)
searchButton.grid(column=2,row=1)

#labels
#customerAttributes found in New Customer page
#customerAttributes = ["Customer ID", "Last Name", "Given Name", "MI", "Address", "City", "Mobile", "Landline", "Postal Code", "Birth Date", "Age"]
attributeWidths = [10,10,10,5,25,12,11,10,10,10,5]

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

#payment page (labelled "Process a Payement")

#Process Payment page
processPaymentFrame = Frame(win)
processPaymentFrame.configure(bg=bgcolor)

#subframes
processPaymentFrameA = Frame(processPaymentFrame)
processPaymentFrameA.configure(bg=bgcolor)
processPaymentFrameB = Frame(processPaymentFrame)
processPaymentFrameB.configure(bg=bgcolor)

#title
title = tk.Label(processPaymentFrameA, text="Ticket Registry", bg=bgcolor, fg="black", font="Times 32")
title.grid(column=1,row=0)

#search
searchLabel = tk.Label(processPaymentFrameA, text="Search ticket: ", bg=bgcolor, fg="black", font="Times 18", borderwidth=1,relief="solid")
searchLabel.grid(column=0,row=1)

searchBar = tk.Entry(processPaymentFrameA, width=60, font="Times 18")
searchBar.grid(column=1,row=1)

def search():
	print("nothing here yet")

searchButton = tk.Button(processPaymentFrameA, text="Search and Create Reciept", font="Times 18", bg=bgcolor, fg="black",command=search)
searchButton.grid(column=2,row=1)

back
def goBack():
    processPaymentFrame.grid_remove()
    win.geometry(f"{width}x{height}")
    f.grid()

back = tk.Button(processPaymentFrameA, text="Go Back", font="Times 18", bg=bgcolor, fg="black",command=goBack)
back.grid(column=2,row=0)

processPaymentFrameA.grid()
processPaymentFrameB.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#extend page (labelled "Extend a Loan")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#expire page (labelled "Report Expired Inventory")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#functions for moving from main to other pages
def add_item():
    f.grid_remove()
    addItemFrame.grid()
    
def item_registry():
    f.grid_remove()
    findItemFrame.grid()
    
def new_customer():
    f.grid_remove()
    newCustomerFrame.grid()
    
def customer_registry():
    f.grid_remove()
    win.geometry("1080x720")
    regCustomerFrame.grid()  

def process_payment():
	f.grid_remove()
	processPaymentFrame.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#title label
blank = tk.Label(f, text="             ", bg=bgcolor, font="Times 32",width=13)
title = tk.Label(f, text="VENTURE UNION", bg=bgcolor, fg="black", font="Times 32")
blank.grid(column=0,row=0)
title.grid(column=1,row=0)

#item appraisal
addAnItem.configure(command=add_item)
findAnItem.configure(command=item_registry)
addAnItem.grid(column=1)
findAnItem.grid(column=1)

#itemNum found in addAnItem page
#itemNum = cur.execute("SELECT COUNT(*) FROM item;")

cur.execute("SELECT COUNT(*) FROM item")
for a in list(cur):
    if a[0] == 0:
        findAnItem.configure(state=DISABLED)
        break;

#loan computation and releasing
newCustomer.configure(command=new_customer)
newCustomer.grid(column=1)

findCustomer.configure(command=customer_registry)
findCustomer.grid(column=1)

cur.execute("SELECT COUNT(*) FROM customer")
for a in list(cur):
    if a[0] == 0:
        findCustomer.configure(state=DISABLED)
        break;

#inventory management
inventoryTag.configure(command=item_registry)
newCustomer.grid(column=1)

#business processes
#process payment
payment.configure(command=process_payment)
payment.grid(column=1)

extend.configure(command=item_registry)
extend.grid(column=1)

expire.configure(command=item_registry)
expire.grid(column=1)

f.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Mainloop = neverending loop, only ends on close
win.mainloop()