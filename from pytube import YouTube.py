from pytube import YouTube

def descargar_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(f"Descargando: {yt.title}")
        video.download()
        print("Descarga completada.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Introduce el enlace del video de YouTube: ")
    descargar_video(url)