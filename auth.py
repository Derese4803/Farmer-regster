import streamlit as st

# Define your authorized users here
USERS = {
    "admin": "amhara2025",
    "surveyor1": "field123",
    "surveyor2": "field456"
}

def login_user(username, password):
    """Checks if the username and password match our records."""
    if username in USERS and USERS[username] == password:
        return True
    return False

def logout():
    """Clears the user session."""
    if "user" in st.session_state:
        del st.session_state["user"]
    st.rerun()

def check_auth():
    """
    Call this at the top of main() to ensure 
    the user is logged in before seeing the app.
    """
    if "user" not in st.session_state:
        st.title("🚜 2025 Amhara Survey Login")
        
        with st.form("login_form"):
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            submit = st.form_submit_button("Enter System")
            
            if submit:
                if login_user(u, p):
                    st.session_state["user"] = u
                    st.success(f"Welcome {u}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid Username or Password")
        st.stop() # Stops the rest of app.py from running
