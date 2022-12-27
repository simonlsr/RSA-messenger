import socket
import hashlib
import sys
sys.path.append("backend_tests")
import backend_main as backend_main
sys.path.append("backend_tests/login")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10001))

username_in = "Paul"
password_in = "Paul1234"
option = "f"

def delete_from_database(message_id_list: list, client_function: socket.socket, username: str):
    client_function.send(str(message_id_list).encode())
    client_function.recv(1024).decode()
    client_function.send(username.encode())
    client_function.recv(1024).decode()
    
    


def fetch_messages(client_function: socket.socket, username_function: str):
    client_function.send("f".encode())

    print(client_function.recv(1024).decode())
    fetched_messages = client_function.recv(4294967296).decode()
    list_of_tuples_containing_fetched_messages = eval(fetched_messages)
    list_decrypted_messages = []
    
    for i, j in enumerate(list_of_tuples_containing_fetched_messages):
        list_decrypted_messages.append({
            "message_id": list_of_tuples_containing_fetched_messages[i][0],
            "sender_id": list_of_tuples_containing_fetched_messages[i][2],
            "receiver_id": list_of_tuples_containing_fetched_messages[i][1],
            "message": backend_main.main().decrypt(int(list_of_tuples_containing_fetched_messages[i][3]), int(list_of_tuples_containing_fetched_messages[i][4]), int(list_of_tuples_containing_fetched_messages[i][5]), int(list_of_tuples_containing_fetched_messages[i][6]), int(list_of_tuples_containing_fetched_messages[i][7]), int(list_of_tuples_containing_fetched_messages[i][8]), int(list_of_tuples_containing_fetched_messages[i][9]), int(list_of_tuples_containing_fetched_messages[i][10]), int(list_of_tuples_containing_fetched_messages[i][11])),
            "date": list_of_tuples_containing_fetched_messages[i][12]
        })
    
    with open("backend_tests/login/fetched_messages.txt", "r") as f:
        file_contents_temp = f.read()
        file_contents_temp = eval(file_contents_temp)
        message_ids = []
        for i in file_contents_temp:
            message_ids.append(i["message_id"])
    
    message_ids_temp = []
    for i in list_decrypted_messages:
        if i["message_id"] not in message_ids:
            file_contents_temp.append(i)
        elif i["message_id"] in message_ids:
            message_ids_temp.append(i["message_id"])
    
    delete_from_database(message_ids_temp, client_function, username_function)
                
    
    with open("backend_tests/login/fetched_messages.txt", "w") as f:
        f.write(str(file_contents_temp))
    
    with open("backend_tests/login/fetched_messages.txt", "r") as f:
        print(f.read())

def send_message(client_function: socket.socket, username_function: str):
    message = input()


username_request = client.recv(1024).decode()
# username_from_user = input(username_request)
username_from_user = username_in
client.send(username_in.encode())
password_request = client.recv(1024).decode()
# password_from_user = input(password_request)
client.send(hashlib.sha256(password_in.encode()).hexdigest().encode())
client.recv(1024)
if option == "f":
    fetch_messages(client, username_from_user)
elif option == "s":
    send_message(client, username_from_user)

    

        




client.send("".encode())

