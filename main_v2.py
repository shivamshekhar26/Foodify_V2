import streamlit as st
from get_started import Foodifyapp as FrontApp
from signup_v2 import UserManager,Foodify as SignupApp
from login_v2 import LoginPage
from menu_v2 import MenuManager,MenuPage
from cart_v2 import OrderManager
from cart_v2 import cart_page
from final_billing_v2 import final_billing_page 
# Your MySQL database config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",  # Change to your MySQL password
    "database": "foodify_db"
}

def main():
    # Initialize the page in session state if not set
    if "page" not in st.session_state:
        st.session_state["page"] = "front"

    # Instantiate front page app with background image path
    front_app = FrontApp(r"C:\Users\SHIVAM\Desktop\streamlit\hd_image.jpg")

    # Instantiate user manager with DB config
    user_manager = UserManager(DB_CONFIG)

    # Instantiate signup app with user manager
    signup_app = SignupApp(user_manager)
    login_app = LoginPage(user_manager)
    # menu_page = MenuPage(user_manager)
    menu_manager = MenuManager(DB_CONFIG)
    menu_page = MenuPage(menu_manager)
    order_manager=OrderManager(DB_CONFIG)
    if 'username' not in st.session_state:
        st.session_state["username"] = "guest"
    username = st.session_state["username"]

    # Route to the correct page based on session state
    if st.session_state["page"] == "front":
        front_app.set_background_image()
        front_app.front_page()
    elif  st.session_state["page"] == "login":
        login_app.login_page()

    elif st.session_state["page"] == "signup":
        signup_app.signup_page()
    elif st.session_state["page"] == "menu":
        menu_page.show()
    elif st.session_state["page"]=="cart":
        cart_page(order_manager,username)
    elif st.session_state["page"] == "final_billing":
        final_billing_page(order_manager, username)
    else:
        st.write("Page not found")

if __name__ == "__main__":
    main()
