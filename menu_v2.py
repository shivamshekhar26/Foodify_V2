
import pymysql
import streamlit as st

class MenuManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return pymysql.connect(**self.db_config)

    def get_menu_items(self):
        con = self.connect()
        try:
            with con.cursor() as cur:
                cur.execute("SELECT * FROM menu_items")
                columns = [desc[0] for desc in cur.description]
                items = [dict(zip(columns, row)) for row in cur.fetchall()]
            return items
        finally:
            con.close()

class MenuPage:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager

    def show(self):
        st.title("Menu")
        menu_items = self.menu_manager.get_menu_items()
        if not menu_items:
            st.info("No menu items found.")
            return
        quantities = {}
        for item in menu_items:
            qty = st.number_input(
                f"**{item['name']}** - ₹{item['price']}",
                min_value=0, max_value=10, value=0, step=1,
                key=f"qty_{item['name']}"
                )
            quantities[item['name']] = qty
            if 'description' in item:
                st.write(item['description'])
                st.markdown("---")

        if st.button("GO TO CART", type='primary'):
            cart = []
            for item in menu_items:
                qty = quantities[item['name']]
                if qty > 0:
                    cart.append({
                        "name": item['name'],
                        "qty": qty,
                        "price": item['price']
                        })
            st.session_state["cart"] = cart  # Store list of dicts, not string
            st.session_state["page"] = "cart"
            st.rerun() 
