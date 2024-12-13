class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

users = [
    User(1, "admin", "admin123", "admin"),
    User(2, "user1", "password1", "user"),
    User(3, "user2", "password2", "user"),
]

def login(users):
    print("Welcome to the Login System")
    try:
        username = input("Enter your username: ")
        if not username:
            raise ValueError("Username cannot be empty.")
        password = input("Enter your password: ")
        if not password:
            raise ValueError("Password cannot be empty.")

        for user in users:
            if user.username == username and user.password == password:
                print(f"Login successful! Welcome, {user.username}.")
                if user.role == "admin":
                    print("You have admin privileges.")
                else:
                    print("You are logged in as a regular user.")
                return user

        print("Invalid username or password. Please try again.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

logged_in_user = login(users)
if logged_in_user:
    print(f"User {logged_in_user.username} with role {logged_in_user.role} is logged in.")
