#######################################
##  M4X4's Youtube Video Downloader  ##
##        Made by M4X4 with <3       ##
#######################################

###############
##  Imports  ##
###############
import tkinter as tk
from datetime import datetime
from io import BytesIO
from tkinter import Toplevel, ttk

import requests
from ffmpeg.audioconvert import convert
from ffmpeg.merge import merge_audio_video
from PIL import Image, ImageEnhance, ImageTk
from youtube.download import download
from youtube.fetch_data import fetch, get_streams

try:
  import pywinstyles
  import sv_ttk
except:
  import subprocess
  import sys
  subprocess.check_call([sys.executable, "-m", "pip", "install", "pywinstyles"])
  subprocess.check_call([sys.executable, "-m", "pip", "install", "sv-ttk"])
  import pywinstyles
  import sv_ttk

###################
##  Application  ##
###################
class YoutubeDownload:
  def __init__(self, root):
    #Version Setup
    self.ver = "v0.0.D2"
    self.verlong = "v0.0 Development Stage 1"

    #Base Window Setup
    self.root = root
    self.root.title(f"That Youtube Downloader | {self.ver}")
    self.root.geometry("700x300")
    pywinstyles.apply_style(root, "acrylic")
    sv_ttk.set_theme("dark")

    #Run Functions
    self.SetupVars(root)
    self.SetupUI(root)

  def SetupVars(self, root):
    #Variable Setup
    self.link = tk.StringVar(root, "Enter link...")
    self.thumb = tk.StringVar(root, "")
    self.title = tk.StringVar(root, "Title")
    self.channel = tk.StringVar(root, "Channel")
    self.views = tk.StringVar(root, "Views")
    self.length = tk.StringVar(root, "Length")
    self.date = tk.StringVar(root, "Date")

  def OnEntryClick(self, event):
    #Clears Link Input On Click
    self.LinkEntry.delete(0, tk.END)

  def SetupUI(self, root):
    #Styling for frames
    s = ttk.Style()
    s.configure("MainFrames.TFrame", background="#101010")

    #Link/Get Info button
    LinkFrame = ttk.Frame(root, padding=3, borderwidth=0, border=0, style="MainFrames.TFrame")
    LinkFrame.pack(fill="x")
    self.LinkEntry = ttk.Entry(LinkFrame, textvariable=self.link)
    self.LinkEntry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    self.LinkEntry.bind("<Button-1>", self.OnEntryClick) #Entry clear on click
    self.GetInfoButton = ttk.Button(LinkFrame, text="Get Info", command=self.GetInfo)
    self.GetInfoButton.pack(side=tk.RIGHT, padx=5)

    #Thumnail/Title/Channel Frame
    TopFrame = ttk.Frame(root, style="MainFrames.TFrame")
    TopFrame.pack(fill=tk.X, padx=10, pady=5)
    self.ThumbLabel = tk.Label(TopFrame, text="Thumbnail", background="#000000")
    self.ThumbLabel.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
    pywinstyles.set_opacity(self.ThumbLabel, 1)
    self.TitleLabel = ttk.Label(TopFrame, textvariable=self.title, background="#101010")
    self.TitleLabel.grid(row=0, column=1, sticky="w", padx=5)
    self.ChannelLabel = ttk.Label(TopFrame, textvariable=self.channel, background="#101010")
    self.ChannelLabel.grid(row=1, column=1, sticky="w", padx=5)

    #Views/Length/Date Frame
    InfoFrame = ttk.Frame(root, style="MainFrames.TFrame")
    InfoFrame.pack(fill=tk.X, padx=10, pady=5)
    self.ViewsLabel = ttk.Label(InfoFrame, textvariable=self.views, background="#101010")
    self.ViewsLabel.grid(row=0, column=0, padx=5, sticky="w")
    self.LengthLabel = ttk.Label(InfoFrame, textvariable=self.length, background="#101010")
    self.LengthLabel.grid(row=1, column=0, padx=5, sticky="w")
    self.DateLabel = ttk.Label(InfoFrame, textvariable=self.date, background="#101010")
    self.DateLabel.grid(row=2, column=0, padx=5, sticky="w")

    #Download buttons Frame
    ButtonFrame = ttk.Frame(root, style="MainFrames.TFrame")
    ButtonFrame.pack(fill=tk.X, padx=10, pady=10, side="bottom")
    self.HighestButton = ttk.Button(ButtonFrame, text="Download Highest Quality", command=self.DownloadHighest)
    self.HighestButton.grid(row=0, column=0, sticky="")
    self.CustomButton = ttk.Button(ButtonFrame, text="[UNDER CONSTRUCTION]", command=self.DownloadCustom)
    self.CustomButton.grid(row=0, column=1, sticky="")
    self.AudioButton = ttk.Button(ButtonFrame, text="Download Audio", command=self.DownloadAudio)
    self.AudioButton.grid(row=0, column=2, sticky="")
    ButtonFrame.grid_rowconfigure(0, weight=1)
    ButtonFrame.grid_columnconfigure(0, weight=1)
    ButtonFrame.grid_columnconfigure(1, weight=1)
    ButtonFrame.grid_columnconfigure(2, weight=1)

  def UpdateThumbnail(self):
    #Updates the thumbnail label to show the image
    url = self.thumb.get()
    try:
      response = requests.get(url)
      img_data = response.content
      img = Image.open(BytesIO(img_data))
      img = img.resize((160, 120)) #1/4 scale
      self.photo = ImageTk.PhotoImage(img)
      self.ThumbLabel.config(image=self.photo, text="")
    except Exception as e:
      self.TxhumbLabel.config(text="Image not available", image="")

  def DownloadHighest(self):
    #Highest quality stream
    download(get_streams(self.link.get(), "highest")["video"], self.title.get(), ".mp4") #Video stream
    download(get_streams(self.link.get(), "highest")["audio"], self.title.get(), ".m4a") #Audio stream
    merge_audio_video(self.title.get()) #Merges into final product

  def DownloadCustom(self):
    #unfinished
    print("Download Custom Quality")

  def DownloadAudio(self):
    download(get_streams(self.link.get(), "audio"), self.title.get(), ".m4a")
    convert(self.title.get())

  def GetInfo(self):
    print(self.link.get())
    data = fetch(self.link.get())
    self.title.set(f"{data["title"]}")
    self.thumb.set(f"{data["thumb"]}")
    self.UpdateThumbnail()
    self.channel.set(f"{data["channel"]}")
    self.views.set(f"Views: {data["views"]}")
    self.length.set(f"Length: {int(data["length"]) // 60}:{int(data["length"] % 60)}")
    
    self.date.set(f"Date Uploaded: {datetime.fromisoformat(str(data["date"])).strftime("%B %d, %Y at %I:%M %p")}")

def MakeGUI():
  root = tk.Tk()
  app = YoutubeDownload(root)
  root.mainloop()