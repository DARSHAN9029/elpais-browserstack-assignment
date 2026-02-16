from collections import Counter
import re

class TextAnalyzer:

    STOPWORDS = {"the", "of", "in", "and", "a", "to", "for", "on"}

    def find_repeated_words(self, headers):
        all_words = []

        for header in headers:
            words = re.findall(r'\b\w+\b', header.lower())
            filtered = [w for w in words if w not in self.STOPWORDS]
            all_words.extend(filtered)

        counter = Counter(all_words)

        repeated = {word: count for word, count in counter.items() if count > 2}

        return repeated
