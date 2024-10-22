import streamlit as st
import langchainHelper as lch

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Select the type of restraunt", ["Indian", "Chinese", "Italian", "Mexican", "American"])


    
if cuisine:
    response = lch.generate_restaurant_name_and_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write("**Menu Items:**")
    
    for item in menu_items:
        st.write(" - ",item)