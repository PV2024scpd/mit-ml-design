
import os
import json
import csv
import bardapi
import os

# set your __Secure-1PSID value to key
os.environ['_BARD_API_KEY']="fAhj3KRqKDgHbQcQTCNYIGcbpVUvNYIBq2KbZhyJxxAEY9b6GyvLst2Cup9g5qIp-2M-tg."

def generate_low(sentence: str) -> str:

    header = """write story about"""   

    # header = """Informativeness = How relevant is the information in an explanation?, Clarity = How clear is the meaning of an explanation?. Generate a version of the provided explanation with low informativeness and clarity. Original Explanation:"""    

    # header = """Craft a version of the provided explanation that lacks clarity and informativeness. Original Explanation:"""   

    # header = """Generate a version of the provided explanation that lacks clarity and informativeness. Original Explanation:"""   
    # header = """Informativeness = How relevant is the information in an explanation?, Clarity = How clear is the meaning of an explanation?. Create a causal version of the provided explanation that lacks informativeness and clarity. Original Explanation:"""
    # header = """Informativeness = How relevant is the information in an explanation?, Clarity = How clear is the meaning of an explanation?. Generate a causal explanation that lacks informativeness and clarity, using these triples: caffeine, cause, insomnia"""
    # header = """Generate an explanation using these triples: caffeine, cause, insomnia"""

    return header + " " + sentence + "max 3 paragraphs"
    # return header

def generate(prompt):
    response = bardapi.core.Bard().get_answer(prompt)
    return response

sentence = "Generative Adversial Networks"
print("Original explanation:", sentence)
prompt = generate_low(sentence)
print("Prompt:", prompt)
# prompt = generate_high(sentence)

response = generate(prompt)
print("New Explanation", response['content'])
print("\n")

