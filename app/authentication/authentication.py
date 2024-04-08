from supabase_config import supabase
import time

def login(email, password):
    """
    Authenticate a user with the provided email and password.

    Parameters:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        dict or None: A dictionary containing user information if login is successful,
                      None if login fails.
    """
    user = supabase.auth.sign_in(email=email, password=password)
    if user['error'] is not None:
        # Handle login error
        print("Login failed:", user['error']['message'])
        return None
    else:
        # Login successful
        print("Login successful!")
        return user['user']

def create_account(email, password):
    """
    Create a new user account with the provided email and password.

    Parameters:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        dict or None: A dictionary containing user information if account creation is successful,
                      None if account creation fails.
    """
    user = supabase.auth.sign_up(email=email, password=password)
    if user['error'] is not None:
        # Handle account creation error
        print("Account creation failed:", user['error']['message'])
        return None
    else:
        # Account creation successful
        print("Account created successfully!")
        return user['user']

def handle_create_account(controls):
    """
    Handle the create account button click event.

    Parameters:
        controls (list): List of UI controls containing user input fields.

    Returns:
        None
    """
    email = controls[3].controls[1].value
    password = controls[5].controls[1].value
    create_account(email, password)
