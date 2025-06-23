import os

print ('''
    \t\t\t\t\t\t\tWelcome to Linux Command System
    \t\t\t\t\t\t\t~~.~~.~~.~~.~~.~~.~~.~~.~~.~~.~~
    ''')

username = input("What is your user name: ")
ipAddress = input("What is your ip address (192.168.____): ")
while True:
    choice = input("What do u want Linux to perform (Type help for options): ")
    
    if "date" in choice:
        os.system(f" ssh {username}@192.168.{ipAddress} date ")
    elif "calender" in choice:
        os.system(f" ssh {username}@192.168.{ipAddress} cal ")
    elif "ip" in choice:
        os.system(f" ssh {username}@192.168.{ipAddress} ifconfig ")
    elif "list" in choice:
        os.system(f" ssh {username}@192.168.{ipAddress} ls ")
    elif "file with permissions" in choice:
        whichFile = input("Which file do u want to see: ")
        os.system(f" ssh {username}@192.168.{ipAddress} ls -l {whichFile}")
    elif "add user" in choice:
        newUser = input("Name of new user: ")
        os.system(f" ssh {username}@192.168.{ipAddress}  useradd {newUser} passwd")
        print("User added.")
    elif "install" in choice:
        newPackage = input("Name of package you want to install: ")
        os.system(f" ssh {username}@192.168.{ipAddress}  yum install {newPackage}")
        print("Package installed.")
    elif "delete user" in choice:
        dltUser = input("Name of user you want to delete: ")
        os.system(f" ssh {username}@192.168.{ipAddress}  userdel {dltUser}")
        print("User deleted.")
    elif "read" in choice:
        readFile = input("Which file do you want to read: ")
        os.system(f" ssh {username}@192.168.{ipAddress} cat {readFile}")
    elif "create" in choice:
        createFile = input("Which file do you want to create: ")
        os.system(f" ssh {username}@192.168.{ipAddress} touch {createFile}")
        print("File created.")
    elif "write" in choice:
        writeFile = input("In which file do you want to write: ")
        inputText = input(f"What message do you want to enter in {writeFile}: ")
        os.system(f"ssh {username}@192.168.{ipAddress} \"echo '{inputText}' >> {writeFile}\"")
        print("Written successfully.")
    elif "delete file" in choice:
        dltFile = input("Which file do you want to delete: ")
        os.system(f" ssh {username}@192.168.{ipAddress} rm {dltFile}")
        print("File created.")
    elif "top line" in choice:
        readHead = input("Which file do you want to read: ")
        numberOfLines = input("How many lines do you want to read: ")
        result = os.system(f" ssh {username}@192.168.{ipAddress} head -n {int(numnumberOfLines)} {readHead}")
        print(result)


    elif "permission" in choice:
        permissionFile = input("In which file do u want to modify permissions: ")
        os.system(f" ssh {username}@192.168.{ipAddress} ls -l {permissionFile} ")
        permChange = input("For whom do u want to change permissions (owner/group/others): ")
        askChange = input("Do you want to add or remove a permission: ")
        whatPerm =  input("What permission do u want to add or remove (read/write/execute): ")

        if "owner" in permChange and "add" in askChange and "read" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod u+r {permissionFile} ")
        elif "group" in permChange and "add" in askChange and "read" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod g+r {permissionFile} ")
        elif "other" in permChange and "add" in askChange and "read" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod o+r {permissionFile} ")
            
        elif "owner" in permChange and "add" in askChange and "write" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod u+w {permissionFile} ")
        elif "group" in permChange and "add" in askChange and "write" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod g+w {permissionFile} ")
        elif "other" in permChange and "add" in askChange and "write" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod o+w {permissionFile} ")
            
        elif "owner" in permChange and "add" in askChange and "execute" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod u+x {permissionFile} ")
        elif "group" in permChange and "add" in askChange and "execute" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod g+x {permissionFile} ")
        elif "other" in permChange and "add" in askChange and "execute" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod o+x {permissionFile} ")
            
        elif "owner" in permChange and "remove" in askChange and "read" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod u-r {permissionFile} ")
        elif "group" in permChange and "remove" in askChange and "read" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod g-r {permissionFile} ")
        elif "other" in permChange and "remove" in askChange and "read" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod o-r {permissionFile} ")
            
        elif "owner" in permChange and "remove" in askChange and "write" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod u-w {permissionFile} ")
        elif "group" in permChange and "remove" in askChange and "write" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod g-w {permissionFile} ")
        elif "other" in permChange and "remove" in askChange and "write" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod o-w {permissionFile} ")
            
        elif "owner" in permChange and "remove" in askChange and "execute" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod u-x {permissionFile} ")
        elif "group" in permChange and "remove" in askChange and "execute" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod g-x {permissionFile} ")
        elif "other" in permChange and "remove" in askChange and "execute" in whatPerm:
            os.system(f" ssh {username}@192.168.{ipAddress} chmod o-x {permissionFile} ")

        else: 
            print("Command not Found!")
            
        print("Change implemented please type show with permissions to check")
    
    elif "help" in choice:
        print('''
        Commands you can try:
        - date
        - calendar / calender
        - ip
        - list
        - list with permissions
        - add user
        - delete user
        - install
        - read
        - create
        - write
        - delete file
        - exit
        ''')
    elif "exit" in choice:
        exit()
    else:
        print("I could not understand what are you saying.")
