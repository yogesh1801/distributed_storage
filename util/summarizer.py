import os
import pandas as pd
import torch
from transformers import BartForConditionalGeneration, BartTokenizer
import warnings
warnings.filterwarnings("ignore")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_summary(summary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summary)

def summarize(file_path, destination, max_length=1450, min_length=40):
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    text = read_file(file_path=file_path)
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

    summary_ids = model.generate(
        inputs['input_ids'], 
        max_length=max_length, 
        min_length=min_length, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    write_summary(summary=summary, output_file=destination)



