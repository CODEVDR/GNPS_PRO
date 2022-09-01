from tkinter import *
from sqlmodule import *
import tkinter.messagebox as msg


root = Tk()
root.title("GNPS-21")
root.maxsize(600, 500)
root.minsize(600, 500)
root.geometry("600x500")
# Functions Defined Here
# =====================================================================================================================================


def signUp():
    try:
        global label3, label4, label5, user_idvalue_sign_up, pwvalue_sign_up, btn2
        # Remove Old Labels,Buttons,Entries
        label1.grid_remove()
        label2.grid_remove()
        serv_passvalue.grid_remove()
        btn1.grid_remove()
        # condition to remove labels
        try:
            label6.grid_remove(), label7.grid_remove(), label8.grid_remove(), user_idvalue.grid_remove(), pwvalue.grid_remove(), btn3.grid_remove(), radio1.grid_remove(), radio2.grid_remove(), radio3.grid_remove(), radio4.grid_remove(), radio5.grid_remove(), radio6.grid_remove(), btn4.grid_remove(
            ), label9.grid_remove(), label10.grid_remove(), label11.grid_remove(), label12.grid_remove(), label13.grid_remove(), label14.grid_remove(), entry6.grid_remove(), entry7.grid_remove(), entry8.grid_remove(), entry9.grid_remove(), entry10.grid_remove(), entry11.grid_remove(), btn5.grid_remove()
        except:
            pass
        label3 = Label(root, text="Sign Up",
                       font="conicsans 10 bold", fg="purple")
        label3.grid(row=1, column=0)
        # Function For Backend

        def store():
            if user_id_sign_up.get() == "":
                msg.showerror("Error", "User ID Cannot Be Empty")
            elif pw_sign_up.get() == "":
                msg.showerror("Error", "Password Cannot Be Empty")
            else:
                try:
                    q1 = "create table if not exists user_data(user_id varchar(20) primary key,password varchar(20));"
                    execute_query(cd, q1)
                    q2 = f"insert into user_data values('{user_id_sign_up.get()}','{pw_sign_up.get()}');"
                    execute_query(cd, q2)
                    msg.showinfo(
                        "Sucess", f"Sucessfully Stores Username : {user_id_sign_up.get()} Password : {pw_sign_up.get()}")
                except:
                    msg.showerror(
                        "Error", f"User Id : {user_id_sign_up.get()} is Already Exists In Database Please Try A Different One.")
        # Variables
        user_id_sign_up = StringVar()
        pw_sign_up = StringVar()
        # Labels
        label4 = Label(root, text="Enter User ID :",
                       font="conicsans 10 bold", fg="purple")
        label4.grid(row=2, column=0)
        label5 = Label(root, text="Enter Password :",
                       font="conicsans 10 bold", fg="purple")
        label5.grid(row=3, column=0)
        # Entries
        user_idvalue_sign_up = Entry(
            root, textvariable=user_id_sign_up, font="conicsans 10 bold")
        pwvalue_sign_up = Entry(
            root, textvariable=pw_sign_up, font="conicsans 10 bold")
        user_idvalue_sign_up.grid(row=2, column=1)
        pwvalue_sign_up.grid(row=3, column=1)
        # Button
        btn2 = Button(root, text="Submit", command=store,
                      fg="purple", font="conicsans 10 bold")
        btn2.grid(row=4, column=1)
    except:
        msg.showerror("Error", "Enter Server Password First")


def help_f():
    msg.showinfo(
        "Help", "Contact Us at https://codevdr.github.io/v/#contact We will Contact You Soon")


def signIn():
    def submit1():
        q1 = f"select * from user_data where user_id='{user_idvalue.get()}';"
        rd = read_query(cd, q1)
        if user_id.get() == "":
            msg.showerror("Error", "User ID Cannot Be Empty")
        elif pw.get() == "":
            msg.showerror("Error", "Password Cannot Be Empty")
        else:
            try:
                if rd[0][1] == pwvalue.get():
                    msg.showinfo("Sucess", "Logged in Sucessfully")
                    try:
                        # Storing Student Details
                        # =================================================================================================================
                        global radio1, radio2, radio3, radio4, radio5, radio6, btn4
                        # Removing old labels,entries,btns
                        try:  # (Removing Sign Up Content If Exists)
                            label6.grid_remove()
                            label7.grid_remove()
                            label8.grid_remove()
                            user_idvalue.grid_remove()
                            pwvalue.grid_remove()
                            btn3.grid_remove()
                        except:
                            pass
                        try:  # (Removing Sign In Content If Exists)
                            label6.grid_remove()
                            label7.grid_remove()
                            label8.grid_remove()
                            user_idvalue.grid_remove()
                            pwvalue.grid_remove()
                            btn3.grid_remove()
                        except:
                            pass
                        # Code Starts from Here For New Page

                        def storevals():
                            # opn1
                            global label9, label10, label11, label12, label13, label14, entry6, entry7, entry8, entry9, entry10, entry11, btn5
                            # opn2
                            global radio7, radio8, radio9, radio10, radio11, radio12, btn7
                            # ==========================================
                            # Under Option 2 inner radio buttons
                            # Inneroption 1
                            global ilabel1, ientry1, ibtn1
                            # Inneroption 2
                            global ilabel2, ientry2, ibtn2
                            # Inneroption 3
                            global ilabel3, ientry3, ibtn3
                            # Inneroption 4
                            global ilabel4, ientry4, ibtn4
                            # Inneroption 5
                            global ilabel5, ientry5, ibtn5
                            # Inneroption 6
                            global ilabel6, ientry6, ibtn6
                            # Extra
                            global otlbl, otent
                            # ==========================================
                            # opn3
                            global label15, label16, entry12, entry13, btn6
                            if var.get() != 0:
                                # Backend Starts From here
                                # =========================================================================================================
                                if var.get() == 1:
                                    try:
                                        otlbl.grid_remove(), otent.grid_remove()
                                    except:
                                        pass

                                    # Removing option 2 grid inner radiobuttons   # ======================>Tested OK<==================================
                                    try:
                                        ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                        ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                        ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                        ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                        ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                        ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                    except:
                                        pass
                                    # ================================================
                                    try:  # Removing grids of option 2
                                        radio7.grid_remove(), radio8.grid_remove(), radio9.grid_remove(), radio10.grid_remove(
                                        ), radio11.grid_remove(), radio12.grid_remove(), btn7.grid_remove()
                                    except:
                                        pass
                                    try:
                                        entry12.grid_remove(), entry13.grid_remove(), label15.grid_remove(
                                        ), label16.grid_remove(), btn6.grid_remove()
                                    except:
                                        pass
                                    # function That Stores Student's Data

                                    def storeStudentVal():
                                        try:
                                            q1 = "create table if not exists student_data(name varchar(20),class varchar(20),father_name varchar(50),mob_no varchar(50),admn_no varchar(50) primary key,blood_group varchar(10));"
                                            execute_query(cd, q1)
                                        except:
                                            print("Main Error Diya")
                                        try:
                                            q2 = f"insert into student_data values('{name.get()}','{cl.get()}','{fname.get()}','{mob_no.get()}','{admn_no.get()}','{blood_grp.get()}');"
                                            execute_query(cd, q2)
                                            msg.showinfo(
                                                "Sucess", "Sucessffully Stored")
                                        except:

                                            msg.showerror(
                                                "Error", "Admission Number Already Exists")
                                    # Entering Student's Details
                                    radio1.grid(row=1, column=0)
                                    # tkinter Variables
                                    name = StringVar()
                                    cl = StringVar()
                                    fname = StringVar()
                                    mob_no = StringVar()
                                    admn_no = StringVar()
                                    blood_grp = StringVar()
                                    # Tkinter Labels
                                    label9 = Label(
                                        root, text="Enter Student's Name :", font="conicsans 10 bold")
                                    label9.grid(row=2, column=0)
                                    label10 = Label(
                                        root, text="Enter Student's Class :", font="conicsans 10 bold")
                                    label10.grid(row=3, column=0)
                                    label11 = Label(
                                        root, text="Enter Student's Fathers's Name :", font="conicsans 10 bold")
                                    label11.grid(row=4, column=0)
                                    label12 = Label(
                                        root, text="Enter Student's Mobile Number :", font="conicsans 10 bold")
                                    label12.grid(row=5, column=0)
                                    label13 = Label(
                                        root, text="Enter Student's Admission Number :", font="conicsans 10 bold")
                                    label13.grid(row=6, column=0)
                                    label14 = Label(
                                        root, text="Enter Student's Blood Group :", font="conicsans 10 bold")
                                    label14.grid(row=7, column=0)
                                    # Tkinter Entries
                                    entry6 = Entry(
                                        root, textvariable=name, font="conicsans 10 bold")
                                    entry6.grid(row=2, column=1)
                                    entry7 = Entry(
                                        root, textvariable=cl, font="conicsans 10 bold")
                                    entry7.grid(row=3, column=1)
                                    entry8 = Entry(
                                        root, textvariable=fname, font="conicsans 10 bold")
                                    entry8.grid(row=4, column=1)
                                    entry9 = Entry(
                                        root, textvariable=mob_no, font="conicsans 10 bold")
                                    entry9.grid(row=5, column=1)
                                    entry10 = Entry(
                                        root, textvariable=admn_no, font="conicsans 10 bold")
                                    entry10.grid(row=6, column=1)
                                    entry11 = Entry(
                                        root, textvariable=blood_grp, font="conicsans 10 bold")
                                    entry11.grid(row=7, column=1)
                                    # Tkinter Button
                                    btn5 = Button(
                                        root, text="Submit", command=storeStudentVal)
                                    btn5.grid(row=8, column=1)

                                    # GRIDDINGS OF OUTER RADIOBUTTIONS
                                    radio2.grid(row=9, column=0)
                                    radio3.grid(row=10, column=0)
                                    radio4.grid(row=11, column=0)
                                    radio5.grid(row=12, column=0)
                                    radio6.grid(row=13, column=0)
                                    btn4.grid(row=14, column=0)

                                elif var.get() == 2:

                                    try:
                                        entry12.grid_remove(), entry13.grid_remove(), label15.grid_remove(
                                        ), label16.grid_remove(), btn6.grid_remove()
                                    except:
                                        pass
                                    try:  # removing Old labels
                                        label9.grid_remove(), label10.grid_remove(), label11.grid_remove(), label12.grid_remove(), label13.grid_remove(), label14.grid_remove(
                                        ), entry6.grid_remove(), entry7.grid_remove(), entry8.grid_remove(), entry9.grid_remove(), entry10.grid_remove(), entry11.grid_remove(), btn5.grid_remove()
                                    except:
                                        pass
                                    # code Starts From Here
                                    # function
                                    radio1.grid(row=1, column=0)
                                    radio2.grid(row=2, column=0)
                                    # OPTION 2 INNER RADIO BUTTONS
                                    # ======ADMISSION NUMBER==========
                                    otlbl = Label(
                                        root, text="Enter Admission Number : ", font="conicsans 10 bold")
                                    otlbl.grid(row=3, column=0)
                                    admn_no = StringVar()
                                    otent = Entry(
                                        root, textvariable=admn_no, font="conicsans 10 bold")
                                    otent.grid(row=3, column=1)
                                    # ================================

                                    def storevalsupdate():
                                        # Inneroption 1
                                        global ilabel1, ientry1, ibtn1
                                        # Inneroption 2
                                        global ilabel2, ientry2, ibtn2
                                        # Inneroption 3
                                        global ilabel3, ientry3, ibtn3
                                        # Inneroption 4
                                        global ilabel4, ientry4, ibtn4
                                        # Inneroption 5
                                        global ilabel5, ientry5, ibtn5
                                        # Inneroption 6
                                        global ilabel6, ientry6, ibtn6
                                        if var1.get() == 1:
                                            # Grid_remove for option 6
                                            try:
                                                ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 5
                                            try:
                                                ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 4
                                            try:
                                                ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 3
                                            try:
                                                ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                            except:
                                                pass
                                            # Update Name
                                            # ===============
                                            # function

                                            def update_val_nm():
                                                adno = admn_no.get()
                                                q0 = f"select * from student_data where admn_no='{adno}'"
                                                res = read_query(cd, q0)
                                                if res != []:
                                                    if adno == "":
                                                        msg.showerror(
                                                            "Error", "Field Cannot Be Empty")
                                                    else:
                                                        if up_nm.get() == "":
                                                            msg.showerror(
                                                                "Error", "Field Cannot Be Empty")
                                                        else:
                                                            q1 = f"""update student_data set name="{up_nm.get()}" where admn_no="{adno}";"""
                                                            execute_query(
                                                                cd, q1)
                                                            msg.showinfo(
                                                                "Sucess", "Name Sucessfully Updated")
                                                else:
                                                    msg.showerror(
                                                        "Error", f"Admission Number {adno} Not Present In Database.")
                                            # Outer Radio buttons
                                            radio1.grid(row=1, column=0)
                                            radio2.grid(row=2, column=0)
                                            # Inner Radio Buttons
                                            radio7.grid(row=4, column=0)
                                            # Inner Labels
                                            ilabel1 = Label(
                                                root, text="Enter Updated Name : ", font="conicsans 10 bold")
                                            ilabel1.grid(row=5, column=0)
                                            up_nm = StringVar()
                                            ientry1 = Entry(
                                                root, textvariable=up_nm, font="conicsans 10 bold")
                                            ientry1.grid(row=5, column=1)
                                            ibtn1 = Button(
                                                root, text="Submit", command=update_val_nm, font="conicsans 10 bold", fg="purple")
                                            ibtn1.grid(row=6, column=1)
                                            # Inner Radio Buttons
                                            radio8.grid(row=7, column=0)
                                            radio9.grid(row=8, column=0)
                                            radio10.grid(row=9, column=0)
                                            radio11.grid(row=10, column=0)
                                            radio12.grid(row=11, column=0)
                                            btn7.grid(row=12, column=0)
                                            # Outer Radio Buttons
                                            radio3.grid(row=13, column=0)
                                            radio4.grid(row=14, column=0)
                                            radio5.grid(row=15, column=0)
                                            radio6.grid(row=16, column=0)
                                            btn4.grid(row=17, column=0)
                                        elif var1.get() == 2:
                                            # Grid_remove for option 6
                                            try:
                                                ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 5
                                            try:
                                                ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 4
                                            try:
                                                ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 3
                                            try:
                                                ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                            except:
                                                pass
                                            # UPDATE CLASS
                                            # Inner option1 Grid_remove
                                            try:
                                                ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                            except:
                                                pass
                                            # function

                                            def update_val_cl():
                                                adno = admn_no.get()
                                                q0 = f"select * from student_data where admn_no='{adno}'"
                                                res = read_query(cd, q0)
                                                if res != []:
                                                    if adno == "":
                                                        msg.showerror(
                                                            "Error", "Field Cannot Be Empty")
                                                    else:
                                                        if up_cl.get() == "":
                                                            msg.showerror(
                                                                "Error", "Field Cannot Be Empty")
                                                        else:
                                                            q1 = f"""update student_data set class="{up_cl.get()}" where admn_no="{adno}";"""
                                                            execute_query(
                                                                cd, q1)
                                                            msg.showinfo(
                                                                "Sucess", "Class Sucessfully Updated")
                                                else:
                                                    msg.showerror(
                                                        "Error", f"Admission Number {adno} Not Present In Database.")
                                            # Outer Radio buttons
                                            radio1.grid(row=1, column=0)
                                            radio2.grid(row=2, column=0)
                                            # Inner Radio Buttons
                                            radio7.grid(row=4, column=0)
                                            radio8.grid(row=5, column=0)
                                            # Inner Labels
                                            ilabel2 = Label(
                                                root, text="Enter Updated Class : ", font="conicsans 10 bold")
                                            ilabel2.grid(row=6, column=0)
                                            up_cl = StringVar()
                                            ientry2 = Entry(
                                                root, textvariable=up_cl, font="conicsans 10 bold")
                                            ientry2.grid(row=6, column=1)
                                            ibtn2 = Button(
                                                root, text="Submit", command=update_val_cl, font="conicsans 10 bold", fg="purple")
                                            ibtn2.grid(row=7, column=1)
                                            # Inner Radio Buttons
                                            radio9.grid(row=8, column=0)
                                            radio10.grid(row=9, column=0)
                                            radio11.grid(row=10, column=0)
                                            radio12.grid(row=11, column=0)
                                            btn7.grid(row=12, column=0)
                                            # Outer Radio Buttons
                                            radio3.grid(row=13, column=0)
                                            radio4.grid(row=14, column=0)
                                            radio5.grid(row=15, column=0)
                                            radio6.grid(row=16, column=0)
                                            btn4.grid(row=17, column=0)
                                        elif var1.get() == 3:
                                            # Grid_remove for option 6
                                            try:
                                                ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 5
                                            try:
                                                ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 4
                                            try:
                                                ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                            except:
                                                pass
                                            # Update Blood Group
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                            except:
                                                pass
                                            # Inner option1 Grid_remove
                                            try:
                                                ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                            except:
                                                pass

                                            def update_val_bd():
                                                adno = admn_no.get()
                                                q0 = f"select * from student_data where admn_no='{adno}'"
                                                res = read_query(cd, q0)
                                                if res != []:
                                                    if adno == "":
                                                        msg.showerror(
                                                            "Error", "Field Cannot Be Empty")
                                                    else:
                                                        if up_bd.get() == "":
                                                            msg.showerror(
                                                                "Error", "Field Cannot Be Empty")
                                                        else:
                                                            q1 = f"""update student_data set blood_group="{up_bd.get()}" where admn_no="{adno}";"""
                                                            execute_query(
                                                                cd, q1)
                                                            msg.showinfo(
                                                                "Sucess", "Blood Group Sucessfully Updated")
                                                else:
                                                    msg.showerror(
                                                        "Error", f"Admission Number {adno} Not Present In Database.")
                                            # Outer Radio buttons
                                            radio1.grid(row=1, column=0)
                                            radio2.grid(row=2, column=0)
                                            # Inner Radio Buttons
                                            radio7.grid(row=4, column=0)
                                            radio8.grid(row=5, column=0)
                                            radio9.grid(row=6, column=0)
                                            # Inner Labels
                                            ilabel3 = Label(
                                                root, text="Enter Updated Blood Group : ", font="conicsans 10 bold")
                                            ilabel3.grid(row=7, column=0)
                                            up_bd = StringVar()
                                            ientry3 = Entry(
                                                root, textvariable=up_bd, font="conicsans 10 bold")
                                            ientry3.grid(row=7, column=1)
                                            ibtn3 = Button(
                                                root, text="Submit", command=update_val_bd, font="conicsans 10 bold", fg="purple")
                                            ibtn3.grid(row=8, column=1)
                                            # Inner Radio Buttons
                                            radio10.grid(row=9, column=0)
                                            radio11.grid(row=10, column=0)
                                            radio12.grid(row=11, column=0)
                                            btn7.grid(row=12, column=0)
                                            # Outer Radio Buttons
                                            radio3.grid(row=13, column=0)
                                            radio4.grid(row=14, column=0)
                                            radio5.grid(row=15, column=0)
                                            radio6.grid(row=16, column=0)
                                            btn4.grid(row=17, column=0)
                                        elif var1.get() == 4:
                                            # Grid_remove for option 6
                                            try:
                                                ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 5
                                            try:
                                                ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 3
                                            try:
                                                ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                            except:
                                                pass
                                            # Inner option1 Grid_remove
                                            try:
                                                ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                            except:
                                                pass
                                            # Update Father's Name

                                            def update_val_fnm():
                                                adno = admn_no.get()
                                                q0 = f"select * from student_data where admn_no='{adno}'"
                                                res = read_query(cd, q0)
                                                if res != []:
                                                    if adno == "":
                                                        msg.showerror(
                                                            "Error", "Field Cannot Be Empty")
                                                    else:
                                                        if up_fnm.get() == "":
                                                            msg.showerror(
                                                                "Error", "Field Cannot Be Empty")
                                                        else:
                                                            q1 = f"""update student_data set father_name="{up_fnm.get()}" where admn_no="{adno}";"""
                                                            execute_query(
                                                                cd, q1)
                                                            msg.showinfo(
                                                                "Sucess", "Father Name Sucessfully Updated")
                                                else:
                                                    msg.showerror(
                                                        "Error", f"Admission Number {adno} Not Present In Database.")
                                            # Outer Radio buttons
                                            radio1.grid(row=1, column=0)
                                            radio2.grid(row=2, column=0)
                                            # Inner Radio Buttons
                                            radio7.grid(row=4, column=0)
                                            radio8.grid(row=5, column=0)
                                            radio9.grid(row=6, column=0)
                                            radio10.grid(row=7, column=0)
                                            # Inner Labels
                                            ilabel4 = Label(
                                                root, text="Enter Updated Stuednts's Father's Name  : ", font="conicsans 10 bold")
                                            ilabel4.grid(row=8, column=0)
                                            up_fnm = StringVar()
                                            ientry4 = Entry(
                                                root, textvariable=up_fnm, font="conicsans 10 bold")
                                            ientry4.grid(row=8, column=1)
                                            ibtn4 = Button(
                                                root, text="Submit", command=update_val_fnm, font="conicsans 10 bold", fg="purple")
                                            ibtn4.grid(row=9, column=1)
                                            # Inner Radio Buttons
                                            radio11.grid(row=10, column=0)
                                            radio12.grid(row=11, column=0)
                                            btn7.grid(row=12, column=0)
                                            # Outer Radio Buttons
                                            radio3.grid(row=13, column=0)
                                            radio4.grid(row=14, column=0)
                                            radio5.grid(row=15, column=0)
                                            radio6.grid(row=16, column=0)
                                            btn4.grid(row=17, column=0)
                                        elif var1.get() == 5:
                                            # Grid_remove for option 6
                                            try:
                                                ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 4
                                            try:
                                                ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                            except:
                                                pass
                                            # Inner option1 Grid_remove
                                            try:
                                                ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                            except:
                                                pass
                                            # Update Phone Number

                                            def update_val_phno():
                                                adno = admn_no.get()
                                                q0 = f"select * from student_data where admn_no='{adno}'"
                                                res = read_query(cd, q0)
                                                if res != []:
                                                    if adno == "":
                                                        msg.showerror(
                                                            "Error", "Field Cannot Be Empty")
                                                    else:
                                                        if up_ph.get() == "":
                                                            msg.showerror(
                                                                "Error", "Field Cannot Be Empty")
                                                        else:
                                                            q1 = f"""update student_data set mob_no="{up_ph.get()}" where admn_no="{adno}";"""
                                                            execute_query(
                                                                cd, q1)
                                                            msg.showinfo(
                                                                "Sucess", "Phone Number Sucessfully Updated")
                                                else:
                                                    msg.showerror(
                                                        "Error", f"Admission Number {adno} Not Present In Database.")
                                            # Outer Radio buttons
                                            radio1.grid(row=1, column=0)
                                            radio2.grid(row=2, column=0)
                                            # Inner Radio Buttons
                                            radio7.grid(row=4, column=0)
                                            radio8.grid(row=5, column=0)
                                            radio9.grid(row=6, column=0)
                                            radio10.grid(row=7, column=0)
                                            radio11.grid(row=8, column=0)
                                            # Inner Labels
                                            ilabel5 = Label(
                                                root, text="Enter Updated Phone Number  : ", font="conicsans 10 bold")
                                            ilabel5.grid(row=9, column=0)
                                            up_ph = StringVar()
                                            ientry5 = Entry(
                                                root, textvariable=up_ph, font="conicsans 10 bold")
                                            ientry5.grid(row=9, column=1)
                                            ibtn5 = Button(
                                                root, text="Submit", command=update_val_phno, font="conicsans 10 bold", fg="purple")
                                            ibtn5.grid(row=10, column=1)
                                            # Inner Radio Buttons
                                            radio12.grid(row=11, column=0)
                                            btn7.grid(row=12, column=0)
                                            # Outer Radio Buttons
                                            radio3.grid(row=13, column=0)
                                            radio4.grid(row=14, column=0)
                                            radio5.grid(row=15, column=0)
                                            radio6.grid(row=16, column=0)
                                            btn4.grid(row=17, column=0)
                                        elif var1.get() == 6:
                                            # Grid_remove For Option 5
                                            try:
                                                ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                            except:
                                                pass
                                            # Grid_remove For Option 4
                                            try:
                                                ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                            except:
                                                pass
                                            # Grid Remove For Option 2
                                            try:
                                                ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                            except:
                                                pass
                                            # Inner option1 Grid_remove
                                            try:
                                                ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                            except:
                                                pass
                                            # Update Admission Number

                                            def update_val_admnno():
                                                adno = admn_no.get()
                                                q0 = f"select * from student_data where admn_no='{adno}'"
                                                res = read_query(cd, q0)
                                                if res != []:
                                                    if adno == "":
                                                        msg.showerror(
                                                            "Error", "Field Cannot Be Empty")
                                                    else:
                                                        if up_adno.get() == "":
                                                            msg.showerror(
                                                                "Error", "Field Cannot Be Empty")
                                                        else:
                                                            q1 = f"""update student_data set admn_no="{up_adno.get()}" where admn_no="{adno}";"""
                                                            execute_query(
                                                                cd, q1)
                                                            msg.showinfo(
                                                                "Sucess", f"Admission Number Sucessfully Updated.\nPlease Remeber The Admission Number\nThe Admission Number is {up_adno.get()}")
                                                else:
                                                    msg.showerror(
                                                        "Error", f"Admission Number {adno} Not Present In Database.")
                                            # Outer Radio buttons
                                            radio1.grid(row=1, column=0)
                                            radio2.grid(row=2, column=0)
                                            # Inner Radio Buttons
                                            radio7.grid(row=4, column=0)
                                            radio8.grid(row=5, column=0)
                                            radio9.grid(row=6, column=0)
                                            radio10.grid(row=7, column=0)
                                            radio11.grid(row=8, column=0)
                                            radio12.grid(row=9, column=0)
                                            # Inner Labels
                                            ilabel6 = Label(
                                                root, text="Enter Updated Admission Number  : ", font="conicsans 10 bold")
                                            ilabel6.grid(row=10, column=0)
                                            up_adno = StringVar()
                                            ientry6 = Entry(
                                                root, textvariable=up_adno, font="conicsans 10 bold")
                                            ientry6.grid(row=10, column=1)
                                            ibtn6 = Button(
                                                root, text="Submit", command=update_val_admnno, font="conicsans 10 bold", fg="purple")
                                            ibtn6.grid(row=11, column=1)
                                            # Inner Radio Buttons
                                            btn7.grid(row=12, column=0)
                                            # Outer Radio Buttons
                                            radio3.grid(row=13, column=0)
                                            radio4.grid(row=14, column=0)
                                            radio5.grid(row=15, column=0)
                                            radio6.grid(row=16, column=0)
                                            btn4.grid(row=17, column=0)

                                    var1 = IntVar()
                                    radio7 = Radiobutton(
                                        root, text="Update Name", padx=14, variable=var1, value=1, font="conocsans 10 bold")
                                    radio7.grid(row=4, column=0)

                                    radio8 = Radiobutton(
                                        root, text="Update Class", padx=14, variable=var1, value=2, font="conocsans 10 bold")
                                    radio8.grid(row=5, column=0)

                                    radio9 = Radiobutton(
                                        root, text="Update BLood Group", padx=14, variable=var1, value=3, font="conocsans 10 bold")
                                    radio9.grid(row=6, column=0)

                                    radio10 = Radiobutton(
                                        root, text="Update Father's Name", padx=14, variable=var1, value=4, font="conocsans 10 bold")
                                    radio10.grid(row=7, column=0)

                                    radio11 = Radiobutton(
                                        root, text="Update Phone Number", padx=14, variable=var1, value=5, font="conocsans 10 bold")
                                    radio11.grid(row=8, column=0)

                                    radio12 = Radiobutton(
                                        root, text="Update Admissin Number", padx=1, variable=var1, value=6, font="conocsans 10 bold")
                                    radio12.grid(row=9, column=0)

                                    btn7 = Button(
                                        root, text="Submit", command=storevalsupdate, fg="purple", font="conicsans 10 bold")
                                    btn7.grid(row=10, column=0)

                                    radio3.grid(row=11, column=0)
                                    radio4.grid(row=12, column=0)
                                    radio5.grid(row=13, column=0)
                                    radio6.grid(row=14, column=0)
                                    btn4.grid(row=15, column=0)

                                elif var.get() == 3:  # ======================>Tested OK<==================================
                                    try:
                                        otlbl.grid_remove(), otent.grid_remove()
                                    except:
                                        pass

                                    # Removing option 2 grid inner radiobuttons
                                    try:
                                        ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                        ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                        ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                        ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                        ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                        ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                    except:
                                        pass
                                    # ================================================
                                    try:  # Removing grids of option 2
                                        radio7.grid_remove(), radio8.grid_remove(), radio9.grid_remove(), radio10.grid_remove(
                                        ), radio11.grid_remove(), radio12.grid_remove(), btn7.grid_remove()
                                    except:
                                        pass

                                    def delStudentVals():
                                        if name.get() == "" or admn_no.get() == "":
                                            msg.showerror(
                                                "Error", "Field Cannot Be Empty")
                                        else:
                                            q1 = f"""select * from student_data where name="{name.get()}" && admn_no="{admn_no.get()}";"""
                                            res = read_query(cd, q1)
                                            if res == []:
                                                msg.showerror(
                                                    "Error", "No Data Present")
                                            else:
                                                try:
                                                    q1 = f"""delete from student_data where name="{name.get()}" && admn_no="{admn_no.get()}";"""
                                                    v = msg.askquestion(
                                                        "Delete", "Do You Want To Delete Data")
                                                    if v == "yes":
                                                        msg.showinfo(
                                                            "Delete", "The Data was Sucessfully Deleted")
                                                        execute_query(cd, q1)
                                                except:
                                                    print("Error")

                                    try:  # removing Old labels
                                        label9.grid_remove(), label10.grid_remove(), label11.grid_remove(), label12.grid_remove(), label13.grid_remove(), label14.grid_remove(
                                        ), entry6.grid_remove(), entry7.grid_remove(), entry8.grid_remove(), entry9.grid_remove(), entry10.grid_remove(), entry11.grid_remove(), btn5.grid_remove()
                                    except:
                                        pass
                                    # code Starts from Here
                                    radio1.grid(row=1, column=0)
                                    radio2.grid(row=2, column=0)
                                    radio3.grid(row=3, column=0)

                                    # Tkinter Labels
                                    label15 = Label(
                                        root, text="Enter Student's Name :", font="conicsans 10 bold")
                                    label15.grid(row=4, column=0)
                                    label16 = Label(
                                        root, text="Enter Student's Admission Number :", font="conicsans 10 bold")
                                    label16.grid(row=5, column=0)
                                    # Tkinter Variables
                                    name = StringVar()
                                    admn_no = StringVar()
                                    # Tkinter Enteries
                                    entry12 = Entry(
                                        root, textvariable=name, font="conicsans 10 bold")
                                    entry12.grid(row=4, column=1)
                                    entry13 = Entry(
                                        root, textvariable=admn_no, font="conicsans 10 bold")
                                    entry13.grid(row=5, column=1)
                                    # Tkinter Button
                                    btn6 = Button(
                                        root, text="Submit", command=delStudentVals, font="conicsans 10 bold")
                                    btn6.grid(row=6, column=1)

                                    radio4.grid(row=7, column=0)
                                    radio5.grid(row=8, column=0)
                                    radio6.grid(row=9, column=0)
                                    btn4.grid(row=10, column=0)

                                elif var.get() == 4:
                                    try:
                                        otlbl.grid_remove(), otent.grid_remove()
                                    except:
                                        pass

                                    # Removing option 2 grid inner radiobuttons
                                    try:
                                        ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                        ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                        ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                        ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                        ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                        ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                    except:
                                        pass
                                    # ================================================
                                    try:  # Removing grids of option 2
                                        radio7.grid_remove(), radio8.grid_remove(), radio9.grid_remove(), radio10.grid_remove(
                                        ), radio11.grid_remove(), radio12.grid_remove(), btn7.grid_remove()
                                    except:
                                        pass
                                    try:
                                        entry12.grid_remove(), entry13.grid_remove(), label15.grid_remove(
                                        ), label16.grid_remove(), btn6.grid_remove()
                                    except:
                                        pass
                                    try:  # removing Old labels
                                        label9.grid_remove(), label10.grid_remove(), label11.grid_remove(), label12.grid_remove(), label13.grid_remove(), label14.grid_remove(
                                        ), entry6.grid_remove(), entry7.grid_remove(), entry8.grid_remove(), entry9.grid_remove(), entry10.grid_remove(), entry11.grid_remove(), btn5.grid_remove()
                                    except:
                                        pass
                                    # New Window
                                    # ===========================================================================================================
                                    #root.destroy()
                                    data = Tk()
                                    data.wm_iconbitmap("gnps_logo.ico")
                                    data.maxsize(900, 600)
                                    data.minsize(900, 600)
                                    data.geometry("900x600")
                                    data.title("All Sudent_details")

                                    def result():

                                        if cl.get() == "":
                                            msg.showerror(
                                                "Error", "Please Enter A Class")
                                        elif (cl.get()).isdigit():
                                            cls = int(cl.get())
                                            if cls > 0 and cls <= 12:
                                                q1 = f"""select * from student_data where class="{cls}" order by name desc;"""
                                                res = read_query(cd, q1)
                                                Label(data, text=f"(name,class,father_name,mob_no,admn_no,blood_group)", font="conicsans 10 bold").grid(
                                                    row=3, column=1)
                                                TextArea = Text(
                                                    data, font="lucida 13")
                                                TextArea.grid(row=4, column=1)
                                                for i in res: 
                                                    TextArea.insert(-1.0,f"{i}\n")
                                                Scroll = Scrollbar(
                                                    data, orient=VERTICAL)
                                                Scroll.grid(row=4, sticky=NS)
                                                Scroll.config(
                                                    command=TextArea.yview)
                                                TextArea.config(
                                                    yscrollcommand=Scroll.set)
                                            else:
                                                msg.showerror(
                                                    "Error", "Enter A Valid Class i.e. from UKG,LKG,Nursery,1-12.")
                                        else:
                                            msg.showerror(
                                                "Error", "Please Enter a Valid Syntax")

                                    Label(data, text="GURUNANAK PUBLIC SCHOOL", font="conicsans 19 bold", fg="purple").grid(
                                        row=0, column=1)
                                    Label(data, text="Enter Class : ", font="conicsans 10 bold").grid(
                                        row=1, column=0)
                                    cl = StringVar()
                                    Entry(data, textvariable=cl, font="conicsans 10 bold").grid(
                                        row=1, column=1)
                                    Button(data, text="Submit", command=result, font="conicsans 10 bold", fg="purple").grid(
                                        row=2, column=1)
                                    data.mainloop()
                                    # ===========================================================================================================
                                elif var.get() == 5:
                                    try:
                                        otlbl.grid_remove(), otent.grid_remove()
                                    except:
                                        pass

                                    # Removing option 2 grid inner radiobuttons
                                    try:
                                        ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                        ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                        ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                        ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                        ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                        ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                    except:
                                        pass
                                    # ================================================
                                    try:  # Removing grids of option 2
                                        radio7.grid_remove(), radio8.grid_remove(), radio9.grid_remove(), radio10.grid_remove(
                                        ), radio11.grid_remove(), radio12.grid_remove(), btn7.grid_remove()
                                    except:
                                        pass
                                    try:
                                        entry12.grid_remove(), entry13.grid_remove(), label15.grid_remove(
                                        ), label16.grid_remove(), btn6.grid_remove()
                                    except:
                                        pass
                                    try:
                                        label9.grid_remove(), label10.grid_remove(), label11.grid_remove(), label12.grid_remove(), label13.grid_remove(), label14.grid_remove(
                                        ), entry6.grid_remove(), entry7.grid_remove(), entry8.grid_remove(), entry9.grid_remove(), entry10.grid_remove(), entry11.grid_remove(), btn5.grid_remove()
                                    except:
                                        pass
                                    msg.showinfo(
                                        "Underdevelopment", "Sorry!! This Part Is Not Developed Yet.")
                                elif var.get() == 6:
                                    try:
                                        otlbl.grid_remove(), otent.grid_remove()
                                    except:
                                        pass

                                    # Removing option 2 grid inner radiobuttons
                                    try:
                                        ilabel1.grid_remove(), ientry1.grid_remove(), ibtn1.grid_remove()
                                        ilabel2.grid_remove(), ientry2.grid_remove(), ibtn2.grid_remove()
                                        ilabel3.grid_remove(), ientry3.grid_remove(), ibtn3.grid_remove()
                                        ilabel4.grid_remove(), ientry4.grid_remove(), ibtn4.grid_remove()
                                        ilabel5.grid_remove(), ientry5.grid_remove(), ibtn5.grid_remove()
                                        ilabel6.grid_remove(), ientry6.grid_remove(), ibtn6.grid_remove()
                                    except:
                                        pass
                                    # ================================================
                                    try:  # Removing grids of option 2
                                        radio7.grid_remove(), radio8.grid_remove(), radio9.grid_remove(), radio10.grid_remove(
                                        ), radio11.grid_remove(), radio12.grid_remove(), btn7.grid_remove()
                                    except:
                                        pass
                                    try:
                                        entry12.grid_remove(), entry13.grid_remove(), label15.grid_remove(
                                        ), label16.grid_remove(), btn6.grid_remove()
                                    except:
                                        pass
                                    try:  # removing Old labels
                                        label9.grid_remove(), label10.grid_remove(), label11.grid_remove(), label12.grid_remove(), label13.grid_remove(), label14.grid_remove(
                                        ), entry6.grid_remove(), entry7.grid_remove(), entry8.grid_remove(), entry9.grid_remove(), entry10.grid_remove(), entry11.grid_remove(), btn5.grid_remove()
                                    except:
                                        pass
                                    msg.showinfo(
                                        "Underdevelopment", "Sorry!! This Part Is Not Developed Yet.")
                                # =========================================================================================================
                            else:
                                msg.showerror(
                                    "Error", "Select An Option Please")
                        var = IntVar()
                        radio1 = Radiobutton(root, text="Entering Student's Details",
                                             padx=14, variable=var, value=1, font="conocsans 10 bold")
                        radio1.grid(row=1, column=0)
                        radio2 = Radiobutton(root, text="Updating Student's Details",
                                             padx=14, variable=var, value=2, font="conocsans 10 bold")
                        radio2.grid(row=2, column=0)
                        radio3 = Radiobutton(root, text="Deleting Student's Details",
                                             padx=14, variable=var, value=3, font="conocsans 10 bold")
                        radio3.grid(row=3, column=0)
                        radio4 = Radiobutton(root, text="See All Student Data",
                                             padx=14, variable=var, value=4, font="conocsans 10 bold")
                        radio4.grid(row=4, column=0)
                        radio5 = Radiobutton(root, text="Entering Teacher's Detials",
                                             padx=14, variable=var, value=5, font="conocsans 10 bold")
                        radio5.grid(row=5, column=0)
                        radio6 = Radiobutton(root, text="Deleting Teacher's Details",
                                             padx=1, variable=var, value=6, font="conocsans 10 bold")
                        radio6.grid(row=6, column=0)
                        btn4 = Button(
                            root, text="Submit", command=storevals, fg="purple", font="conicsans 10 bold")
                        btn4.grid(row=7, column=0)
                        # =================================================================================================================
                    except:  # (If An Error Occurs It Doesnt't Show Errror)
                        pass
                else:
                    msg.showerror("Error", "Incorrect Password")
            except:
                msg.showerror("Error", "Incorrect User Id")
    try:
        global label6, label7, label8, user_idvalue, pwvalue, btn3
        # Removes Previous Buttons
        label1.grid_remove()
        label2.grid_remove()
        serv_passvalue.grid_remove()
        btn1.grid_remove()
        # Condition to remove Labels
        try:
            label3.grid_remove()
            label4.grid_remove()
            label5.grid_remove()
            user_idvalue_sign_up.grid_remove()
            pwvalue_sign_up.grid_remove()
            btn2.grid_remove()
            radio1.grid_remove()
            radio2.grid_remove()
            radio3.grid_remove()
            radio4.grid_remove()
            radio5.grid_remove()
            radio6.grid_remove()
            btn4.grid_remove()
        except:
            pass
        label6 = Label(root, text="Sign In",
                       font="conicsans 10 bold", fg="purple")
        label6.grid(row=1, column=0)
        # Text Variables
        user_id = StringVar()
        pw = StringVar()
        # Labels
        label7 = Label(root, text="Enter User ID :",
                       font="conicsans 10 bold", fg="purple")
        label7.grid(row=2, column=0)
        label8 = Label(root, text="Enter Password :",
                       font="conicsans 10 bold", fg="purple")
        label8.grid(row=3, column=0)
        # Entries
        user_idvalue = Entry(root, textvariable=user_id,
                             font="conicsans 10 bold")
        pwvalue = Entry(root, textvariable=pw, font="conicsans 10 bold")
        user_idvalue.grid(row=2, column=1)
        pwvalue.grid(row=3, column=1)
        # Button That Submits User Id And Password
        btn3 = Button(root, text="Submit", command=submit1,
                      fg="violet", font="conicsans 10 bold")
        btn3.grid(row=4, column=1)
    except:
        msg.showerror("Error", "Enter Server Password First")


def exit():
    root.destroy()


def submit():
    global label2, val, ans, cs, cd
    val = serv_pass.get()
    if val == "":
        msg.showerror("Error", "Please Enter Password")
    else:
        if serv_pass.get() == "":
            msg.showerror("Error", "Enter A Password Please")
        else:
            try:
                cs = connect_server(val)
                q1 = "create database if not exists gnps21_db;"
                execute_query(cs[0], q1)
                ans = 1
                label2 = Label(
                    root, text="Click On Options in Menubar To Move Further", fg="violet")
                label2.grid(column=1)
                cd = connect_database(cs[1])
            except:
                msg.showerror("Error", "Incorrect Password")


# ========================================================================================================================
# menu
MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="Sign Up", command=signUp)
FileMenu.add_command(label="Sign In", command=signIn)
FileMenu.add_command(label="Help", command=help_f)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=exit)
MenuBar.add_cascade(label="Options", menu=FileMenu)
root.config(menu=MenuBar)
root.wm_iconbitmap("gnps_logo.ico")
# label
Label(root, text="Welcome To GNPS-21 Rkl",
      font="conicsans 19 bold", fg="purple").grid(row=0, column=1)
# Tkinter Variables
serv_pass = StringVar()
# Field Names
label1 = Label(root, text="Enter Server Password : ",
               font="conicsans 10 bold", fg="purple")
label1.grid(row=1, column=0)
# Entries
serv_passvalue = Entry(root, textvariable=serv_pass, font="conicsans 10 bold")
serv_passvalue.grid(row=1, column=1)
btn1 = Button(root, text="Submit", command=submit,
              fg="purple", font="conicsans 10 bold")
btn1.grid(row=2, column=1)

root.mainloop()
