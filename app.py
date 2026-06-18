import streamlit as st
from email_analyzer import analyze_email
from reply_generator import generate_reply

# Page config
st.set_page_config(
    page_title="AI Email Reply Agent",
    page_icon="✉️",
    layout="wide"
)

# Header
st.title("✉️ AI Email Reply Agent")
st.markdown("*Powered by Claude AI + NLP — Analyze emails and generate smart replies instantly*")
st.divider()

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    tone = st.selectbox(
        "Reply Tone",
        ["Professional", "Friendly", "Concise", "Empathetic", "Assertive"],
        index=0
    )
    your_name = st.text_input("Your Name (for sign-off)", placeholder="e.g. Sarah")
    sender_name = st.text_input("Sender's Name", placeholder="e.g. John")
    custom_instructions = st.text_area(
        "Custom Instructions (optional)",
        placeholder="e.g. Mention we'll respond within 2 business days...",
        height=100
    )
    st.divider()
    st.markdown("**How it works:**")
    st.markdown("1. 📥 Paste the email\n2. 🔍 Analyze with NLP\n3. 🤖 Generate AI reply\n4. ✏️ Edit & copy")

# Main layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📥 Original Email")
    email_input = st.text_area(
        "Paste the email you received:",
        height=280,
        placeholder="Dear Team,\n\nI wanted to follow up on our discussion last week regarding...",
        label_visibility="collapsed"
    )

    analyze_btn = st.button("🔍 Analyze & Generate Reply", type="primary", use_container_width=True)

    # NLP Analysis results
    if "analysis" in st.session_state:
        a = st.session_state.analysis
        st.subheader("🧠 NLP Analysis")

        m1, m2, m3 = st.columns(3)
        m1.metric("Sentiment", a["sentiment"])
        m2.metric("Intent", a["intent"])
        m3.metric("Formality", a["formality"])

        m4, m5 = st.columns(2)
        m4.metric("Word Count", a["word_count"])
        m5.metric("Read Time", f"{a['read_time']} min")

        if a["entities"]:
            st.markdown("**🏷️ Detected Entities:**")
            entity_text = " | ".join([f"`{e[0]}` ({e[1]})" for e in a["entities"][:8]])
            st.markdown(entity_text)

        if a["key_sentences"]:
            with st.expander("📌 Key Sentences"):
                for s in a["key_sentences"]:
                    st.markdown(f"- {s}")

with col2:
    st.subheader("🤖 AI Generated Reply")

    if analyze_btn:
        if not email_input.strip():
            st.error("Please paste an email first!")
        else:
            with st.spinner("🔍 Analyzing email..."):
                analysis = analyze_email(email_input)
                st.session_state.analysis = analysis

            with st.spinner("✍️ Generating reply..."):
                reply = generate_reply(
                    original_email=email_input,
                    analysis=analysis,
                    tone=tone,
                    custom_instructions=custom_instructions,
                    sender_name=sender_name,
                    your_name=your_name
                )
                st.session_state.reply = reply

    if "reply" in st.session_state:
        edited_reply = st.text_area(
            "Edit your reply:",
            value=st.session_state.reply,
            height=320,
            label_visibility="collapsed"
        )

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔄 Regenerate", use_container_width=True):
                with st.spinner("Regenerating..."):
                    st.session_state.reply = generate_reply(
                        original_email=email_input,
                        analysis=st.session_state.analysis,
                        tone=tone,
                        custom_instructions=custom_instructions,
                        sender_name=sender_name,
                        your_name=your_name
                    )
                st.rerun()
        with c2:
            st.download_button(
                "💾 Download Reply",
                data=edited_reply,
                file_name="email_reply.txt",
                mime="text/plain",
                use_container_width=True
            )

        st.success("✅ Reply ready! Edit above and copy to your email client.")
    else:
        st.info("👈 Paste an email and click **Analyze & Generate Reply** to get started.")