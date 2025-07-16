import os
import sys
import yt_dlp

def download_youtube_video(url):
    output_dir = 'output'

    # Create 'output' directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Save as title.ext
        'quiet': False,
        'noplaylist': True,  # Avoid downloading playlists
        'merge_output_format': 'mp4',  # Merge to mp4 if needed
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"\n✅ Video downloaded successfully to '{output_dir}'")
    except Exception as e:
        print(f"\n❌ Error downloading video: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python download_youtube_video.py <YouTube_URL>")
        sys.exit(1)

    video_url = sys.argv[1]
    download_youtube_video(video_url)
