try:
    file = open("test.py")
except:
    print('Read file error')
finally:
    file.close()
