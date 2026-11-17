# 🚀 QUICK START GUIDE - WonderWorld Project

This is the fastest way to get up and running with WonderWorld!

## ⚡ 5-Minute Setup (For Team Members)

### 1. Clone/Get the Project
```bash
# If cloning from GitHub:
git clone <repository-url>
cd WonderWorld
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
.venv\Scripts\activate.bat
```

You'll see `(.venv)` appear at the start of your terminal line when activated.

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the App
```bash
streamlit run app.py
```

That's it! Your browser will open to http://localhost:8501

## 📋 The Three Files You Need to Know

### 1. `app.py` - The User Interface
- Streamlit components (buttons, sliders, input fields)
- The "look and feel" of the app
- **Status:** ✅ Complete - Don't need to change this much
- **Your role:** Understand how it calls functions from `mylibrary.py`

### 2. `mylibrary.py` - The Logic
- Attraction data (10 sample attractions)
- `recommend_attractions()` function - **THIS IS WHAT YOU NEED TO IMPLEMENT**
- **Status:** ⚠️ Needs implementation
- **Your role:** Write the filtering logic

### 3. `requirements.txt` - Dependencies
- Lists all Python packages needed
- **Status:** ✅ Complete - Don't change this
- **Your role:** Run `pip install -r requirements.txt` when setting up

## 🎯 What You Need to Implement

### The Task: Complete `recommend_attractions()` Function

**Location:** `mylibrary.py`, around line 70

**Input Parameters:**
- `selected_categories` - List of categories user chose
- `budget` - Maximum money to spend
- `duration` - Maximum time available
- `environment` - "Indoor", "Outdoor", or "Both"

**What it should do:**
Return a list of attractions that match ALL of these criteria:
1. ✅ Category is in the selected categories
2. ✅ Price is less than or equal to budget
3. ✅ Duration is less than or equal to available time
4. ✅ Environment matches the preference

**Example:**
```
User selects:
- Categories: ["Family Ride", "Adventure"]
- Budget: $25
- Duration: 20 minutes
- Environment: "Outdoor"

Expected result: Only outdoor Family Rides or Adventures that cost ≤$25 and take ≤20 minutes
```

## 📝 Implementation Hints

### Approach:
1. Create an empty list to store results
2. Loop through each attraction in the `attractions` list
3. Check if it matches the criteria (category, budget, time, environment)
4. If it matches all criteria, add it to the results list
5. Return the results list

### Pseudocode:
```python
def recommend_attractions(selected_categories, budget, duration, environment):
    results = []  # Start with empty list
    
    for attraction in attractions:
        # Check if category matches
        if attraction['category'] in selected_categories:
            
            # Check if price is within budget
            if attraction['price'] <= budget:
                
                # Check if duration is acceptable
                if attraction['duration'] <= duration:
                    
                    # Check if environment matches
                    if (environment == "Both" or 
                        attraction['environment'] == environment):
                        
                        # All criteria match! Add to results
                        results.append(attraction)
    
    return results
```

## 🧪 Testing Your Implementation

After you implement the function:

1. Run the app: `streamlit run app.py`
2. Select some categories
3. Set a budget
4. Set available time
5. Choose indoor/outdoor preference
6. Click "Recommend Attractions"
7. Verify only matching attractions appear

### Test Cases to Try:

**Test 1: Everything matches**
- Categories: All three (or mix)
- Budget: $50
- Duration: 60 minutes
- Environment: Both
- Expected: Most or all attractions should appear

**Test 2: Very restrictive**
- Categories: Just one
- Budget: $15
- Duration: 10 minutes
- Environment: Indoor
- Expected: Only a few attractions (or maybe none)

**Test 3: No selections**
- Categories: None selected
- Expected: Should show warning message (already in app.py)

**Test 4: Impossible criteria**
- Budget: $5
- Duration: 2 minutes
- Expected: No results (should show "no matches" message)

## 🔧 Troubleshooting

### "streamlit: command not found"
→ Virtual environment not activated. Check for `(.venv)` in terminal.

### "ModuleNotFoundError: No module named 'streamlit'"
→ Run `pip install -r requirements.txt`

### App crashes when clicking "Recommend"
→ Check the terminal output. Python errors will be printed there.

### Only see empty page in browser
→ Check that you saved the file. Also check terminal for errors.

## 💡 Code Quality Tips

When implementing `recommend_attractions()`:

✅ **DO:**
- Use clear variable names
- Add comments explaining your logic
- Test frequently
- Follow the hints provided
- Ask for help if stuck

❌ **DON'T:**
- Copy complex code you don't understand
- Skip testing
- Ignore error messages
- Change files you don't need to change

## 🤝 Working as a Team

### Task Division Example:
- **Person A:** Implements `recommend_attractions()` function
- **Person B:** Tests the function thoroughly
- **Person C:** Handles GitHub (branches, merges, commits)

### Collaboration Steps:
1. Create feature branch: `git checkout -b feature/implement-recommendations`
2. Implement the function
3. Test it locally
4. Commit: `git add mylibrary.py && git commit -m "Implement recommendation logic"`
5. Push: `git push origin feature/implement-recommendations`
6. Create Pull Request for team review
7. Merge after approval

## 📚 Reference - How Attraction Data Looks

```python
{
    "name": "Thunder Mountain",
    "category": "Thrill Ride",
    "description": "An exhilarating roller coaster...",
    "price": 25,           # In dollars
    "duration": 5,         # In minutes
    "environment": "Outdoor"  # "Indoor" or "Outdoor"
}
```

Available categories in the sample data:
- Thrill Ride
- Family Ride
- Adventure
- Interactive
- Water Ride
- Sci-Fi

## ✅ Checklist Before Submitting

- [ ] Virtual environment created and activated
- [ ] `pip install -r requirements.txt` ran successfully
- [ ] `streamlit run app.py` starts without errors
- [ ] `recommend_attractions()` function is implemented
- [ ] Tested with multiple preference combinations
- [ ] No errors appear in terminal during testing
- [ ] Code is clean with comments
- [ ] Pushed to GitHub
- [ ] All team members' names are documented
- [ ] Project is ready for submission

## 🎓 Learning Outcomes

After completing this project, you'll understand:
- ✅ How to work with Python lists and dictionaries
- ✅ How to use loops and conditional statements
- ✅ How to write functions that solve problems
- ✅ How to build web interfaces with Streamlit
- ✅ How to collaborate using Git and GitHub
- ✅ How to test and debug your code

## 🆘 Still Stuck?

1. **Check README.md** for detailed explanations
2. **Check SETUP_COMPLETE.md** for setup troubleshooting
3. **Check VS_CODE_SETUP.md** for editor tips
4. **Read the TODO comments** in the code
5. **Look at the pseudocode** above
6. **Ask your teammates** for help
7. **Attend office hours** if available

---

**You've got this! Build something amazing! 🚀🎢**
