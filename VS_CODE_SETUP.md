# VS Code Setup Guide for WonderWorld Project

This guide explains how to properly set up VS Code to work with the WonderWorld project.

## 🔧 Opening the Project in VS Code

1. **Open VS Code**
2. **Click:** File → Open Folder
3. **Navigate to:** `C:\Users\zhenk\WonderWorld`
4. **Click:** Select Folder

VS Code will now open the entire project folder.

## 🐍 Setting Up Python Interpreter

To make VS Code recognize your Python virtual environment:

### Method 1: Auto-Detection (Recommended)

1. Press `Ctrl + Shift + P` to open the command palette
2. Type: `Python: Select Interpreter`
3. You should see `.\.venv` listed
4. Click on it to select it

### Method 2: Manual Configuration

1. Create a file called `.vscode\settings.json` in your project folder
2. Add this content:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true
}
```

## 💻 Using the Integrated Terminal in VS Code

VS Code has a built-in terminal which is convenient:

### Opening the Terminal

- Press `` Ctrl + ` `` (backtick) or
- Go to View → Terminal

### Activating Virtual Environment in VS Code Terminal

When you open the integrated terminal in VS Code, it should automatically detect and activate your virtual environment.

If it doesn't, you can manually activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

You'll know it worked when you see `(.venv)` at the start of the line.

### Running Streamlit from VS Code Terminal

```bash
streamlit run app.py
```

## 📂 Project Files in Explorer

When you open the project, you'll see this structure in the VS Code Explorer:

```
WonderWorld/
├── .gitignore
├── .venv/
├── README.md
├── SETUP_COMPLETE.md
├── VS_CODE_SETUP.md (this file)
├── app.py           ← Main application
├── mylibrary.py     ← Attraction data and logic
└── requirements.txt
```

## 🎯 Recommended VS Code Extensions

While not required, these extensions make Python development easier:

1. **Python** (by Microsoft)
   - Install from: Extensions → Search "Python" by Microsoft
   - Provides syntax highlighting, debugging, linting

2. **Pylance** (by Microsoft)
   - Install from: Extensions → Search "Pylance"
   - Provides intelligent code completion

3. **Streamlit** (by Streamlit)
   - Install from: Extensions → Search "Streamlit"
   - Helpful tips for Streamlit development

## 🔍 Editing Code in VS Code

### Syntax Highlighting

When you open `app.py` or `mylibrary.py`, VS Code should automatically recognize them as Python files and provide syntax highlighting (colors for different code elements).

### IntelliSense (Code Completion)

As you type Python code:
- Press `Ctrl + Space` for code suggestions
- Press `Ctrl + Hover` to see function documentation
- This makes coding faster and catches errors early

### Finding TODO Comments

The TODO comments in the skeleton code are useful markers:

1. Press `Ctrl + Shift + F` to open Find in Files
2. Search for: `TODO`
3. VS Code will highlight all TODO locations where you need to implement code

## 🐛 Debugging Python Code

If your code has errors:

1. **Check the Terminal:** When you run `streamlit run app.py`, errors appear in the terminal
2. **Read Error Messages:** Python error messages tell you what's wrong and where
3. **Use Print Statements:** Add `print()` statements to debug
4. **VS Code Debugger:** You can set breakpoints by clicking left of line numbers

## 📝 Useful Keyboard Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl + S` | Save file |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` | Redo |
| `Ctrl + F` | Find in file |
| `Ctrl + H` | Find and replace |
| `Ctrl + /` | Toggle comment |
| `Ctrl + Space` | IntelliSense |
| `F5` | Start debugging |
| `Ctrl + \`` | Toggle terminal |

## 🚀 Full Workflow in VS Code

Here's a typical development session:

1. **Open VS Code** and the WonderWorld folder
2. **Open Terminal** (`` Ctrl + ` ``)
3. **Virtual environment activates automatically** (you see `(.venv)`)
4. **Run the app:**
   ```bash
   streamlit run app.py
   ```
5. **Browser opens** to http://localhost:8501
6. **While app runs, edit code** in VS Code
7. **Save changes** (Ctrl + S)
8. **Browser auto-reloads** — Streamlit detects changes
9. **Test your changes** in the browser
10. **Check terminal** for any error messages

## ⚙️ File Formatting (Optional)

To automatically format your Python code nicely:

1. Install Black formatter:
   ```bash
   pip install black
   ```

2. In VS Code, right-click a Python file and select "Format Document"

## 🔄 Git Integration in VS Code

VS Code has built-in Git support:

1. Click the Source Control icon (left sidebar, looks like a branch)
2. You'll see changed files listed
3. To commit:
   - Type a commit message
   - Press Ctrl + Enter or click the checkmark

## 💡 Tips for Success

1. **Save frequently** - Get in the habit of pressing `Ctrl + S`
2. **Read error messages** - They tell you exactly what's wrong
3. **Use the terminal** - It's right there in VS Code
4. **Test as you code** - Save, check browser, repeat
5. **Keep the terminal visible** - You can see errors and app status
6. **Use TODO comments** - They mark where you need to implement logic

## 🆘 Common Issues

### Issue: Python interpreter not found
- Make sure virtual environment is activated
- Try Method 1 (Auto-detection) in "Setting Up Python Interpreter" above
- Or restart VS Code

### Issue: Changes don't appear when I save
- Make sure Streamlit's auto-reload is active (watch for "Rerun" button in the app)
- Try pressing the "Rerun" button manually if auto-reload doesn't trigger

### Issue: Import errors for streamlit
- Make sure virtual environment is activated
- Check that requirements are installed: `pip install -r requirements.txt`

### Issue: Terminal won't activate virtual environment
- Try closing and reopening the terminal
- Try using Command Prompt instead of PowerShell

## 📚 Next Steps

Now that VS Code is set up:

1. Read the `README.md` for project overview
2. Review `mylibrary.py` to understand the data structure
3. Review `app.py` to see the UI components
4. Find the TODO comments and start implementing!

---

Happy coding! 🚀
