def flatten(aList):
    '''
    aList: a list
    Returns a flattened version of a List
    '''
    flatList = []

    def makeFlatList(someList):
        for el in someList:
            if type(el) == list:
                makeFlatList(el)
            else:
                flatList.append(el)

    makeFlatList(aList)
    return flatList



testList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(testList))
