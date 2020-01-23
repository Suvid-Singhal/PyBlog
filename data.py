import os
def Articles():
    os.chdir("static")
    dirlist = os.listdir()
    articles = []
    for i in range(len(dirlist)):
        junk = {
        'id':i+1,
        'title':dirlist[i],
        'body':open(dirlist[i], "r").read()
        }
        articles.append(junk)
    os.chdir("../")
    return articles
