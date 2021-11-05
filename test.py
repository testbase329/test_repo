def createTxt():
    print(getWindowsUsername())
    with open('C:\Users\'+getWindowsUsername()+'\Desktop\test.txt', 'w') as f:
        f.write('Hello World!')
def getWindowsUsername():
    import getpass
    return getpass.getuser()
if __name__ == '__main__':
     createTxt()