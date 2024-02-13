import Database_Connection
import datetime

time_date = datetime.datetime.now()
db = Database_Connection
command_handler = db.db.cursor()

class db_functions:
    def __init__(self):
        pass

    #Patient's Functionality CRUD
    def insert(self, name , age , address):
        while True:
            try:
                db.DB_Open_Connection()
                command_handler.execute("SELECT * FROM patient_doc WHERE name = %s", [name])
                row = command_handler.fetchone()
                if row is None:
                    query = (name, age, address)
                    command_handler.execute("INSERT INTO patient_doc (name,age,address,privilages,status) VALUES (%s,%s,%s,'Patient','Active')",query)
                    db.db.commit()
                    print("Sucessfully inserted", name)
                    return False
                else:
                    print("This information is Existed")
                    return True

            except TypeError as error:
                print("Sorry wrong places of details",error)
            finally:
                db.db.close()

    def delete(self, id):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE id = %s ", [id])
            row = command_handler.fetchone()
            if row is None:
                #check whether the data is have or none
                print("Patient doesn't exist!")
            else:
                #delete data
                query = [id]
                command_handler.execute("UPDATE patient_doc SET status = 'Inactive' WHERE id = %s", query)
                db.db.commit()
                print("Sucessfully deleted")
        except TypeError as er:
            print(er)

        finally:
            db.db.close()


    def update(self,name,age,address,id):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE id = %s", [id])
            row = command_handler.fetchone()
            if row is None:
                print("the id does not exist")
            else:
                query = (name,age,address,id)
                command_handler.execute("UPDATE patient_doc SET name = %s , age = %s , address = %s , status = 'Active' WHERE id = %s", query)
                db.db.commit()
                print("Successfully updated details")
        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    def display_active_patient(self):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE status = 'Active' AND privilages = 'Patient'")
            records = command_handler.fetchall()
            for record in records:
                print(record)
        except TypeError as er:
            print(er)

        finally:
            db.db.close()

    def display_Inactive_patient(self):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE status = 'Inactive' AND privilages = 'Patient'")
            records = command_handler.fetchall()
            for record in records:
                print(record)
        except TypeError as er:
            print(er)
        finally:
            db.db.close()
    # Patient's Functionality Ended here!

    #Doctor's Functionality!! CRUD!!
    def doc_add(self, name , age , address):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE name = %s", [name])
            row = command_handler.fetchone()
            if row is None:
                query = (name, age, address)
                command_handler.execute("INSERT INTO patient_doc (name,age,address,privilages,status) VALUES (%s,%s,%s,'Doctor','Active')",query)
                db.db.commit()
                print("Sucessfully inserted", name)
            else:
                print("This information is Existed")

        except TypeError as error:
            print("Sorry wrong places of details", error)
        finally:
            db.db.close()
    def doc_delete(self, id):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE id = %s AND privilages = 'Doctor' ", [id])
            row = command_handler.fetchone()
            if row is None:
                # check whether the data is have or none
                print("Doctor doesn't exist!")
            else:
                # delete data
                query = [id]
                command_handler.execute("UPDATE patient_doc SET status = 'Inactive' WHERE id = %s", query)
                db.db.commit()
                print("Sucessfully deleted")
        except TypeError as er:
            print(er)
        finally:
            db.db.close()
    def doc_update(self,name, age, address, id):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE id = %s", ([id]))
            row = command_handler.fetchone()
            if row is None:
                print("the id does not exist")
            else:
                query = (name, age, address, id)
                command_handler.execute("UPDATE patient_doc SET name = %s , age = %s , address = %s , status = 'Active' WHERE id = %s", query)
                db.db.commit()
                print("Successfully updated details")
        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    def doc_display_Active(self):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE status = 'Active' AND privilages = 'Doctor'")
            records = command_handler.fetchall()
            for record in records:
                print(record)
        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    def doc_display_Inactive(self):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM patient_doc WHERE status = 'Inactive' AND privilages = 'Doctor'")
            records = command_handler.fetchall()
            for record in records:
                print(record)
        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    #Doctor's Functionality Ended here!

    #Register account for user!
    def reg_user(self, username,password):
        try:
            db.DB_Open_Connection()
            query = (username,password)
            command_handler.execute("SELECT username FROM register_log WHERE username = %s AND password = %s",query )
            row = command_handler.fetchone()
            if row is None:
                query = (username,password)
                command_handler.execute("INSERT INTO register_log (username,password) VALUES (%s,%s)",query)
                db.db.commit()
                print("Sucessfully Register")
            else:
                print("This account is existed please input another username!")
        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    def log_user(self, username,password):
        try:
            db.DB_Open_Connection()
            query = (username,password)
            command_handler.execute("SELECT username FROM register_log WHERE username = %s AND password = %s",query)
            if command_handler.fetchone() is not None:
                return True
            else:
                print("Account does not exist")
                return False
        except TypeError as err:
            print(err)

        finally:
            db.db.close()
    #Register Account Ended Here!

    #USER MENU!!
    def user_booking(self,name,age,phone_num,address,time_in,time_out,total):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM appointment WHERE name = %s", [name])
            row = command_handler.fetchone()
            if row is None:
                query = (name, age, phone_num, address, time_in, time_out,total)
                command_handler.execute("INSERT INTO appointment (name,age,address,phone_num,time_in,time_out,total_spent,status) VALUES (%s,%s,%s,%s,%s,%s,%s,'Active')",query)
                db.db.commit()
            else:
                print("This information is Existed")

        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    def user_paybills(self, name,total_spent,pay,total,change):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM pay_bills WHERE name = %s", [name])
            row = command_handler.fetchone()
            if row is None:
                query = (name, total_spent, pay, total, change)
                command_handler.execute("INSERT INTO pay_bills (name,hours,pay,total,transition) VALUES (%s,%s,%s,%s,%s)", query)
                db.db.commit()
            else:
                print("This information is Existed")
                return False

        except TypeError as er:
            print(er)
        finally:
            db.db.close()


    def user_view_details(self, name):
        appointment_col = ["Id: ","Name: ", "Age: ", "Address: ", "Phone_number: ", "Time_in: ", "Time_out: ", "Status: " , "total_spent"]
        try:
            db.DB_Open_Connection()
            query = [name]
            command_handler.execute("SELECT * FROM appointment WHERE name = %s ",query)
            row = command_handler.fetchone()
            if row is None:
                print("Name does not exist in database")
            for rows,col_list in zip(appointment_col,row):
                print(rows,col_list)

        except TypeError as er:
            print(er)
        finally:
            db.db.close()

        #User menu ended's Here

    #Manage Appointment Function Start's Here!
    def Manage_Appointment_Delete(self,id):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM appointment WHERE id = %s", ([id]))
            row = command_handler.fetchone()
            if row is None:
                print("the id does not exist")
            else:
                # delete data
                query = [id]
                command_handler.execute("UPDATE appointment SET status = 'Inactive' WHERE id = %s", query)
                db.db.commit()
                print("Sucessfully deleted")
        except TypeError as er:
            print(er)
        finally:
            db.db.close()
    def Manage_Appointment_Update(self,name, age, address,phone_num,time_in,time_out,total,id):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM appointment WHERE id = %s", ([id]))
            row = command_handler.fetchone()
            if row is None:
                print("the id does not exist")
            else:
                query = (name, age, address,phone_num,time_in,time_out,total, id)
                command_handler.execute("UPDATE appointment SET name = %s , age = %s , address = %s ,phone_num = %s ,time_in = %s,time_out = %s, total_spent = %s, status = 'Active' WHERE id = %s", query)
                db.db.commit()
                print("Successfully updated details")
        except TypeError as er:
            print(er)
        finally:
            db.db.close()

    def Manage_Appointment_View(self,id):
        appointment_col = ["Name: ", "Age: ", "Address: ", "Phone_number: ", "Time_in: ", "Time_out: ", "Total_spent: ", "Status: "]
        try:
            db.DB_Open_Connection()
            query = [id]
            command_handler.execute("SELECT name,age,address,phone_num,time_in,time_out,total_spent,status FROM appointment WHERE id = %s ", query)
            row = command_handler.fetchone()
            if row is None:
                print("Id does not exist in database")
            else:
                for rows, col_list in zip(appointment_col, row):
                    print(rows, col_list)

        except TypeError as er:
            print(er)

        finally:
            db.db.close()
    def Manage_Appointment_InactiveView(self):
        try:
            db.DB_Open_Connection()
            command_handler.execute("SELECT * FROM appointment WHERE status = 'Inactive'")
            row = command_handler.fetchall()
            for rows in row:
                print(rows)
        except TypeError as er:
            print(er)

        finally:
            db.db.close()

    #Manage_Appointment Ends Here!!!