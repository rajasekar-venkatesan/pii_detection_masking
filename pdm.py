"""
PDM - PII Detection and Masking
"""

# Imports
from time import time
from pprint import pprint
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine


# Globals
ENTITIES_OF_INTEREST = ['PERSON', 'PHONE_NUMBER', 'LOCATION', 'NRP', 'IP_ADDRESS', 'EMAIL_ADDRESS', 'DOMAIN_NAME', 'DATE_TIME', 'CREDIT_CARD', 'SG_NRIC_FIN']


# Classes
class PDM:
    def __init__(self, language='en'):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
        self.language = language

    def predict(self, text, entities_of_interest=ENTITIES_OF_INTEREST):
        t0 = time()
        analyzer_results = self.analyzer.analyze(text, entities=entities_of_interest, language=self.language)
        t1 = time()
        anonymized_results = self.anonymizer.anonymize(text=text, analyzer_results=analyzer_results)
        t2 = time()
        results = {'time_to_analyze': f'{t1-t0:.4f} seconds',
                   'time_to_anonymize': f'{t2-t1:.4f} seconds',
                   'anonymized_text': anonymized_results.text,
                   'detected_items': [{'start': item.start, 'end': item.end, 'entity_type': item.entity_type} for item in anonymized_results.items]}
        return results


pdm_model = PDM()


# Main
if __name__ == '__main__':
    text = "My name is Rajasekar Venkatesan and my phone number is +6597720584. I live in Singapore but I am from Tamil Nadu, India. I'm an Indian and Hindu. My GPU machine's local address is 192.162.18.9 and my email address is rajasekar_venkatesan@singaporeair.com.sg. I'm working on a search project for www.singaporeair.com.sg for about 2 months 12 days and 6 hours as of 04:30 PM today. My credit card number is 4119-1101-0319-4913 and my FIN number is G1162041N"
    result = pdm_model.predict(text)
    pprint(result)
