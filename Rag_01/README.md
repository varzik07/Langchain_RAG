# Langchain RAG 

1. Now run this command to install dependenies in the requirements.txt file.

       pip install -r requirements.txt
 
2. Install markdown depenendies with:

       pip install "unstructured[md]"

# Create database
## Create the Chroma DB.
      python python create_database.py

# Query the database
##  Query the Chroma DB.

      python query_data.py "How does Alice meet the Mad Hatter?"

You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.
