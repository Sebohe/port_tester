import multiprocessing as mp
#python-nmap
import nmap

def scan(host, ports):

    nm = nmap.PortScanner()
    print ("host: {}".format(host))
   

    if type(ports) == int:
        ports = range(ports, ports + 1)

    for p in ports:
        nm.scan(host, str(p))
        if nm[host]['tcp'][int(p)]['state'] == 'open':
            print ("Open port: {}:{}".format(host, p))

if __name__ == "__main__":


    all_ports = range(0, 65536)
    hosts = []
    ports = [all_ports, all_ports]



    for i, h in enumerate(hosts):

        proc = mp.Process(target=scan, args=(h, ports[i], ))
        proc.start()
