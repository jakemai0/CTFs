a = [85, 54, 45, 58, 89, 76, 46, 34, 43, 10]

def togetha():
    passwd = ""
    for i in a:
        passwd+=str(chr(i))
    print(passwd)
if __name__ == "__main__":
    togetha()
