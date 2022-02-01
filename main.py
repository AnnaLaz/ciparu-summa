teksts=input("Ievadi vārdu:  ")
skaititais=0
for burts in teksts:
  if burts=='a':
    skaititais+=1
print("Burtu a skaits:", skaititais)


# teksts = input("Ievadi vārdu:  ")
# def countZeros(teksts):
#   return teksts.count("a")
# print ("Burtu a skaits:",countZeros(teksts))


# teksts = input("Ievadi tekstu:")
# def replaceTwos(teksts):
#   if teksts.count("4")>0:
#     teksts = teksts.replace("4","četri")
#     print (teksts)
#   else:
#     teksts= "Nekas netika aizvietots"
#     print (teksts)
#   return teksts
# replaceTwos(teksts) 