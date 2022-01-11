# import all required modules

from tkinter import *
from tkinter import messagebox
from pytube import YouTube

# initialize the Tkinter
root = Tk()

# size of the window and to fix the size if the window
root.geometry("600x300+1310+4")
root.minsize(600, 300)
root.maxsize(600, 300)

# window name
root.title("YouTube Video downloader")

# window Background colour
root.config(bg="Black")

# creating the labels
Label(root, text="Video Downloader", font=('Courier', 20, "bold"), bg="Black", fg="White").pack(padx=1, pady=50)
# creating the video link
video_link = StringVar()
Label(root, text="Place your link here and enjoy!", font=('courier', 20, "bold"), bg="Black", fg="white").place(x=60, y=100)

# placing the link
text = Entry(root, width=30, textvariable=video_link, font="courier")
text.place(x=110, y=148)


# method for clearing the entry box
def clear_text():
    text.delete(0, END)


# method for downloading the video
def video_download():
    video_url = YouTube(str(video_link.get()))
    # you can change the resolution by get_lowest_resolution, get_highest_resolution, get_by_resolution
    videos = video_url.streams.get_by_resolution("720p")
    videos.download()
    # it will pop if the download is completed
    messagebox.showinfo("Download completed", "Check your project folder!")


# download button
Button(root, text="Download", font=("Courier", 15, "bold"), bg="White", fg="black", command=video_download).place(x=111, y=200)
# clearing button
Button(root, text="Clear Url", font=("courier", 15, "bold"), bg="White", fg="black", command=clear_text).place(x=347, y=200)


root.mainloop()
						
