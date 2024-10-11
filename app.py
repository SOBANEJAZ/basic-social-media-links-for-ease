import streamlit as st

st.title("Social Media & AI Tools Checker")

# Define all links with their labels, organized by category
links = {
    "Email & Work": {
        "Personal Email": "https://mail.google.com/mail/u/0/#inbox",
        "Work Email": "https://mail.google.com/mail/u/1/#inbox",
        "Github": "https://github.com/",
        "LinkedIn": "https://linkedin.com/",
        "Upwork": "https://www.upwork.com/",
    },
    "News": {
        "Reuters": "https://www.reuters.com/",
        "Verge": "https://www.theverge.com/"},
    "AI Tools": {
        "ChatGPT": "https://chatgpt.com/",
        "Claude": "https://claude.ai/",
        "Groq": "https://groq.com/",
        "Perplexity": "https://www.perplexity.ai/",
        "Gemini": "https://gemini.google.com/app",
    },
    "Liesure + Social Media": {
        "Instagram": "https://www.instagram.com/",
        "Goodreads": "https://goodreads.com/",
        "Robin Waldun": "https://www.youtube.com/@RCWaldun/videos",
        "YouTube": "https://www.youtube.com/feed/subscriptions",
    },
}

# Custom CSS to style the buttons and categories
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        margin-bottom: 10px;
    }
    .category-header {
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #ff4b4b;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Process each category
for category, category_links in links.items():
    # Add category header
    st.markdown(f"<p class='category-header'>{category}</p>", unsafe_allow_html=True)

    # Create three columns for this category
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]

    # Distribute buttons across three columns within this category
    for index, (label, url) in enumerate(category_links.items()):
        with columns[index % 3]:
            if st.button(label, key=f"{category}-{label}"):
                js = f"""
                <script>
                    window.open('{url}', '_blank').focus();
                </script>
                """
                st.markdown(js, unsafe_allow_html=True)
                st.markdown(
                    f"[Click here if the page doesn't open automatically]({url})"
                )

    # Add some space between categories
    st.markdown("<br>", unsafe_allow_html=True)
