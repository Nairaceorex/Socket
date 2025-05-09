import socket


qa = {
    "Как тебя зовут?": "Я - сервер.",
    "Какой сегодня день?": "Сегодня отличный день!",
    "Сколько будет 2+2?": "2+2=4, как всегда.",
    "Какая погода за окном?": "Я сервер, мне не холодно и не жарко.",
}


def handle_client(conn, addr):
    print(f"Клиент подключился: {addr}")
    while True:
        try:
            # Получаем вопрос от клиента
            question = conn.recv(1024).decode('utf-8')
            if not question:
                break

            print(f"Клиент задал вопрос: {question}")
            # Подбираем ответ или выдаем случайный
            answer = qa.get(question, "Я не знаю ответа на этот вопрос.")
            conn.send(answer.encode('utf-8'))
            print(f"Ответ отправлен: {answer}")
        except ConnectionResetError:
            print(f"Клиент {addr} отключился.")
            break
    conn.close()


def main():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Сервер запущен и ждет подключения...")

        while True:
            conn, addr = server_socket.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    main()
