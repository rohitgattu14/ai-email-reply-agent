AI Email Reply Generator

An AI-powered email assistant that automatically generates context-aware and professional email replies using the Groq LLM API. The system analyzes incoming emails to detect intent, sentiment, and key information, then produces a structured response using an LLM-based generation pipeline. A Streamlit web interface is used to provide an interactive user experience.

Live Demo

https://ai-email-reply-agentrohit.streamlit.app/

Project Overview

This project simulates a real-world email automation assistant designed to reduce manual effort in drafting email responses. It combines lightweight NLP techniques with a large language model (Groq) to understand email context and generate meaningful replies.

The system performs three main tasks:

Email analysis (sentiment, intent, basic metadata)
Context extraction
AI-based response generation using LLM
Key Features
1. AI-Powered Email Reply Generation
Uses Groq LLM API to generate human-like email responses
Produces context-aware replies based on user input
2. Email Analysis Module
Detects email intent (Request, Complaint, Appreciation, Question, Follow-up)
Performs sentiment analysis (Positive, Neutral, Negative)
Extracts basic metadata such as word count and structure
3. Streamlit Web Interface
Simple and interactive UI for input and output
Real-time email processing and response generation
4. Secure API Key Handling
Uses environment variables (.env file locally)
Prevents hardcoding of sensitive credentials
Tech Stack
Python 3.x
Streamlit
Groq API (LLM inference)
TextBlob (sentiment analysis)
python-dotenv (environment variable management)
How It Works
Step 1: User Input

The user provides an email text via the Streamlit UI.

Step 2: Email Analysis

The system analyzes:

Sentiment (positive, neutral, negative)
Intent classification (request, complaint, etc.)
Basic text statistics
Step 3: Context Building

The analyzed metadata is combined with the original email text.

Step 4: LLM Processing

Groq LLM generates a structured, professional email reply.

Step 5: Output

The final response is displayed in the web interface.
