from textblob import TextBlob
import re

def analyze_email(email_text: str) -> dict:
    """Lightweight email analysis for deployment-safe version."""

    blob = TextBlob(email_text)

    # Sentiment
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😟"
    else:
        sentiment = "Neutral 😐"

    # Intent detection
    text_lower = email_text.lower()
    intent = "General Inquiry"

    if any(w in text_lower for w in ["complaint", "issue", "problem"]):
        intent = "Complaint"
    elif any(w in text_lower for w in ["thank", "appreciate"]):
        intent = "Appreciation"
    elif any(w in text_lower for w in ["request", "please", "could you", "can you"]):
        intent = "Request"
    elif any(w in text_lower for w in ["question", "how", "what", "why", "?"]):
        intent = "Question"
    elif "follow up" in text_lower:
        intent = "Follow-up"

    # Basic stats
    word_count = len(email_text.split())

    return {
        "sentiment": sentiment,
        "intent": intent,
        "word_count": word_count
    }

