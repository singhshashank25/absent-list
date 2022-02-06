import pandas as pd

df = pd.read_csv('./DS-OS(LECT-04-02-2022)SORTED.csv')
total = pd.read_csv('./Book 1.csv')
total = total["NAME"]
df = df["Full Name"]
name = []
for i in range(0,len(df)):
    name.append(df[i])
name = set(name)
turn = 0;
while(1>0):
    bhar = 1
    # name.remove("RITIKA SINGH")
    # name.remove("SHRESHTHA GUPTA")
    # name.remove("PRERNA KUMARI")
    # name.remove("Rajesh Tripathi")
    if turn != 0:
        name.remove(df[name_index-1])
        print(df[name_index-1])
    name_lis = sorted(name)
    df = pd.DataFrame({"Full Name" : name_lis})
    df = df["Full Name"]
    absent_list = []
    name_index = 0
    i = 0
    while i<103:
        if(name_index > len(df)):
            absent_list.append(i+1)
            i +=1
            continue
        while (df[name_index]!=total[i]):
#            print(total[i])
            absent_list.append(i+1)
            if(i==102):
                break
            i +=1
        name_index +=1
        i +=1
    for k in range(0,103):
        if(df[name_index-1]==total[k]):
#           print(total[k])
            bhar = 0
            break
    if(bhar==0):
        break
    turn +=1
print(" ")
print(" ")
print(" ")
print(" ")
for i in absent_list:
    print(total[i-1])
print(absent_list)