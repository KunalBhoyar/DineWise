import streamlit as st
import requests

# Define the API endpoint URL
URL = 'http://bigdata7245-finalproject.ue.r.appspot.com'

def handleForgotPassword(_username, _password):
    data = {
        "username": _username,
        "password": _password
    }

    response = requests.post(URL + '/forgot_password', json=data)

    if response.status_code == 201:
        return {"status_code": response.status_code}
    else:
        return {
            "status_code": response.status_code,
            "res": response.json()['detail']
        }

def forgotPasswordPage():
    
    st.title('Forgot Password')

    with st.form('Forgot Password'):

        #Username
        _username = st.text_input('Username')

        #Password
        _password = st.text_input('New Password', type="password")

        _submit = st.form_submit_button('Submit')

        if _submit:
            if _username and _password:
                res = handleForgotPassword(_username, _password)

                if res['status_code'] == 201:
                    st.write("Password updated successfully!")
                    
                else:
                    st.write(res['res'])
            _username = ''



if __name__ == "__main__":
    forgotPasswordPage()