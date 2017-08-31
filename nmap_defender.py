"""
Filename: nmap_defender.py
Description: This script will allow for the automated scanning of network assets and dumping these results to a CSV file.
This is accomplished by first starting a host discovery scan using the nmap API. This list of targets is then scanned by
nmap. Once the scan completes a CSV is outputted for review.
Author: DJ Moder
"""
import sys
import os
try:
    import nmap
except:
    sys.exit("[!] Install the nmap library: pip install python-nmap")

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"


sys.stdout.write(BLUE)
SQLi_humor = "SELECT nmap_defender from tables--"
print SQLi_humor
sys.stdout.write(GREEN)
print "Running Nmap Defender"

nm = nmap.PortScanner()

# Start Nmap Scan
sys.stdout.write(RED)
print "[!] Starting nmap host discovery: Please be patient..."
os.system('nmap -sn 192.168.1.0/24 |grep 192.* |cut -d " " -f 5 > alive.txt')


print "[!] Starting nmap scan of target(s): Please be patient..."
#nmap scan from list TCP Connect, looking for weak protocols. Pulls target info from alive.txt
nm.scan(hosts='', arguments='-Pn -sT -T4 --top-ports 1000 -iL ./alive.txt')

#Running last nmap scan results at XML
content = nm.get_nmap_last_output()
nm.analyse_nmap_xml_scan(content)
sys.stdout.write(BLUE)
print "[!] converting XML to CSV"
#store csv data in variable "Data"
data = nm.csv()
print "[!] Generating CSV file for review"

# Final output file
with open('nmapresults.csv','w') as myCSV:
    for line in data.split("\r\n"):
        myCSV.write(line.replace(';',',')+'\n')
sys.stdout.write(GREEN)
print "[*]Process Complete[*]"
sys.stdout.write(RESET)

