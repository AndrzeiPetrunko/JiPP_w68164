import re
from collections import Counter

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]', text)
    paragraphs = text.split('\n')

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])
    paragraph_count = len([p for p in paragraphs if p.strip()])

    stop_words = set(["i", "a", "the", "and", "of", "in", "to", "it", "is", "that", "this", "on", "for", "with"])
    filtered_words = [word for word in words if word not in stop_words]
    most_common_words = Counter(filtered_words).most_common(10)

    transformed_words = [word[::-1] if word.startswith('a') else word for word in words]

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "most_common_words": most_common_words,
        "transformed_text": ' '.join(transformed_words)
    }

text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'

So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
"""

result = analyze_text(text)
print("Liczba słów:", result["word_count"])
print("Liczba zdań:", result["sentence_count"])
print("Liczba akapitów:", result["paragraph_count"])
print("Najczęstsze słowa:", result["most_common_words"])
print("Tekst po transformacji:", result["transformed_text"])
