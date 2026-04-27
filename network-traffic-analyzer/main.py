from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP]

        print(f"\nSource: {ip.src} → Destination: {ip.dst}")

        if packet.haslayer(TCP):
            print("Protocol: TCP")

        elif packet.haslayer(UDP):
            print("Protocol: UDP")

        print("-" * 50)

print("Starting smart capture...")
sniff(prn=process_packet, store=False)
