
import pymysql
import streamlit as st

class OrderManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return pymysql.connect(**self.db_config)

    def save_orders(self, username, cart, total_price):
        """
        Save order and order items to the database.
        cart: list of dicts with keys: name, qty, price
        """
        con = self.connect()
        try:
            with con.cursor() as cur:
                # Insert order into orders table
                cur.execute(
                    "INSERT INTO orders (username, total_price) VALUES (%s, %s)",
                    (username, total_price)
                )
                order_id = cur.lastrowid

                # Insert each cart item into order_items table
                for item in cart:
                    cur.execute(
                        "INSERT INTO order_items (order_id, item_name, quantity, price) VALUES (%s, %s, %s, %s)",
                        (order_id, item['name'], item['qty'], item['price'])
                    )
                con.commit()
                return order_id
        except Exception as e:
            con.rollback()
            st.error(f"Failed to save order: {e}")
            return None
        finally:
            con.close()

def cart_page(order_manager, username):
    st.title("CART")
    cart = st.session_state.get("cart", [])
    # st.write("DEBUG: Cart contents:", cart)  # <-- Correct placement

    # if not cart:
    #     st.info("Your cart is empty")
    #     return

    total_price = 0
    st.write("### Selected Items are:")
    for item in cart:
        try:
            item_total = item['qty'] * item['price']
            total_price += item_total
            st.write(f"{item['qty']} x {item['name']} -- ₹{item['price']} each = ₹{item_total}")
        except (TypeError, KeyError):
            st.error("Cart item is malformed. Please check your cart data.")
            return

    st.write(f"### Total Price: ₹{total_price}")

    if st.button("Final Billing",type="primary"):
    # Save cart and total_price in session_state for final billing page
      st.session_state["final_cart"] = cart
      st.session_state["final_total_price"] = total_price
      st.session_state["page"] = "final_billing"
      st.rerun()

        


