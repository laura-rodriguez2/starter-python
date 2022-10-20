def Fonction (*parametre):
    MyList = []
    for param in parametre:
        if isinstance(param, (int)):
            MyList.append(param)
    for element in MyList:
        if element %2 == 0:
            print (element)

Fonction(7,15,4,8,33,12,41)