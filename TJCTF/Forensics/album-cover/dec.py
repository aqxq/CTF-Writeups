from PIL import Image
import numpy as np
import wave

# Load the image
img = Image.open('albumcover.png').convert('L')
arr = np.array(img)

# Undo normalization
arr = arr.astype(np.float32) / 255 * 65535 - 32767
arr = arr.astype(np.int16)
frames = arr.flatten()

# Save as WAV
with wave.open('recovered.wav', 'wb') as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    w.writeframes(frames.tobytes())
