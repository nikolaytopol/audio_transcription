from transformers import pipeline

class NLPAnalysis:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.nlp_pipeline = pipeline("fill-mask", model=model_name)

    def extract_meaning(self, text):
        results = self.nlp_pipeline(text)
        return results

if __name__ == "__main__":
    nlp = NLPAnalysis()
    sample_text = "The quick brown fox jumps over the lazy [MASK]."
    meaning = nlp.extract_meaning(sample_text)
    print(meaning)