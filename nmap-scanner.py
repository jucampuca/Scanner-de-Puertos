import nmap
import pyfiglet


def print_shade():
    ascii_art = pyfiglet.figlet_format("""
                                            <- _ -> 
                                       Zombits""")
    print(ascii_art)

print_shade()

print("[Info] Herramienta para escanear los puertos abiertos en una dirección IP")
print("     ||     Escrito en Python y usando Nmap")

host = input("[+] Introduce la IP objetivo: ")
nm = nmap.PortScanner()
puertos_abiertos = '-p '
count = 0
results = nm.scan(host)
# print(results)


print('Host : %s' % host)
print('State : %s' % nm[host].state())
for proto in nm[host].all_protocols():
    print('Protocol : %s' % proto)
    lport = nm[host][proto].keys()
    sorted(lport)
    for port in lport:
        print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
        if count == 0:
            puertos_abiertos = puertos_abiertos + " " + str(port)
            count = 1
        else:
            puertos_abiertos = puertos_abiertos + "," + str(port)

print("Puertos abiertos " + puertos_abiertos + " " + str(host))

