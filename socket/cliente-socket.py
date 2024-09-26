import socket
import threading  

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP
    host = '127.0.0.1'  # Define la dirección IP del servidor (localhost)
    port = 12345  # Define el puerto al que se conectará el cliente
    client_socket.connect((host, port))  # Conecta el socket del cliente al servidor

    while True: 
        message = input("Enter your message: ") 
        client_socket.sendall(message.encode('utf-8'))  # Envía el mensaje al servidor en formato de bytes
        data = client_socket.recv(1024)  # Recibe la respuesta del servidor
        response = data.decode('utf-8')  # Decodifica la respuesta de bytes a cadena
        print(f"Server response: {response}")  # Muestra la respuesta del servidor en la consola

if __name__ == "__main__": 
    main() 
