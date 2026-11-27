# app.py
# Main Streamlit application for WonderWorld Attraction Recommendation System

import streamlit as st
from mylibrary import recommend_attractions


def get_price(attraction):
    return attraction["price"]


def get_duration(attraction):
    return attraction["duration"]


# Page configuration
st.set_page_config(
    page_title="WonderWorld - Attraction Recommender",
    page_icon="🎢",
    layout="wide"
)

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
    available_categories = [
        "Thrill",
        "Nature",
        "Shows",
        "Great Views",
        "Family",
        "Water Rides"
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
        options=["Indoor", "Outdoor", "Any"],
        index=2,
        help="Choose your environment preference"
    )

# Sorting preference
sort_option = st.selectbox(
    "📊 Sort recommendations by",
    options=["Lowest price", "Shortest duration"]
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
        recommendations = recommend_attractions(
            selected_categories,
            budget,
            duration,
            environment
        )

        if sort_option == "Lowest price":
            recommendations.sort(key=get_price)
        else:
            recommendations.sort(key=get_duration)
        
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
                            st.metric("Categories", ", ".join(attraction['category']))
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
            st.info("No matching attractions found. Try adjusting your preferences.")

# Footer
st.divider()
st.markdown("""
---
**WonderWorld** - Making your theme park experience unforgettable! 🎉

Have fun exploring our attractions!
""")
