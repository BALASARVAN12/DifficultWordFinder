import textstat
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
# Download stopwords data (run this only once)
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
def find_difficult_words(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Filter out difficult words with their meanings and syllables
    difficult_words = []
    for word in words:
        if textstat.syllable_count(word) >= 3:
            meanings_nltk = get_meanings_nltk(word)
            difficult_words.append({"word": word, "syllables": textstat.syllable_count(word), "meaning_nltk": meanings_nltk})

    return difficult_words

def get_meanings_nltk(word):
    meanings = []
    synsets = wn.synsets(word)
    for synset in synsets:
        for definition in synset.definition().split(";"):
            meanings.append(definition.strip())
    return meanings

def main():
    try:
        # Sample text for testing
        text = input("Enter:")
        # Finding difficult words in the text with meanings
        difficult_words = find_difficult_words(text)

        # Display the difficult words and their meanings
        print("Difficult Words:")
        for word_obj in difficult_words:
            print(f"{word_obj['word']} (Syllables: {word_obj['syllables']})")
            print("Meaning from NLTK (WordNet):")
            print(", ".join(word_obj['meaning_nltk']))
            print("=" * 30)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()