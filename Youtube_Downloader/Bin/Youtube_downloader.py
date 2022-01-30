#Youtube Downloader Program 

from tkinter import *
from pytube import YouTube

#Function to Download the Youtube Video
def download_video():
    link = ui_link.get()
    file_name = ui_file_name.get()
    file_name_user = str(file_name)
    file_name_arguement = file_name_user + ".mp4"
    yt = YouTube(link)      
    try:
        yt.streams.filter(progressive = True,file_extension = "mp4").first().download(output_path = "C:\\Users\\Admin\\Downloads\\Youtube_downloads", filename = file_name_arguement)
    except:
        return "Download Error" 
        
    return "Download Complete" 

#UI Creation and Getting Input from the user
master = Tk()
ui_link = StringVar()
ui_file_name = StringVar()
fun_result = StringVar()
master.title("YouTube Downloader")
Label(master, text = "Enter the YouTube Link : ").grid(row=0, sticky=W)
Label(master, text = "Enter the File name : ").grid(row=1, sticky=W)
e1 = Entry(master, textvariable = ui_link)
e2 = Entry(master, textvariable = ui_file_name)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b = Button(master, text="Download Video", command=download_video)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

mainloop()