from rpc import RPCClient
server = RPCClient('localhost', 8088)
server.connect()
print(server.add(5, 6))
print(server.sub(5, 6))
print(server.multi(2, 2))
print(server.hi())

while True:
    operation = input("¿Qué operación quieres realizar? (add/sub/multi/hi o 'salir' para terminar): ")
    if operation == "salir":
        break
    elif operation in ["add", "sub", "multi"]:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        print(getattr(server, operation)(a, b))  # Llama a la función correspondiente
    elif operation == "hi":
        print(server.hi())
    else:
        print("Operación no válida.")
server.disconnect()



