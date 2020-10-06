"""Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile 
trebuie să găsească cinci numere consecutive,crescătoare,numărul din mijloc fiind cel ales de Ion.
Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească răspunsul mai repede."""
m= int(input("dați un număr:"))
print(m-2,m-1,m,m+1,m+2,sep='')