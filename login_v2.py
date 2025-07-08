import streamlit as st
import pymysql

class LoginPage:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def login_page(self):
        st.title("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login",type="primary"):
            if not username or not password:
                st.error("Please enter both username and password.")
                return

            # Check credentials in DB
            if self.validate_credentials(username, password):
                st.success(f"Welcome back, {username}!")
                st.session_state["page"] = "menu"  # Change to your next page
                st.rerun()
            else:
                st.error("Invalid username or password.")
        if st.button("SIGN UP HERE",type="primary"):
            st.session_state["page"]="signup"
            st.rerun()


        if st.button("Back to home",type="primary"):
            st.session_state["page"] = "front"
            st.rerun()

    def validate_credentials(self, username, password):
        try:
            con = self.user_manager.connect()
            with con.cursor() as cur:
                # Adjust column names if needed
                cur.execute("SELECT password FROM users WHERE username=%s", (username,))
                result = cur.fetchone()
                if result:
                    stored_password = result[0]
                    # For now, plain text comparison; replace with hashed password check if implemented
                    return stored_password == password
                else:
                    return False
        except Exception as e:
            st.error(f"Database error: {e}")
            return False
