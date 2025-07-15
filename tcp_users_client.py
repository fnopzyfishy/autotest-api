import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    print("Подключено к серверу")

    message = "Привет, сервер!"
    client_socket.send(message.encode())
    print(f"Отправлено серверу: {message}")

    response = client_socket.recv(1024).decode()
    print("Получена история сообщений от сервера:")
    print(response)

    client_socket.close()
    print("Соединение закрыто")


if __name__ == '__main__':
    client()