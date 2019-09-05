## DATA EXTRACTION OF RAW DATA TO TEXT DATA
## Spliting and Organising the data 
""" Read each line
    when find "e\":[
        optional - read and write each line till it gets ] and save written location
        - copy till it gets ]
        - write, get to next line, get written file location and save
        - close the file and break
"""
import gc
import csv

loc = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/storres.txt"
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
## tcohlvvo
count = 0
cstr = '"t\\":['
cstr2 = '"c\\":['

def seqDetector(self, _filename):
    pass

with open(loc, 'r+', encoding='utf8') as src: #, open(stors,'w') as dest:
    while True:
        # allC = src.read(1)     
        allC = src.readlines()
## check sequence and start from bottom if in sequence 
## else start from top - always check the sequence

        for cs in src.readlines():
            if '"t\\":[' in cs:                
                ts = open(volumer, 'r+', encoding='utf8')
                ts.write(cs)
                # if ']' in c:
                #     ts.write("\n")
                #     ts.close()
            elif '"c\\":[' in cs:
                clse = open(closure, 'w')
                clse.write(cs)
                if ']' in cs:
                    clse.write("\n")
                    clse.close()
            elif '"o\\":[' in src.readline():
                opn = open(openers, 'w')
                opn.write(src)
                if ']' in src.readline():
                    opn.write("\n")
                    opn.close()
                    break
            elif '"h\\":[' in src.readline():
                hgs = open(highs, 'w')
                hgs.write(src)
                if ']' in src.readline():
                    hgs.write("\n")
                    hgs.close()
                    break
            elif '"l\\":[' in src.readline():
                lwr = open(lowers, 'w')
                lwr.write(src)
                if ']' in src.readline():
                    lwr.write("\n")                    
                    lwr.close()
                    break
            elif '"v\\":[' in src.readline():
                vlm = open(volumer, 'w')
                vlm.write(src)
                if ']' in src.readline():
                    vlm.write("\n")
                    vlm.close()
                    break
        if not allC:            
            print ("End of line")
            break
print(count)
f.close()
gc.collect()
#  dest.close()