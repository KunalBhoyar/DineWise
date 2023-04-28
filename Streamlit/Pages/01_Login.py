import streamlit as st
import requests

# Define the API endpoint URL
URL = 'http://bigdata7245-finalproject.ue.r.appspot.com'

#Session State for Login
if 'login_success' not in st.secrets:
    st.session_state['login_success'] = False
if 'login_token' not in st.secrets:
    st.session_state['login_token'] = False

def handleLogin(username, password):
    loginData = {
        'username': username,
        'password': password
    }

    print(loginData)

    response = requests.post(URL + '/login', json=loginData)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        res = response.json()
        return {'code': 401, 'res': res['detail']}

def loginPage():
    st.title('Login')
    
    with st.form("login"):       
        
        #Username
        _username = st.text_input('Username')
        
        #Password
        _password = st.text_input('Password', type="password")

        _submit = st.form_submit_button("Login")
        if _submit:
            if _username and _password:
                res = handleLogin(_username, _password)
                if 'token' in res:
                    print(res['token'])
                    st.session_state['login_success'] = True
                    st.session_state['login_token'] = res['token']
                    st.write('Login successful! ✅')
                else:
                    st.write(res['res'])
            elif not _username:
                st.write("Enter username!")
            elif not _password:
                st.write("Enter password!")

if __name__ == "__main__":
    if st.session_state.login_success:
        st.write('You\'re logged in!, access the other tabs.')
    else:
        loginPage()