def history(sortType, listLength, runSpeed, runTime, numOfSwaps):
    # Open for Read
    historyFile_I = open("history.txt", "r")
    # Number of data
    lines = int(historyFile_I.readline().strip(' '))

    data = [''] * (lines+1)

    data[0] = str(sortType) + ' ' + str(listLength) + ' ' +  str(round(runSpeed, 1)) + ' ' +  str(round(runTime, 3)) + ' ' +  str(numOfSwaps) + '\n'
    for i in range(1, lines+1):
        data[i] = str(historyFile_I.readline())
    print(data)
    # Close
    historyFile_I.close()

    # Open for Write
    historyFile_O = open("history.txt", "w")
    
    historyFile_O.write(str(int(lines)+1) + '\n')
    historyFile_O.writelines(data)
    # Close
    historyFile_O.close()
