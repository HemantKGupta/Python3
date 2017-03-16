import urllib.request

def wget2(url):
    try:
        ufile = urllib.request.urlopen(url)
        print(ufile.read())
    except IOError:
        print('problem reading url:', url)


wget2('https://www.google.com/')