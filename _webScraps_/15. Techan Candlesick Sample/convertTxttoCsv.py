import csv

with open('E:/MaNoJ/My_Docs/EXP/D3/13. Example csv pasing/exindex.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('E:/MaNoJ/My_Docs/EXP/D3/13. Example csv pasing/log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Date','Open','High','Low','Close','Volume'))
        writer.writerows(lines)



# import os
# import pandas as pd
 
# save_path = "C:\Users\desktop\Python-testing\"
 
# in_filename = os.path.join(save_path,'Input.txt')
# out_filename = os.path.join(save_path,'Output.csv')
 
# df = pd.read_csv(in_filename, sep=";")
# df.to_csv(out_filename, index=False)