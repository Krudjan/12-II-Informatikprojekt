# # import sqlite3

# a = "Avicii and Friends Addicted to you"
# b = "Avicii and Friends Hey Brother"
# c = "Avicii and Friends For a better day"
# filenames = [a, b, c]
# pieces = []

# if "Avicii Friends Addicted to you" not in filenames:
#         print("yes")

# def top(filenames):
#     for e in filenames:
#         z = e.split(" ")
#         pieces.append(z)

# global count
# count = 0
# global final
# final = []

# def analyzer(f,r,compound_guess,nextpart,count,legacy):
#         if f.find(compound_guess) != -1:
#                 count = count + 1
#                 i = r.index(nextpart) # getting index of nextpart
#                 nextpart = r[i+1] # redefining nextpart as the item following the current nextpart in list r
#                 legacy = compound_guess # savin the confirmed / approved compound_guess for next recursion so that if it fails it will go to else and return legacy, the last ompound_guess that worked
#                 compound_guess = compound_guess + " " + nextpart
#                 analyzer(f,r,compound_guess,nextpart,count,legacy)
#         else: 
#                 if count == 3:
#                         q = input("Is " + legacy + " an artist?\n y/n")
#                         if q == "y":
#                                 print("Nice we´ll be creating a folder for you")
#                                 # add artist to database inorder to run comparison with database again and copy all those whose artist was just added
#                                 # artistsdatabaseobject = sqlite3.connect("artists.db")
#                                 # pointer = artistsdatabaseobject.cursor()
#                                 # num = len(legacy)
#                                 # comp = [num, legacy]
#                                 # pointer.execute("INSERT INTO artists_table values (?, ?)", comp)
#                                 # artistsdatabaseobject.commit()
#                                 # artistsdatabaseobject.close()
#                                 # directorator(musicdirpath,f,musicdirpath,legacy) - bad idea, as it causes only the third and following files to be copied

# def one_under_top(filenames, pieces):
#         for f in filenames:
#                 for r in pieces:
#                         if pieces.index(r) != filenames.index(f) and f.find(r[0]) != -1:
#                                 analyzer(f,r,r[0],r[0],0,"") # f = filename; r = Liste der filenamesubstrings auf die ein Leerzeichen folgt; r[0]; r[1]; count = 0; legacy ist leerer string da es kein legacy gibt

# top(filenames)
# one_under_top(filenames,pieces)

print("\\" + "\\")