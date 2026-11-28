# mylibrary.py
# This module contains attraction data and recommendation logic for WonderWorld

# Sample attraction data
# Each attraction is a dictionary with the following keys:
# - "name": Attraction name
# - "category": A list of attraction categories
# - "description": Short description
# - "price": Cost in dollars
# - "duration": Estimated time in minutes
# - "environment": "Indoor" or "Outdoor"

attractions = [
    {
        "name": "Thunder Mountain",
        "category": ["Thrill", "Great Views"],
        "description": "An exhilarating roller coaster through a mountain landscape.",
        "price": 25,
        "duration": 5,
        "environment": "Outdoor"
    },
    {
        "name": "Jungle Expedition",
        "category": ["Nature", "Family"],
        "description": "Explore a mysterious jungle on an exciting ride through exotic scenery.",
        "price": 20,
        "duration": 10,
        "environment": "Outdoor"
    },
    {
        "name": "Ice Palace",
        "category": ["Family", "Shows"],
        "description": "A magical journey through a frozen wonderland.",
        "price": 15,
        "duration": 8,
        "environment": "Indoor"
    },
    {
        "name": "Laser Tag Arena",
        "category": ["Thrill", "Family"],
        "description": "Battle your friends in an indoor laser tag competition.",
        "price": 18,
        "duration": 20,
        "environment": "Indoor"
    },
    {
        "name": "Carousel Dreams",
        "category": ["Family"],
        "description": "A classic carousel ride perfect for all ages.",
        "price": 10,
        "duration": 5,
        "environment": "Indoor"
    },
    {
        "name": "Pirate Cove",
        "category": ["Nature", "Family"],
        "description": "Sail the seas and discover hidden pirate treasures.",
        "price": 22,
        "duration": 12,
        "environment": "Outdoor"
    },
    {
        "name": "Space Station",
        "category": ["Shows", "Great Views"],
        "description": "Travel through outer space in an immersive simulation.",
        "price": 30,
        "duration": 15,
        "environment": "Indoor"
    },
    {
        "name": "Water Splash Park",
        "category": ["Water Rides", "Family"],
        "description": "Cool off with exciting water slides and splash zones.",
        "price": 20,
        "duration": 60,
        "environment": "Outdoor"
    },
    {
        "name": "Mirror Maze",
        "category": ["Family"],
        "description": "Navigate through a mind-bending maze of mirrors.",
        "price": 12,
        "duration": 15,
        "environment": "Indoor"
    },
    {
        "name": "Mega Drop",
        "category": ["Thrill", "Great Views"],
        "description": "Experience the ultimate adrenaline rush with this free-fall ride.",
        "price": 28,
        "duration": 3,
        "environment": "Outdoor"
    }
]


def recommend_attractions(selected_categories, budget, duration, environment):
    """
    Return attractions matching the visitor's preferences.
    
    Parameters:
    - selected_categories: Categories selected by the visitor
    - budget: Maximum price for one attraction
    - duration: Maximum time for one attraction, in minutes
    - environment: "Indoor", "Outdoor", or "Any"
    
    Returns a list of attractions matching every preference.
    """
    recommendations = []

    for attraction in attractions:
        category_matches = False

        for selected_category in selected_categories:
            if selected_category in attraction["category"]:
                category_matches = True

        environment_matches = (
            environment == "Any"
            or attraction["environment"] == environment
        )

        if (
            category_matches
            and attraction["price"] <= budget
            and attraction["duration"] <= duration
            and environment_matches
        ):
            recommendations.append(attraction)

    return recommendations
