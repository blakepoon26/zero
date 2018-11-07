import users

while(1):
    primary_user = str(input("Input your initials: "))
    if primary_user in users.USERS["Initials"].values:
        break
    else:
        print("Invalid user initials. "
              "Please select intials from \n{}.".format(users.USERS))
        continue

print(primary_user)