def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def hi():
    return "Saludos humano"

def multi(a, b):
    return a * b  # Multiplicación simple

from rpc import RPCServer

# Configura el servidor para escuchar en localhost y puerto 8088
server = RPCServer('localhost', 8088)
server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(multi)
server.registerMethod(hi)

# Corre el servidor
server.run()
