import socket 
import threading  
def handle_client(client_socket):
    while True:  
        data = client_socket.recv(1024)  # Recibe hasta 1024 bytes de datos del cliente
        if not data:  # Si no hay datos, significa que el cliente ha cerrado la conexión
            break  
        message = data.decode('utf-8')  # Decodifica los datos recibidos de bytes a cadena
        print(f"Received message: {message}")  # Muestra el mensaje recibido en la consola
        response = "Server received your message: " + message  # Prepara la respuesta para el cliente
        client_socket.sendall(response.encode('utf-8'))  # Envía la respuesta al cliente en formato de bytes
    client_socket.close()  # Cierra el socket del cliente cuando termina la comunicación

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP
    host = '127.0.0.1'  # Define la dirección IP del servidor (localhost)
    port = 12345  # Define el puerto en el que el servidor escuchará las conexiones
    server_socket.bind((host, port))  # Asocia el socket a la dirección y puerto definidos
    server_socket.listen(5)  # El servidor comienza a escuchar hasta 5 conexiones en espera
    print(f"Server listening on {host}:{port}")  # Informa que el servidor está activo

    while True:
        client_socket, client_address = server_socket.accept()  # Acepta una conexión entrante
        print(f"Accepted connection from {client_address}")  # Muestra la dirección del cliente conectado
        # Crea un nuevo hilo para manejar la comunicación con el cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()  

if __name__ == "__main__": 
    main() 
