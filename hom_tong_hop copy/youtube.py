# from __future__ import unicode_literals
# import youtube_dl

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=XOecYFlspHw'])

# from __future__ import unicode_literals
# import youtube_dl
# list_video_download = ["https://www.youtube.com/watch?v=unVCbBEjMEI","https://www.youtube.com/watch?v=P-3Lfpivw68"]
# ydl_opts = {}
# emptyList = []
# for link in list_video_download:
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         r = ydl.extract_info(link,download = False)
#         emptyList.append(r)
# print (emptyList)
# with open ("baitap.txt","a") as out:
#     out.write("i love coding" )
# import json
# for link in list_video_download:
#     with open ("baitap.json","w") as outfile:
#         json.dump(link,outfile) 

import requests

r = requests.get("https://jsonplaceholder.typicode.com/users", auth=('user', 'pass'))


import json
d = r.json()
# print (d)
i =-1
loop = True
while loop:
    i+=1
    if "Delphine" in d[i]["username"]:
        print (d[i])
        loop = False

n = input("tim nguoi co username la: ")
i =-1
loop = True
while loop:
    i+=1
    if n in d[i]["username"]:
        print (d[i])
        loop = False

n = input("tim nguoi co username la: ")
n = n.title()
i =-1
loop = True
while loop:
    i+=1
    if n in d[i]["username"]:
        print (d[i])
        loop = False


