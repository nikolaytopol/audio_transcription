import os
import yaml
from app.pipeline import SoundProcessingPipeline

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    config_path = 'config.yaml'
    config = load_config(config_path)

    pipeline = SoundProcessingPipeline(config)
    pipeline.run()

if __name__ == "__main__":
    main()