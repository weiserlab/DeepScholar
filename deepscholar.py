# DeepScholar is an open-source framework for performing deepserarch of online and offline sources
# (C) 2025, Ambuj Varshney, ambujv@nus.edu.sg
# WEISER Research Group, National University of Singapore
# This code is released under license BSD 3-Clause

import localllm

import os

# Import necessary libraries for PDF processing
import reportlab
import pypdf

# Import necessary libraries for LLM
# import openai 
import ollama

# Import necessary libraries for web scraping
from googlesearch import search

# Example Usage
if __name__ == "__main__":
    available_models = localllm.get_local_available_models()
    print("Available Models:", available_models)

    # Set a specific model (User-defined)
    try:
        localllm.set_local_model("deepseek-r1:14b")  # Change model name here
    except ValueError as e:
        print(e)

    print("Using Model:", localllm.DEFAULT_MODEL)

    # Query Ollama
    response = localllm.query_local_model("What is artificial intelligence?")
    print("\nOllama Response:\n", response)


query = "Best Python web scraping libraries"
num_results = 25  # Number of search results to fetch

# Get search results
for i, result in enumerate(search(query, num_results=num_results, lang="en"), start=1):
    print(f"{i}. {result}")

# Import necessary libraries for web scraping


