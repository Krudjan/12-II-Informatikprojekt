import os

musicdirs = ['Musik', 'Music']

def pathfinder():
    if os.name == 'nt':
        x = str(os.environ.get("TEMP"))
        if x.find("User") != -1:
            lang = "\\Music"
        if x.find("Benutzer") != -1:
            lang = "\\Musik"
        y = x.split("\\")
        middle = ":\\" + str(y[1]) + "\\" + str(y[2])
        driveletters = ["A", "B", "C", "D", "E", "F", "G"]
        for e in driveletters:
            musicdirpath = e + middle + lang
            if os.path.isdir(musicdirpath) == True:
                return musicdirpath
    elif os.name == 'posix':
        home = os.getenv('Home')
        for musicdir in musicdirs:
            musicdirpath = home + '/' + musicdir
            if os.path.isdir(musicdirpath):
                return musicdirpath
