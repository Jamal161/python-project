from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

payroll = Tk()
payroll.geometry("1350x650")
payroll.resizable(0, 0)
payroll.title("Payroll Management Systems")

def exit():
    payroll.destroy()

def reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    City.set("")
    Basic.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    Pension.set("")
    StudenLoan.set("")
    NIPayment.set("")
    Deducations.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentDue.set("")

def PayRef():
    PayDate.set(time.strftime("%d/%m/%Y"))
    refPay = random.randint(20000, 709467)
    refPaid = ("PR" + str(refPay))
    Reference.set(refPaid)

    NIPay = random.randint(20000, 559467)
    NIPaid = ("NI" + str(NIPay))
    NINumber.set(NIPaid)

def PayPeriod():
    i = datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode = random.randint(1200, 3467)
    CodeNI = ("NICode" + str(NCode))
    NICode.set(CodeNI)

def MonthlySalary():
    if Basic.get() == "":
        BS = 0
    else:
        try:
            BS = float(Basic.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
            Basic.set("")

    if City.get() == "":
        CW = 0
    else:
        try:
            CW = float(City.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
            City.set("")

    if OverTime.get() == "":
        OT = 0
    else:
        try:
            OT = float(OverTime.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
            OverTime.set("")





    MTax = ((BS + CW + OT) * 0.3)
    TTax = "pln", str('%.2f' % ((MTax)))
    Tax.set(TTax)

    M_StudenLoan = ((BS + CW + OT) * 0.02)
    MM_StudenLoan = "pln", str('%.2f' % ((M_StudenLoan)))
    StudenLoan.set(MM_StudenLoan)

    M_Pension = ((BS + CW + OT) * 0.012)
    MM_Pension = "pln", str('%.2f' % ((M_Pension)))
    Pension.set(MM_Pension)

    M_NIPayment = ((BS + CW + OT) * 0.021)
    MM_NIPayment = "pln", str('%.2f' % ((M_NIPayment)))
    NIPayment.set(MM_NIPayment)

    Deduct = MTax + M_Pension + M_StudenLoan + M_NIPayment
    Deducat_Payment =  "pln", str('%.2f' % ((Deduct)))
    Deducations.set(Deducat_Payment)

    NetPayAfter = ((BS + CW + OT) - Deduct)
    NetAfter = "pln", str('%.2f' % ((NetPayAfter)))
    NetPay.set(NetAfter)

    Gross_Pay = "pln", str('%.2f' % (BS + CW + OT))
    GrossPay.set(Gross_Pay)

    TaxablePay.set(TTax)
    PensionablePay.set(MM_Pension)
    OtherPaymentDue.set("0.00")

EmployeeName = StringVar()
Address = StringVar()
Reference = StringVar()
EmployerName = StringVar()
City = StringVar()
Basic = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax = StringVar()
PostCode = StringVar()
Gender = StringVar()
PayDate = StringVar()
Pension = StringVar()
StudenLoan = StringVar()
NIPayment = StringVar()
Deducations = StringVar()
TaxPeriod = StringVar()
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionablePay = StringVar()
OtherPaymentDue = StringVar()


textInput = StringVar()

Tops=Frame(payroll, width=1350, height=50, bd=16, relief="raise")
Tops.pack(side=TOP)

LF=Frame(payroll, width=700, height=650, bd=12, relief="raise")
LF.pack(side=LEFT)

RF=Frame(payroll, width=600, height=650, bd=12, relief="raise")
RF.pack(side=RIGHT)

#==================

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Payroll Management Systems", fg="Steel blue", bd=10, anchor="w")
lblTitle.grid(row=0, column=0)

#==================

InsideLF=Frame(LF, width=700, height=100, bd=8, relief="raise")
InsideLF.pack(side=TOP)

InsideLFL=Frame(LF, width=325, height=400, bd=8, relief="raise")
InsideLFL.pack(side=LEFT)

InsideLFR=Frame(LF, width=325, height=400, bd=8, relief="raise")
InsideLFR.pack(side=RIGHT)

#==================

InsideRF=Frame(RF, width=600, height=200, bd=8, relief="raise")
InsideRF.pack(side=TOP)

InsideRFL=Frame(RF, width=300, height=400, bd=8, relief="raise")
InsideRFL.pack(side=LEFT)

InsideRFR=Frame(RF, width=300, height=400, bd=8, relief="raise")
InsideRFR.pack(side=RIGHT)

#==================Left Side

lblEmployeeName = Label(InsideLF, font=('arial', 12, 'bold'), text="Employee Name", fg="Steel blue", bd=10, anchor="w")
lblEmployeeName.grid(row=0, column=0)
txtEmployeeName = Entry(InsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg="powder blue", justify="left", textvariable = EmployeeName)
txtEmployeeName.grid(row=0, column=1)

lblAddress = Label(InsideLF, font=('arial', 12, 'bold'), text="Address", fg="Steel blue", bd=10, anchor="w")
lblAddress.grid(row=1, column=0)
txtAddress = Entry(InsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg="powder blue", justify="left", textvariable = Address)
txtAddress.grid(row=1, column=1)

lblReference = Label(InsideLF, font=('arial', 12, 'bold'), text="Reference", fg="Steel blue", bd=10, anchor="w")
lblReference.grid(row=2, column=0)
txtReference = Entry(InsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg="powder blue", justify="left", textvariable = Reference)
txtReference.grid(row=2, column=1)

lblEmployerName = Label(InsideLF, font=('arial', 12, 'bold'), text="Employer Name", fg="Steel blue", bd=10, anchor="w")
lblEmployerName.grid(row=3, column=0)
txtEmployerName = Entry(InsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg="powder blue", justify="left", textvariable = EmployerName)
txtEmployerName.grid(row=3, column=1)

#----------------------Left Left Side

lblCity = Label(InsideLFL, font=('arial', 12, 'bold'), text="City Weighting", fg="Steel blue", bd=10, anchor="w")
lblCity.grid(row=0, column=0)
txtCity = Entry(InsideLFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = City)
txtCity.grid(row=0, column=1)

lblBasic = Label(InsideLFL, font=('arial', 12, 'bold'), text="Basic Salary", fg="Steel blue", bd=10, anchor="w")
lblBasic.grid(row=1, column=0)
txtBasic = Entry(InsideLFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = Basic)
txtBasic.grid(row=1, column=1)

lblOverTime = Label(InsideLFL, font=('arial', 12, 'bold'), text="Over Time", fg="Steel blue", bd=10, anchor="w")
lblOverTime.grid(row=2, column=0)
txtOverTime = Entry(InsideLFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = OverTime)
txtOverTime.grid(row=2, column=1)

lblGrossPay = Label(InsideLFL, font=('arial', 12, 'bold'), text="Gross Pay", fg="Steel blue", bd=10, anchor="w")
lblGrossPay.grid(row=3, column=0)
lblGrossPay = Entry(InsideLFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = GrossPay)
lblGrossPay.grid(row=3, column=1)

lblNetPay = Label(InsideLFL, font=('arial', 12, 'bold'), text="Net Pay", fg="Steel blue", bd=10, anchor="w")
lblNetPay.grid(row=4, column=0)
lblNetPay = Entry(InsideLFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = NetPay)
lblNetPay.grid(row=4, column=1)

#-------------------Left Right Side
lblTax = Label(InsideLFR, font=('arial', 12, 'bold'), text="Tax", fg="Steel blue", bd=10, anchor="w")
lblTax.grid(row=0, column=0)
txtTax = Entry(InsideLFR, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = Tax)
txtTax.grid(row=0, column=1)

lblPension = Label(InsideLFR, font=('arial', 12, 'bold'), text="Pension", fg="Steel blue", bd=10, anchor="w")
lblPension.grid(row=1, column=0)
txtPension = Entry(InsideLFR, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = Pension)
txtPension.grid(row=1, column=1)

lblStudenLoan = Label(InsideLFR, font=('arial', 12, 'bold'), text="StudenLoan", fg="Steel blue", bd=10, anchor="w")
lblStudenLoan.grid(row=2, column=0)
txtStudenLoan = Entry(InsideLFR, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = StudenLoan)
txtStudenLoan.grid(row=2, column=1)

lblNIPavment = Label(InsideLFR, font=('arial', 12, 'bold'), text="NI Pavment", fg="Steel blue", bd=10, anchor="w")
lblNIPavment.grid(row=3, column=0)
txtNIPavment = Entry(InsideLFR, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = NIPayment)
txtNIPavment.grid(row=3, column=1)

lblDeducations = Label(InsideLFR, font=('arial', 12, 'bold'), text="Deducations", fg="Steel blue", bd=10, anchor="w")
lblDeducations.grid(row=4, column=0)
txtDeducations = Entry(InsideLFR, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="right", textvariable = Deducations)
txtDeducations.grid(row=4, column=1)

#==================Right Side
lblPostCode = Label(InsideRF, font=('arial', 12, 'bold'), text="Post Code", fg="Steel blue", bd=10, anchor="w")
lblPostCode.grid(row=0, column=0)
txtPostCode = Entry(InsideRF, font=('arial', 12, 'bold'), bd=10, width=50, bg="powder blue", justify="right", textvariable = PostCode)
txtPostCode.grid(row=0, column=1)

lblGender = Label(InsideRF, font=('arial', 12, 'bold'), text="Gender", fg="Steel blue", bd=10, anchor="w")
lblGender.grid(row=1, column=0)
txtGender = Entry(InsideRF, font=('arial', 12, 'bold'), bd=10, width=50, bg="powder blue", justify="right", textvariable = Gender)
txtGender.grid(row=1, column=1)

#----------------------------
lblPayDate = Label(InsideRFL, font=('arial', 12, 'bold'), text="Pay Date", fg="Steel blue", bd=10, anchor="w")
lblPayDate.grid(row=0, column=0)
txtPayDate = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = PayDate)
txtPayDate.grid(row=0, column=1)

lblTaxPeriod = Label(InsideRFL, font=('arial', 12, 'bold'), text="Tax Period", fg="Steel blue", bd=10, anchor="w")
lblTaxPeriod.grid(row=1, column=0)
txtTaxPeriod = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = TaxPeriod)
txtTaxPeriod.grid(row=1, column=1)

lblNINumber = Label(InsideRFL, font=('arial', 12, 'bold'), text="NI Number", fg="Steel blue", bd=10, anchor="w")
lblNINumber.grid(row=2, column=0)
txtNINumber = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = NINumber)
txtNINumber.grid(row=2, column=1)

lblNICode = Label(InsideRFL, font=('arial', 12, 'bold'), text="NI Code", fg="Steel blue", bd=10, anchor="w")
lblNICode.grid(row=3, column=0)
txtNICode = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = NICode)
txtNICode.grid(row=3, column=1)

lblTaxablePay = Label(InsideRFL, font=('arial', 12, 'bold'), text="Taxable Pay ", fg="Steel blue", bd=10, anchor="w")
lblTaxablePay .grid(row=4, column=0)
txtTaxablePay  = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = TaxablePay)
txtTaxablePay .grid(row=4, column=1)

lblPensionablePay = Label(InsideRFL, font=('arial', 12, 'bold'), text="Pensionable Pay", fg="Steel blue", bd=10, anchor="w")
lblPensionablePay.grid(row=5, column=0)
txtPensionablePay = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = PensionablePay)
txtPensionablePay.grid(row=5, column=1)

lblOtherPaymentDue = Label(InsideRFL, font=('arial', 12, 'bold'), text="Other Payment Due", fg="Steel blue", bd=10, anchor="w")
lblOtherPaymentDue.grid(row=6, column=0)
txtOtherPaymentDue = Entry(InsideRFL, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify="left", textvariable = OtherPaymentDue)
txtOtherPaymentDue.grid(row=6, column=1)

#----------------------
btnWagePayment = Button(InsideRFR, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=14,
                        text="Wage Paymant", bg="sky blue", command=MonthlySalary).grid(row=0, column=0)

btnReset = Button(InsideRFR, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=14,
                        text="Reset System", bg="sky blue", command=reset).grid(row=1, column=0)

btnPayRef = Button(InsideRFR, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=14,
                        text="Pay Reference", bg="sky blue", command=PayRef).grid(row=2, column=0)

btnPayCode = Button(InsideRFR, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=14,
                        text="Pay Code", bg="sky blue", command=PayPeriod).grid(row=3, column=0)

btnExit = Button(InsideRFR, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=14,
                        text="Exit", bg="sky blue", command=exit).grid(row=4, column=0)

payroll.mainloop()