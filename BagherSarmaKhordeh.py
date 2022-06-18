
strings = []  
count = ""
  
for i in range(1,6):
    Recevie = input().upper()[:20]
    if 'MOLANA' in Recevie or 'HAFEZ' in Recevie:   
            strings.append(i)
       
if strings == []:
    print("NOT FOUND!")

print(*strings)
