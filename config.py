from dotenv import load_dotenv
import yaml
import os
load_dotenv()


class Config:
    
    WATI_SERVER = os.getenv('WATI_SERVER')
    WATI_API_KEY = os.getenv('WATI_API_KEY')

    def __init__(self, environment='development'):
        self.environment = environment
        self.config = self.load_config()

    def load_config(self):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        return config.get(self.environment, {})

    def get(self, key, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value else default
