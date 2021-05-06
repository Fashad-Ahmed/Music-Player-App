import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from  mutagen.id3 import ID3

root = Tk()
root.minsize(300, 300)

listSongs = []
realName = []

v = StringVar()
songLabel = Label(root, textvariable=v, width=35)
index = 0

def nextSong(event):
    global index
    index += 1
    pygame.mixer.music.load(listSongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevSong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listSongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopSong(event):
    pygame.mixer.music.stop()
    v.set('')

def updatelabel():
    global index
    global songName
    v.set(realName[index])

def directoryChooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith('.mp3'):

            realDir = os.path.realpath(files)
            audio = ID3(realDir)
            realName.append(audio['TIT2'].text[0])  # meta-tag
            listSongs.append(files)
            print(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listSongs[0])
    pygame.mixer.music.play()

directoryChooser()

label = Label(root, text='Music Player')
label.pack()

listBox = Listbox(root)
listBox.pack()

realName.reverse()

for i in realName:
    listBox.insert(0, i)

realName.reverse()

nextBtn = Button(root, text='Next')
nextBtn.pack()

previousBtn = Button(root, text='Previous')
previousBtn.pack()

stopBtn = Button(root, text='Stop')
stopBtn.pack()

nextBtn.bind('<Button-1>', nextSong)
previousBtn.bind('<Button-1>', prevSong)
stopBtn.bind('<Button-1>', stopSong)

songLabel.pack()

root.mainloop()