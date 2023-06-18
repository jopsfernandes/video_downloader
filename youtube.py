from pytube import YouTube

link = input("coloque a url de seu vídeo aqui:")
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
prin("Prontinho, aproveite o vídeo")