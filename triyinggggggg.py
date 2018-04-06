from urllib.request import urlopen
def fet():
    with urlopen ('http://sixty-north.com/c/t.txt') as  s:

        empty= []
        for line in s:
            word_line = line.decode('utf-8').split()
            for word in word_line :
                empty.append(word)
        for word in word_line:
            print (word)
if __name__ =='__main__':
    fet()














