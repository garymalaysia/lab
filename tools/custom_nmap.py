import nmap3
import json
import sys


# nmap = nmap3.Nmap()
# json_output  = nmap.scan_top_ports(sys.argv[1])
# json_in_dict = json.dumps(json_output, indent=4)
# json_in_str  = json.loads(json_in_dict)

buffer = []

def josh_idea(ip):
    nmap = nmap3.NmapScanTechniques()
    json_output  = nmap.nmap_syn_scan(target=ip, args=" -A -v -p-")
    for each_ in json_output:
        for dictionary in json_output.get(each_):
            if type(dictionary) is dict:
                print (dictionary.get("service"))


if __name__ == "__main__":  
    print(josh_idea(sys.argv[1]))

