import streamlit as st
import webbrowser

# Define all links with their labels, organized by category
links = {
    "Always On": {
        "Personal Email": "https://mail.google.com/mail/u/0/#inbox",
        "Work Email": "https://mail.google.com/mail/u/1/#inbox",
        "Upwork": "https://www.upwork.com/",
        "Github": "https://github.com/",
        "Tasks": "https://tasks.google.com/tasks/",
    },
    "News": {
        "DAWN": "https://www.dawn.com/",
        "Al Jazeera": "https://www.aljazeera.com/",
        "RUN247": "https://run247.com/",
        "iRunFar": "https://www.irunfar.com/",
        "TechCrunch": "https://techcrunch.com/",
        "Hacker News": "https://news.ycombinator.com/",
    },
    "Social Media Check-List": {
        "Whatsapp": "https://web.whatsapp.com/",
        "LinkedIn": "https://linkedin.com/",
        "Goodreads": "https://goodreads.com/",
        "Instagram": "https://www.instagram.com",
        "Twitter": "https://x.com/",
        "YouTube": "https://www.youtube.com/feed/subscriptions",
    },
}
# Custom CSS for better button styling
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        margin-bottom: 10px;
        background-color: #262730;
        color: white;
        border: 1px solid #FF4B4B;
    }
    div.stButton > button:hover {
        border: 1px solid #FF4B4B;
        background-color: #FF4B4B;
        color: white;
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
            # Create a link that looks like a button using markdown
            st.markdown(
                f"""
                <a href="{url}" target="_blank">
                    <button style="
                        width: 100%;
                        padding: 10px;
                        border: 1px solid #FF4B4B;
                        border-radius: 5px;
                        background-color: #262730;
                        color: white;
                        cursor: pointer;
                        margin-bottom: 10px;
                        font-size: 1em;
                        transition: all 0.3s;
                    "
                    onmouseover="this.style.backgroundColor='#FF4B4B'"
                    onmouseout="this.style.backgroundColor='#262730'"
                    >{label}</button>
                </a>
            """,
                unsafe_allow_html=True,
            )

# Add a small footer with instructions
st.markdown(
    """
---
<div style='text-align: center; color: #666;'>
All links will open in a new tab automatically
</div>
""",
    unsafe_allow_html=True,
)
