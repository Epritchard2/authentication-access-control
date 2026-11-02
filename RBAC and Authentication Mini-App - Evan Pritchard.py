
# Users and their roles
users = {
    "admin123": "admin",
    "student123": "user"
}

# Admin-only function
def admin_page(role):
    if role == "admin":
        print("Admin page: Access granted.")
    else:
        print("Admin page: Access denied.")

# User-only function
def user_page(role):
    if role == "user":
        print("User page: Access granted.")
    else:
        print("User page: Access denied.")

# Simulate logging in as each user
for username, role in users.items():
    print("\n----------------------")
    print("Logged in as:", username)
    print("Role:", role)

    admin_page(role)
    user_page(role)

print("\nSimulation complete.")
