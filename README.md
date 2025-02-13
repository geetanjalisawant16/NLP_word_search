

# N-Grams Finder App

This is a simple Python application that uses **Tkinter** to create a graphical user interface (GUI) for finding **bigrams** and **trigrams** from user input text. The app utilizes **NLTK (Natural Language Toolkit)** for text processing, tokenization, stopword removal, and generating n-grams.

## Requirements

To run this application, you need to install the following dependencies:

- **Tkinter** (for the GUI)
- **NLTK** (for text processing and n-gram generation)

You can install these dependencies using the following commands:

```bash
pip install nltk
```

Tkinter is generally included with Python, but if it's not installed, you can follow instructions for your operating system:

- For **Windows**, Tkinter is typically installed by default with Python.
- For **Mac** and **Linux**, Tkinter may need to be installed separately. Refer to the relevant documentation for installation.

## Usage

1. Clone or download this repository to your local machine.
2. Open the script in a Python environment that supports Tkinter.
3. Run the script. This will launch a simple Tkinter window.
4. Enter any text in the input box and press the "Find N-Grams" button.
5. The application will generate and display the **bigrams** and **trigrams** found in the entered text.

### Example

1. Input: "I love programming and working with Python."
2. Output:
   - **Bigrams**: (I, love), (love, programming), (programming, and), ...
   - **Trigrams**: (I, love, programming), (love, programming, and), ...

## Explanation

1. The text entered by the user is cleaned by removing punctuation using regex.
2. The text is tokenized into individual words.
3. Stopwords (common words like "and", "the", "a", etc.) are filtered out using NLTK's stopwords corpus.
4. Bigrams (2-word combinations) and trigrams (3-word combinations) are generated using the `nltk.util.ngrams` function.
5. The results (bigrams and trigrams) are displayed in a message box.

## Required NLTK Data

Before running the script, ensure that the following NLTK data packages are downloaded:

- **punkt**: Tokenizer models.
- **stopwords**: Common stopwords for filtering.
- **averaged_perceptron_tagger**: Part-of-speech tagger (used in some NLTK functions).

The script automatically downloads these resources when run.

## License

This project is open-source and available under the Apache 2.0 License.link https://github.com/geetanjalisawant16/NLP_word_search/tree/main#Apache-2.0-1-ov-file



