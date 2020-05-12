import urllib.request
with urllib.request.urlopen('http://125.186.202.51:8080/api/v1/getMonitorToken') as f:
    print(f.read(300))