from tkinter import *
from math import *
from tkinter.messagebox import *
root = Tk()



g = LabelFrame(root, text="Development Costs : Personell", padx=5, pady=5)
g.grid(row=1)

##display functions for the first pane
def show_inputs():
    answer =int(en1.get())* int(e1.get())* int(entr1.get())
    ble1.delete(0, END)
    ble1.insert(0, answer)

def show_inputs1():
    answer =int(en2.get())* int(e2.get())* int(entr2.get())
    ble2.delete(0, END)
    ble2.insert(0, answer)

def show_inputs2():
    answer =int(en3.get())* int(e3.get())* int(entr3.get())
    ble3.delete(0, END)
    ble3.insert(0, answer)

def show_inputs3():
    answer =int(en4.get())* int(e4.get())* int(entr4.get())
    ble4.delete(0, END)
    ble4.insert(0, answer)

def show_inputs4():
    answer =int(en5.get())* int(e5.get())* int(entr5.get())
    ble5.delete(0, END)
    ble5.insert(0, answer)

def show_inputs5():
    answer =int(en6.get())* int(e6.get())* int(entr6.get())
    ble6.delete(0, END)
    ble6.insert(0, answer)

def show_inputs6():
    answer =int(en7.get())* int(e7.get())* int(entr7.get())
    ble7.delete(0, END)
    ble7.insert(0, answer)

def subtotals():
    ans = int(ble1.get())+int(ble2.get())+int(ble3.get())+int(ble4.get())+int(ble5.get())+int(ble6.get())+int(ble7.get())
    ble8.delete(0, END)
    ble8.insert(0, ans)

#######functions for geting totals of 2nd pane

def show_inputs7():
    answer=int(we1.get())*int(we2.get())*int(we.get())
    we3.delete(0, END)
    we3.insert(0, answer)

######################third pane sub totals
def show_inputs8():
    ans1 =int(qe1.get())*int(re1.get())*int(ce.get())
    ans2 =int(qe2.get())*int(re2.get())*int(ce1.get())
    ans3 =int(qe3.get())*int(re3.get())*int(ce2.get())
    ans4 =int(qe4.get())*int(re4.get())*int(ce3.get())


    st1.delete(0, END)
    st2.delete(0, END)
    st3.delete(0, END)
    st4.delete(0, END)
    st1.insert(0, ans1)
    st2.insert(0, ans2)
    st3.insert(0, ans3)
    st4.insert(0, ans4)

##################pane 4 subtotals functions

def show_inputs9():
    anss1 = int(lbn1.get())*int(lbr1.get())
    anss2 = int(lbn2.get())*int(lbr2.get())

    lbk1.delete(0, END)
    lbk2.delete(0, END)
    lbk1.insert(0, anss1)
    lbk2.insert(0, anss2)

    sum=int(lbk1.get())+int(lbk2.get())
    lbr3.delete(0, END)
    lbr3.insert(0, sum)    #sum very important

##############################################pane 5 computations

def show_inputs10():
    a=int(lbnn1.get())*int(lbn11.get())
    b=int(lbnn2.get())*int(lbn22.get())
    c=int(lbnn3.get())*int(lbn33.get())

    llbnn1.delete(0, END)
    llbnn2.delete(0, END)
    llbnn3.delete(0, END)
    llbnn1.insert(0, a)
    llbnn2.insert(0, b)
    llbnn3.insert(0, c)



def combine():
    show_inputs()
    show_inputs1()
    show_inputs2()
    show_inputs3()
    show_inputs4()
    show_inputs5()
    show_inputs6()
    show_inputs7()
    show_inputs8()
    show_inputs9()
    show_inputs10()
    subtotals()

#######################total costs paramettree
def computations():
    skkra = int(llbnn1.get())+int(llbnn2.get())+int(llbnn3.get())+int(lbr3.get())+int(st1.get())+int(st2.get())+int(st3.get())+int(st4.get())+int(ble8.get())+int(we3.get())
    skra.insert(0, skkra)

    q = (30000 + 15000) / (1.09) + ((33000 + 15000) / 1.09) + ((36300 + 15000) / 1.09) + ((39930 + 15000) / (1.09))
    skra2.insert(0,q)

    npv=q - skkra#########net present value
    npv2.insert(0, npv)

    roi = (q - skkra)/skkra#############return on investment
    npv3.insert(0, roi)




def presval():
    q=((30000+15000)/1.09)+((33000+15000)/1.09)+((36300+15000)/1.09)+((39930+15000)/(1.09))


def disp():
    from tkinter import messagebox
    messagebox.showinfo("Title", "a Tk MessageBox")






####labels pane 1
group = LabelFrame(g, text="TASK")
group.grid(row=0)
Label(group, text ="System Analyst", bg="white").grid(row =1, sticky = W, padx=10, pady=15)
Label(group, text= "Programmer Analyst", bg = "white").grid(row =2, sticky=W, padx=10, pady=15)
Label(group, text= "GUI Designer", bg = "white").grid(row=3, sticky=W, padx=10,pady=15)
Label(group, text="Telecommunication Specialist", bg="white").grid(row=4, sticky=W, padx=10,pady=15)
Label(group, text="System Architect", bg="white").grid(row=5, sticky=W, padx=10,pady=15)
Label(group, text="Database Specialist", bg="white").grid(row=6, sticky=W, padx=10,pady=15)
Label(group, text="System Liblarian", bg ="white").grid(row=7, sticky=W, padx=10,pady=15)

##entry pane 2
group2= LabelFrame(g, text="NUMBER OF PERSOMELL")
group2.grid(row=0, column = 1)

en1= Entry(group2)
en1.insert(END, '0')
en1.grid(row=1, pady =15, padx=15)
en2= Entry(group2)
en2.insert(END, '0')
en2.grid(row=2, pady =15, padx=15)
en3= Entry(group2)
en3.insert(END, '0')
en3.grid(row=3, pady =15, padx=15)
en4= Entry(group2)
en4.insert(END, '0')
en4.grid(row=4, pady =15, padx=15)
en5= Entry(group2)
en5.insert(END, '0')
en5.grid(row=5, pady =15, padx=15)
en6= Entry(group2)
en6.insert(END, '0')
en6.grid(row=6, pady =15, padx=15)
en7= Entry(group2)
en7.insert(END, '0')
en7.grid(row=7, pady =15, padx=15)

##entry pane3
group1= LabelFrame(g, text="HOURS WORKED")
group1.grid(row=0, column = 2)

e1= Entry(group1)
e1.insert(END, '0')
e1.grid(row=1, pady =15, padx=15)
e2= Entry(group1)
e2.insert(END, '0')
e2.grid(row=2, pady =15, padx=15)
e3= Entry(group1)
e3.insert(END, '0')
e3.grid(row=3, pady =15, padx=15)
e4= Entry(group1)
e4.insert(END, '0')
e4.grid(row=4, pady =15, padx=15)
e5= Entry(group1)
e5.insert(END, '0')
e5.grid(row=5, pady =15, padx=15)
e6= Entry(group1)
e6.insert(END, '0')
e6.grid(row=6, pady =15, padx=15)
e7= Entry(group1)
e7.insert(END, '0')
e7.grid(row=7, pady =15, padx=15)


##entry pane 4
group3= LabelFrame(g, text="RATE PER HOUR")
group3.grid(row=0, column = 3)

entr1= Entry(group3)
entr1.insert(END, '0')
entr1.grid(row=1, pady =15, padx=15)
entr2= Entry(group3)
entr2.insert(END, '0')
entr2.grid(row=2, pady =15, padx=15)
entr3= Entry(group3)
entr3.insert(END, '0')
entr3.grid(row=3, pady =15, padx=15)
entr4= Entry(group3)
entr4.insert(END, '0')
entr4.grid(row=4, pady =15, padx=15)
entr5= Entry(group3)
entr5.insert(END, '0')
entr5.grid(row=5, pady =15, padx=15)
entr6= Entry(group3)
entr6.insert(END, '0')
entr6.grid(row=6, pady =15, padx=15)
entr7= Entry(group3)
entr7.insert(END, '0')
entr7.grid(row=7, pady =15, padx=15)

#reults summation pane

group4= LabelFrame(g, text="SUBTOTALS")
group4.grid(row=0, column = 4)

ble1= Entry(group4)
ble1.grid(row=1, pady =15, padx=15)
ble2= Entry(group4)
ble2.grid(row=2, pady =15, padx=15)
ble3= Entry(group4)
ble3.grid(row=3, pady =15, padx=15)
ble4= Entry(group4)
ble4.grid(row=4, pady =15, padx=15)
ble5= Entry(group4)
ble5.grid(row=5, pady =15, padx=15)
ble6= Entry(group4)
ble6.grid(row=6, pady =15, padx=15)
ble7= Entry(group4)
ble7.grid(row=7, pady =15, padx=15)




subt = Label(g, text="totals", padx=5, pady=5)
subt.grid(row=2, column=3)

ble8=Entry(g)
ble8.grid(row=2, column =4, pady =15, padx=15)




submit= Button(g, text="submit", command=combine)
submit.grid(row=2, column = 1)
exitbtn = Button(g, text="exit", command=g.quit, padx=20)
exitbtn.grid(row=2, column = 2)


########################### development costs training
t = LabelFrame(root, text="Development Costs : Training", padx=5, pady=5)
t.grid(row=2)

costs=LabelFrame(t, text="task", padx=5,pady=5)
costs.grid(row=1)

lab1=Label(costs,text="Oracle Training Registration")
lab1.grid(row=1)

ser = LabelFrame(t, text="no of students", padx=5, pady=5)
ser.grid(row=1, column =1)

we = Entry(ser)
we.insert(END, '0')
we.grid(row=1, padx=15,pady=15 )

ser1 = LabelFrame(t, text="rate per student", padx=5, pady=5)
ser1.grid(row=1, column =2)

we1 = Entry(ser1)
we1.insert(END, '0')
we1.grid(row=1, padx=15,pady=15 )

ser2 = LabelFrame(t, text="number of sessions", padx=5, pady=5)
ser2.grid(row=1, column =3)

we2 = Entry(ser2)
we2.insert(END, '0')
we2.grid(row=1, padx=15,pady=15 )

ser3 = LabelFrame(t, text="total", padx=5, pady=5)
ser3.grid(row=1, column =4)

we3 = Entry(ser3)
we3.grid(row=1, padx=15,pady=15 )

subt2 = Button(t, text="submit", command=combine)
subt2.grid(row=2, column =1, pady=20)


#######DEVELOPMENT COSTS NEW HARDWARE AND SOFTWARE
dc = LabelFrame(root, text="Development Costs : new HardWare and Software", padx=5, pady=5)
dc.grid(row=3)

lf =LabelFrame(dc, text="Infrastructure")
lf.grid(row=1)

lbl1=Label(lf, text="Development Server")
lbl1.grid(row=1, padx=10, pady=15)

lbl2=Label(lf, text="Server Software")
lbl2.grid(row=2, padx=10, pady=15)

lbl3=Label(lf, text="DBMS Server software")
lbl3.grid(row=3, padx=10, pady=15)

lbl4=Label(lf, text="DBMS Client Software")
lbl4.grid(row=4, padx=10, pady=15)

qtyf=LabelFrame(dc, text="Quantity")
qtyf.grid(row=1, column=1)

qe1=Entry(qtyf)
qe1.insert(END, '0')
qe1.grid(row=1,padx=15, pady=15)

qe2=Entry(qtyf)
qe2.insert(END, '0')
qe2.grid(row=2,padx=15, pady=15)

qe3=Entry(qtyf)
qe3.insert(END, '0')
qe3.grid(row=3,padx=15, pady=15)

qe4=Entry(qtyf)
qe4.insert(END, '0')
qe4.grid(row=4,padx=15, pady=15)

rat=LabelFrame(dc, text="Rate")
rat.grid(row=1, column=2)

re1=Entry(rat)
re1.insert(END, '0')
re1.grid(row=1,padx=15, pady=15)

re2=Entry(rat)
re2.insert(END, '0')
re2.grid(row=2,padx=15, pady=15)

re3=Entry(rat)
re3.insert(END, '0')
re3.grid(row=3,padx=15, pady=15)

re4=Entry(rat)
re4.insert(END, '0')
re4.grid(row=4,padx=15, pady=15)


client=LabelFrame(dc, text="no of Clients")
client.grid(row=1, column=3)

ce=Entry(client)
ce.insert(END, '0')
ce.grid(row=1,padx=15, pady=15)

ce1=Entry(client)
ce1.insert(END, '0')
ce1.grid(row=2,padx=15, pady=15)

ce2=Entry(client)
ce2.insert(END, '0')
ce2.grid(row=3,padx=15, pady=15)

ce3=Entry(client)
ce3.insert(END, '0')
ce3.grid(row=4,padx=15, pady=15)

SUBT=LabelFrame(dc, text="sub totals")
SUBT.grid(row=1, column=4)

st1 = Entry(SUBT)
st1.grid(row=1, padx=15, pady=15)

st2 = Entry(SUBT)
st2.grid(row=2, padx=15, pady=15)

st3 = Entry(SUBT)
st3.grid(row=3, padx=15, pady=15)

st4 = Entry(SUBT)
st4.grid(row=4, padx=15, pady=15)



############annual operating costs

hw1 = LabelFrame(root)
hw1.grid(row=1, column=1)

personell = LabelFrame(hw1, text="Annual Operating Costs: Personell")
personell.grid(row=1)

aoc = LabelFrame(personell, text="Title")
aoc.grid(row=1)

lb1 = Label(aoc, text="Programmer Analyst")
lb1.grid(row=1, padx=10, pady=15)

lb2 = Label(aoc, text="System Liblarian")
lb2.grid(row=2, padx=10, pady=15)

aoc1=LabelFrame(personell, text="number")
aoc1.grid(row=1, column=1)

lbn1 =Entry(aoc1)
lbn1.insert(END, '0')
lbn1.grid(row=1, padx=10, pady=15)

lbn2= Entry(aoc1)
lbn2.insert(END, '0')
lbn2.grid(row=2, padx=10, pady=15)

aoc2=LabelFrame(personell, text="rate")
aoc2.grid(row=1, column=2)

lbr1=Entry(aoc2)
lbr1.insert(END, '0')
lbr1.grid(row=1, padx=10, pady=15)

lbr2=Entry(aoc2)
lbr2.insert(END, '0')
lbr2.grid(row=2, padx=10, pady=15)

aoc3=LabelFrame(personell, text="Total")
aoc3.grid(row=1, column=3)

lbk1=Entry(aoc3)
lbk1.grid(row=1, padx=10, pady=15)

lbk2=Entry(aoc3)
lbk2.grid(row=2, padx=10, pady=15)

lbr3=Entry(personell)
lbr3.grid(row=2, column=3, padx=10, pady=15)

############################l fifth pane manenoz
hw=LabelFrame(hw1, text="Annual Operating costs - H/W, S/W, MISC")
hw.grid(row=2)



title=LabelFrame(hw, text="Title")
title.grid(row=1)

rc1=Label(title, text="Maintenance Agreement for Server")
rc1.grid(row=1, padx=10, pady=15)

rc2=Label(title, text="Maintenance Agreement for Server")
rc2.grid(row=2, padx=10, pady=15)

rc3=Label(title, text="Preprinted Forms")
rc3.grid(row=3, padx=10, pady=15)


lbnn=LabelFrame(hw, text="Number")
lbnn.grid(row=1, column=1)

lbnn1=Entry(lbnn)
lbnn1.insert(END,'0')
lbnn1.grid(row=1, padx=10, pady=15)

lbnn2=Entry(lbnn)
lbnn2.insert(END, '0')
lbnn2.grid(row=2, padx=10, pady=15)

lbnn3=Entry(lbnn)
lbnn3.insert(END, '0')
lbnn3.grid(row=3, padx=10, pady=15)

amt=LabelFrame(hw, text="amount")
amt.grid(row=1, column=2)

lbn11=Entry(amt)
lbn11.insert(END, '0')
lbn11.grid(row=1, padx=10, pady=15)

lbn22=Entry(amt)
lbn22.insert(END,'0')
lbn22.grid(row=2, padx=10, pady=15)

lbn33=Entry(amt)
lbn33.insert(END, '0')
lbn33.grid(row=3, padx=10, pady=15)


lbnn=LabelFrame(hw, text="totals")
lbnn.grid(row=1, column=3)

llbnn1=Entry(lbnn)
llbnn1.grid(row=1, padx=10, pady=15)

llbnn2=Entry(lbnn)
llbnn2.grid(row=2, padx=10, pady=15)

llbnn3=Entry(lbnn)
llbnn3.grid(row=3, padx=10, pady=15)

hw2 = LabelFrame(root, text="results from backend computations")
hw2.grid(row=2, column =1)

compu=Button(hw2, text="calculate", command=computations)
compu.grid(row=1, padx=15, pady=20)

lb=Label(hw2, text="Total Costs")
lb.grid(row=1, column=1, padx=7, pady=7)

skra=Entry(hw2)
skra.grid(row=1, column=2, padx=15,pady=15)


lb1=Label(hw2, text="Total  NPV")
lb1.grid(row=2, column=1, padx=15,pady=15)

skra2=Entry(hw2)
skra2.grid(row=2, column=2, padx=15,pady=15)


gs=Label(hw2, text="N P V")
gs.grid(row=3, column=1, padx=15,pady=15)

gs2 = Label(hw2, text="R O I")
gs2.grid(row=4, column=1, padx=15,pady=15)

npv2 = Entry(hw2)
npv2.grid(row=3, column=2, padx=15,pady=15)

npv3 = Entry(hw2)
npv3.grid(row=4, column=2, padx=15,pady=15)

root.mainloop()