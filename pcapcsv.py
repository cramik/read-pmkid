from manuf import manuf
from mac_vendor_lookup import MacLookup
from netaddr import *
import sys
p = manuf.MacParser(update=True)
if(len(sys.argv)!=3): sys.exit("Usage: python3 pcapcsv.py input.hccapx output.csv")
else:
    with open(sys.argv[2], "w") as readable:
        readable.write("ESSID,AP MAC,CLIENT MAC,AP OUI,CLIENT OUI\n")
        with open(sys.argv[1], "r") as hccapx:
            for line in hccapx:
                data = line.split("*")
                oui_ap = ""
                oui_client = ""
                try:
                    oui_ap = MacLookup().lookup(data[3])
                except:
                    try:
                        oui_ap = EUI(data[3]).oui.registration().org
                    except:
                        if(p.get_manuf(data[3]) is not None): oui_ap = p.get_manuf(data[3])
                try:
                    oui_client = MacLookup().lookup(data[4])
                except:
                    try:
                        oui_client = EUI(data[4]).oui.registration().org
                    except:
                        if(p.get_manuf(data[4]) is not None): oui_client = p.get_manuf(data[4])
                readable.write("\"" + bytes.fromhex(data[5]).decode('utf-8') + "\"," +
                data[3] + "," +
                data[4] + ",\"" +
                oui_ap + "\",\"" +
                oui_client + "\"" +
                "\n") 