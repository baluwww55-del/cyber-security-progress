# Day 09 – Networking Lab (Cisco Packet Tracer + Nmap)

## Overview
Today I continued practicing networking fundamentals by building a simple network using Cisco Packet Tracer and performing basic network scanning using Kali Linux and Nmap.

This lab is part of my ongoing learning in networking and cybersecurity.

## Tools Used
- Cisco Packet Tracer
- Kali Linux
- Nmap
- Virtual lab environment

## Network Setup
I created a small local network with:

- 1 Router  
- 1 Switch  
- 2 PCs  
- 1 Kali Linux machine (attacker machine)

All devices were configured in the same subnet.

Example IP scheme:
- Router: 192.168.1.1  
- PC1: 192.168.1.2  
- PC2: 192.168.1.3  
- Kali Linux: 192.168.1.4  

Subnet: 255.255.255.0

## Lab Steps

### 1. Created topology in Cisco Packet Tracer
- Added router and switch  
- Connected PCs using copper straight-through cables  
- Configured IP addresses manually  
- Verified connections  

### 2. Connectivity Test
Used ping to confirm devices communicate:

ping 192.168.1.1  
ping 192.168.1.2  
ping 192.168.1.3  

All hosts responded successfully.

### 3. Nmap Scanning (Kali Linux)

#### Host discovery
