# User Configuration Manager (Python)

A robust backend utility for managing user-specific application settings. This project demonstrates the implementation of **CRUD** (Create, Read, Update, Delete) operations and strict data validation using Python dictionaries and tuples.

## 🚀 Features
- **Case-Insensitive Handling:** Automatically normalizes keys and values to lowercase to prevent duplicate settings (e.g., "Theme" vs "theme").
- **State Validation:** Checks for the existence of settings before attempting updates or deletions to prevent runtime errors.
- **Formatted Reporting:** Generates a clean, user-facing summary of all current settings with proper capitalization and layout.
- **Punctuation Precision:** Error messages are strictly formatted for consistent UI/UX feedback.

## 🛠️ Technical Skills Demonstrated
- **Dictionary Manipulation:** Using `.items()`, `del`, and key-checking logic.
- **String Formatting:** Advanced use of `f-strings` for dynamic messaging.
- **Data Normalization:** Systematic use of `.lower()` and `.capitalize()` for data integrity.
- **Tuple Unpacking:** Efficiently handling multi-value parameters.

## 📋 How It Works

### Adding a Setting
```python
# Function signature: add_setting(dictionary, (key, value))
add_setting(test_settings, ("Theme", "Dark")) 
# Returns: Setting 'theme' added with value 'dark' successfully!
```

### Update a Setting
```python
# Initial state: {'theme': 'dark'}
update_setting(test_settings, ("Theme", "Solarized"))
# Returns: Setting 'theme' updated to 'solarized' successfully!
```

### View Settings
```python
view_settings(test_settings)
# Returns:
# Current User Settings:
# Theme: Soloraized
```

### Delete Settings
```python
delete_setting(test_settings, 'Theme')
# Returns:
# Setting 'Theme; deleted successfully!
```
