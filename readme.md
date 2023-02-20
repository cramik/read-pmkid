Takes in a file with WPA hashes formatted as "WPA-PBKDF2-PMKID+EAPOL" / hashcat 22000 and outputs all of the human readable information into a csv file formatted as (ESSID,AP MAC,CLIENT MAC,AP OUI,CLIENT OUI)





## Installation

1. clone repo or download as zip and extract

2. Download pip repo's used to handle OUI lookups
   
   ```
   pip install -r requirements.txt
   ```



## Usage

```
python3 pcapcsv.py input output.csv
```




