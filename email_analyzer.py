import spacy
import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from collections import Counter
import re

nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

def analyze_email(email_text: str) -> dict:
    """Full NLP analysis of an email."""
    doc = nlp(email_text)
    blob = TextBlob(email_text)
    sentiment_scores = sia.polarity_scores(email_text)

    # Sentiment
    compound = sentiment_scores["compound"]
    if compound >= 0.05:
        sentiment = "Positive 😊"
    elif compound <= -0.05:
        sentiment = "Negative 😟"
    else:
        sentiment = "Neutral 😐"

    # Intent detection
    text_lower = email_text.lower()
    intent = "General Inquiry"
    if any(w in text_lower for w in ["complaint", "unhappy", "disappointed", "issue", "problem"]):
        intent = "Complaint"
    elif any(w in text_lower for w in ["thank", "grateful", "appreciate"]):
        intent = "Appreciation"
    elif any(w in text_lower for w in ["request", "please", "could you", "can you", "need"]):
        intent = "Request"
    elif any(w in text_lower for w in ["question", "how", "what", "when", "where", "why", "?"]):
        intent = "Question"
    elif any(w in text_lower for w in ["follow up", "following up", "checking in"]):
        intent = "Follow-up"

    # Key entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Key sentences (top 2 by word count, simple extraction)
    sentences = sent_tokenize(email_text)
    key_sentences = sorted(sentences, key=len, reverse=True)[:2]

    # Formality
    formal_words = {"please", "kindly", "regarding", "herewith", "sincerely", "dear"}
    casual_words = {"hey", "hi", "thanks", "cool", "awesome", "yeah", "nope"}
    words = set(text_lower.split())
    formality = "Formal" if len(words & formal_words) > len(words & casual_words) else "Casual"

    # Word count & reading time
    word_count = len(email_text.split())
    read_time = max(1, round(word_count / 200))

    return {
        "sentiment": sentiment,
        "sentiment_score": round(compound, 2),
        "intent": intent,
        "formality": formality,
        "entities": entities,
        "key_sentences": key_sentences,
        "word_count": word_count,
        "read_time": read_time,
        "sentences_count": len(sentences),
    }