import nmap3
import json
import sys
# nmap = nmap3.Nmap()
# json_output  = nmap.scan_top_ports(sys.argv[1])
# json_in_dict = json.dumps(json_output, indent=4)
# json_in_str  = json.loads(json_in_dict)
buffer = []
def scan_all_ports(host): # perfrom all port scan
    nmap = nmap3.NmapScanTechniques()
    json_output  = nmap.nmap_syn_scan(target=host, args="-Pn -p 1-65535")
    json_in_dict = json.dumps(json_output, indent=4)
    json_in_str  = json.loads(json_in_dict)
    for page in json_in_str:
       for each in json_in_str.get(page):
            if type(each) is dict:
                if each['state'] == 'open':
                    buffer.append(each['portid'])
    return buffer
def josh_idea(ip):
    nmap = nmap3.NmapScanTechniques()
    json_output  = nmap.nmap_syn_scan(target=ip, args="-Pn -A -p-")
    json_in_dict = json.dumps(json_output, indent=4)
    return json_in_dict
def scan_all_open_ports(ports:list):
    nmap = nmap3.NmapHostDiscovery()
    #print(listToString(ports))
    json_output  = nmap.nmap_portscan_only(target=sys.argv[1], args="-sV -sT -A -p %s" % (listToString(ports)))
    json_in_dict = json.dumps(json_output, indent=4)
    print (json_in_dict)
def listToString(s):
    str1 = ","
    return (str1.join(s))
if __name__ == "__main__":  
    #scan_all_open_ports(scan_all_ports(sys.argv[1]))
    print(josh_idea(sys.argv[1]))
