import librosa
import soundfile as sf
import os
import uuid

KEYS_MAJOR = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def transpose_audio(file_path: str, original_key: str, target_key: str):
    """
    Transpose the audio file from original_key to target_key.
    Returns path to the new transposed audio file.
    """

    # Load audio
    y, sr = librosa.load(file_path, sr=None)

    # Calculate semitone shift
    try:
        orig_idx = KEYS_MAJOR.index(original_key)
        target_idx = KEYS_MAJOR.index(target_key)
    except ValueError:
        raise ValueError("Invalid key name. Use standard keys: C, C#, D, ...")

    n_semitones = target_idx - orig_idx

    # Shift pitch
    y_shifted = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=n_semitones)

    # Save new file
    output_dir = "/tmp/ytdl_audio"
    os.makedirs(output_dir, exist_ok=True)
    file_id = uuid.uuid4().hex
    output_file = os.path.join(output_dir, f"{file_id}_transposed.mp3")

    sf.write(output_file, y_shifted, sr, format='MP3')

    return output_file
