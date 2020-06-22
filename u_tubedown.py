import pafy

# url of video
url =input("please paste the url link of videos you want to download : ")

# instant created
video = pafy.new(url)

# print title
print(video.title)

# print rating
print(video.rating)

# print viewcount
print(video.viewcount)

# print author & video length
print(video.author, video.length)

# print duration, likes, dislikes & description
print(video.duration, video.likes, video.dislikes, video.description)

#you can speak them to speech recognistion
print('Press 1 for video download \n press 2 for audio download' )


choice=input('Please enter a choice')
wq=0
if choice=="1":
#          " to dowload video  "
  video = pafy.new(url)

  streams = video.streams

     # it will print quality of videos availabe in all stream
  for i in streams:
    print(f"for {i} press {wq}")
    wq=wq+1


# get best resolution regardless of format
  #best = video.getbest()
  pref=int(input(' \n As the list show above enter you choices : '))
  #best = video.getbest(preftype=pref)

  #print(best.resolution, best.extension,best.get_filesize())

# Download the video
  #best.download()

# or  steams in while loop if you want to select any in variable i there a list is created you can select and use them i=4 480p video

  streams[pref].download()


#                 "to download audio of that video"
elif choice=="2":
 #url = "https://url of that video"
 video = pafy.new(url)
 # for download audio of your choice
 audiostreams = video.audiostreams
 #for i in audiostreams:
  #  print(f"for i.bitrate, i.extension, i.get_filesize() press {wq}")
   # wq=wq+1

 # pref =int(input(' \n As the list show above enter you choices : '))

 #audiostreams[pref].download()

 #for download best auudio
 bestaudio = video.getbestaudio()
 bestaudio.download()
