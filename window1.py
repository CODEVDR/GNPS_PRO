from tkinter import*
from sqlmodule import *
import tkinter.messagebox as msg


def newWindow(root, cd):
    while True:
        try:
            root.destroy()
        except:
            break
    data = Tk()
    data.wm_iconbitmap("gnps_logo.ico")
    data.maxsize(900, 600)
    data.minsize(900, 600)
    data.geometry("900x600")
    data.title("All Student Details")

    def result():
        if CLASS.get() == "":
            msg.showerror(
                "Error", "Please Enter A Class")
        elif (CLASS.get()).upper() == "UKG" or (CLASS.get()).upper() == "LKG" or (CLASS.get()).upper() == "NURSERY":
            cls = CLASS.get()
            q1 = f"""select * from student_data where class="{cls}" order by name desc;"""
            res = read_query(cd, q1)
            Label(data, text=f"(name,class,father_name,mob_no,admn_no,blood_group)", font="conicsans 10 bold").grid(
                row=3, column=1)
            TextArea = Text(
                data, font="lucida 13")
            TextArea.grid(row=4, column=1)
            for i in res:
                TextArea.insert(-1.0,
                                f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]}\n")
            Scroll = Scrollbar(
                data, orient=VERTICAL)
            Scroll.grid(row=4, sticky=NS)
            Scroll.config(
                command=TextArea.yview)
            TextArea.config(
                yscrollcommand=Scroll.set)
        elif (CLASS.get()).isdigit():
            cls = int(CLASS.get())
            if (cls > 0 and cls <= 12):
                q1 = f"""select * from student_data where class="{cls}" order by name desc;"""
                res = read_query(cd, q1)
                Label(data, text=f"(name,class,father_name,mob_no,admn_no,blood_group)", font="conicsans 10 bold").grid(
                    row=3, column=1)
                TextArea = Text(
                    data, font="lucida 13")
                TextArea.grid(row=4, column=1)
                for i in res:
                    TextArea.insert(-1.0,
                                    f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]}\n")
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

    def back():
        data.destroy()
        from mainwindow import rootw1
        rootw1()

    Button(data, text=u"\u2190", command=back,
           font="conicsans 15", fg="green").grid(row=0, column=0)
    Label(data, text="GURUNANAK PUBLIC SCHOOL", font="conicsans 19 bold", fg="purple").grid(
        row=0, column=1)
    Label(data, text="Enter Class : ", font="conicsans 10 bold").grid(
        row=1, column=0)
    CLASS = StringVar()
    de1 = Entry(data, textvariable=CLASS, font="conicsans 10 bold")
    de1.grid(
        row=1, column=1)
    Button(data, text="Submit", command=result, font="conicsans 10 bold", fg="purple").grid(
        row=2, column=1)
    data.mainloop()
    # ===========================================================================================================
