import re
from collections import Counter



stop_words = {"i", "a", "the", "and", "or", "is", "of", "in", "to", "into", "on"}

def text_count(text):
    text = text.strip()
    words_count = len(re.findall(r'\b\w+\b', text))
    sentences = [s for s in re.split(r'[.!?]', text) if s.strip() != '']
    sentences_count = len(sentences)
    paragraphs_count = len(text.split("\n\n"))
    return words_count, sentences_count, paragraphs_count
text = """a."""
words, sentences, paragraphs = text_count(text)
print(f"Ilość słów: {words}\nIlość zdań: {sentences}\nIlość akapitów: {paragraphs}")




