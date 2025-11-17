import librosa
import numpy as np

KEYS_MAJOR = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
KEYS_MINOR = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def detect_key(file_path: str):
    """
    Detect the key and scale of an audio file.
    Returns: dict { detected_key, scale, confidence }
    """
    y, sr = librosa.load(file_path, sr=None, mono=True)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)

    # Major key correlation
    # maj_profiles = librosa.key_to_notes('C')  # placeholder for actual profile correlation
    # For simplicity, we just pick the max chroma
    max_idx = np.argmax(chroma_mean)
    detected_key = KEYS_MAJOR[max_idx]  # simplistic, mostly works for demonstration
    scale = 'major'  # we’ll assume major for now
    confidence = float(chroma_mean[max_idx] / np.sum(chroma_mean))
    
    return {
        "detected_key": detected_key,
        "scale": scale,
        "confidence": round(confidence, 2)
    }
