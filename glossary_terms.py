import tkinter as tk
from tkinter import messagebox
import nltk
nltk.data.path.append(r'C:\Users\ajink\AppData\Roaming\nltk_data')
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Function to find n-grams (bigrams, trigrams) in text
def find_ngrams():
    text = entry.get()

    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize the cleaned text
    words = word_tokenize(text)
    
    # Get the list of stopwords in English
    stop_words = set(stopwords.words('english'))
    
    # Filter out stopwords from the tokenized words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Generate bigrams and trigrams
    bigrams = list(ngrams(filtered_words, 2))
    trigrams = list(ngrams(filtered_words, 3))

    result = "Bigrams:\n"
    for bigram in bigrams:
        result += str(bigram) + "\n"
    
    result += "\nTrigrams:\n"
    for trigram in trigrams:
        result += str(trigram) + "\n"

    messagebox.showinfo("N-Grams", result)

# Create main window
root = tk.Tk()
root.title("N-Grams Finder")

# Create UI elements
label = tk.Label(root, text="Enter text to find Bigrams and Trigrams:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Find N-Grams", command=find_ngrams)
button.pack()

# Start the GUI loop
root.mainloop()

