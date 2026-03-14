def add_setting(settings, pair):
    key, value = pair
    key, value = key.lower(), value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key, value = pair
    key, value = key.lower(), value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    output = "Current User Settings:\n"

    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output

test_settings = {
    'theme': 'dark',
    'language': 'english'
}

#FOR TESTING ONLY
print(f"""
### Display "test_settings" before changes

{view_settings(test_settings)}

### Add setting to "test_settings"

{add_setting(test_settings, ('color', 'blue'))}

{view_settings(test_settings)}

### Delete setting from "test_settings"

{delete_setting(test_settings, 'color')}

{view_settings(test_settings)}

### View settings after changes

{view_settings(test_settings)}
""")
