import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_reply(
    original_email: str,
    analysis: dict,
    tone: str = "Professional",
    custom_instructions: str = "",
    sender_name: str = "",
    your_name: str = ""
) -> str:

    tone_guide = {
        "Professional": "formal, clear, and professional business language",
        "Friendly": "warm, friendly, and approachable while remaining respectful",
        "Concise": "brief and to the point, using bullet points where helpful",
        "Empathetic": "highly empathetic, understanding, and supportive",
        "Assertive": "confident, direct, and assertive",
    }

    system_prompt = f"""You are an expert email communication assistant.
Your task is to write a perfect email reply based on the original email and its analysis.

Tone to use: {tone_guide.get(tone, tone_guide['Professional'])}
Detected intent of original email: {analysis['intent']}
Detected sentiment: {analysis['sentiment']}
Email formality level: {analysis['formality']}

Rules:
- Match the reply length appropriately to the original email
- Address all questions or points raised
- Be helpful and constructive
- Sign off appropriately
{"- Additional instructions: " + custom_instructions if custom_instructions else ""}
{"- Address the sender as: " + sender_name if sender_name else ""}
{"- Sign the reply as: " + your_name if your_name else "- Use an appropriate sign-off"}
- Only output the email reply text, nothing else"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Write a reply to this email:\n\n{original_email}"}
        ]
    )

    return response.choices[0].message.content