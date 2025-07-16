import os
import sys
import yt_dlp

def download_video(url):
    output_dir = 'output'

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'noplaylist': True,
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"\n✅ Video downloaded successfully to '{output_dir}'")
        except Exception as e:
            print(f"\n❌ Error downloading video: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python download_x_video.py <X_video_url>")
        sys.exit(1)

    video_url = sys.argv[1]
    download_video(video_url)

