import streamlit as st
import requests

def handleRestaurantSearch(_restaurant_name):
    print(_restaurant_name)

def analyseReviewsPage():
    st.title('Analyze Reviews')

    with st.form('Analyze'):

        #Restaurant Name
        _restaurant_name = st.text_input('Restaurant Name')

        _submit = st.form_submit_button('Submit')

        if _submit:
            handleRestaurantSearch(_restaurant_name)


if __name__ == "__main__":
    analyseReviewsPage()