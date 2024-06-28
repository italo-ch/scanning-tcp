import socket
import subprocess

def executar_nmap(comando):
    try:
        resultado = subprocess.check_output(comando, shell=True)
        return resultado.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

def servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('0.0.0.0', 8080))
    servidor_socket.listen(5)
    print("Servidor escutando na porta 8080...")

    while True:
        cliente_socket, addr = servidor_socket.accept()
        print(f"Conexão de {addr}")
        
        comando = cliente_socket.recv(1024).decode()
        print(f"Comando recebido: {comando}")
        
        resultado = executar_nmap(comando)
        cliente_socket.sendall(resultado.encode())
        
        cliente_socket.close()

if __name__ == "__main__":
    servidor()
