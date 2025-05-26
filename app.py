import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # Used for dummy data in placeholder chart
import time # For simulating loading spinner

# --- Page Configuration ---
st.set_page_config(
    page_title="Sentify AI: Your Smart Sentiment Analyzer",
    page_icon="✨", # A more eye-catching icon
    layout="wide", # Use wide layout for more space
    initial_sidebar_state="expanded",
)

# --- Custom CSS for a polished look and improved metric display ---
st.markdown(
    """
    <style>
    /* General Styling */
    .reportview-container {
        background: #f0f2f6; /* Light gray background */
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1A2E44; /* Darker, slightly blue headings */
        font-family: 'Segoe UI', sans-serif;
    }
    p, li, div {
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #6C63FF; /* Vibrant purple */
        color: white;
        padding: 12px 30px; /* Larger padding */
        border-radius: 10px; /* More rounded corners */
        border: none;
        cursor: pointer;
        font-size: 20px; /* Larger font */
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease; /* Smooth transitions */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Subtle shadow */
    }
    .stButton>button:hover {
        background-color: #5B54D9; /* Darker purple on hover */
        transform: translateY(-2px); /* Slight lift effect */
    }
    
    /* Input Fields Styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px; /* More rounded corners */
        padding: 12px; /* More padding */
        border: 2px solid #D1D9E6; /* Slightly thicker, softer border */
        box-shadow: inset 2px 2px 5px #B8C0D3, inset -3px -3px 7px #FFFFFF; /* Neumorphic inset shadow */
        font-size: 16px;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #6C63FF; /* Highlight border on focus */
        box-shadow: 0 0 0 2px rgba(108, 99, 255, 0.5); /* Glowing effect on focus */
        outline: none;
    }

    /* Custom classes for larger fonts and metrics */
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1A2E44;
    }
    .metric-value-large {
        font-size: 42px !important; /* Even larger for more impact */
        font-weight: bold;
        line-height: 1.2;
        margin-top: 5px;
        margin-bottom: 5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .metric-label-bold {
        font-size: 20px !important; /* Slightly larger label */
        font-weight: bold;
        color: #555; /* Slightly softer label color */
        margin-bottom: 0px !important; /* Remove default paragraph margin */
    }
    
    /* Alerts and expanders */
    .stAlert {
        border-radius: 10px; /* More rounded corners for alerts */
        padding: 18px; /* More padding */
        margin-top: 15px; /* More space above */
        margin-bottom: 15px; /* More space below */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Subtle shadow for alerts */
    }
    .stAlert p {
        font-size: 1.2em; /* Larger text in alerts */
        margin-bottom: 0px;
    }
    /* Specific styling for the sentiment alert to control its content appearance */
    /* This style will center the *default text* within the alert. */
    .stAlert div[data-testid="stMarkdownContainer"] {
        display: flex;
        justify-content: center; /* Center the text horizontally */
        align-items: center; /* Center vertically */
        height: 100%; /* Take full height of the alert box */
    }
    .stExpander {
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .stExpander div[data-testid="stExpanderChevron"] {
        font-size: 1.5em; /* Larger chevron icon */
    }

    /* Sidebar specific styling */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa; /* Slightly off-white for sidebar */
        padding-top: 2rem;
        box-shadow: 2px 0 5px rgba(0,0,0,0.1);
    }
    section[data-testid="stSidebar"] .stSelectbox {
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Sentiment Analysis Function ---
@st.cache_data # Cache the function to improve performance
def analyze_sentiment(text):
    # Simulate a small delay for the loading spinner
    time.sleep(0.5) 
    if not text:
        return "N/A", 0.0

    analysis = TextBlob(text)

    # Determine sentiment label (adjusting thresholds slightly for clearer categories)
    if analysis.sentiment.polarity > 0.2: # More strictly positive
        sentiment_label = "Positive"
    elif analysis.sentiment.polarity < -0.2: # More strictly negative
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_label, analysis.sentiment.polarity

# --- Placeholder Function for Other ML Models ---
def show_placeholder_content(feature_name):
    st.markdown(f"<div class='big-font'>🚧 {feature_name} - Coming Soon! 🚧</div>", unsafe_allow_html=True)
    st.write(f"This section will feature advanced machine learning capabilities for **{feature_name}**.")
    st.info("Stay tuned for updates! We're building exciting new features to empower your insights.")
    
    # Using a placeholder image that looks more like a "coming soon" banner
    st.image("https://via.placeholder.com/800x400/1E90FF/FFFFFF?text=Exciting+AI+Feature+Coming+Soon!", caption=f"{feature_name} Preview", use_column_width=True)
    st.markdown("---")
    
    st.subheader("💡 What to expect from this feature:")
    col_left, col_right = st.columns(2)
    with col_left:
        st.write("✅ State-of-the-art models for superior accuracy")
        st.write("✅ Highly intuitive and interactive Demos")
        st.write("✅ Seamless Integration for effortless use")
    with col_right:
        st.write("✅ Real-time Processing for instant results")
        st.write("✅ Comprehensive Results with detailed insights")
        st.write("✅ User-friendly Interface designed for everyone")
        
    st.markdown("---")
    st.subheader("📊 Glimpse of Future Insights:")
    # Example placeholder chart
    chart_data = {
        'Scenario': ['Optimistic', 'Neutral', 'Pessimistic', 'Growth', 'Decline'],
        'Performance Metric': np.random.randint(20, 150, 5)
    }
    st.bar_chart(chart_data, x='Scenario', y='Performance Metric', color='#6C63FF')
    st.write("This chart is a placeholder to demonstrate potential data visualization and performance tracking capabilities within this upcoming feature.")


# --- Sidebar for Navigation (Our 'Navbar') ---
st.sidebar.title("🚀 Sentify AI Navigation")
st.sidebar.markdown("---")

# Use a selectbox for navigation
selected_feature = st.sidebar.selectbox(
    "Explore AI Features:", # More inviting text
    [
        "Sentiment Analysis",
        "Image Captioning (Soon!)",
        "Text Summarization (Soon!)",
        "Spam Detection (Soon!)",
        "Object Detection (Soon!)",
        "Historical Analysis (Placeholder)" # New Placeholder
    ],
    key="nav_selectbox"
)

st.sidebar.markdown("---")

# Add more interactive elements to sidebar (placeholders)
st.sidebar.subheader("Connect with Us")
st.sidebar.markdown("[🌐 Our Website (Coming Soon)](https://www.example.com)") # Placeholder link
st.sidebar.markdown("[📧 Feedback & Support (Email)](mailto:support@sentify.ai)") # Placeholder email
st.sidebar.markdown("[🐦 Follow us on Twitter (Coming Soon)](https://twitter.com/sentifyai)") # Placeholder link

st.sidebar.markdown("---")
st.sidebar.subheader("About Sentify AI")
st.sidebar.info(
    "**Sentify AI** is designed to provide quick and insightful sentiment analysis. "
    "We're constantly expanding our capabilities to bring you more powerful AI tools. "
    "Built with Streamlit for a seamless user experience, we aim to make AI accessible to everyone."
)
st.sidebar.markdown("---")
st.sidebar.write("© 2025 Sentify AI. All rights reserved.")


# --- Main Content Area based on Selection ---
if selected_feature == "Sentiment Analysis":
    st.title("✨ Sentify AI: Tweet & Text Sentiment Analyzer")
    st.markdown(
        """
        ### Uncover the Emotion Behind the Words!
        Our powerful **Sentiment Analyzer** instantly evaluates any text to tell you whether it expresses a
        **positive**, **negative**, or **neutral** sentiment. Perfect for understanding customer feedback,
        social media trends, or written communication.
        """
    )
    st.markdown("---")

    # --- User Input ---
    st.subheader("✍️ Enter your tweet or any text below for instant analysis:")
    user_input = st.text_area("Text Input", height=180, placeholder="E.g., 'This product is absolutely fantastic and works flawlessly!' or 'I am very disappointed with the slow service and rude staff.'", key="sentiment_input")

    # --- Analyze Button ---
    # Centering the button more effectively
    col_left_spacer, col_analyze_button, col_right_spacer = st.columns([1.5, 2, 1.5]) 
    
    with col_analyze_button:
        # Place the button directly here
        if st.button("Analyze Sentiment Now! 🚀"):
            if user_input:
                # Add a spinner while analysis is running
                with st.spinner('Analyzing sentiment...'):
                    sentiment, polarity = analyze_sentiment(user_input)
                
                st.success("Analysis Complete! Here are your insights:")

                # --- Improved Analysis Result Section ---
                st.markdown("---")
                st.subheader("📊 Your Sentiment Breakdown:")

                # Using larger columns for metrics and customizing their display
                col_sentiment, col_polarity, col_length = st.columns([1.5, 1, 1]) # Column ratios for distribution

                with col_sentiment:
                    st.markdown("<p class='metric-label-bold'>Overall Sentiment:</p>", unsafe_allow_html=True)
                    # CORRECTED: No unsafe_allow_html in st.success/error/info
                    # We display the main sentiment word/emoji in the alert.
                    if sentiment == "Positive":
                        st.success(f"**{sentiment}** 😊")
                    elif sentiment == "Negative":
                        st.error(f"**{sentiment}** 😞")
                    else:
                        st.info(f"**{sentiment}** 😐")

                with col_polarity:
                    st.markdown("<p class='metric-label-bold'>Polarity Score:</p>", unsafe_allow_html=True)
                    # Apply custom styling via markdown for the large value
                    if polarity > 0.1:
                        st.markdown(f"<p class='metric-value-large' style='color:#28a745;'>{polarity:.2f} ⬆️</p>", unsafe_allow_html=True)
                    elif polarity < -0.1:
                        st.markdown(f"<p class='metric-value-large' style='color:#dc3545;'>{polarity:.2f} ⬇️</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p class='metric-value-large' style='color:#6c757d;'>{polarity:.2f} ↔️</p>", unsafe_allow_html=True)
                    st.caption("Score: -1 (Negative) to +1 (Positive)")

                with col_length:
                    st.markdown("<p class='metric-label-bold'>Text Length:</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='metric-value-large'>{len(user_input)} 📏</p>", unsafe_allow_html=True)
                    st.caption("Number of characters")

                st.markdown("---")
                st.write(f"**Original Text:** *{user_input}*")


                # --- Sentiment Visualization ---
                st.markdown("---")
                st.subheader("📈 Visualizing Your Sentiment:")

                # Use an expander for the plot to make the UI cleaner
                with st.expander("Click to View Polarity Chart", expanded=True): # Expanded by default
                    fig, ax = plt.subplots(figsize=(10, 6)) # Increased figure size significantly

                    # Ensure consistent colors with the metrics
                    colors_plot = {'Positive': '#28a745', 'Negative': '#dc3545', 'Neutral': '#6c757d', 'N/A': '#ffc107'}
                    
                    plot_sentiment = sentiment if sentiment in colors_plot else 'N/A'
                    
                    sns.barplot(x=[plot_sentiment], y=[abs(polarity)], palette=[colors_plot[plot_sentiment]], ax=ax)
                    ax.set_ylim(0, 1)
                    ax.set_title("Polarity Magnitude", fontsize=18, fontweight='bold', color='#333')
                    ax.set_ylabel("Absolute Polarity", fontsize=14, color='#555')
                    ax.tick_params(axis='x', labelsize=16, colors='#555')
                    ax.tick_params(axis='y', labelsize=14, colors='#555')
                    
                    # Add value on top of the bar for clarity
                    for p in ax.patches:
                        ax.annotate(f"{abs(polarity):.2f}",
                                   (p.get_x() + p.get_width() / 2., p.get_height()),
                                   ha='center', va='center', xytext=(0, 5),
                                   textcoords='offset points', fontsize=14, color='black', fontweight='bold')

                    # Remove top and right spines for a cleaner look
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    ax.grid(axis='y', linestyle='--', alpha=0.7) # Add subtle horizontal grid lines

                    st.pyplot(fig) # Display the plot

                # --- How it works expander ---
                with st.expander("🤔 How Sentiment Analysis Works (Pro Tips!):"):
                    st.write(
                        "This app utilizes `TextBlob`, a Python library for straightforward Natural Language Processing (NLP). "
                        "It processes your text to calculate a **polarity score** (ranging from -1 to +1) "
                        "and a **subjectivity score** (from 0 to 1, where 0 is objective and 1 is subjective)."
                    )
                    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Sentiment_analysis_spectrum_v2.svg/1200px-Sentiment_analysis_spectrum_v2.svg.png",
                             caption="Sentiment Polarity Spectrum", use_column_width=True)
                    st.markdown("---")
                    st.subheader("💡 Pro Tips for Better Results:")
                    st.write(
                        """
                        1.  **Context is Key:** Sentiment analysis is best when provided with sufficient context. A single word might be ambiguous.
                        2.  **Avoid Sarcasm/Irony:** Automated tools often struggle with sarcasm, as it relies on implied meaning.
                        3.  **Domain-Specific Language:** Sentiment can vary by industry. Tools like this are general-purpose.
                        4.  **Emoji Impact:** While TextBlob can handle some, complex emojis or emoticons might not always contribute perfectly to sentiment scores.
                        """
                    )


            else:
                st.warning("Oops! 📝 Please enter some text into the box above before hitting 'Analyze Sentiment'.")
        
        # Spacers for centering are now handled implicitly by the column structure.

elif selected_feature == "Historical Analysis (Placeholder)":
    st.header("⏳ Historical Analysis Dashboard (Coming Soon!)")
    st.write("This section will allow you to view a history of your past sentiment analyses, track trends, and manage your data.")
    
    st.markdown("---")
    st.subheader("Future Features:")
    st.write("📈 **Interactive Charts:** Visualize sentiment trends over time.")
    st.write("💾 **Save & Load:** Securely store your analyzed texts.")
    st.write("🔍 **Search & Filter:** Easily find past analyses.")
    st.warning("For now, this is a placeholder. Your current analysis is not saved.")
    
    # Dummy chart for historical data
    st.line_chart(np.random.randn(20, 2), use_container_width=True)
    st.info("Imagine this chart showing your sentiment scores over different analysis sessions!")

else:
    # Show placeholder content for other selected features
    show_placeholder_content(selected_feature)

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; color: gray; font-size: 0.9em;'>
        Built with ❤️ using Streamlit | Designed with ✨ by Sentify AI Team
    </p>
    """,
    unsafe_allow_html=True
)