import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
def save_to_file():
   Newfile = open ("DataFile.txt","a")
   
def supplierinformation():
    window5 = tk.Tk()
    greeting = tk.Label(window5, text = "Supplier Order")
    greeting.pack()
     

    Label = tk.Label(window5, text="SupplierID")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()


    Label = tk.Label(window5, text="ProductID")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window5, text="Name")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window5, text="Quantity")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window5,text="Street Name")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window5,text="House Number")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window5,text="Email")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window5,text="Post Code")
    Entry = tk.Entry(window5)
    Label.pack()
    Entry.pack()

    button = tk.Button(
        window5,
        text="Add Details",
        width=23 ,
        height=2,
        bg="white",
        fg="black",
)
    button.pack()

    button = tk.Button(
        window5,
        text = "Main Menu",
        width=23,
        height=2,
        bg="white",
        fg="black",
        command = mainmenu)
    button.pack()

        






def stocklevels():
    #global variable
  window4 = tk.Tk()
  greeting = tk.Label(window4,text = "Stock levels")
  greeting.pack()
 
  Label = tk.Label(window4, text="ProductID")
  Entry = tk.Entry(window4)
  Label.pack()
  Entry.pack()


  Label = tk.Label(window4,text="Name of item")
  Entry = tk.Entry(window4)
  Label.pack()
  Entry.pack()


  Label = tk.Label(window4,text="Quantity")
  Entry = tk.Entry(window4)
  Label.pack()
  Entry.pack()


  Label = tk.Label(window4,text="Date")
  Entry = tk.Entry(window4)
  Label.pack()
  Entry.pack()


  Label = tk.Label(window4,text="Price")
  Entry = tk.Entry(window4)
  Label.pack()
  Entry.pack()


  Label = tk.Label(window4,text="Product levels")
  Entry = tk.Entry(window4)
  Label.pack()
  Entry.pack()

  button = tk.Button(
        window4,
        text="Add Stock",
        width=23,
        height=2,
        bg="white",
        fg="black",
)
  button.pack()

  button = tk.Button(
        window4,
        text="Output Stock Levels",
        width=23,
        height=2,
        bg="white",
        fg="black",

        )
  button.pack()

  button = tk.Button(
        window4,
        text="Main menu",
        width=23,
        height=2,
        bg="white",
        fg="black",
        command = mainmenu)

  button.pack()

  button = tk.Button(
        window4,
        text="Low Stock levels",
        width=23,
        height=2,
        bg="white",
        fg="black",
)
  button.pack()






    
#customer information function
def customerinformation():
    #global variable
    window3 = tk.Tk()
    #greeting
    greeting = tk.Label(window3,text="Cuastomer Details")
    greeting.pack()

#generating labels for input

    Label = tk.Label(window3, text="CustomerID")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="Name")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()
    
    Label = tk.Label(window3, text="Surname")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="Email")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="Phone")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="Street Name")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="House Number")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="Post Code")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="County")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

    Label = tk.Label(window3, text="City")
    Entry = tk.Entry(window3)
    Label.pack()
    Entry.pack()

#Generating a button to save information
    button = tk.Button(window3,
    text="Add Information",
    width=23,
    height=2,
    bg="white",
    fg="black",
            #calls the orders function
    command = mainmenu
        )

    button.pack()

    button = tk.Button(
    window3,
    text="Display customer information",
    width=23,
    height=2,
    bg="white",
    fg="black",
)
    button.pack()

    button = tk.Button(
    window3,
    text="Main Menu",
    width=23,
    height=2,
    bg="white",
    fg="black",
    command = mainmenu
)
    button.pack()






        



        
#Customer orders function
def orders():
    #global variable
    window2 = tk.Tk()
    #Displaying a greeting
    greeting = tk.Label(window2, text="Online Orders")
    greeting.pack()
    #creating a label
    Label1 = tk.Label(window2, text ="OrderID")
    entry1 = tk.Entry(window2)
    Label1.pack()
    entry1.pack()
    OrderID = entry1.get()
    

    Label2 = tk.Label(window2, text ="ProductID")
    Label2_Entry = tk.Entry(window2)
    Label2.pack()
    Label2_Entry.pack()
    

    Label3 = tk.Label(window2, text ="OrderID")
    Label3_Entry = tk.Entry(window2)
    Label3.pack()
    Label3_Entry.pack()

    Label4 = tk.Label(window2, text ="CustomerID")
    Label4_Entry = tk.Entry(window2)
    Label4.pack()
    Label4_Entry.pack()

    Label5 = tk.Label(window2, text ="Quantity")
    Label5_Entry = tk.Entry(window2)
    Label5.pack()
    Label5_Entry.pack()

    Label6 = tk.Label(window2, text ="Price")
    Label6_Entry = tk.Entry(window2)
    Label6.pack()
    Label6_Entry.pack()

    Label7 = tk.Label(window2, text ="NumberOrder")
    Label7_Entry = tk.Entry(window2)
    Label7.pack()
    Label7_Entry.pack()

    Label8 = tk.Label(window2, text ="Timeslot")
    Label8_Entry = tk.Entry(window2)
    Label8.pack()
    Label8_Entry.pack()

    button = tk.Button(
    window2,
    text="Add Order",
    width=23,
    height=2,
    bg="white",
    fg="black",
    
)
    button.pack()

    button = tk.Button(
    window2,
    text="Main Menu",
    width=23,
    height=2,
    bg="white",
    fg="black",
    command = mainmenu
)
    button.pack()

    button = tk.Button(
    window2,
    text="Calendar",
    width=23,
    height=2,
    bg="white",
    fg="black",
)
    button.pack()

Newfile = open("Systemfile.txt","a")
Newfile.write(str(orders)+",")
    







    
#Main menu function 
def mainmenu():
    #global variable
    window1 = tk.Tk()
    #greeting
    greeting = tk.Label(window1, text="Main Menu")
    greeting.pack()
    #creating a interactive button
    button = tk.Button(window1,
        text="Online order",
        width=23,
        height=2,
        bg="white",
        fg="black",
        #calls the orders function
        command = orders)
    button.pack()
    button = tk.Button(window1,
        text="Customer information",
        width=23,
        height=2,
        bg="white",
        fg="black",
        #calls the customer information function
        command = customerinformation)
    button.pack()
    button = tk.Button(window1,
            text="Stock Levels",
            width=23,
            height=2,
            bg="white",
            fg="black",
        #calls the stock level function
            command = stocklevels)
    button.pack()
    button = tk.Button(window1,
            text="Supplier information",
            width=23,
            height=2,
            bg="white",
            fg="black",
            #calls the supplier function
            command = supplierinformation 
        )

    button.pack()



    
            
def validate_login():
    #username
    userName = username_entry.get()
    #password
    password = password_entry.get()
    #conditions
    if userName =="staff1" and password =="1234":
        messagebox.showinfo("Login successful","Welcome to the main menu! ")
        mainmenu()
    else:
        #error message 
        messagebox.showerror("Login failed","Please try again")
def login():
    #creating a window
    window = tk.Tk()
    greeting = tk.Label(text = "Login")
    greeting.pack()
    #entry feilds for username and password
    Label = tk.Label(text ="Login")
    greeting.pack()
    #entry feilds for username and password
    Label = tk.Label(text="Username")
    global username_entry
    username_entry = tk.Entry()
    Label.pack()
    username_entry.pack()
    Label = tk.Label(text="Password")
    global password_entry
    password_entry = tk.Entry(show="*")
    Label.pack()
    password_entry.pack()
    #creating a button
    button = tk.Button(
    text="Enter",
    width=10,
    height=2,
    bg="white",
    fg="black",
    command = validate_login
)
    button.pack()
save_to_file()
login()
