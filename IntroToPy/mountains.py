import ast
import statistics
tari = {}
munti = {}
inalt = {}
names = []
count= 0
with open("IntroToPy/mountains.tsv", "r") as data:
    for line in data.readlines():
        part = line.split("\t", -1)
        print(f"{part[0]} _ {part[1]} _ {part[2]} _ {part[3]}")
        names.append(part[0])
        if part[0] not in munti:
            munti[part[0]] = []
        munti[part[0]].append(count)
        if part[1] not in inalt:
            inalt[part[1]] = []
        inalt[part[1]].append(count)
        if part[2] not in tari:
            tari[part[2]] = []
        tari[part[2]].append(count)
        count += 1
print(f"THe number of countries :: {len(tari.keys())}")
print(f"The unmber of unknown altitudes :: {len(inalt["NULL"])}")
sort_inalt = sorted(inalt.keys())
sort_inalt.pop()
sort_inalt = [int(x) for x in sort_inalt]
print(f"Minimum altitude :: {sort_inalt[0]}; Maximum random :: {sort_inalt[-1]} ")
print(f"The average value of altitude :: {statistics.mean(sort_inalt)}")
print(f"Median of the heights :: {statistics.median(sort_inalt)}")
topp =int( input("How many mountains should be on the podium?"))
for n in range(1,int(topp)):
    print(f"Place {n} goes to :: {names[sort_inalt[-1]]}")
#print(f"Standard Deviation of the sequence: {statistics.stdev(sorted_randoms)}")
#for n in inalt.keys():
#    print(f"{n} _ {inalt[n]}")