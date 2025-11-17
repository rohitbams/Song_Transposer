import React, { useState } from "react";
import axios from "axios";

export default function AudioTransposer() {
    const [youtubeURL, setYoutubeURL] = useState("");
    const [originalKey, setOriginalKey] = useState("");
    const [targetKey, setTargetKey] = useState("C");
    const [filePath, setFilePath] = useState("");
    const [transposedFile, setTransposedFile] = useState("");
    const [status, setStatus] = useState("");

    const file_name = transposedFile ? transposedFile.split("/").pop() : "";

    const handleDownload = async () => {
        setStatus("Downloading audio...");
        try {
            const formData = new FormData();
            formData.append("youtube_url", youtubeURL);

            const res = await axios.post("http://127.0.0.1:8000/api/download", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });
            setFilePath(res.data.file_path);
            setStatus("Download complete!");
        } catch (err) {
            console.error(err);
            setStatus("Download failed!");
        }
    };

const handleAnalyse = async () => {
    setStatus("Analysing key...");
    try {
        const formData = new FormData();
        formData.append("file_path", filePath);

        const res = await axios.post("http://127.0.0.1:8000/api/analyse", formData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        setOriginalKey(res.data.detected_key);
        setStatus(`Detected key: ${res.data.detected_key}`);
    } catch (err) {
        console.error(err);
        setStatus("Analysing failed!");
    }
};

const handleTranspose = async () => {
    setStatus("Transposing audio...");
    try {
        const formData = new FormData();
        formData.append("file_path", filePath);
        formData.append("original_key", originalKey);
        formData.append("target_key", targetKey);

        const res = await axios.post("http://127.0.0.1:8000/api/transpose", formData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        setTransposedFile(res.data.file_path);
        setStatus("Transposition complete!");
    } catch (err) {
        console.error(err);
        setStatus("Transposition failed!");
    }
};


    return (
        <div>
            <h1>Audio Transposer</h1>

            <input
                type="text"
                value={youtubeURL}
                placeholder="YouTube URL"
                onChange={(e) => setYoutubeURL(e.target.value)}
            />
            <button onClick={handleDownload}>Download Audio</button>

            <button onClick={handleAnalyse} disabled={!filePath}>Analyse Key</button>
            {originalKey && <p>Detected Key: {originalKey}</p>}

            <select value={targetKey} onChange={(e) => setTargetKey(e.target.value)}>
                {["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"].map((key) => (
                    <option key={key} value={key}>{key}</option>
                ))}
            </select>
            <button onClick={handleTranspose} disabled={!originalKey}>Transpose</button>

            {transposedFile && (
                <div>
                    <a href={`http://127.0.0.1:8000/ytdl_audio/${file_name}`} download>
                        Download Transposed Audio
                    </a>
                </div>
            )}

            <p>{status}</p>
        </div>
    );
}
