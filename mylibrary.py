# mylibrary.py
# This module contains attraction data and recommendation logic for WonderWorld

# Sample attraction data
# Each attraction is a dictionary with the following keys:
# - "name": Attraction name
# - "category": Type of attraction (e.g., "Thrill Ride", "Family Ride", etc.)
# - "description": Short description
# - "price": Cost in dollars
# - "duration": Estimated time in minutes
# - "environment": "Indoor" or "Outdoor"

attractions = [
    {
        "name": "Thunder Mountain",
        "category": "Thrill Ride",
        "description": "An exhilarating roller coaster through a mountain landscape.",
        "price": 25,
        "duration": 5,
        "environment": "Outdoor"
    },
    {
        "name": "Jungle Expedition",
        "category": "Adventure",
        "description": "Explore a mysterious jungle on an exciting ride through exotic scenery.",
        "price": 20,
        "duration": 10,
        "environment": "Outdoor"
    },
    {
        "name": "Ice Palace",
        "category": "Family Ride",
        "description": "A magical journey through a frozen wonderland.",
        "price": 15,
        "duration": 8,
        "environment": "Indoor"
    },
    {
        "name": "Laser Tag Arena",
        "category": "Interactive",
        "description": "Battle your friends in an indoor laser tag competition.",
        "price": 18,
        "duration": 20,
        "environment": "Indoor"
    },
    {
        "name": "Carousel Dreams",
        "category": "Family Ride",
        "description": "A classic carousel ride perfect for all ages.",
        "price": 10,
        "duration": 5,
        "environment": "Indoor"
    },
    {
        "name": "Pirate Cove",
        "category": "Adventure",
        "description": "Sail the seas and discover hidden pirate treasures.",
        "price": 22,
        "duration": 12,
        "environment": "Outdoor"
    },
    {
        "name": "Space Station",
        "category": "Sci-Fi",
        "description": "Travel through outer space in an immersive simulation.",
        "price": 30,
        "duration": 15,
        "environment": "Indoor"
    },
    {
        "name": "Water Splash Park",
        "category": "Water Ride",
        "description": "Cool off with exciting water slides and splash zones.",
        "price": 20,
        "duration": 60,
        "environment": "Outdoor"
    },
    {
        "name": "Mirror Maze",
        "category": "Interactive",
        "description": "Navigate through a mind-bending maze of mirrors.",
        "price": 12,
        "duration": 15,
        "environment": "Indoor"
    },
    {
        "name": "Mega Drop",
        "category": "Thrill Ride",
        "description": "Experience the ultimate adrenaline rush with this free-fall ride.",
        "price": 28,
        "duration": 3,
        "environment": "Outdoor"
    }
]


def recommend_attractions(selected_categories, budget, duration, environment):
    """
    Recommend attractions based on user preferences.
    
    Parameters:
    - selected_categories: List of selected attraction categories (e.g., ["Thrill Ride", "Family Ride"])
    - budget: Maximum budget in dollars
    - duration: Available time in minutes
    - environment: "Indoor", "Outdoor", or "Both"
    
    Returns:
    - A list of recommended attractions that match the criteria
    
    TODO: IMPLEMENT THIS FUNCTION
    - Filter attractions by selected categories
    - Filter by budget (price <= budget)
    - Filter by available duration (estimated duration <= available duration)
    - Filter by environment preference
    - Return the filtered list of attractions
    
    Hints:
    1. Use loops to go through the attractions list
    2. Use if statements to check each condition
    3. Add matching attractions to a new list
    4. Return the results list
    """
    pass


# TODO: Add any additional helper functions as needed
# Examples of functions you might want to create:
# - get_all_categories(): Returns unique categories from attractions
# - filter_by_price(max_price): Returns attractions within a price range
# - filter_by_duration(max_duration): Returns attractions within time limit
