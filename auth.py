# auth.py - Basic user authentication module



class Authenticator:

    def __init__(self):

        # A sample user database (for demonstration purposes)

        self.users = {"admin": "password123", "john_doe": "securepass"}



    def login(self, username, password):

        """Check if the provided credentials are correct."""

        if username in self.users and self.users[username] == password:

            return f"Login successful! Welcome, {username}."

        else:

            return "Invalid username or password. Please try again."



# Sample usage

if __name__ == "__main__":

    auth = Authenticator()

    

    # Test login with a valid user

    print(auth.login("admin", "password123"))

    

    # Test login with incorrect credentials

    print(auth.login("admin", "wrongpassword"))
