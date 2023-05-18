import re
import spacy
from collections import Counter
from Levenshtein import distance as levenshtein_distance
from jellyfish import jaro_winkler_similarity

def find_companies(text):
    # Define a regular expression pattern to match company names
    pattern = r'\b(?:[A-Z][\w&\'\-.]*[a-z]+(?:\s+|\-|\&)(?:[A-Z][\w&\'\-.]*[a-z]+)*|[\w&\'\-.]*[a-z]+(?:\s+|\-|\&)(?:[\w&\'\-.]*[a-z]+)*(?:\s+(?:[\w&\'\-.]*[a-z]+|\([A-Z][\w&\'\-]*\)))?|^[A-Z][\w&\'\-.]*|\b[a-zA-Z0-9&\'\-.]+\b)\b'

    # Load the pre-trained NER model
    nlp = spacy.load("en_core_web_lg")

    # Process the input text with the NER model
    doc = nlp(text)

    # Extract named entities of type "ORG" (i.e., organizations)
    entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

    # Find matches between the entities and the pattern matches using Levenshtein distance and Jaro-Winkler similarity
    matches = []
    for entity in entities:
        for match in re.findall(pattern, entity):
            if levenshtein_distance(entity.lower(), match.lower()) <= 2 or jaro_winkler_similarity(entity.lower(), match.lower()) >= 0.9:
                matches.append(match)

    # Count the occurrences of each match
    match_counts = Counter(matches)

    # Get the most common match, i.e., the company mentioned most frequently in the text
    if match_counts:
        most_common_match = match_counts.most_common(1)[0][0]
    else:
        most_common_match = None

    return most_common_match
