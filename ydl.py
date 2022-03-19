#used pyinstaller ydl.py --onefile -w --noconsole --windowed
#ffmpeg set with Systemumgebungsvariablen


import tkinter as tk
from youtube_dl import YoutubeDL


def ydl(url, path):
    url = url.get()
    path = path.get()
    print(url, path)
    ydl_opts = {
        'outtmpl': f'{path}%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }
    ]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

body = tk.Tk()
body.configure(background='black')
body.geometry("975x300+200+200")
body.title("YDLGUI")
processinfo = "waiting for some work..."

body_grid = tk.Label(body, bg="black", width=5)
body_grid.grid(row=0, column =2)

input_url_text = tk.Label(body, text="URL: ", bg="black", fg="green", font=("bold", 10), pady=20)
input_url_text.grid(row=0,column=0)

url = tk.StringVar()
test_parameter = tk.StringVar()
input_url = tk.Entry(body, bg="white", width="50", textvariable=url)
input_url.grid(row=0, column=1)

input_path_text = tk.Label(body, text="PATH: ", bg="black", fg="green", font=("bold", 10))
input_path_text.grid(row=1,column=0)

path = tk.StringVar()
input_path = tk.Entry(body,  bg="white", width="50", textvariable=path)
input_path.grid(row=1, column=1)
input_path.insert(0, "Your directory path...")

button_convert_to_mp3 = tk.Button(body, bg="black", fg="green", highlightcolor="green", text="Convert to .mp3", command= lambda: ydl(url,path) ,  font=("bold", 10))
button_convert_to_mp3.grid(row=0, column=3)

process_info = tk.Entry(body, bg="black", fg="green", width=30)
process_info.grid(row=0,column=4)
process_info.insert(0, processinfo)


funny_comment = tk.Label(body, text="- Please donate some coffee. :')", bg="black", fg="green", font=("bold", 10), pady=190, padx=210)
funny_comment.grid(row=2, column=4)




body.mainloop()



