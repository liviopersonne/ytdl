import yt_dlp
import os
import sys
from env.vars import DEST_PATH, MY_URLS

TEMP_PATH = os.path.join(os.getcwd(), "temp")
LAST_ID_PATH = os.path.join(os.getcwd(), "env", "last_id.txt")

base_options = {
    'verbose': False,
    'updatetime': False,
    'paths': {
        "temp": TEMP_PATH,
        "home": DEST_PATH
    },
    'outtmpl': "%(title)s.%(ext)s"
}
audio_options = base_options | {
    'format': "bestaudio/best",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
video_options = base_options | {
    'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
}

def empty():
    print("Emptying temp folder", end = "\r")
    for file in os.listdir(TEMP_PATH):
        os.remove(os.path.join(TEMP_PATH, file))
    print("Successfully emptied temp folder !")

def playlist_items(start: str, end: str, reverse: bool):
    if reverse:
        start, end = end, start
    rep = ""
    start, end = start.strip(), end.strip()
    if start.isdecimal():
        rep += start
    rep += ":"
    if end.isdecimal():
        rep += end
    if reverse:
        rep += ":-1"
    return rep

def search_id_in_playlist(playlist_url, target_id):
    scraper_options = {
        'verbose': False,
        'quiet': True,
        'extract_flat': True,
        'playlistend': 100,
    }
    with yt_dlp.YoutubeDL(scraper_options) as playlist_scraper:
        playlist_info = playlist_scraper.extract_info(playlist_url, download=False)
        playlist_entries = playlist_info.get('entries', [])
        first_id = playlist_entries[0].get('id')
        for (i, vid) in enumerate(playlist_entries):
            if vid.get('id') == target_id:
                if i == 0:
                    input("Already up to date !")
                    raise Exception("Already up to date !")
                return str(first_id), str(i)
    input("Target id not found in playlist")
    raise Exception("Target id not found in playlist")

def match_url(url: str):
    if url in MY_URLS:
        return MY_URLS[url]
    else:
        return url

def download(playlist, url, audio_only, start, end, reverse):
    if len(os.listdir(TEMP_PATH)) > 0:
        resume = input("A download was interrupted, would you like to finish it ? ") == "1"
        if resume:
            raise NotImplementedError("Need to implement resumption of download")
        else:
            empty()
    if audio_only:
        options = audio_options
    else:
        options = video_options
    if playlist:
        options['playlist_items'] = playlist_items(start, end, reverse)
    
    ytdl = yt_dlp.YoutubeDL(options)
    ytdl.download(url)
    ytdl.close()

def download_in_terminal():
    playlist = input("Playlist ? ") == "1"
    url = match_url(input("Url: "))
    audio_only = input("Audio only ? ") == "1"
    start, end, reverse = None, None, None
    if playlist:
        start = input("Start: ")    # Leave empty for start of playlist
        end = input("End: ")        # Leave empty for end of playlist
        reverse = input("Reverse ? ") == "1"
    download(playlist, url, audio_only, start, end, reverse)

def update_music():
    with open(LAST_ID_PATH, "r") as infile:
        last_downloaded_id = infile.read()
    new_ldi, end = search_id_in_playlist(MY_URLS['music'], last_downloaded_id)
    download(True, MY_URLS['music'], True, "", end, True)
    with open(LAST_ID_PATH, "w") as outfile:
        outfile.write(new_ldi)


if __name__ == '__main__':
    try:
        try:
            type_of_download = sys.argv[1]
            if type_of_download == "update_playlist":
                update_music()
                exit(0)
        except IndexError:
            pass

        download_in_terminal()
    
    except Exception as e:
        print(e)
        input("Exit...")