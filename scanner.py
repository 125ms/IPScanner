import socket
from datetime import datetime

def port_scanner(target):
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n ❌ El nombre del host no pudo ser resuelto.")
        return

    print(f"\n Escaneando objetivo: {target_ip}")
    print(f" Tiempo de inicio: {datetime.now()}")
    print("-" * 50)

    common_ports = [21, 22, 80, 443, 8080, 3306]

    for port in common_ports: 

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f" [+] Puerto {port}: ABIERTO")
        else:
            print(f" [-] Puerto {port}: Cerrado / Filtrado")
            s.close()

if __name__ == "__main__":
    target = input("Introduce la IP o dominio a escanear (ej. 192.168.1.1):")
    port_scanner(target) 