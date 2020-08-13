# a={1:2, 3:4}
#
# print (a.keys())
# print (a.values())
# print (a.items())
# print (a.items())
#
#
# print (list(a.keys()))



lista=list()
lista.append([1,2])
lista.append([1,2])
lista.append([1,2])



for item in zip(*lista):
    print(item)