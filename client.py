import socket

def enviar_comando(comando):
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('endereco_do_servidor', 8080))
    
    cliente_socket.sendall(comando.encode())
    
    resultado = cliente_socket.recv(4096).decode()
    print(f"Resultado do Nmap:\n{resultado}")
    
    cliente_socket.close()

if __name__ == "__main__":
    comando_nmap = input("Digite o comando Nmap: ")
    enviar_comando(comando_nmap)
