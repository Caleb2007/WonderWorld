# app.py
# Main Streamlit application for WonderWorld Attraction Recommendation System

import streamlit as st
from mylibrary import attractions, recommend_attractions

# Page configuration
st.set_page_config(
    page_title="WonderWorld - Attraction Recommender",
    page_icon="🎢",
    layout="wide"
)

# Rose Garden visual theme
st.markdown("""
<style>
    :root {
        --blush-bg: #FFF7F9;
        --rose-50: #FFF1F5;
        --rose-100: #FDE2EA;
        --rose-200: #F7C8D6;
        --rose-500: #C94F79;
        --rose-600: #AD3E65;
        --rose-700: #91314F;
        --plum: #4A2034;
        --mauve: #806978;
        --border: #E7CDD5;
        --white: #FFFFFF;
    }

    .stApp {
        background: var(--blush-bg);
        color: var(--plum);
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 92% 4%, rgba(201, 79, 121, 0.06), transparent 20rem),
            var(--blush-bg);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1120px;
        padding-top: 2.25rem;
        padding-bottom: 3rem;
    }

    h1 {
        color: var(--plum) !important;
        font-size: clamp(2rem, 4vw, 3.1rem) !important;
        font-weight: 750 !important;
        letter-spacing: -0.035em;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        color: var(--plum) !important;
        font-size: clamp(1.35rem, 2.3vw, 1.75rem) !important;
        font-weight: 700 !important;
        margin-top: 0.25rem !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: var(--mauve);
        line-height: 1.65;
        font-size: 1rem;
    }

    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label {
        color: var(--plum) !important;
        font-size: 0.96rem !important;
        font-weight: 650 !important;
    }

    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input,
    [data-baseweb="select"] > div,
    [data-testid="stTextArea"] textarea {
        background: var(--white) !important;
        color: var(--plum) !important;
        border-color: var(--border) !important;
        border-radius: 12px !important;
    }

    [data-baseweb="tag"] {
        background: var(--rose-100) !important;
        border: 1px solid var(--rose-200) !important;
        color: var(--rose-700) !important;
        border-radius: 999px !important;
    }

    [data-baseweb="tag"] span {
        color: var(--rose-700) !important;
    }

    [data-testid="stRadio"] [role="radiogroup"] label {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 0.55rem 0.8rem;
        margin: 0.15rem 0.25rem 0.15rem 0;
        transition: border-color 160ms ease, background 160ms ease, transform 160ms ease;
    }

    [data-testid="stRadio"] [role="radiogroup"] label:has([aria-checked="true"]) {
        background: var(--rose-100);
        border-color: var(--rose-500);
        color: var(--rose-700);
    }

    [data-testid="stRadio"] [role="radiogroup"] label:hover {
        border-color: var(--rose-500);
        transform: translateY(-1px);
    }

    [data-testid="stRadio"] [role="radiogroup"] label:active {
        transform: translateY(0);
    }

    div.stButton > button {
        background: var(--rose-500);
        color: var(--white) !important;
        border: 1px solid var(--rose-500);
        border-radius: 12px;
        min-height: 3.05rem;
        font-size: 1rem;
        font-weight: 750;
        box-shadow: 0 8px 18px rgba(173, 62, 101, 0.16);
        transition: background 160ms ease, border-color 160ms ease,
                    transform 160ms ease, box-shadow 160ms ease;
    }

    div.stButton > button:hover {
        background: var(--rose-600);
        border-color: var(--rose-600);
        color: var(--white) !important;
        transform: translateY(-2px);
        box-shadow: 0 11px 22px rgba(173, 62, 101, 0.22);
    }

    div.stButton > button:active {
        background: var(--rose-700);
        border-color: var(--rose-700);
        transform: translateY(0);
        box-shadow: 0 4px 10px rgba(173, 62, 101, 0.18);
    }

    div.stButton > button:focus-visible {
        outline: 3px solid rgba(201, 79, 121, 0.28);
        outline-offset: 3px;
    }

    [data-testid="stAlert"] {
        border-radius: 14px;
        border: 1px solid var(--border);
    }

    [data-testid="stAlert"]:has([data-testid="stIconWarning"]) {
        background: #FFF8EA;
        color: #6E4A20;
        border-color: #ECD9B6;
    }

    [data-testid="stAlert"]:has([data-testid="stIconSuccess"]) {
        background: var(--rose-50);
        color: var(--rose-700);
        border-color: var(--rose-200);
    }

    [data-testid="stAlert"]:has([data-testid="stIconInfo"]) {
        background: #FFF9FB;
        color: var(--plum);
        border-color: var(--border);
    }

    [data-testid="stMetricLabel"] p,
    [data-testid="stMetricLabel"] label {
        color: var(--mauve) !important;
        font-size: 0.78rem !important;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    [data-testid="stMetricValue"] {
        color: var(--rose-700) !important;
        font-size: 1.18rem !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.90);
        border: 1px solid var(--border) !important;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(122, 68, 91, 0.055);
        padding: 1.25rem 1.35rem;
        margin-bottom: 1rem;
        animation: rose-card-enter 360ms ease-out both;
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, var(--border), transparent);
        margin: 1.65rem 0;
    }

    [data-testid="stMarkdownContainer"] strong {
        color: var(--plum);
    }

    @keyframes rose-card-enter {
        from {
            opacity: 0;
            transform: translateY(8px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @media (max-width: 768px) {
        [data-testid="stMainBlockContainer"] {
            padding: 1.25rem 1rem 2.25rem;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            padding: 1rem;
        }

        [data-testid="stRadio"] [role="radiogroup"] {
            display: flex;
            flex-wrap: wrap;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        [data-testid="stVerticalBlockBorderWrapper"],
        div.stButton > button,
        [data-testid="stRadio"] [role="radiogroup"] label {
            animation: none !important;
            transition: none !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🎢 WonderWorld - Smart Attraction Recommender")
st.markdown("""
Welcome to **WonderWorld**! Our theme park has exciting attractions for everyone.

Not sure which rides to visit? Tell us your preferences and we'll recommend the perfect attractions just for you!
""")

# Divider
st.divider()

# Section 1: User Preferences Input
st.header("📋 Tell Us Your Preferences")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    # Category selection using multiselect
    # TODO: Extract unique categories from attractions
    # Hint: Create a list of all unique categories available
    available_categories = [
        "Thrill Ride",
        "Family Ride",
        "Adventure",
        "Interactive",
        "Water Ride",
        "Sci-Fi"
    ]
    
    selected_categories = st.multiselect(
        "🎯 What types of attractions interest you?",
        options=available_categories,
        default=[],
        help="Select one or more categories that appeal to you"
    )
    
    # Budget input
    budget = st.number_input(
        "💰 What's your maximum budget? (in dollars)",
        min_value=0,
        max_value=200,
        value=50,
        step=5,
        help="Select the maximum amount you want to spend"
    )

with col2:
    # Duration input
    duration = st.number_input(
        "⏱️ How much time do you have? (in minutes)",
        min_value=0,
        max_value=480,
        value=60,
        step=10,
        help="Select how many minutes you have to spend"
    )
    
    # Environment preference
    environment = st.radio(
        "🌳 Do you prefer indoor or outdoor attractions?",
        options=["Indoor", "Outdoor", "Both"],
        index=2,
        help="Choose your environment preference"
    )

# Divider
st.divider()

# Section 2: Recommendation Button
st.header("🔍 Get Recommendations")

if st.button("🎯 Recommend Attractions", use_container_width=True):
    # Validation: Check if user selected at least one category
    if not selected_categories:
        st.warning("⚠️ Please select at least one attraction category to get recommendations.")
    else:
        # TODO: Call recommend_attractions() function
        # Pass the user preferences as parameters
        # Store the results in a variable
        
        recommendations = []  # TODO: Replace with actual function call
        
        if recommendations:
            # Display results
            st.success(f"✅ Found {len(recommendations)} matching attractions!")
            st.divider()
            
            # Display each recommendation
            for i, attraction in enumerate(recommendations, 1):
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.subheader(f"{i}. {attraction['name']}")
                        st.write(f"**Description:** {attraction['description']}")
                        
                        # Display details in columns
                        detail_col1, detail_col2, detail_col3 = st.columns(3)
                        with detail_col1:
                            st.metric("Category", attraction['category'])
                        with detail_col2:
                            st.metric("Price", f"${attraction['price']}")
                        with detail_col3:
                            st.metric("Duration", f"{attraction['duration']} min")
                        
                        st.write(f"**Environment:** {attraction['environment']}")
                    
                    with col2:
                        if attraction['environment'] == 'Indoor':
                            st.write("🏢")
                        else:
                            st.write("🌳")
        else:
            # No results message
            st.info(
                "😕 No attractions match your preferences. "
                "Try adjusting your budget, duration, or selecting different categories!"
            )

# Footer
st.divider()
st.markdown("""
---
**WonderWorld** - Making your theme park experience unforgettable! 🎉

Have fun exploring our attractions!
""")
