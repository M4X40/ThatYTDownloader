from pytubefix import YouTube

from youtube import download


def fetch(link):
  yt = YouTube(link, on_progress_callback=download.download_progress)
  return {
    "obj": yt,
    "title": str(yt.title).replace("!","").replace(".",""),
    "thumb": yt.thumbnail_url,
    "channel": yt.author,
    "views": yt.views,
    "length": yt.length,
    "date": yt.publish_date
  }

def get_streams(link, streamtype):
  yt = fetch(link)["obj"]
  match streamtype:
    case "highest":
      return {
        "video": yt.streams.filter(is_dash=True)[0], # Highest quality video stream
        "audio": yt.streams.filter(is_dash=True)[-1] # Highest quality audio stream (usually 160kbps m4a)
      }
    case "custom":
      print("NONE")
    case "audio":
      return yt.streams.filter(is_dash=True)[-1] # Highest quality audio stream (usually 160kbps m4a)