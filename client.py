import socket
import random

questions = [
    "Как тебя зовут?",
    "Какой сегодня день?",
    "Сколько будет 2+2?",
    "Какая погода за окном?",
    "Что нового?",
]


def main():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Подключено к серверу.")

        while True:
            question = random.choice(questions)
            print(f"Отправляется вопрос: {question}")
            client_socket.send(question.encode('utf-8'))

            # Получение ответа от сервера
            answer = client_socket.recv(1024).decode('utf-8')
            print(f"Ответ от сервера: {answer}")

            break


if __name__ == "__main__":
    main()
