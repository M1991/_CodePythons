## DATA EXTRACTION OF RAW DATA TO TEXT DATA
## Spliting and Organising the data 
##

import gc
import csv

loc = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Rw/Jan18Aug19BN5min.txt"
f = open(loc, 'r')

#  stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/Converted.txt"
stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/Cnv_Jan18Aug19BN5min.txt"
timeSeqs = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/timeSeqs.txt"  # o/p file
highs = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/highs.txt"
lowers = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/lowers.txt"
openers = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/openers.txt"
closure = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/closure.txt"
volumer = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/volumer.txt"

#f = open(loc, 'w')  ## "ok\"  "t\":
count = 0
cstr = '"c\\":['
strt = '"t\\":['
end = '"ok\\"'
flgs = False

def seqDetector(self, _filename):
    pass

with open(loc, 'r+', encoding='utf8') as src: #, open(stors,'w') as dest:
    ts = open(timeSeqs, 'w', encoding='utf8')
    # allC = src.readlines()
    for lne in src.readlines():                          
        if strt in lne:
            ts.write(lne)


f.close()
ts.close()
gc.collect()
#  dest.close()

"""
 i = 0
    while i < len(lines):
        if catch_start in lines[i]:
            for j in range(i + 1, len(lines)):
                if catch_end in lines[j] or j == len(lines)-1:
                    results.append(lines[i:j])
                    i = j
                    break
        else:
            i += 1


 while True:
        allC = src.read(1)        
        for c in allC.strip():
            # allC = allC.strip()
            if c:
                c=c.strip()
                if c == ',':                    
                    dest.write("\n")                
                    c = c.replace(',','')
                dest.write(c)
            elif c == ',':
                print("\n")
        # if allC == ',':
        #     print("\n")        
        #     # pass
        if not allC:
            print ("End of line")
            break
dest.close()


start = '#main'
end = '#extra'
numbers = []
file_handler = open('read_up_to_a_point.txt')
started = False
for line in file_handler:
    if end in line:
        started = False       
    if started:
        numbers.append(line.strip())
    if start in line:
        started = True
file_handler.close()



"""