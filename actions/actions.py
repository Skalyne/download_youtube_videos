from pytube import YouTube
from tkinter import E, EW, NW, W, messagebox as MessageBox
from tkinter import Label, Button, ttk
from PIL import Image, ImageTk
from urllib.request import urlopen
import io

def download_accion(video_url, output_path = None):
    video = YouTube(video_url.get())
    download = video.streams.get_highest_resolution()
    download.download(output_path=output_path)

def show_video_info_action(video_url, file_folder):
    if video_url.get() == "":
        MessageBox.showinfo(
            "Empty Field", 
            "the url field is empty, please add a valid link")
        return None

    try: 
        video = YouTube(video_url.get())
        thumbnail_url = urlopen(video.thumbnail_url)
    except:
        MessageBox.showerror(
            "Url not valid",
            "A problem happends trying to get the video for te link you provided, please, ensure is a valid link"
        )
        video_url.delete(0, 'end')
        return None
    
    raw_data = thumbnail_url.read()
    thumbnail_url.close()
    im = Image.open(io.BytesIO(raw_data))
    video_image = ImageTk.PhotoImage(im.resize((60,60)))

    image_video_lbl = Label(image=video_image)
    image_video_lbl.image = video_image
    image_video_lbl.grid(row=4,column=0, rowspan=3)

    title_lbl = ttk.Label(text=f"Title: {str(video.title)}...")
    title_lbl.grid(row=4,column=1, sticky=W, padx=10, columnspan=2)
    download_button(video_url, file_folder)

def download_button(video_url, file_folder):
        download_btn = ttk.Button(text="Download", command= lambda: download_accion(video_url, file_folder), width=10)
        download_btn.grid(row=7,column=1, columnspan=2, sticky=EW, padx=2, pady=2)

def author_info_popup():
    MessageBox.showinfo("about me:", "Skalyne")
