import pandas as pd
import openai
import subprocess
import json


def fine_tune(dataset_to_train):
    # print("Starting to fine-tune...")
    # ## prepared_data.csv --> prepared_data_prepared.json
    # print("Starting to prepare data...")
    # subprocess.run(f'openai tools fine_tunes.prepare_data -f {dataset_to_train}'.split())

    # ## Start fine-tuning
    # print("Starting the training...")
    # final_dataset_name_as_jsonl = dataset_to_train.replace(".xlsx", "_prepared.jsonl")
    subprocess.run(f'openai api fine_tunes.create --training_file {dataset_to_train} --model davinci --suffix "Kodzilla-try-1"'.split())
    

def main(dataset_to_train):
    ## fine_tune
    fine_tune(dataset_to_train=dataset_to_train)

    
if __name__ == "__main__":
    dataset_to_train = "../datasets/final_prepared_short.jsonl"
    
    main(dataset_to_train=dataset_to_train)