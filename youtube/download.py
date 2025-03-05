try:
  from pytubefix import YouTube
except:
  import subprocess
  import sys
  subprocess.check_call([sys.executable, "-m", "pip", "install", "pytubefix"])

def download(stream, title, type):
  stream.download(output_path="./downloads/", filename=f"{title}-m4x4download{type}")

def download_progress(stream, chunk, bytesremaining):
  print(f"{stream.filesize - bytesremaining} / {stream.filesize} ({bytesremaining} Remaining)")