def extractStock():
    f = open('stocks.txt', 'rb')
    line = f.readline()
    result = []
    count = 0
    corr = list(line)[:30]
    while line:
        for item in range(0,30):
            target = int(corr[item])
            if target == 1:
                dit = {}
                dit["source"] = count
                dit["target"] = item
                dit["value"] = 1
                result.append(dit)
        line = f.readline()
        corr = list(line)[:30]
        count = count +1
    return result        


def extractZachary():
    f = open('zachary.txt', 'rb')
    line = f.readline()
    result = []
    count = 0
    while line:
        dit = {}
        space = line.find(' ')
        source = int(line[0:space])-1
        line2 = line[space+1:]
        space2 = line2.find(' ')
        target = int(line2[0:space2])-1
        line3 = line2[space2+1:]
        end = line3.find('\r')
        value = int(line3[0:end])
        dit["source"] = source
        dit["target"] = target
        dit["value"] = value
        result.append(dit)
        line = f.readline()
    return result
        
