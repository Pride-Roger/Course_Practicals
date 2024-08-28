"""with open('Sample.txt', 'w') as V_1:
    V_1.write('Sample text.')"""

"""with open('Sample.txt', 'r') as V_1:
    V=V_1.readlines()
    print(len(V))"""
    
"""with open('Sample.txt', 'r') as V_1, open('Sample_2.txt', 'w') as V_2:
    V=V_1.readlines()
    for z in V:
        V_2.write(z)"""
        
import csv

with open('Sample_CSV.csv', 'w', newline='') as V_1:
    V=csv.writer(V_1)
    
    V.writerow(['Sample', 'line', 1])
    V.writerow(['Sample', 'line', 2])
    V.writerow(['Sample', 'line', 3])
    
with open('Sample_CSV.csv', 'r') as V_2:
    Var=csv.reader(V_2)
    for read in Var:
        print(read)