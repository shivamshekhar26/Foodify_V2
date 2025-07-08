import pymysql 
import streamlit as st 
# final_price = total_price * 10/100
#     tfinal_price= total_price* 9/100
#     delivery_charge=100
#     super_final= total_price + final_price + tfinal_price + delivery_charge
#     st.markdown(f"### The total order price is: ₹{total_price}")
#     st.markdown(f"### 10% convinience fee:₹{final_price}")
#     st.markdown(f"### 9% GST:₹{tfinal_price}")
#     st.markdown(f"### Delivery Charge:₹{delivery_charge}")
#     st.warning(f"## FINAL AMOUNT:₹{super_final}")
#     order_id = order_manager.save_orders(username, cart, total_price)
#     if order_id:
#             st.success(f"Order #{order_id} placed successfully!")
#             st.session_state["cart"] = []  # Clear cart after successful order
#     else:
#         st.error("Order failed. Please try again.")
def final_billing_page(order_manager, username):
    st.title("Final Billing")

    cart = st.session_state.get("final_cart", [])
    total_price = st.session_state.get("final_total_price", 0)

    if not cart or total_price == 0:
        st.warning("No order details found. Please add items to your cart.")
        return

    # Calculate fees and final amount
    convenience_fee = total_price * 10 / 100
    gst = total_price * 9 / 100
    delivery_charge = 100
    final_amount = total_price + convenience_fee + gst + delivery_charge

    # Display breakdown
    st.markdown(f"### Order Price: ₹{total_price:.2f}")
    st.markdown(f"### Convenience Fee (10%): ₹{convenience_fee:.2f}")
    st.markdown(f"### GST (9%): ₹{gst:.2f}")
    st.markdown(f"### Delivery Charge: ₹{delivery_charge}")
    st.info(f"## FINAL AMOUNT: ₹{final_amount:.2f}")

    if st.button("Confirm Order",type="primary"):
        order_id = order_manager.save_orders(username, cart, total_price)
        if order_id:
            st.success(f"Order #{order_id} placed successfully!")
            st.session_state["cart"] = []  # Clear cart
            # Clear final billing info
            st.session_state.pop("final_cart", None)
            st.session_state.pop("final_total_price", None)
            # Redirect to front or menu page
            st.session_state["page"] = "front"
            st.rerun()
        else:
            st.error("Order failed. Please try again.")
