import time
import urllib.request

http = urllib.request.urlopen("https://www.google.com/")
c = http.read()
print("Programm has started")
while True:
    print(c)
    t = time.strftime('%M')
    time.sleep(60)
    print(f'das ist ein Test Plugin {t}')
