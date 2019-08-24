## CONVERSION FROM TEXT TO DATA SET

import csv

loc = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Rw/Raw19.txt"
f = open(loc, 'r')

stors = "E:/MaNoJ/My_Docs/EXP/PYTHON/_WebScrapper_/Data/Dtata/Converted.txt"
#f = open(loc, 'w')

with open(loc, 'r') as src, open(stors,'w') as dest:
    #for itr in src:
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

# for itr in f:
#     x = f.readline()
#     for ltr in x:
#         if ltr == ']':
#             print("\n")
#             print(itr) 
    # if itr == ',':
    #     break
    # else:
    #     print(x)
