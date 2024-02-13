from db_function import db_functions
func = db_functions()
import datetime

def admin_auth():
    while True:
        print("Welcome Admin menu")
        print("[1]. Manage Patient , [2]. Manage Doctor's , [3]. Manage Appointment , [4]. Logut")
        choose = input("Choose: ")

        match choose:
            case "1":
                print("-------------Manage Patient's------------------")
                print("[1]. Add Patient , [2] Delete Patient , [3]. Update Patient , [4]. Display Active Patients , [5]. Display Archieved Patients , [6]. Logout")
                choose = input("Choose: ")

                match choose:
                    case "1":
                        name = input("Enter your name: ")
                        age = input("Enter your age: ")
                        address = input("Enter your address: ")
                        if age.isdigit():
                            age = int(age)
                            func.insert(name, age, address)
                        else:
                            print("You must enter integers not string!")


                    case "2":
                        id = input("Enter the id that you want to remove: ")
                        if id.isdigit():
                            id = int(id)
                            func.delete(id)
                        else:
                                print("You must input numbers not letters!")

                    case "3":
                        print("Enter new details!")
                        id = input("Enter the id that you want to update: ")
                        name = input("Enter new name: ")
                        age = input("Enter new age: ")
                        address = input("Enter new address: ")
                        if id.isdigit() and age.isdigit():
                            id = int(id)
                            age = int(age)
                            func.update(name, age, address, id)
                        else:
                            print("You must input numbers not letters!")


                    case "4":
                        print("Displaying active patients")
                        func.display_active_patient()
                    case "5":
                        print("Displaying inactive patients")
                        func.display_Inactive_patient()
                    case "6":
                        admin_auth()
            #doctor_manage:
            case "2":
                print("-----Managing's Doctor-----")
                print("[1]. Add Doctor , [2]. Delete Doctor , [3]. Update Doctor , [4]. View Active Doctor , [5]. View Archieved Doctor , [6]. logout ")
                choose = input("Choose: ")
                match choose:

                    case "1":
                        print("Inserting Doctor")
                        name = input("Enter doctor name: ")
                        age = input("Enter age of doctor: ")
                        address = input("Enter address of doctor: ")
                        if age.isdigit():
                            age = int(age)
                            func.doc_add(name, age, address)
                        else:
                            print("You must enter integers not string!")

                    case "2":
                        id = input("Enter the id that you want to remove: ")
                        if id.isdigit():
                            id = int(id)
                            func.doc_delete(id)
                        else:
                            print("You must input number not letters!")

                    case "3":
                        id = input("Enter the id that you want to update: ")
                        print("Enter new details!")
                        name = input("Enter new name: ")
                        age = input("Enter new age: ")
                        address = input("Enter new address: ")
                        if id.isdigit() and age.isdigit():
                            id = int(id)
                            age = int(age)
                            func.doc_update(name, age, address, id)
                        else:
                            print("You must input numbers not letters!")

                    case "4":
                        print("Displaying all Doctors")
                        func.doc_display_Active()
                    case "5":
                        print("Archieved Doctors")
                        func.doc_display_Inactive()
                    case "6":
                        admin_auth()
            case "3":
                print("-----Managing Appointment-----")
                print("[1]. Delete Appointment , [2]. Update Appointment , [3] View Appointment , [4] View appointment Inactive")
                choose = input("Choose:")

                match choose:
                    case "1":
                        id = input("Enter the id that you want to remove: ")
                        if id.isdigit():
                            id = int(id)
                            func.Manage_Appointment_Delete(id)
                        else:
                            print("You must input numbers not letters!")
                    case "2":
                        id = input("Enter the id that you want to update: ")
                        print("Enter new details!")
                        name = input("Enter new name: ")
                        age = input("Enter new age: ")
                        address = input("Enter new address: ")
                        phone_num = input("Enter your new phone number: ")
                        time_in = input("Enter your new Time_in: ")
                        time_out = input("Enter your new Time_out: ")
                        time_in_str = datetime.datetime.strptime(time_in, "%Y-%m-%d %I:%M %p")
                        time_out_str = datetime.datetime.strptime(time_out, "%Y-%m-%d %I:%M %p")
                        if id.isdigit() and age.isdigit():
                            id = int(id)
                            age = int(age)
                            total = time_out_str - time_in_str
                            print("Total time spent:" + str(total) + " Hour")
                            func.Manage_Appointment_Update(name, age, address,phone_num,time_in,time_out,total,id)
                        else:
                            print("You must input numbers not letters")
                    case "3":
                        print("Viewing patient details! ")
                        id = int(input("Enter id that you want to view: "))
                        func.Manage_Appointment_View(id)

                    case "4":
                        print("Viewing all Inactive or cancelled appointment")
                        func.Manage_Appointment_InactiveView()

            case "4":
                main()
                break
def User():
    while True:
        print("[1]. Register , [2]. Login , [3]. logut")
        choose = input("Choose: ")
        match choose:
            case "1":
                print("----Register Page-----")
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                if username == "" or password == "":
                    print("Complete details please: ")
                else:
                    func.reg_user(username,password)
            case "2":
                print("Login page")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if not func.log_user(username,password):
                    User()
                    pass
                elif username == "" or password == "":
                    print("Please Complete Details: ")
                else:
                    print("Login Sucessfully Welcome: ", username)
                    func.log_user(username,password)
                    print("[1]. Book appointment , [2]. Paybills , [3]. View_details")
                    choose = input("Choose: ")

                    match choose:
                        case "1":
                            print("Booking Appointment: ")
                            name = input("Enter your name: ")
                            age = input("Enter your age: ")
                            address = input("Enter your address: ")
                            phone_num = input("Enter your Phone number: ")
                            time_in = input("Time_in: ")
                            time_out = input("Time_out: ")
                            time_in_str = datetime.datetime.strptime(time_in, "%Y-%m-%d %I:%M %p")
                            time_out_str = datetime.datetime.strptime(time_out, "%Y-%m-%d %I:%M %p")

                            if age.isdigit():
                                age = int(age)
                                total = time_out_str - time_in_str
                                print("Total time spent:" + str(total) + " Hour")
                                func.user_booking(name, age, address, phone_num, time_in, time_out, total)
                            else:
                                print("You must input numbers not letters")

                        case "2":
                            print("-----Paying bills------")
                            name = input("Enter your name: ")
                            total_spent = input("How many hours did you stay in hospital: ")
                            pay = input("pay: ")

                            if pay.isdigit() and total_spent.isdigit():
                                pay = int(pay)
                                total_spent = int(total_spent)
                                total = (350 * total_spent)
                                change = pay - total
                                if pay >= total:
                                    if func.user_paybills(name, total_spent, pay, total, change) is False:
                                        return True
                                    else:
                                        print("------Receipt-----")
                                        print("Name: " + name + "\n" + "hours: " + str(total_spent) + "\n" + "pay: " + str(pay) + "\n" + "total_amount " + str(total) + "\n" + "Change: " + str(change))
                                        print("Thankyou For choosing GAMCO Staysafe always and Godbless!")
                                else:
                                    print("insufficient Money")
                                    return False
                            else:
                                print("you must input numbers not letters")
                        case "3":
                            print("Viewing patient details! ")
                            name = input("Enter name that you want to view: ")
                            func.user_view_details(name)
            case "3":
                main()
def Admin():
    print("========Login Page==========")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "123":
        print("Login Sucessfully")
        admin_auth()
    else:
        print("Invalid account")

def main():
    while True:
        print("===============Welcome to Gamco Hospital Management System===============")
        print("[1] Admin , [2] User , [3]. Exit")
        choose = input("Choose: ")
        match choose:
            case "1":
                Admin()
            case "2":
                User()
            case "3":
                exit()


main()