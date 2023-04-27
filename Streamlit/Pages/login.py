import streamlit as st

def loginPage():
    st.title('Login')
    
    with st.form("login"):
        #Session State for Login
        if 'username' not in st.secrets:
            st.session_state['username'] = False
        if 'password' not in st.secrets:
            st.session_state['password'] = False
        
        #Username
        _username = st.text_input('Username')
        
        #Password
        _password = st.text_input('Password', type="password")

        # Every form must have a submit button.
        _submit = st.form_submit_button("Login")
        if _submit:
            st.write("Login successful!")

if __name__ == "__main__":
    loginPage()