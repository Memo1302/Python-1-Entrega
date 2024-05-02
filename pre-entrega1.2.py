def register_user(database):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Comprueba si el nombre de usuario ya existe en la base de datos

    if username in database:
        return "Username already exists."
    
    # Almacena la contraseña
    
    database[username] = password
    return "User registered successfully."

def login_user(database):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Comprueba si el nombre de usuario existe en la base de datos
    if username not in database:
        return "Username not found."
    
    # Comprueba si la contraseña ingresada coincide con la contraseña almacenada

    stored_password = database.get(username)
    if stored_password != password:
        return "Incorrect password."
    
    return "Login successful."

def list_users(database):
    return "\n".join(database.keys())

def main():
    user_database = {}
    interacting = True

    while interacting:
        option = input("Select an option (register/login/list users/quit): ")
        
        if option.lower() == "register":
            message = register_user(user_database)
            print(message)
        elif option.lower() == "login":
            message = login_user(user_database)
            print(message)
        elif option.lower() == "list users":
            users = list_users(user_database)
            print("User database:\n", users)
        elif option.lower() == "quit":
            interacting = False
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
