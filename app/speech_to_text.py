import torch
import whisper

class SpeechToText:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

        options = whisper.DecodingOptions(language="en")
        result = whisper.decode(self.model, mel, options)
        return result.text

if __name__ == "__main__":
    stt = SpeechToText()
    transcription = stt.transcribe("path_to_audio_file.wav")
    print(transcription)