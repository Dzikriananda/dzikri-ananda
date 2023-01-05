import ctypes #sengaja pake ctype,soalnya kalo pake list ribet 

UINT_ARRAY_30 = ctypes.c_uint*30
arr = UINT_ARRAY_30()
arr = [1,1,2,5,2,5,2,2,2,1,1,7,5,6,9,9]
arr2= UINT_ARRAY_30()

for i in range(len(arr2)):
    arr2[i]=0

for i in arr:
    arr2[i]+=1

for i in range(len(arr2)):
    if (arr2[i]!=0): print('Angka',i,'Muncul Sebanyak :',arr2[i],'Kali!')


    
    
    



