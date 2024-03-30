import json
import nltk
import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def analyze_segment(segment):
    sentences = sent_tokenize(segment)
    words = word_tokenize(segment)
    num_sentences = len(sentences)
    avg_sentence_length = sum(len(word_tokenize(sentence)) for sentence in sentences) / num_sentences
    lexical_diversity = len(set(words)) / len(words)

    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords.words('english')]
    word_freqs = Counter(filtered_words).most_common(2)
    summary = ' '.join([word for word, freq in word_freqs])

    return avg_sentence_length, lexical_diversity, summary

def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    segments = [text[i:i+500] for i in range(0, len(text), 500)]
    results = []

    for segment in segments:
        avg_sentence_length, lexical_diversity, summary = analyze_segment(segment)
        results.append({
            'avg_sentence_length': avg_sentence_length,
            'lexical_diversity': lexical_diversity,
            'summary': summary
        })

    with open('analysis_results_with_summaries.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

file_path = '/path/to/your/file.txt'
main(file_path)
