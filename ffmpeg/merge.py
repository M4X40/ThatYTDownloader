import os
import subprocess


def merge_audio_video(title):
  print("Merging")
  command = [
    "ffmpeg",
    "-i", f"./downloads/{title}-m4x4download.mp4",
    "-i", f"./downloads/{title}-m4x4download.m4a",
    "-c:v", "copy",
    "-c:a", "aac",
    "-strict", "experimental",
    f"./downloads/{title}.mp4"
  ]

  print(subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE))

  os.remove(f"./downloads/{title}-m4x4download.mp4")
  os.remove(f"./downloads/{title}-m4x4download.m4a")