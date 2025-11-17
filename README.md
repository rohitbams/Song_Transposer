# Song Transposer

A full-stack web application that downloads audio from YouTube, detects its musical key, and generates a pitch-shifted (transposed) version of the audio in a new key. The project combines a React frontend, a FastAPI backend, and audio processing techniques using Python DSP libraries.

## Features

- YouTube audio download using yt-dlp

- Automatic musical key detection using a Krumhansl–Schmuckler–based algorithm

- Pitch-shifting / audio transposition using librosa

- Frontend interface for inputting a YouTube link, detecting key, selecting a target key, and downloading the transposed audio
- Temporary storage of downloaded and processed audio files

- CORS-enabled FastAPI server

- Clean separation of backend services and frontend UI

## Tech Stack
###Frontend

- React (Vite)

- Axios for HTTP requests

## Backend

- FastAPI

- Python 3.12

- yt-dlp for audio extraction

- librosa, numpy, scipy for DSP processing

- Custom Krumhansl–Schmuckler key detection implementation

##Project Structure

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
│
├── frontend/
│   ├── src/
│   │   ├── AudioTransposer.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   ├── package.json
│
├── .gitignore
└── README.md

## Backend Setup
1. Create a Python virtual environment
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

2. Install backend dependencies
```bash
pip install -r requirements.txt
```
3. Run the FastAPI server
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

- Click Download Audio to fetch the MP3.

- Click Analyse Key to automatically detect the musical key.

- Choose your target key from the dropdown.

- Click Transpose to generate a pitch-shifted version.

- Download the processed audio via the provided link.

## Notes

Audio files are stored temporarily in /tmp/ytdl_audio.

.gitignore excludes virtual environments, Node modules, caches, and temporary audio.

