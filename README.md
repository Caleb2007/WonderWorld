# WonderWorld - Smart Attraction Recommendation System

## 🎢 Project Overview

WonderWorld is a web application for a fictional theme park that recommends attractions based on visitor preferences. This is a beginner-friendly Python project built with Streamlit for SUTD's 10.025 Introduction to Programming course.

### Features

- **Interactive Preference Selection**: Visitors can choose:
  - Attraction categories they're interested in
  - Maximum budget
  - Available time
  - Indoor/outdoor preference
- **Smart Recommendations**: The app filters attractions based on all preferences
- **Simple Design**: Clean, easy-to-use interface perfect for beginners

## 📋 Project Structure

```
WonderWorld/
├── .venv/                 # Virtual environment (do not commit)
├── app.py                 # Main Streamlit application
├── mylibrary.py           # Attraction data and recommendation logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system
- Windows, macOS, or Linux

### Installation

1. **Clone or navigate to the WonderWorld directory:**
   ```bash
   cd WonderWorld
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   
   **On Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **On macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

With the virtual environment activated, run:

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501` showing the WonderWorld app.

## 📚 Project Structure Explanation

### app.py
- Displays the web interface using Streamlit
- Collects user preferences (categories, budget, duration, environment)
- Displays recommendations or a "no matches" message
- Contains TODO comments for integration with mylibrary.py

### mylibrary.py
- Contains the `attractions` list with 10 sample attractions
- Each attraction is a dictionary with:
  - `name`: Attraction name
  - `category`: Type of attraction
  - `description`: Short description
  - `price`: Cost in dollars
  - `duration`: Estimated time in minutes
  - `environment`: "Indoor" or "Outdoor"
- Contains the `recommend_attractions()` function that YOU need to implement

## 🛠️ Development Workflow

### Step 1: Understand the Data Structure
Review `mylibrary.py` to understand how attractions are stored.

### Step 2: Implement the Recommendation Logic
Complete the `recommend_attractions()` function in `mylibrary.py`:
- Filter attractions by category
- Filter by budget (price <= max budget)
- Filter by duration (duration <= available time)
- Filter by environment preference
- Return matching attractions

### Step 3: Test Your Implementation
Run the app and test different preference combinations.

## 🎓 Learning Concepts

This project reinforces:
- Lists and dictionaries in Python
- For loops and nested loops
- If/else statements
- Functions with parameters and return values
- Streamlit basics for web interfaces
- GitHub collaboration

## 💡 Tips for Implementation

1. **Start Simple**: First filter by just one criterion, then add more
2. **Test Incrementally**: After each filter, test to see if it works
3. **Use Meaningful Variable Names**: Make your code easy to understand
4. **Add Comments**: Explain what your code does
5. **Collaborate**: Use GitHub to work together with your team

## 🔧 Troubleshooting

### Issue: Virtual environment won't activate
- Make sure you're in the correct directory
- Try using Command Prompt instead of PowerShell if on Windows
- Check that .venv exists in your project folder

### Issue: Streamlit not found
- Confirm virtual environment is activated (you should see `(.venv)` in your terminal)
- Run `pip install streamlit` again
- Try `pip list` to see installed packages

### Issue: App crashes when running
- Check that all imports in app.py can be found
- Ensure mylibrary.py has valid Python syntax
- Check browser console for error messages

## 📖 Streamlit Documentation

For more information about Streamlit components:
- Official docs: https://docs.streamlit.io/
- Useful components:
  - `st.multiselect()` - For category selection
  - `st.number_input()` - For budget and duration
  - `st.button()` - For the recommend button
  - `st.metric()` - For displaying key information

## 👥 Team Collaboration

### Using GitHub

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd WonderWorld
   ```

2. **Create your feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "Add your descriptive message"
   ```

4. **Push to your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** on GitHub for team review

## 📝 Assignment Requirements

- ✅ Python and Streamlit only
- ✅ Beginner-friendly code with clear variable names
- ✅ Meaningful comments
- ✅ No unnecessary technologies or advanced techniques
- ✅ GitHub-ready project structure
- ✅ Simple rule-based recommendation (no AI/ML)
- ✅ Team collaboration via GitHub

## 🎉 What's Next?

After implementing the basic recommendation system, consider:
- Adding more attractions to the database
- Implementing additional filter options
- Improving the UI design
- Adding a favorites feature
- Creating category suggestions

## 📄 License

This project is for educational purposes as part of SUTD's 10.025 Introduction to Programming course.

---

**Happy coding! 🚀**
