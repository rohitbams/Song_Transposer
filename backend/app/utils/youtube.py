import yt_dlp
import os
import uuid

def download_youtube_audio(url: str) -> str:
    """
    Downloads the audio of a YouTube video using yt-dlp and stores it in /tmp.
    Returns the full path to the downloaded audio file.
    """

    output_dir = "/tmp/ytdl_audio"
    os.makedirs(output_dir, exist_ok=True)

    # unique filename to avoid collisions
    file_id = uuid.uuid4().hex
    output_template = f"{output_dir}/{file_id}.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "quiet": True,
        "no_warnings": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    # Resolve actual file path
    downloaded_file = f"{output_dir}/{file_id}.mp3"
    return downloaded_file
