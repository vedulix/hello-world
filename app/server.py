import io
import http
import http.server
import shutil
import socket


# Обработчик HTTP-запросов
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':  # отвечаем только на /ping
            message = 'OK'
            self.send_response(http.HTTPStatus.OK)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(message)))
            self.end_headers()
            self.wfile.write(message.encode())  # отправляем "OK" в ответ


# Класс сервера, наследующийся от ThreadingHTTPServer для многопоточной работы
class Server(http.server.ThreadingHTTPServer):
    # Использование IPv6
    address_family = socket.AF_INET6


# Основная функция
def main():
    # Установка адреса сервера и порта
    server_address = ('::', 8080)
    # Создание экземпляра сервера с заданным адресом и обработчиком
    httpd = Server(server_address, Handler)
    # Запуск сервера и бесконечный цикл обработки запросов
    httpd.serve_forever()
