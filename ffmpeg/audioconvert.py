import os
import subprocess


def convert(title):
  print("Converting")
  command = [
    "ffmpeg",
    "-i", f"./downloads/{title}-m4x4download.m4a",
    "-c:v", "copy",
    "-c:a", "libmp3lame",
    "-q:a", "4",
    f"./downloads/{title}.mp3"
  ]

  print(subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
  os.remove(f"./downloads/{title}-m4x4download.m4a")