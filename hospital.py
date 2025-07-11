from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
 
class Hospital: 
    #(self,root) is our window names we         have to initialse it 
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
    
        lbltitle = Label(self.root, bd=20, relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50,"bold" ))
        #now to show the title
        lbltitle.pack(side=TOP, fill=X)

        #Creating the DataFrame - box typem
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0,y=130, width=1530, height=400)

        #creating one more dataframe- at left side for PATIENT
        DataFrameLeft = LabelFrame(Dataframe,bd=10, padx=10,relief=RIDGE,
                                                    font=("arial",12,"bold"),text="PATIENT INFORMATION")
        DataFrameLeft.place(x=0,y=5,width=980, height=350)
                                                    
        #cretaing right sside frame
        DataFrameRight = LabelFrame(Dataframe,bd=10, padx=10,relief=RIDGE,
                                                    font=("arial",12,"bold"),text="PRESCRIPTION")
        DataFrameRight.place(x=990,y=5,width=460, height=350)

        #CREATING THE BUTTONS----
        #Creating the DataFrame - for buttons
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0,y=530, width=1530, height=70)

         #Creating the DataFrame - for details
         
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0,y=600, width=1530, height=190)

        #now create the Labels and Input stream (INSIDE PERSONLA INFORMATION)
         #below telling add lable in Dtaframe left(person information vala frame)
        lblNameTablet = Label(DataFrameLeft,text="Names of Tablets", font=("times new roman",12,"bold"),padx=2,pady=6) #padx->padding x
        #above one text 
        lblNameTablet.grid(row=0,column=0)
        # creating the input fied(where can type)->Combofome
        comNametablet = ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),
                                     width=33)
        #belwo is the option comes (arrow)
        comNametablet["values"] =("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        
        comNametablet.grid(row=0, column=1) 

        lblref = Label(DataFrameLeft,font=("arial",12,"bold"), text="Refrence No", padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        
        lblDose = Label(DataFrameLeft,font=("arial",12,"bold"), text="Dose:", padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        
        lblNoOftablets = Label(DataFrameLeft,font=("arial",12,"bold"), text="No of Tablets:", padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot = Label(DataFrameLeft,font=("arial",12,"bold"), text="Lot:", padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblIssueDate = Label(DataFrameLeft,font=("arial",12,"bold"), text="Issue Date:", padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate = Label(DataFrameLeft,font=("arial",12,"bold"), text="Exp Date:", padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataFrameLeft,font=("arial",12,"bold"), text="Daily Dose:", padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataFrameLeft,font=("arial",12,"bold"), text="Side Effects:", padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo = Label(DataFrameLeft,font=("arial",12,"bold"), text="Further Information:", padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure = Label(DataFrameLeft,font=("arial",12,"bold"), text="Blood Pressure:", padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage = Label(DataFrameLeft,font=("arial",12,"bold"), text="Storage Advice:", padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine = Label(DataFrameLeft,font=("arial",12,"bold"), text="Medication:", padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId = Label(DataFrameLeft,font=("arial",12,"bold"), text="Patient Id:", padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber = Label(DataFrameLeft,font=("arial",12,"bold"), text="NHS Number:", padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName = Label(DataFrameLeft,font=("arial",12,"bold"), text="Patient Name:", padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth = Label(DataFrameLeft,font=("arial",12,"bold"), text="Date of Birth:", padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataFrameLeft,font=("arial",12,"bold"), text="Patient Address:", padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)

       #Now DtaFrame Right->Prescription(where our data show which we input)
       #creating the text frame (wher we can write text in->Prescription)
        self.txtPrescription= Text(DataFrameRight,font=("arial",12,"bold"),width=46, height=16,padx=2,pady=6)
        #now to show the above line
        self.txtPrescription.grid(row=0,column=0)


        #creating buttons for submit etc

        #buttonframe->is where we want to create the buttons
        btnPrescription =Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23, height=16,padx=2,pady=6)
        #now to show this button we have to grid this
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe,text="Prescription Data",bg="red",fg="white",font=("arial",12,"bold"),width=23, height=16,padx=2,pady=6)
        #now to show this button we have to grid this
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,text="Update",bg="red",fg="white",font=("arial",12,"bold"),width=23, height=16,padx=2,pady=6)
        #now to show this button we have to grid this
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23, height=16,padx=2,pady=6)
        #now to show this button we have to grid this
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,text="Clear",bg="red",fg="white",font=("arial",12,"bold"),width=23, height=16,padx=2,pady=6)
        #now to show this button we have to grid this
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,text="Exit",bg="red",fg="white",font=("arial",12,"bold"),width=23, height=16,padx=2,pady=6)
        #now to show this button we have to grid this
        btnExit.grid(row=0, column=5)

        #now adding 2 scroll bar x and y axis
         #CREATING SCROLLBAR WITH HELP OF ttk
        scroll_x= ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        #NOW WE WILL CREATE THE Table
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameoftable","ref","dose","noOftablets",
                                                                  "lot","issueDate","expdate","dailydose","storage","NHSnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #now we pac this all
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)   

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Refrence No.")
        self.hospital_table.heading("dose",text="Dose")
        #self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        #self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        #self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
         
       
         #now to show all the headings
        self.hospital_table["show"]="headings"
        #now to pack this 
        #fill it both side
        self.hospital_table.pack(fill=BOTH,expand=1) #the new data add will expand 
        #reducing the wdth of headings
        
        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        #self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        #self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        #self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        
        

        

        
        
        
        
        



   




        
        


root = Tk()
ob=Hospital(root)
root.mainloop()

    

        