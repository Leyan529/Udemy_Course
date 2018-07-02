import re
import sys
import urllib.request


def URL():
    url = "https://www.google.com.tw/search?q="
    stock = input("Enter your stock: ")
    url = url + stock
    return url


def getURLdata():
    try:
        Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        requestURL = urllib.request.Request(URL(), headers=Headers)
        data = urllib.request.urlopen(requestURL).read().decode("utf-8")
        return data
    except:
        print("Decode Fail")
        return None


def writeFile(URLdata):
    data = URLdata.encode("utf8").decode("cp950", "ignore")
    # print(data)
    file = open("urlData.txt", "w+")
    file.write(data)
    file.close()
    print("write finish")


def dataSearch():
    posList=[]
    data = getURLdata()
    writeFile(data)
    search = re.search('content="', data)
    print(search)
    pos = search.start()
    nextPos = search.end()
    newString = data[pos:nextPos]
    posList.append(pos)
    posList.append(newString)

    next = data[nextPos:]
    search = re.search('content="', next)
    print(search)
    pos = search.start()
    nextPos = search.end()
    newString = data[pos:nextPos]
    posList.append(pos)
    posList.append(newString)
    print(posList)
