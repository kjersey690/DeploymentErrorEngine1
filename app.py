from flask import Flask, render_template, request, jsonify
import openai
import pandas as pd
import numpy as np
from config import OPENAI_API_KEY
from getpass import getpass
from openai.embeddings_utils import get_embedding

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)


df = pd.read_csv('title.csv')
print(df)

# df['embedding'] = df['text'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
# df.to_csv('title_embeddings.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Handle search logic here
    query = request.form['query']
    # Implement search using your preferred search engine (e.g., Elasticsearch)
    # and return search results as a JSON response
    # search_results = search_engine.search(query)
    search_results = []  # Placeholder for search results
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)
