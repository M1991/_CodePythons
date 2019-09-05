## DATA EXTRACTION OF RAW DATA TO TEXT DATA
## Spliting and Organising the data 
##

## STATUS :  TESTING PHASE

import gc
import csv

loc = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/storres.txt"   ## org raw dt
f = open(loc, 'r')

#  stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/Converted.txt"
stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/storres.txt"
timeSeqs = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/timeSeqs.txt"  # o/p file
highs = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/highs.txt"
lowers = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/lowers.txt"
openers = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/openers.txt"
closure = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/closure.txt"
volumer = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/volumer.txt"


#f = open(loc, 'w')  ## "ok\"  "t\":
strt = '"t\\":['
end = '"ok\\"'
clsr = '"c\":['
flgs = False
rplc = '\\"s\\":\\"ok\\"}""text":'

def seqDetector(self, _filename):
    pass

with open(loc, 'r+', encoding='utf8') as src: #, open(stors,'w') as dest:
    ts = open(highs, 'w', encoding='utf8')    ## highs
    for lne in src.readlines():                          
        # if strt in lne:
        #     lne = lne.replace(']',']\n')
        #     ts.write(lne)
        if strt in lne:                
            tsd = open(volumer, 'w', encoding='utf8')
            tsd.write(lne)
            if ']' in lne:
                tsd.write("\n")
                tsd.close()
        elif clsr in lne:
            clse = open(closure, 'w')
            clse.write(lne)
            if ']' in lne:
                clse.write("\n")
                clse.close()
        elif '"o\\":[' in src.readline():
            opn = open(openers, 'w')
            opn.write(src)
            if ']' in src.readline():
                opn.write("\n")
                opn.close()
                break

f.close()
ts.close()
tsd.close()


# with open(stors, 'r') as src, open(timeSeqs,'w') as dest:   
#     while True:
#         allC = src.read(1)        
#         for c in allC.strip():
#             if c:
#                 c=c.strip()
#                 if c == ',':                    
#                     dest.write("\n")                
#                     c = c.replace(',','')
#                 dest.write(c)
#             elif c == ',':
#                 print("\n")        
#         if not allC:
#             print ("End of line")
#             break
src.close()
# dest.close()
gc.collect()
#  dest.close()
