
from requests import get
from user_agent import generate_user_agent
import yt_dlp
from wget import download
from os import mkdir
from os.path import join, exists, basename
from .mediafire import get as getmf
from classes.google_drive import googleDrive

def download_file(url):
    path_download = 'downloads'
    if not exists('downloads'):
        mkdir('downloads')
        
    options = {
                'format': 'best',
                'outtmpl': join(path_download, '%(title)s.%(ext)s')    
            }
    
    keywords = [
        "youtu.be",
        "short"
        "twitch",
        "fb.watch",
        "www.xvideos.com",
        "www.xnxx.com",
        "www.yourupload.com",
    ]
    
    if any(keyword in url for keyword in keywords): # -------------------------- DESCARGAR VIDEOS DE YOUTUBE
        with yt_dlp.YoutubeDL(options) as ydl: 
            ydl.download([url])
        return
    
    # elif 'https://youtu' in url and 'playlist?' in url: # ------------------------------------------- DESCARGAR PLAYLISTS DE YOUTUBE
    #     ytdl = YoutubeDL(progressytdl, sms, app, False)
    #     try:
    #         ytdl.downloadlist(url, path_download)
    #     except Exception as e:
    #         print(e)
    
    elif "drive.google.com" in url: # ---------------------------------------- DESCARGAR ARCHIVOS DE GOOGLE DRIVE
        googleDrive().download(url, path_download)
        return
        
        
    elif "mediafire" in url: # ------------------------------------------------ DESCARGAR ARCHIVOS DE MEDIAFIRE
        download( getmf(url), path_download )
        return
    
    
    elif url.startswith("http"): # ----------------------------------------- DESCARGAR ARCHIVOS DE ENLACE DIRECTO
        r = get(url, headers={"user-agent": generate_user_agent()})
        with open(f"{path_download}/{basename(url)}", "wb") as f:
            f.write(r.content)
        return
    
    