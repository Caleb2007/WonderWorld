# WonderWorld - Smart Attraction Recommendation System

## 🎢 Project Overview

WonderWorld is a web application for a fictional theme park that recommends attractions based on visitor preferences. This is a beginner-friendly Python project built with Streamlit for SUTD's 10.025 Introduction to Programming course.

### Features

- **Interactive Preference Selection**: Visitors can choose:
  - Attraction categories they're interested in
  - Maximum budget
  - Available time
  - Indoor/outdoor preference
- **Attraction recommendations**: Filter by selected categories, maximum price, duration, and environment
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

- Python 3.12 or higher for the currently pinned dependencies. Python 3.15.2 is the version verified in the existing environment.
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
   python -m pip install -r requirements.txt
   ```

The requirements file pins Streamlit and its dependencies. Install them in your own virtual environment, not globally.

### Running the Application

With the virtual environment activated, run:

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501` showing the WonderWorld app.

On Windows, you can also run the app without activating the environment:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The app filters recommendations after the visitor clicks the button. The current implementation is AI-assisted; review the disclosure and verify that the code follows your course's AI-use rules before submission.

## 📚 Project Structure Explanation

### app.py
- Displays the web interface using Streamlit
- Collects preferences and calls `recommend_attractions()` when the visitor clicks the button
- Displays matching attractions, sorting options, and validation/no-match messages

### mylibrary.py
- Contains the `attractions` list with 10 sample attractions
- Each attraction is a dictionary with:
  - `name`: Attraction name
  - `category`: A list using Thrill, Nature, Shows, Great Views, Family, and/or Water Rides
  - `description`: Short description
  - `price`: Cost in dollars
  - `duration`: Estimated time in minutes
  - `environment`: "Indoor" or "Outdoor"
- Contains `recommend_attractions()`, which checks category, price, duration, and environment

## 🛠️ Development Workflow

### Step 1: Understand the Data Structure
Review `mylibrary.py` to understand how attractions are stored.

### Step 2: Implement the Recommendation Logic
Review the `recommend_attractions()` function in `mylibrary.py`:
- Filter attractions by category
- Filter by budget (price <= max budget)
- Filter by duration (duration <= available time)
- Filter by environment preference
- Return matching attractions

The function accepts `(selected_categories, budget, duration, environment)`. The UI calls it after the visitor clicks Recommend.

Suggested pseudocode for your team:

```text
Start an empty list of matches
For each attraction:
    Check whether any of its categories is selected
    Check whether its price is at most the budget
    Check whether its duration is at most the available time
    Check whether the environment matches, or the preference is Any
    If all checks pass, add the attraction to the matches
Return the matches
```

The app uses the same category names in the sample data and multiselect. Sorting uses two small key functions and Python's built-in list sorting.

Some older setup guides describe the original scaffold. Follow this README and the current code when those guides differ.

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

### Setup with GitHub Desktop

1. If the repository has not been published, choose **Publish repository** in GitHub Desktop and select **Keep this code private**. The current repository already has an `origin` remote; do not publish a second copy.
2. On GitHub, open the repository and confirm the **Private** label. If needed, check **Settings > General > Danger Zone > Change repository visibility** before inviting anyone.
3. In the repository's **Settings > Collaborators** (or **Collaborators and teams**), invite both teammates. They must accept their invitations.
4. Each teammate signs in to GitHub Desktop and chooses **File > Clone repository**, selects the private repository, and chooses a local folder.
5. In GitHub Desktop, choose **Repository > Open in Visual Studio Code**. Each teammate creates and activates their own virtual environment, installs the requirements, and runs the app using the instructions above. Never share or commit `.venv`.

### Daily workflow

1. In GitHub Desktop, **Fetch origin**, then **Pull origin** if changes are available.
2. Make changes, review the changed files, and commit with a clear message.
3. **Push origin**. If the remote has changed, fetch and pull before pushing again.
4. Coordinate so only one person edits a particular file at a time. Communicate before changing shared code; pull frequently and commit small related changes. If a conflict occurs, discuss it, resolve it in the affected file, then complete the merge before pushing.

Suggested responsibilities:
- Member 1: `app.py`, the interface, inputs, and result display.
- Member 2: `mylibrary.py`, the attraction data, and recommendation algorithm.
- Member 3: testing, integration, bug identification, documentation, and presentation coordination.

Everyone should review and understand the whole codebase before the interview.

### Development checklist

- [x] Project setup verified
- [x] Virtual environment working on the current computer
- [x] Streamlit working on the current computer
- [x] Git repository configured
- [x] GitHub repository published privately
- [ ] Two teammates invited and invitations accepted
- [ ] All teammates can clone the repository
- [x] Sample attraction dataset uses multiple categories
- [x] Recommendation algorithm connected to the UI (AI-assisted; team review required)
- [x] Budget, duration, category, and environment filters tested
- [x] Any-environment and no-result behavior tested
- [x] Sorting by price and duration tested
- [x] Application startup tested locally
- [ ] Team has reviewed the implementation and confirmed it follows course AI-use rules
- [ ] Presentation completed
- [ ] All members prepared for the interview

## AI Assistance Disclosure

An AI assistant helped update the sample attraction categories, implement the recommendation function, connect it to the Streamlit interface, add sorting, and run tests. The team should review each change, verify the results, and follow the course's rules for AI-assisted work before submission.

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
