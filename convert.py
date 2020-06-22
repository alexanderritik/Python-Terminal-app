import os
import pydub
print("Press 1 for audio conversion")
print("Press 2 for video conversion")
choice=int(input('Enter your choice : '))

a=input('enter the directory name : ')
os.chdir(a)
b=input('enter the file name with extension : ')
list=['mp3','mp4','ogg','wav','avi','fly','raw']
print("wav for 1 \n"
                  "mp4 for 2 \n"
                  "ogg for 3 \n"
                  "avi for 4 \n"
                  "fly for 5 \n"
                  "raw for 6 \n")
d=int(input('Enter your choice : ' ))
if d==1:
                e=list[3]
elif d == 2:
                e=list[1]
elif d == 3:
                e =list[2]
elif d == 4:
                e =list[4]
elif d == 5:
                e =list[5]
elif d == 6:
                e =list[6]
jhj=b.split('.')
dst=jhj[0]+"converted"+"."+e
src =b
    # file you want to convert


if choice==1:
                try:
                    sound = pydub.AudioSegment.from_mp3(src)
                    sound.export(dst, format="wav")
                    print("Conversion has done ")
                except Exception as e:
                    ("there is some error retry it")

elif choice==2:
                try:
                    sound = pydub.AudioSegment.from_mp4(src)
                    sound.export(dst, format="wav")
                    print("Conversion has done ")
                except Exception as e:
                    ("there is some error retry it")


os.chdir('C:\\Users\\Alexander\\PycharmProjects\\JARVIS')