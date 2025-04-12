from speech_to_text import transcribe_audio
from noise_filter import reduce_noise
from sound_recognition import classify_sound
from nlp_analysis import analyze_text

class SoundProcessingPipeline:
    def __init__(self, audio_file, config):
        self.audio_file = audio_file
        self.config = config

    def run(self):
        # Step 1: Noise reduction
        clean_audio = reduce_noise(self.audio_file, self.config['noise_reduction'])

        # Step 2: Speech to text transcription
        transcription = transcribe_audio(clean_audio, self.config['whisper_model'])

        # Step 3: Natural language processing analysis
        analysis_results = analyze_text(transcription, self.config['nlp_model'])

        # Step 4: Sound event classification
        sound_classification = classify_sound(clean_audio, self.config['sound_recognition_model'])

        return {
            'transcription': transcription,
            'analysis_results': analysis_results,
            'sound_classification': sound_classification
        }