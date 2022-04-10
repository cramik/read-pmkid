Takes in a modern hccapx file for WPA hashes and outputs all of the human readable information into a csv file formatted as (ESSID,AP MAC,CLIENT MAC,AP OUI,CLIENT OUI)





## Installation

1. clone repo or download as zip and extract

2. Download pip repo's used to handle OUI lookups
   
   ```
   pip install -r requirements.txt
   ```



## Usage

```
python3 pcapcsv.py input.hccapx output.csv
```




