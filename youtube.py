from cProfile import label
from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import os
from email.mime import base

def createWidgets():

    link_label = Label(root, text="YouTube URL: ", bg="#8C8C8C")
    link_label.grid(row=1, column=1, pady=15, padx=15)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=2, pady=10, padx=10)

    destination_label = Label(root, text="File Location: ", bg="#8C8C8C")
    destination_label.grid(row=2, column=1, pady=15, padx=15)

    root.destination_text = Entry(root, width=60, textvariable=download_path)
    root.destination_text.grid(row=2, column=2, pady=10, padx=10)

    browse_but = Button(root, text = "Browse", command=browse, width=7, bg="#FFD700")
    browse_but.grid(row=2, column=3, padx=1, pady=1)

    downloadv_bot = Button(root, text = "Download Video", command=download_video,width=25, bg="#7FFF00")
    downloadv_bot.grid(row=3, column=2, pady=3, padx=3)
    download3_bot = Button(root, text = "Download MP3", command=download_mp3,width=25, bg="#7FFF00")
    download3_bot.grid(row=4, column=2, pady=3, padx=3)

    destina_label = Label(root, text="Directed: PM", bg="#4B0082")
    destina_label.grid(row=5, column=3, pady=15, padx=15)


def browse():

    currdir = os.getcwd()
    download_dir = filedialog.askdirectory(parent=root, initialdir=currdir, title="Please select a directory")
    download_path.set(download_dir)

def download_video():
    url = video_link.get()
    folder = download_path
    video = YouTube(url)
    stream_g = video.streams.first()
    stream_g.download(folder)
    messagebox.showinfo("","Successfuly!!")


def download_mp3():
    url = video_link.get()
    folder = download_path
    mp3 = YouTube(url)
    stream_g = mp3.streams.filter(only_audio=True).first()
    out_file = stream_g.download(folder)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file,new_file)
    messagebox.showinfo("","Successfuly!!")

root = tk.Tk()

root.geometry("600x220")
root.resizable(False,False)
root.title("YouTube Downloader")
root.config(background=	"#EE2C2C")
video_link = StringVar()
download_path = StringVar()

createWidgets()
root.mainloop()