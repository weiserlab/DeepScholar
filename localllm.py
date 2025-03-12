# DeepScholar is an open-source framework for performing deepserarch of online and offline sources
# (C) 2025, Ambuj Varshney, ambujv@nus.edu.sg
# WEISER Research Group, National University of Singapore
# This code is released under license BSD 3-Clause
# locallm.py - Defines the local LLM interface building on Ollama

import ollama

def get_local_available_models():
    """Fetch available models from Ollama and extract their names properly."""
    models = ollama.list()  # Fetch available models

    # Print to debug the response format
    print("Raw models output:", models)

    if hasattr(models, "models"):  # Check if it has a 'models' attribute
        return [model.model for model in models.models]  # Extract model names properly

    raise ValueError("Unexpected response format from ollama.list()")

# Define a global variable for selected model (default)
DEFAULT_MODEL = "mistral"

# Set the model 
def set_local_model(model_name):
    global DEFAULT_MODEL
    if model_name in get_local_available_models():
        DEFAULT_MODEL = model_name
    else:
        raise ValueError(f"Model '{model_name}' not found. Available models: {get_available_models()}")

def query_local_model(prompt):
    response = ollama.chat(model=DEFAULT_MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]


