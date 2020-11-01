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
                    # print (each['portid'], 'is',each['state'] )

    return buffer



if __name__ == "__main__":  
    print(scan_all_ports(sys.argv[1]))
