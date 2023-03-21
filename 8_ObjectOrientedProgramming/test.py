def arrange(n):
    hundredsPlace = n // 100    #4
    tensPlace = (n - (hundredsPlace * 100)) // 10   #9
    onesPlace = n % 10  #5

    minNum = min(hundredsPlace, tensPlace, onesPlace)   #4
    maxNum = max(hundredsPlace, tensPlace, onesPlace)   #9
    # midSet = set([hundredsPlace, tensPlace, onesPlace]) - set([minNum, maxNum]) #{5}
    # # {4, 9, 5} - {4, 9} = {5}
    #
    # midNum = list(midSet)[0]    #5

    #alternative method - solve for midNumber
    if hundredsPlace != minNum and hundredsPlace != maxNum:
        midNum = hundredsPlace
    elif tensPlace != minNum and tensPlace != maxNum:
        midNum = tensPlace
    else:
        midNum = onesPlace

    return maxNum * 100 + midNum * 10 + minNum


print(arrange(19))
