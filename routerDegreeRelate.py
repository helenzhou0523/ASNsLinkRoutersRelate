"""
 Name: Bingjie-Zhou
 UCSD PID: A13711806
 Date: November,12nd,2016
 File: routerDegreeRelate.py
 
 This python program is used for correlate the degrees and routers of each AS
 that both appear in links.txt file and routers.txt file

"""
fiLinks = open ( "links.txt" , "r" )
fiRouters = open ( "routers.txt" , "r" )
fo = open("output","w");

links = fiLinks.readlines ()
routers = fiRouters.readlines()
numLinks = [0 for i in range(1000000)]
numRouters = [0 for i in range(1000000)]

for i in range(len(links)):
    word = links[i].split()
    numLinks[int(word[0])]+= 1
    numLinks[int(word[1])]+= 1

for i in range(len(routers)):
    word = routers[i].split()
    numRouters[int(word[0])] += int(word[1])

for i in range(1000000):
    if numLinks[i]>0 and numRouters[i]>0:
        fo.write(str(i)+"\t"+str(numLinks[i])+"\t"+str(numRouters[i])+"\n")

fiLinks.close()
fiRouters.close()
fo.close()
