import streamlit as st
import requests

# Define the API endpoint URL
URL = 'http://bigdata7245-finalproject.ue.r.appspot.com'

#Session State for Login
if 'login_success' not in st.secrets:
    st.session_state['login_success'] = False
#Session State for Register
if 'register_success' not in st.secrets:
    st.session_state['register_success'] = False

def handleRegister(_username, _password, _restaurant_name, _tier):
    registerData = {
        "username": _username,
        "password": _password,
        "restaurant_name": _restaurant_name,
        "user_tier": _tier.lower()
    }

    print(registerData)

    response = requests.post(URL + '/register', json=registerData)

    if response.status_code == 201:
        return True
    else:
        return False


def registerPage():
    st.title('Register')

    with st.form('register'):

        #username
        _username = st.text_input('Username')

        #Password
        _password = st.text_input('Password', type="password")

        #Restaurant Name
        _restaurant_name = st.text_input('Restaurant Name')

        #Tier
        _tier = st.selectbox('Tier', ('Free', 'Gold', 'Platinum'))

        _submit = st.form_submit_button("Register")

        if _submit:
            if _username and _password and _restaurant_name and _tier:
                res = handleRegister(_username, _password, _restaurant_name, _tier)
                if res:
                    st.session_state.register_success = True
                else:
                    st.session_state.register_success = False
                    st.write('Registered successfully! Please login to access.')


if __name__ == "__main__":
    if st.session_state.login_success:
        st.write("You're already logged in, please accesss other tabs!")
    else:
        registerPage()