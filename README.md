# Cogni Srch

Cogni Srch is a powerful search application built with Streamlit, DuckDuckGo search, semantic search using Sentence Transformers, and text summarization using LLaMA via the Ollama library.

## Features

- **DuckDuckGo Search:** Utilizes the DuckDuckGo search API to fetch relevant web results.
- **Semantic Search:** Ranks the search results based on semantic similarity using a pre-trained Sentence Transformer model.
- **Summarization with LLaMA:** Summarizes the content of the search results using the LLaMA model through the Ollama library.

## Installation

To run this project locally, follow these steps:

### **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Cogni-Srch.git
   cd Cogni-Srch
   ```

### Install the required dependencies:

   Create a virtual environment (optional but recommended):

```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install the dependencies:

``` bash
pip install -r requirements.txt
```

## Run the application:

``` bash
streamlit run app.py
```

## Dependencies
The required Python packages are listed in requirements.txt. Install them using pip.

## Usage
   Enter a query in the input box and hit Enter.
   The application will search the web using DuckDuckGo and rank the results based on relevance.
   You can view the summarized content of each result by expanding the "View Summary" section.

## Acknowledgments
Streamlit
DuckDuckGo Search API
Sentence Transformers
Ollama LLaMA

### License
This project is licensed under the MIT License - see the LICENSE file for details.


### 4. `requirements.txt`

Create a `requirements.txt` file to list all the dependencies needed to run your app. Here is a sample based on the libraries you used:

```plaintext
streamlit
requests
beautifulsoup4
duckduckgo-search  # DuckDuckGo search library
sentence-transformers
scikit-learn
numpy
ollama
``` 
### Steps to Push to GitHub
Initialize the Git repository:

``` bash
git init
git add .
git commit -m "Initial commit for Cogni Srch"
``` 
Create a new repository on GitHub and follow the instructions to push your local repository to GitHub:

``` bash

git remote add origin https://github.com/yourusername/Cogni-Srch.git
git branch -M main
git push -u origin main
``` 
Replace yourusername with your actual GitHub username.

### Run the App
To run the app locally after cloning the repository:

``` bash
streamlit run app.py
``` 
This will launch the app in your web browser, where you can enter search queries and see the semantic search results and summaries.
