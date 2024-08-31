import streamlit as st
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS  # Updated import
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import ollama

# Load the semantic model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def search_duckduckgo(query, num_results=5):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=num_results))
    return results

def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except:
        return ""

def get_semantic_similarity(query, text, model):
    query_embedding = model.encode([query])
    text_embedding = model.encode([text])
    similarity = cosine_similarity(query_embedding, text_embedding)[0][0]
    return similarity

def summarize_with_llama(text):
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt, 'stream': False}
    ])
    message = response['message']
    output = message['content']
    return output

st.title("Cogni Srch")

query = st.text_input("Enter your search query:")

if query:
    with st.spinner("Searching and processing results..."):
        # Search DuckDuckGo
        search_results = search_duckduckgo(query)
        
        # Process and rank results
        processed_results = []
        for result in search_results:
            content = fetch_content(result['href'])
            similarity = get_semantic_similarity(query, content, model)
            processed_results.append({
                'title': result['title'],
                'url': result['href'],
                'content': content,
                'similarity': similarity
            })
        
        # Sort results by similarity
        processed_results.sort(key=lambda x: x['similarity'], reverse=True)
        
        # Display results and summaries
        for i, result in enumerate(processed_results[:3], 1):
            st.subheader(f"Result {i}: {result['title']}")
            st.write(f"URL: {result['url']}")
            st.write(f"Relevance Score: {result['similarity']:.2f}")
            
            with st.expander("View Summary"):
                summary = summarize_with_llama(result['content'][:1000])  # Limit content length for summarization
                st.write(summary)

st.sidebar.markdown("## About")
st.sidebar.info("This app uses DuckDuckGo for search, a semantic model for relevance ranking, and Llama (via Ollama) for summarization.")
