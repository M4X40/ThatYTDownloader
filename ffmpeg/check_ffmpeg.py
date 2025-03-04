import subprocess

def check():
  try:
    subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return True
  except (subprocess.CalledProcessError, FileNotFoundError):
    return False