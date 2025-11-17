# Song Transposer

A full-stack web application that downloads audio from YouTube, detects its musical key, and generates a pitch-shifted (transposed) version of the audio in a new key. The project combines a React frontend, a FastAPI backend, and audio processing techniques using Python DSP libraries.

## Features

- YouTube audio download using **yt-dlp**
- Automatic musical key detection using a [Krumhansl–Schmuckler–based algorithm](https://rnhart.net/articles/key-finding/)
- Pitch-shifting / audio transposition using librosa
- Simple UI for:
    - entering a YouTube url
    - detecting key
    - selecting a new key
    - downloading the transposed audio
- Temporary storage of downloaded and processed audio files
- CORS-enabled FastAPI server
- Clean modular separation of services and UI

## Tech Stack
### Frontend

- React (Vite)
- Axios

## Backend

- FastAPI
- Python 3.12
- yt-dlp
- librosa, numpy, scipy

## Project Structure

```
Song_Transposer/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py
│   │   ├── services/
│   │   │   ├── key_detection.py
│   │   │   ├── transposer.py
│   │   ├── utils/
│   │   │   ├── youtube.py
│   │   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── AudioTransposer.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   ├── package.json
│
└── README.md
```

## Backend Setup

1. Create and activate a virtual environment
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```
Windows
```cmd
venv\Script\activate
```
2. Install backend dependencies
```bash
pip install -r requirements.txt
```
3. Install ffmpeg
macOS
```bash
brew install ffmpeg
```
Ubuntu / Debian
```bash
sudp apt install ffmpeg
```
Windows
Download from: https://ffmpeg.org/download.html and add to PATH.
4. Start the FastAPI server
```bash
uvicorn app.main:app --reload
```
The backend will be available at:
http://127.0.0.1:8000

## Frontend Setup

1. Install dependencies
```bash
cd frontend
npm install
```
2. Start development server
```bash
npm run dev
```
The frontend will be available at:
http://127.0.0.1:5173

## How to Use

- Open the frontend in your browser.
- Enter any YouTube video URL containing music.
- Click Download Audio.
- Click Analyse Key to detect the musical key.
- Choose your target key from the dropdown.
- Click Transpose to generate a pitch-shifted version.
- Download the processed audio.

## Notes

- Audio files are stored temporarily in a system temp directory (e.g., `/tmp/ytdl_audio` on macOS/Linux; on Windows a platform-appropriate temp directory is used).
- The .gitignore excludes virtual environments, node_modules, caches, and temporary audio files.
- This project is cross-platform (macOS, Linux, Windows), but Windows users must install ffmpeg manually and activate the venv using `venv\Scripts\activate`
