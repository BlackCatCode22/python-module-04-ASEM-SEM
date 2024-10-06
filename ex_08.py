fx=open("mbox-short.txt")
for my_line in fx:
    my_line=my_line.rstrip()
    wrs=my_line.split()
    if len(wrs) < 3 or wrs[0] != 'form':
     continue
    print(wrs[2])







