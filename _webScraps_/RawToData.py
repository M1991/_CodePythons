## DATA EXTRACTION OF RAW DATA TO TEXT DATA
## Spliting and Organising the data 
##

import gc
import csv

loc = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Rw/Jan18Aug19BN5min.txt"
f = open(loc, 'r')

#  stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/Converted.txt"
stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/Cnv_Jan18Aug19BN5min.txt"
timeSeqs = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/timeSeqs.txt"
highs = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/highs.txt"
lowers = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/lowers.txt"
openers = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/openers.txt"
closure = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/closure.txt"
volumer = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/volumer.txt"

#f = open(loc, 'w')
count = 0
cstr = '"c\\":['

def seqDetector(self, _filename):
    pass

with open(loc, 'r', encoding='utf8') as src: #, open(stors,'w') as dest:
    while True:
        # allC = src.read(1)     
        allC = src.readline()
        for c in allC:
            if '"t\\":[' in src.readline():
                ts = open(timeSeqs, 'w', encoding='utf8')
                ts.write(src.read())
                if ']' in src.readline():
                    ts.write("\n")
                    count = count + 1
                    ts.write("Sequence", + count)
                    ts.close()                        
                    break
        if not allC:            
            print ("End of line")
            break
print(count)
f.close()
gc.collect()
#  dest.close()