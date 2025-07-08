import streamlit as st 
import base64
class Foodifyapp:
    def __init__(self,bg_image_path):
        self.bg_image_path=bg_image_path
    def set_background_image(self):
        with open(self.bg_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    def front_page(self):
        # Add vertical space to push content toward the center
        st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        # Use columns to center horizontally
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown(
                "<h1 style='text-align: left; color:white;font-size:80px;'>FOODIFY</h1>"
                "<p style='text-align: left; color:white;font-size:30px'>Get started by exploring our delicious menu.</p>",
                unsafe_allow_html=True
            )
            if st.button("Get Started", type="primary"):
                st.session_state["page"] = "login"
                st.rerun()

def main():
    # Initialize session state page if not set
    if "page" not in st.session_state:
        st.session_state["page"] = "front"

    app=Foodifyapp(r"C:\Users\SHIVAM\Desktop\streamlit\hd_image.jpg")
    app.set_background_image()

    if st.session_state["page"] == "front":
        app.front_page()
    elif st.session_state["page"] == "login":
        st.write("Login page goes here...")  # Placeholder for next page

if __name__ == "__main__":
    main()
