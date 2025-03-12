# DeepScholar is an open-source framework for performing deep search of online and offline sources
# (C) 2025, Ambuj Varshney, ambujv@nus.edu.sg
# WEISER Research Group, National University of Singapore
# This code is released under license BSD 3-Clause
# File handles task of querying Google search engine and extracting links

# Import necessary libraries
from googlesearch import search

# Default query settings
QUERY = "This is a dummy query"
NUM_RESULTS = 10

def set_google_search_query(query_model, nos):
    """Set the Google search query and number of results."""

    global QUERY, NUM_RESULTS
    
    QUERY = query_model
    NUM_RESULTS = max(nos, 10)  # Ensure a positive number of results

def perform_google_search():
    """Perform Google search and extract links with brief descriptions."""
    search_results = []

    for i, result in enumerate(search(QUERY, num_results=NUM_RESULTS, lang="en"), start=1):
        search_results.append({"rank": i, "link": result})  # Store rank and link

    return search_results







