# nmap_defender
Script to automate the protection and discovery of the top 1000 vulnerable ports in an enterprise using the Nmap API. This script was developed on my own time and is free to use for everyone.

Script Objective: Provide an automated way for cyber defenders to scan their enterprises using the Nmap API and outputing those results to a CSV file for analysis.

Intended Operating Systems: OSX/Linux

Nmap Scan Options Reference: https://nmap.org/book/man-port-scanning-techniques.html

Script Usage Examples:

#Changing IP CIDR range. Grep the first octect of the Target IP Address (IE: 172. 192. etc)

os.system('nmap -sn IPAddressesHere/24 |grep 192.* |cut -d " " -f 5 > alive.txt')


#Look for top 1000 ports

nm.scan(hosts='', arguments='-Pn -sT -T4 —top-ports 1000 -iL ./alive.txt')

#Look for webservers on common port(s)

nm.scan(hosts='', arguments='-Pn -sT -T4 —p 80,443 -iL ./alive.txt')

#Stealth Syn Scan (Script must be run as root for this to work)

nm.scan(hosts='', arguments='-Pn -sS -T4 —top-ports 1000 -iL ./alive.txt')

Warning: Each scan you run will overwrite the previous CSV file, be sure to copy scan to a safe location if you intend to keep the results before re-running this tool.






