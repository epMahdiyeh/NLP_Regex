from hazm import Normalizer
from hazm import sent_tokenize
import json
import codecs

class Detector:

    def __init__(self):
        self.vehicles = json.load(codecs.open(F'Files/vehicles.json', 'r', 'utf-8'))
        self.stopwords_v = ['با', 'به کمک', 'به وسیله', 'بوسیله', 'با استفاده از', 'بکمک']


    def normalize(self, inputs):
        normalized = Normalizer().normalize(inputs)
        samples = sent_tokenize(normalized)
        return samples

    def find(self, matched]:
        matched_phrases = []
        # look for matched phrases
        if not matched_phrases:
            return None
        # return matched


    def output_generator(self):
        output = []
        entities = {0: "from", 1: "to", 2: "vehicle"}
        for i in range(3):
        #idk
        return output
