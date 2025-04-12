import tensorflow as tf
import numpy as np
import librosa

class SoundRecognition:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def preprocess_audio(self, audio_path):
        audio, sr = librosa.load(audio_path, sr=None)
        audio = librosa.resample(audio, sr, 16000)
        audio = np.expand_dims(audio, axis=0)
        return audio

    def classify_sound(self, audio_path):
        audio = self.preprocess_audio(audio_path)
        predictions = self.model.predict(audio)
        return np.argmax(predictions, axis=1)

    def load_labels(self, labels_path):
        with open(labels_path, 'r') as f:
            labels = f.readlines()
        return [label.strip() for label in labels]