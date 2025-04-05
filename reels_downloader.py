import os
import sys
import re
from yt_dlp import YoutubeDL

def download_facebook_reel(url, output_dir=None):
    if output_dir is None:
        output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    video_id = re.search(r'\/reel\/(\d+)', url)
    filename = f"facebook_reel_{video_id.group(1) if video_id else 'video'}.mp4"
    output_path = os.path.join(output_dir, filename)
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': False,
        'no_warnings': False,
        'progress': True,
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nDownload concluído com sucesso! Salvo em: {output_path}")
        return True
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {str(e)}")
        return False

def main():
    print("===== Facebook Reels Downloader =====")
    reel_url = input("Digite a URL do Reel do Facebook: ")
    
    # Verificar se a URL é válida
    if not (reel_url.startswith("https://www.facebook.com/reel/") or 
            "facebook.com" in reel_url and "/videos/" in reel_url or
            "facebook.com" in reel_url and "/share/r/" in reel_url or
            "fb.watch" in reel_url):
        print("URL inválida! Por favor, forneça uma URL válida de Reel do Facebook.")
        return
    
    # Baixar o vídeo
    print("Iniciando download...")
    download_facebook_reel(reel_url)

if __name__ == "__main__":
    main()
