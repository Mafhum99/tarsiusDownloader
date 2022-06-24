import yt_dlp
import argparse


# downloads playlist youtube videos

def vid_downloads():
    ydl_o = {
        'ignoreerrors': True,
        'format':'mp4',    
    }

    with yt_dlp.YoutubeDL(ydl_o) as ydl:
        ydl.download(inp)
        
    return True

#downloads audio playlist youtube
def aud_downloads():
    ydl_o = {
        'ignoreerrors': True,
        'format':'bestaudio/best',
        'extracaudio':True,
        'outtmpl' : '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
            
    with yt_dlp.YoutubeDL(ydl_o) as ydl:
                ydl.download(inp)
                
    return True
            
           
#exsekusi

inp = str(input("masukkan url :"))
pil = str(input("yang ingin di downloads video/audio:"))

if pil == "video" || pil == "Video" || pil == "VIDEO" :
    vid_downloads()
    print(f"all done")
elif pil == "audio" || pil == "Audio" || pil == "AUDIO" :
    aud_downloads()
    print(f"all done")
else :
    print("maaf pilihan anda tidak tersedia !")
