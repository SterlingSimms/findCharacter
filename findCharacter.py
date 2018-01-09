def findCharacter(xlist, xChar):
    newList = []
    for val in xlist:
        if type(val) == str:
            for element in val:
                if xChar == element:
                    newList.append(val)
                    break
    print newList
findCharacter(["hello", 1, 2, 3,"goodbye", "fruit loops"], "o")



# 1) write a program that takes a list of strings, and a single char  DONE!
# 2) check every item in list to see if single char is in item
# 3) return a new list with any items that contain the single char



