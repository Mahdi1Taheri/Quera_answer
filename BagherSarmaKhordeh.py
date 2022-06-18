



strings = []  
count = ""
  
for i in range(1,6):
    Recevie = input().upper()[:20]
    if 'MOLANA' in Recevie or 'HAFEZ' in Recevie:   
            strings.append(i)
            # count += str(f'{i} ')

          
if strings == []:
    print("NOT FOUND!")

print(*strings)




# for i in range(1,6):
#     Recevie = input("please enter the strings(capital letters, numbers, char(-)) %s: " % (int(i))).upper()
#     strings.append(Recevie)

# for j in range(len(strings)):
#     if 'MOLANA' in strings[j] or 'HAFEZ' in strings[j]:
#         print(j)
#     if 'MOLANA' not in strings[j] or 'HAFEZ' not in strings[j]:
#         print("NOT FOUND!")


    
    
    


