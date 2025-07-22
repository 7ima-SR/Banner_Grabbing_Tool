import socket
import sys
import argparse
import termcolor
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Banner Grabbing Tool"), "red"))
print(termcolor.colored("Powered by Hima", "yellow"))

parser = argparse.ArgumentParser(description='Banner Grabbing Tool')
parser.add_argument('-t', '--target', help='Target IP address or domain name', required=True)
parser.add_argument('-p', '--ports', help='Port(s) to connect to (e.g., 80 or 21,22,80)', default='80')
parser.add_argument('-T', '--timeout', type=int, default=1, help='Socket timeout in seconds')
parser.add_argument('-o', '--output', help='Output file to save results', default='results_banner_grabbing.txt')

args = parser.parse_args()
target  = args.target
timeout = args.timeout

def parse_ports(port_str):
    ports = []
    try:
        for p in port_str.split(','):
            ports.append(int(p.strip()))
        return ports
    except ValueError:
        print(f"[-] Invalid port format: {port_str}")
        sys.exit(1)

ports  = parse_ports(args.ports)    

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"[-] Could not resolve {target}. Please check the target IP or domain name.")
    sys.exit(1)

print(f"[+] Target IP: {target_ip}")
print(f"[+] Ports: {ports}")

def grab_banner(target_ip, port, timeout):
    try:
        with socket.socket() as s:
            s.settimeout(timeout)
            s.connect((target_ip, port))
            banner = s.recv(1024).decode(errors="ignore").strip()
            print(termcolor.colored(f"[+] Banner from {target}:{port} → {banner}", "green"))
            return f"{target}:{port} → {banner}"

    except socket.timeout:
        print(f"[-] Connection to {target}:{port} timed out.")
    except socket.error:
        print(f"[-] Could not connect to {target}:{port}.")
    except Exception as e:
        print(f"[-] Error on port {port}: {e}")
    return None

def save_banner_to_file(all_banner, output_file):
    if all_banner:
        try:
            with open(output_file, 'w') as f:
                for banner in all_banner:
                    f.write(f"{banner}\n")
            print(termcolor.colored(f"[+] All banners saved to {output_file}", "cyan"))
        except IOError as e:
            print(f"[-] Could not write to file {output_file}: {e}")
        except Exception as e:  
            print(f"[-] An error occurred while saving to file: {e}")

all_banner = []
for port in ports:
    banner = grab_banner(target_ip, port, timeout)
    if banner:
        all_banner.append(banner)


save_banner_to_file(all_banner, args.output)

