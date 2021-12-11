from tkinter import*
window= Tk()

window.geometry("1280x700")

window.title("BILLING SYSTEM")

window.configure(background="black")


#--------------CALCULATION METHODS--------------------------
def calculate():
    
    KARAHI= e1.get(1)
    PULAO= e2.get(2)
    HALEEM= e3.get(4)
    BIRYANI= e4.get(6)
    HANDI= e5.get(2)
    CHICKEN_TIKKA= e6.get(3)
    MALAI_BOOTI= e7.get(2)
    SEEKH_KABAB= e8.get(5)
    SALAD= e9.get(5)
    COLD_DRINK= e10.get(2)
    NAAN= e11.get(5)
    CHAPATI= e12.get(43)
    CAKE= e13.get(6)
    KULFI= e14.get(53)
    KHEER= e15.get(2)
    total=((int(KARAHI)*200)+(int(PULAO)*150)+(int(HALEEM)*170)+(int(BIRYANI)*160)+(int(HANDI)*250)+(int(CHICKEN_TIKKA)*130)+(int(MALAI_BOOTI)*350)+(int(SEEKH_KABAB)*190)+(int(SALAD)*100)+(int(COLD_DRINK)*50)+(int(NAAN)*10)+(int(CHAPATI)*10)+(int(CAKE)*160)+(int(KULFI)*140)+(int(KHEER)*140))
    label= Label(window, text=total, font=("Lucida Handwriting", 24), foreground="red", background="black")
    label.place(x=500, y= 610)
    label= Label(window, text="YOUR BILL IS : RS" , foreground="white", font=("Lucida Handwriting", 24), background="black")
    label.place(x=100, y=610)
    

#---------------------HEADING-----------
label0= Label(window, font= ("Lucida Handwriting", 28) , text="BILLING SYSTEM", background="light green")
label0.place(x=450,y=10)


#-------------------creating menu section-----------------------

label1= Label(window, font= ("Lucida Handwriting", 18), text="\t MENU\t\t\t\t\t\t\t\t", background="light green", foreground="red")
label1.place(x=750,y=80)

label2= Label(window, font= ("Lucida Console", 16), text="\t\tDISHES:\t\t\t\t\t\t\t\t\t", background="light pink", foreground="blue")
label2.place(x=750,y=120)

label2= Label(window, font= "times 10 bold", text=" KARAHI\t\t\t\t\t\tRS:200\t\t\t\t ", background="#d1c279")
label2.place(x=750,y=150)

label3= Label(window, font= "times 10 bold", text=" PULAO\t\t\t\t\t\tRS:200\t\t\t\t", background="#d1c279")
label3.place(x=750,y=180)

label4= Label(window, font= "times 10 bold", text=" HALEEM\t\t\t\t\t\tRS:170\t\t\t\t", background="#d1c279")
label4.place(x=750,y=210)

label5= Label(window, font= "times 10 bold", text=" BIRYANI\t\t\t\t\t\tRS:160\t\t\t\t", background="#d1c279")
label5.place(x=750,y=240)

label6= Label(window, font= "times 10 bold", text=" HANDI\t\t\t\t\t\tRS:250\t\t\t\t\t", background="#d1c279")
label6.place(x=750,y=270)

label7= Label(window, font= "times 10 bold", text=" CHICKEN TIKKA\t\t\t\t\tRS:130\t\t\t\t\t", background="#d1c279")
label7.place(x=750,y=300)

label8= Label(window, font= "times 10 bold", text=" MALAI BOOTI\t\t\t\t\tRS:350\t\t\t\t\t ", background="#d1c279")
label8.place(x=750,y=330)

label9= Label(window, font= "times 10 bold", text=" SEEKH KABAB\t\t\t\t\tRS:190\t\t\t\t\t", background="#d1c279")
label9.place(x=750,y=360)


#-------------------------EXTRAS----------

label10= Label(window, font= ("Lucida Console", 16), text="\t\tEXTRAS:\t\t\t\t\t\t\t\t", background="light pink", foreground="blue")
label10.place(x=750,y=390)

label11= Label(window, font= "times 10 bold", text=" SALAD\t\t\t\t\t\t RS:100\t\t\t\t", background="#d1c279")
label11.place(x=750,y=420)

label12= Label(window, font= "times 10 bold", text=" COLDDRINK \t\t\t\t\t RS: 50\t\t\t\t", background="#d1c279")
label12.place(x=750,y=450)

label13= Label(window, font= "times 10 bold", text=" NAAN\t\t\t\t\t\t RS:10\t\t\t\t\t", background="#d1c279")
label13.place(x=750,y=480)

label14= Label(window, font= "times 10 bold", text=" CHAPATI\t\t\t\t\t RS:10\t\t\t\t\t", background="#d1c279")
label14.place(x=750,y=510)

#------------------DESERTS-------------------

label15= Label(window, font= ("Lucida Console", 16), text="\t\tDESERTS:\t\t\t\t\t", background="light pink", foreground="blue")
label15.place(x=750,y=540)

label16= Label(window, font= "times 10 bold", text=" CAKE\t\t\t\t\t\t RS:160\t\t\t\t", background="#d1c279")
label16.place(x=750,y=570)

label17= Label(window, font= "times 10 bold", text=" KULFI\t\t\t\t\t\t RS:140\t\t\t\t", background="#d1c279")
label17.place(x=750,y=600)

label18= Label(window, font= "times 10 bold", text=" KHEER\t\t\t\t\t\t RS:140\t\t\t\t", background="#d1c279")
label18.place(x=750,y=630)

#---------------------------ENTRY SECTION OF DISHES------------

label19= Label(window, font= ("Copperplate", 18), text="\t\tDISHES:\t\t\t\t", background="orange", foreground="blue")
label19.place(x=100,y=80)

label20= Label(window, font= "times 10 bold", text=" KARAHI\t\t ", background="#d1c279")
label20.place(x=100,y=120)

e1 = Entry(window)
e1.place(x=100,y=150)

label21= Label(window, font= "times 10 bold", text=" PULAO\t\t ", background="#d1c279")
label21.place(x=300,y=120)

e2 = Entry(window)
e2.place(x=300,y=150)

label21= Label(window, font= "times 10 bold", text=" HALEEM\t\t ", background="#d1c279")
label21.place(x=500,y=120)

e3 = Entry(window)
e3.place(x=500,y=150)


label20= Label(window, font= "times 10 bold", text=" BIRYANI\t\t", background="#d1c279")
label20.place(x=100,y=180)

e4 = Entry(window)
e4.place(x=100,y=210)

label21= Label(window, font= "times 10 bold", text=" HANDI\t\t ", background="#d1c279")

label21.place(x=300,y=180)

e5 = Entry(window)
e5.place(x=300,y=210)

label22= Label(window, font= "times 10 bold", text=" CHICKEN TIKKA\t ", background="#d1c279")
label22.place(x=500,y=180)

e6 = Entry(window)
e6.place(x=500,y=210)

label23= Label(window, font= "times 10 bold", text=" MALAI BOOTI \t", background="#d1c279")
label23.place(x=100,y=240)

e7 = Entry(window)
e7.place(x=100,y=270)

label24= Label(window, font= "times 10 bold", text=" SEEKH KABAB \t", background="#d1c279")
label24.place(x=300,y=240)

e8 = Entry(window)
e8.place(x=300,y=270)

#-----------------ENTRY SECTION FOR EXTRAS----------------

label25= Label(window, font= ("Copperplate", 18), text="\t\tEXTRAS:\t\t\t\t", background="orange", foreground="blue")
label25.place(x=100,y=300)

label26= Label(window, font= "times 10 bold", text=" SALAD\t\t", background="#d1c279")
label26.place(x=100,y=340)

e9 = Entry(window)
e9.place(x=100,y=370)

label27= Label(window, font= "times 10 bold", text=" COLDDRINK\t", background="#d1c279")
label27.place(x=300,y=340)

e10 = Entry(window)
e10.place(x=300,y=370)

label28= Label(window, font= "times 10 bold", text=" NAAN\t\t", background="#d1c279")
label28.place(x=500,y=340)

e11 = Entry(window)
e11.place(x=500,y=370)

label29= Label(window, font= "times 10 bold", text=" CHAPATI\t", background="#d1c279")

label29.place(x=100,y=400)

e12 = Entry(window)
e12.place(x=100,y=430)

#-------------- ENTRY SECTION FOR DESERTS---------

label30= Label(window, font= ("Copperplate", 18), text="\t\tDESERT:\t\t\t\t", background="orange", foreground="blue")
label30.place(x=100,y=470)

label31= Label(window, font= "times 10 bold", text=" CAKE\t\t ", background="#d1c279")

label31.place(x=100,y=510)

e13 = Entry(window)
e13.place(x=100,y=540)

label32= Label(window, font= "times 10 bold", text=" KULFI\t\t ", background="#d1c279")
label32.place(x=300,y=510)

e14 = Entry(window)
e14.place(x=300,y=540)

label33= Label(window, font= "times 10 bold", text=" KHEER\t\t ", background="#d1c279" )
label33.place(x=500,y=510)

e15 = Entry(window)
e15.place(x=500,y=540)

b1= Button(window, text= " BILL ", width=30, command=calculate, background="#ffd04f", font=("Brush Script MT", 12))
b1.place(x=300, y=570)
window.mainloop()
