import yt_dlp
import argparse

#argsparses option
parser = argparse.ArgumentParser(description="There are command for used downloaded a file, you can use  ' yt-download [-option] [url] '")
parser.add_argument("-a","--audio",metavar="",dest="audio",help="this is a command for download audio only")
parser.add_argument("-v","--video",metavar="",dest="video",help="this is a command for download video ")
args=parser.parse_args()

# downloads playlist youtube videos
def vid_downloads():
    ydl_o = {
        'ignoreerrors': True,
        'format':'mp4',
        'outtmpl' : '%(uploader)s/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_o) as ydl:
        ydl.download(inp)
    return True

#downloads audio playlist youtube
def aud_downloads():
    ydl_o = {
        'playlist' : True,
        'ignoreerrors': True,
        'format':'bestaudio/best',
        'extracaudio':True,
        'outtmpl' : '%(uploader)s/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
    }
            
    with yt_dlp.YoutubeDL(ydl_o) as ydl:
                ydl.download(inp)
    return True
                
           
#exsekusi

if args.audio:
    inp = str(args.audio)
    aud_downloads()       
    print("all done")
    quit()

elif args.video:
    inp = str(args.video)
    vid_downloads()
    print("all done")
    quit()
else :
    print(f"please read a documentation in for use " )
    print(f"      [yt-download.py -h]      ") 
    print(f"...Happy ending...")
