# Facebook Reels Downloader

Facebook Reels Downloader is a simple Python script that allows you to download and save your favorite Facebook reels to your computer in high quality. The tool supports various Facebook video URL formats and saves videos in MP4 format.

## Features

- Download Facebook Reels in the best available quality
- Support for multiple URL formats (reels, videos, share links)
- Simple command-line interface
- Automatic file naming based on video ID
- Progress tracking during download

## Requirements

- Python 3.6 or higher
- yt-dlp library

## Installation

Clone the repository:
```
git clone https://github.com/yourusername/facebook_reels_downloader.git
cd facebook_reels_downloader
```

Install the required dependencies:
```
pip install yt-dlp
```

## Usage

Run the script using Python:
```
python reels_downloader.py
```


When prompted, enter the URL of the Facebook Reel you want to download. The script will verify if the URL is valid and then download the video to your Downloads folder.

### Supported URL formats

- `https://www.facebook.com/reel/123456789`
- `https://www.facebook.com/username/videos/123456789`
- `https://www.facebook.com/share/r/123456789`
- `https://fb.watch/abcdef`

## How It Works

The script uses yt-dlp, a powerful media downloader that supports numerous websites including Facebook. It extracts the video ID from the URL, configures the download options, and saves the video to your specified directory.

## Limitations

- Some videos may not be downloadable if they are private or have restricted access.
- Facebook occasionally changes its structure, which might require updates to the script.
- As of April 2025, there are some known issues with Facebook Reels parsing in older versions of yt-dlp.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for personal use only. Please respect copyright and terms of service of Facebook. Only download videos you have permission to download.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
