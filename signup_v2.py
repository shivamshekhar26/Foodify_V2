# import streamlit as st 
# import pymysql 
# import datetime

# class User_manager:
#     def __init__(self,DB_CONFIG):
#         self.DB_CONFIG=DB_CONFIG
#     def connect(self):
#         return pymysql.connect(**self.DB_CONFIG)
#     def users_exist(self,username):
#         with self.connect as con:
#             with con.cursor() as cur :
#                 cur.execute("SELECT 1 from users WHERE Username=%s",(username,))
#                 return cur.fetchone() is not None
#     def email_exits(self,email):
#         with self.connect as con:
#             with con.cursor() as cur:
#                 cur.execute("SELECT 1 from users WHERE email=%s",(email,))
#                 return cur.fetchone() is not None
#     def new_users(self,USERNAME,PASSWORD,DOB,Address,Email):
#         with self.connect as con:
#             with con.cursor() as cur:
#                 cur.execute("INSERT INTO users(USERNAME,PASSWORD,DOB,Address,Email)VALUES(%s,%s,%s,%s,%s)",(USERNAME,PASSWORD,DOB,Address,Email))
#                 con.commit()
#     @staticmethod
#     def valid_password(pwd):
#         has_upper = any(c.isupper() for c in pwd) 
#         has_digit = any(c.isdigit() for c in pwd)  
#         return has_upper and has_digit
#     @staticmethod
#     def valid_email(email):
#         return"@gmail.com" in email
#     def valid_username(USERNAME):
#         return len(USERNAME)>=3
    
#     #THE FOLLOWING CODE WILL BE FOR STREAMLIT DISPLAY :
#     class Foodifyapp:
#         def __init__(self, User_manager):
#             self.User_manager = User_manager

#     def signup_page(self):

#         st.title("SIGN UP") 
#         username = st.text_input("Enter Name", placeholder="Username>=3 Characters")
#         if username:
#             if self.user_manager.valid_username(username):
#                 st.success("Correct username!")
#             else:
#                 st.error("Fill correct username")

#         dob = st.date_input("Date of Birth", datetime.date(2000, 1, 1))

#         password = st.text_input("Enter Password", type="password")
#         if password:
#             if self.User_manager.valid_password(password):
#                 st.success("Strong password!")
#             else:
#                 st.error("Add a capital letter and a digit to password")

    
#         address = st.text_input("Enter your permanent address")

#         email = st.text_input("Enter Email", placeholder="example@gmail.com")
#         if email:
#             if self.User_manager.valid_email(email):
#                 st.success("Valid Email Entered")
#             else:
#                 st.error("Fill Correct Email")

#         if st.button("ACCOUNT CONFIRM!", type="primary"):
#             if not (username and password and address and email):
#                 st.error("ERROR: Please fill in all fields.")
#                 return

#             if not self.User_manager.valid_username(username):
#                 st.error("Username must be at least 3 characters.")
#                 return
#             if not self.User_manager.valid_password(password):
#                 st.error("Password must have a capital letter and a digit.")
#                 return
#             if not self.User_manager.valid_email(email):
#                 st.error("Email must be a valid Gmail address.")
#                 return
#             if self.user_manager.user_exists(username):
#                 st.error("This username already exists.")
#                 return
#             if self.user_manager.email_exists(email):
#                 st.error("This email already exists.")
#                 return
#             self.User_manager.add_user(username, password, dob, address, email)
#             st.success("Great! You have successfully signed up.")
#             st.session_state["page"] = "login"
#             st.rerun() 

        
#         if st.button("Back to Home", type="primary"):
#             st.session_state["page"] = "front"
#             st.rerun()
import streamlit as st 
import pymysql 
import datetime

class UserManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return pymysql.connect(**self.db_config)

    def user_exists(self, username):
        with self.connect() as con:
            with con.cursor() as cur:
                cur.execute("SELECT 1 FROM users WHERE username=%s", (username,))
                return cur.fetchone() is not None

    def email_exists(self, email):
        with self.connect() as con:
            with con.cursor() as cur:
                cur.execute("SELECT 1 FROM users WHERE email=%s", (email,))
                return cur.fetchone() is not None

    def add_user(self, username, password, dob, address, email):
        with self.connect() as con:
            with con.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (username, password, dob, address, email) VALUES (%s, %s, %s, %s, %s)",
                    (username, password, dob, address, email)
                )
                con.commit()

    @staticmethod
    def valid_password(pwd):
        has_upper = any(c.isupper() for c in pwd) 
        has_digit = any(c.isdigit() for c in pwd)  
        return has_upper and has_digit

    @staticmethod
    def valid_email(email):
        return "@gmail.com" in email

    @staticmethod
    def valid_username(username):
        return len(username) >= 3

class Foodify:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def signup_page(self):
        st.title("SIGN UP") 
        username = st.text_input("Enter Name", placeholder="Username>=3 Characters")
        if username:
            if self.user_manager.valid_username(username):
                st.success("Correct username!")
            else:
                st.error("Fill correct username")

        dob = st.date_input("Date of Birth", datetime.date(2000, 1, 1))

        password = st.text_input("Enter Password", type="password")
        if password:
            if self.user_manager.valid_password(password):
                st.success("Strong password!")
            else:
                st.error("Add a capital letter and a digit to password")

        address = st.text_input("Enter your permanent address")

        email = st.text_input("Enter Email", placeholder="example@gmail.com")
        if email:
            if self.user_manager.valid_email(email):
                st.success("Valid Email Entered")
            else:
                st.error("Fill Correct Email")

        if st.button("ACCOUNT CONFIRM!", type="primary"):
            if not (username and password and address and email):
                st.error("ERROR: Please fill in all fields.")
                return

            if not self.user_manager.valid_username(username):
                st.error("Username must be at least 3 characters.")
                return
            if not self.user_manager.valid_password(password):
                st.error("Password must have a capital letter and a digit.")
                return
            if not self.user_manager.valid_email(email):
                st.error("Email must be a valid Gmail address.")
                return
            if self.user_manager.user_exists(username):
                st.error("This username already exists.")
                return
            if self.user_manager.email_exists(email):
                st.error("This email already exists.")
                return
            self.user_manager.add_user(username, password, dob, address, email)
            st.success("Great! You have successfully signed up.")
            st.session_state["page"] = "login"
            st.rerun() 

        if st.button("Back to Home", type="primary"):
            st.session_state["page"] = "front"
            st.rerun()

