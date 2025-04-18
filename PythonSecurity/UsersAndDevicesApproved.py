approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

def login(username,device_id):

    if username in approved_users:
        print("The user", username, "is approved to access the system.")
        ind = approved_users.index(username)

        if device_id == approved_devices[ind]:
          print(device_id, "is the assigned device for", username)
        else:
          print(device_id, "is not their assigned device.")

    else:
        print("The username", username, "is not approved to access the system.")

login("elarson", "8rp2k75")
