from tkinter import *
def intropic():
    root = Tk()
    canvas = Canvas(root, width =1584, height = 396)
    canvas.pack()
    img = PhotoImage(file=r"C:\Users\AKSHARA\OneDrive\Desktop\airline.png")
    canvas.create_image(20,20, anchor=NW, image=img)
    mainloop()

def ins():
    print(" WELCOME TO AI AIRLINE RESERVATION SERVICE!")
    print(" ENTER 1 FOR BOOKING A TICKET ")
    print(" ENTER 2 FOR CANCELLING A TICKET ")
    print(" ENTER 3 FOR CUSTOMER CARE ")

def detailsF():
    master = Tk()
    master.title("PLS ENTER YOUR REQUIREMENTS ")
    DEP=Label(master, text='Departure City ',bg="red").grid(row=0)
    DATE=Label(master, text='Date of Departure',bg="light cyan").grid(row=1)
    ARR=Label(master, text='Arrival City',bg="light green").grid(row=2)
    submit = Button(master, text="Submit", command=master.destroy).grid(row=3)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
def flightdis():
    class Table:
        def __init__(self,root):
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='yellow',bg='black',font=('MS Gothic',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
    lst = [("S_No","TIME",'FLIGHT_NAME','FLIGHT_ID'),
    (1,'06:00','AI Airlines','B7#130713'),
    (2,'08:00','Avis Airlines','A4#103899'),
    (3,'10:00','Reise Airlines','R3#456839'),
    (5,'14:00','Sichere Airlines','S4#004445'),
    (6,'18:45','Viaje Airlines','G3#858999'),
    (7,'22:22','Ostatnia Airlines','O0#755722')]
    total_rows = len(lst)
    total_columns = len(lst[0])
    root = Tk()
    t = Table(root)
    root.mainloop()

def meal():
	master = Tk()
	Label(master, text='Meal initial ',bg="red").grid(row=0)
	
	submit = Button(master, text = "Submit",command=master.destroy).grid(row=1)
	a1 = Entry(master)
	
	a1.grid(row=0, column=1)
	
	
	root = Tk()
	text = Text(root, height=20, font=('Times New Roman',20,),bg="lightyellow",fg="black")
	text.insert(INSERT, "********INDIAN VEGETARIAN MEAL (AVML)*******\n")
	text.insert(INSERT, "* This meal is available for vegetarian passengers. It is usually aromatic and spicy, and incorporates flavours from the Indian sub‑continent.\n")
	text.insert(INSERT, "*It can contain all types of vegetables, fresh fruit, dried fruits, legumes, dairy products, tofu, cereal, grains and vegetarian gelatine.\n")
	text.insert(INSERT, "----------------------------------------------------------------------------------------------------------\n")
	text.insert(INSERT, "*******Diabetic Meal (DBML)*******\n")
	text.insert(INSERT, "*This is a low‑sugar meal for passengers with diabetes, or those requiring low sugar diet.\n")
	text.insert(INSERT, "*It can contain lean meat, fish, wholegrain breads and cereals (brown rice, whole meal pasta, quinoa, barley), starchy vegetables, legumes, fresh fruit, low‑fat dairy products, plant‑based oils, and diabetic‑friendly products such as sugar‑free jam.\n")
	text.insert(INSERT, "*It does NOT contain white bread, white pasta, candies, fried foods, full‑fat sweetened dairy products, cream‑based sauces and fruits in syrup.\n")
	text.insert(INSERT, "----------------------------------------------------------------------------------------------------------\n")
	text.insert(INSERT, "*******Baby Meal (BBML)*******\n")
	text.insert(INSERT, "This meal is available on board for infants less than 2 years old. A standard range of proprietary brands of baby meals is available on board. Milk formula is also available, however we encourage parents to carry food familiar to and preferred by their babies.\n")
	text.insert(INSERT, "----------------------------------------------------------------------------------------------------------\n")
	text.pack()
	master.mainloop()
	
def detailsP():
    master = Tk()
    master.title("PLS ENTER YOUR DETAILS ")
    Passno=Label(master, text='Passport No.').grid(row=0)
    Name=Label(master, text='Name').grid(row=1)
    Gender=Label(master, text='Gender').grid(row=2)
    Phno=Label(master, text='Phone No.').grid(row=3)
    DOB=Label(master, text='DOB').grid(row=4)
    Nat=Label(master, text='Nationality').grid(row=5)
    Add=Label(master, text='residential address').grid(row=6)
    flightname=Label(master, text='FLIGHT NAME').grid(row=7)
    flightID=Label(master, text='FLIGHT ID').grid(row=8)
    flightt=Label(master,text="Departure time").grid(row=9)
    submit = Button(master, text = "Submit",command=master.destroy).grid(row=10)
    b1 = Entry(master)
    b2 = Entry(master)
    b3 = Entry(master)
    b4 = Entry(master)
    b5 = Entry(master)
    b6 = Entry(master)
    b7 = Entry(master)
    b8 = Entry(master)
    b9 = Entry(master)
    b10 = Entry(master)
    b1.grid(row=0, column=1)
    b2.grid(row=1, column=1)
    b3.grid(row=2, column=1)
    b4.grid(row=3, column=1)
    b5.grid(row=4, column=1)
    b6.grid(row=5, column=1)
    b7.grid(row=6, column=1)
    b8.grid(row=7, column=1)
    b9.grid(row=8, column=1)
    b10.grid(row=9, column=1)
# def seatingarr():
def paymentc():
    master = Tk()
    master.title("PLS ENTER YOUR BANK DETAILS ")
    Label(master, text='CARD NO.').grid(row=0)
    Label(master, text='Name').grid(row=1)
    Label(master, text='Expiry date').grid(row=2)
    Label(master, text='CVV').grid(row=3)
    submit = Button(master, text = "Submit",command=master.destroy).grid(row=4)
    c1 = Entry(master)
    c2 = Entry(master)
    c3 = Entry(master)
    c4 = Entry(master)
    c1.grid(row=0, column=1)
    c2.grid(row=1, column=1)
    c3.grid(row=2, column=1)
    c4.grid(row=3, column=1)

def paymentqr():
	root = Tk()
	canvas = Canvas(root, width = 500, height = 500)
	canvas.pack()
	img = PhotoImage(file=r"C:\Users\AKSHARA\OneDrive\Desktop\ai qr.png")
	canvas.create_image(20,20, anchor=NW, image=img)
	mainloop()

def customercare():
	root = Tk()
	canvas = Canvas(root, width = 1920, height = 1080)
	canvas.pack()
	img = PhotoImage(file=r"C:\Users\AKSHARA\OneDrive\Desktop\customer service.png")
	canvas.create_image(20,20, anchor=NW, image=img)
	mainloop()

def seatingarr():
    win = Tk()
    print("Choose the seat of your choice")
    def display_input1():
        if var1.get() == 1:
            print("ur seat is R1C1")

    def display_input2():
        if var2.get() == 1:
            print("ur seat is R2C1")

    def display_input3():
        if var3.get() == 1:
            print("ur seat is R3C1")

    def display_input4():
        if var4.get() == 1:
            print("ur seat is R4C1")

    def display_input5():
        if var5.get() == 1:
            print("ur seat is R5C1")

    def display_input6():
        if var6.get() == 1:
            print("ur seat is R6C1")

    def display_input7():
        if var7.get() == 1:
            print("ur seat is R7C1")

    def display_input8():
        if var8.get() == 1:
            print("ur seat is R8C1")

    def display_input9():
        if var9.get() == 1:
            print("ur seat is R9C1")

    def display_input10():
        if var10.get() == 1:
            print("ur seat is R10C1")

    ######################################

    def display_input11():
        if var11.get() == 1:
            print("ur seat is R1C2")

    def display_input12():
        if var12.get() == 1:
            print("ur seat is R2C2")

    def display_input13():
        if var13.get() == 1:
            print("ur seat is R3C2")

    def display_input14():
        if var14.get() == 1:
            print("ur seat is R4C2")

    def display_input15():
        if var15.get() == 1:
            print("ur seat is R5C2")

    def display_input16():
        if var16.get() == 1:
            print("ur seat is R6C2")

    def display_input17():
        if var17.get() == 1:
            print("ur seat is R7C2")

    def display_input18():
        if var18.get() == 1:
            print("ur seat is R8C2")

    def display_input19():
        if var19.get() == 1:
            print("ur seat is R9C2")

    def display_input20():
        if var20.get() == 1:
            print("ur seat is R10C2")

    ###################################

    def display_input21():
        if var21.get() == 1:
            print("ur seat is R3C4")

    def display_input22():
        if var22.get() == 1:
            print("ur seat is R4C4")

    def display_input23():
        if var23.get() == 1:
            print("ur seat is R5C4")

    def display_input24():
        if var24.get() == 1:
            print("ur seat is R6C4")

    def display_input25():
        if var25.get() == 1:
            print("ur seat is R7C4")

    def display_input26():
        if var26.get() == 1:
            print("ur seat is R8C4")

    def display_input27():
        if var27.get() == 1:
            print("ur seat is R9C4")

    def display_input28():
        if var28.get() == 1:
            print("ur seat is R10C4")

    ##################################

    def display_input29():
        if var29.get() == 1:
            print("ur seat is R3C5")

    def display_input30():
        if var30.get() == 1:
            print("ur seat is R4C5")

    def display_input31():
        if var31.get() == 1:
            print("ur seat is R5C5")

    def display_input32():
        if var32.get() == 1:
            print("ur seat is R6C5")

    def display_input33():
        if var33.get() == 1:
            print("ur seat is R7C5")

    def display_input34():
        if var34.get() == 1:
            print("ur seat is R8C5")

    def display_input35():
        if var35.get() == 1:
            print("ur seat is R9C5")

    def display_input36():
        if var36.get() == 1:
            print("ur seat is R10C5")

    ##################################

    def display_input37():
        if var37.get() == 1:
            print("ur seat is R3C6")

    def display_input38():
        if var38.get() == 1:
            print("ur seat is R4C6")

    def display_input39():
        if var39.get() == 1:
            print("ur seat is R5C6")

    def display_input40():
        if var40.get() == 1:
            print("ur seat is R6C6")

    def display_input41():
        if var41.get() == 1:
            print("ur seat is R7C6")

    def display_input42():
        if var42.get() == 1:
            print("ur seat is R8C6")

    def display_input43():
        if var43.get() == 1:
            print("ur seat is R9C6")

    def display_input44():
        if var44.get() == 1:
            print("ur seat is R10C6")

    ###################################

    def display_input45():
        if var45.get() == 1:
            print("ur seat is R1C8")

    def display_input46():
        if var46.get() == 1:
            print("ur seat is R2C8")

    def display_input47():
        if var47.get() == 1:
            print("ur seat is R3C8")

    def display_input48():
        if var48.get() == 1:
            print("ur seat is R4C8")

    def display_input49():
        if var49.get() == 1:
            print("ur seat is R5C8")

    def display_input50():
        if var50.get() == 1:
            print("ur seat is R6C8")

    def display_input51():
        if var51.get() == 1:
            print("ur seat is R7C8")

    def display_input52():
        if var52.get() == 1:
            print("ur seat is R8C8")

    def display_input53():
        if var53.get() == 1:
            print("ur seat is R9C8")

    def display_input54():
        if var54.get() == 1:
            print("ur seat is R10C8")

    ######################################

    def display_input55():
        if var55.get() == 1:
            print("ur seat is R1C9")

    def display_input56():
        if var56.get() == 1:
            print("ur seat is R2C9")

    def display_input57():
        if var57.get() == 1:
            print("ur seat is R3C9")

    def display_input58():
        if var58.get() == 1:
            print("ur seat is R4C9")

    def display_input59():
        if var59.get() == 1:
            print("ur seat is R5C9")

    def display_input60():
        if var60.get() == 1:
            print("ur seat is R6C9")

    def display_input61():
        if var61.get() == 1:
            print("ur seat is R7C9")

    def display_input62():
        if var62.get() == 1:
            print("ur seat is R8C9")

    def display_input63():
        if var63.get() == 1:
            print("ur seat is R9C9")

    def display_input64():
        if var64.get() == 1:
            print("ur seat is R10C9")
    ###################################
    def display_input():
        # Define what happens when a checkbox is checked
        pass  # Replace with your desired function

    # Main window setup
    win = Tk()
    win.title("Seating Arrangement")
    rows, columns = 10, 9

    # Create labels for rows and columns
    for x in range(rows):
        for y in range(columns):
            Label(win, text=f"C {y + 1}").grid(row=0, column=y + 1)
            Label(win, text=f"R {x + 1}").grid(row=x + 1, column=0)

    # Define IntVar list for checkboxes
    check_vars = [IntVar() for _ in range(rows * columns)]

    # Create checkboxes using loops
    for x in range(rows):
        for y in range(1, columns + 1):
            Checkbutton(win, variable=check_vars[x * columns + y - 1], onvalue=1, offvalue=0, command=display_input).grid(row=x + 1, column=y, sticky=W)

    # NEXT button to close the window
    Button(win, text="NEXT", command=win.destroy).grid(row=22, sticky=SE)

    win.mainloop()
# Function to insert customer details
def customer_details():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Akisn@277', database='cscproject')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s1 = "INSERT INTO customer_details VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Sno, b1, b2, b3, b4, b5, b6)
    cursor.execute(s1)

# Function to insert flight details
def flight_details():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Akisn@277', database='cscproject')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s2 = "INSERT INTO flight_details VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(Sno, b1, e1, e2, b10, e3)
    cursor.execute(s2)

# Payment method selection
x = int(input("ENTER THE NUMBER: "))
if x == 1:
    # Booking logic
    detailsF()
    flightdis()
    detailsP()
    seatingarr()
    meal()
    customer_details()
    flight_details()
    payment_method = int(input("To pay through card enter 1. To pay through QR code enter 2: "))
    if payment_method == 1:
        paymentc()
    elif payment_method == 2:
        paymentqr()
    print("Thank you for choosing our service! Your ticket details will be sent to your registered mobile number.")
elif x == 2:
    # Deletion logic
    passpno = input("Enter passport no. of passenger whose ticket has to be deleted: ")
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='manager', database='cscproject')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s1 = "DELETE FROM customer_details WHERE passportno = '{}'".format(passpno)
    cursor.execute(s1)
    print("Your ticket will be refunded within 6-7 working days. Thank you!")
else:
    customercare()