# DeepScholar is an open-source framework for performing deepserarch of online and offline sources
# (C) 2025, Ambuj Varshney, ambujv@nus.edu.sg
# WEISER Research Group, National University of Singapore
# This code is released under license BSD 3-Clause

# Import necessary modules for using local LLM
import localllm
import searchgoogle

import os

# Import necessary libraries for PDF processing
import reportlab
import pypdf

# Import necessary libraries for LLM
# import openai 
import ollama



# Example Usage
# if __name__ == "__main__":
#     # Get list of available LLM models from Ollama
#     available_models = localllm.get_local_available_models()
#     print("Available Models:", available_models)
#
#     # Attempt to set specific LLM model, with error handling
#     # Default is "mistral" if specified model not available
#     try:
#         localllm.set_local_model("deepseek-r1:14b")  # Change model name here
#     except ValueError as e:
#         print(e)  # Print error if model not found
#
#     # Display currently active model
#     print("Using Model:", localllm.DEFAULT_MODEL)
#
#     # Send test query to LLM model and print response
#     # Simple query to verify model is working
#     response = localllm.query_local_model("What is artificial intelligence?")
#     print("\nOllama Response:\n", response)

if __name__ == "__main__":
    # Example: Change this to your required search query
    searchgoogle.set_google_search_query("Latest trends in AI", 10)
    
    results = searchgoogle.perform_google_search()

    for res in results:
        print(f"{res['rank']}. {res['link']}")


