from tkinter import *
from PIL import Image, ImageTk
from actions.actions import author_info_popup, show_video_info_action
from tkinter import filedialog

class App(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Config Main frame
        self.parent.geometry("480x320")
        self.parent.title("Download youtube videos")

        # Variables
        self.folder_path= StringVar()
        self.browse_message = StringVar()
        self.file_folder = None

        # components
        self.set_logo()
        self.menu_bar()
        self.instructions()
        self.search_button()
        self.browse_folder_button()
        self.entry_url()
        self.browse_folder_label()

    def set_logo(self):
        self.img = ImageTk.PhotoImage(Image.open('img/youtube-logo.png').resize(size=[60, 60]))
        self.photo = Label(self.parent, image=self.img, bd=0, width=60, height=60)
        self.photo.grid(row=0, column=0, padx=10, pady=10, sticky=NW)

    def menu_bar(self):
        self.mb = Menu(self.parent)
        self.parent.config(menu=self.mb)
        self.help_menu = Menu(self.mb, tearoff=0)
        self.mb.add_cascade(label="INFO", menu=self.help_menu)
        self.help_menu.add_command(label="About the Author", command=author_info_popup)
        self.mb.add_command(label="Exit", command=root.destroy)

    def instructions(self):
        self.description = Label(
            root, 
            text="Download your youtube Videos\n \
                Add the link to the below field and click download, \
                your video will be downloaded automatically in the \
                highest resolution", 
            wraplengt=350, 
            width=53
            )
        self.description.grid(row=0, column=1, columnspan=2)
    
    def entry_url(self):
        self.video_url = Entry(root)
        self.video_url.grid(row=1,column=1, sticky=EW, columnspan=2)

    def search_button(self):
        self.search_btn = Button(
            root, text="Search", 
            command= lambda: show_video_info_action(self.video_url, self.file_folder), 
            width=10
        )
        self.search_btn.grid(row=2,column=1, sticky=EW, padx=2)

    def browse_folder_button(self):
        self.folder_btn = Button(root, text="folder", command=self.browse_action, width=10)
        self.folder_btn.grid(row=2,column=2, sticky=EW, padx=2)
    
    def browse_folder_label(self):
        self.browse_message.set(f"Set a download folder")
        self.browse_lbl = Label(master=self.parent,textvariable=self.browse_message)
        self.browse_lbl.grid(row=3, column=1, columnspan=2, sticky=W)

    def browse_action(self):
        self.file_folder = filedialog.askdirectory()
        self.folder_path.set(self.file_folder)
        self.browse_message.set(f"Download folder:   {str(self.file_folder)[0:6]}...   {str(self.file_folder)[-40:]}")

if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
