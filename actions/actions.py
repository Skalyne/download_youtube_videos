from pytube import YouTube
from tkinter import messagebox as MessageBox
from tkinter import Label, OptionMenu, StringVar

def download_accion(video_url, output_path = None):
    video = YouTube(video_url.get())
    download = video.streams.get_highest_resolution()
    download.download(output_path=output_path)

def author_info_popup():
    MessageBox.showinfo("about me:", "Skalyne")
