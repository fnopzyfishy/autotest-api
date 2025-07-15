import socket

response_arr = []

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        response_arr.append(data)

        response = '\n'.join(response_arr)
        client_socket.send(response.encode())


if __name__ == '__main__':
    server()