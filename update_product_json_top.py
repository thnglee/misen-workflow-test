import json
import os

filepath = 'templates/product.json'

with open(filepath, 'r') as f:
    data = json.load(f)

# Define new sections
data['sections']['trust_bar'] = {
    "type": "multicolumn",
    "settings": {
        "title": "",
        "columns_desktop": 4,
        "color_scheme": "scheme-1"
    },
    "blocks": {
        "logo_1": {"type": "column", "settings": {}},
        "logo_2": {"type": "column", "settings": {}},
        "logo_3": {"type": "column", "settings": {}},
        "logo_4": {"type": "column", "settings": {}}
    },
    "block_order": ["logo_1", "logo_2", "logo_3", "logo_4"]
}

data['sections']['problem_symptoms'] = {
    "type": "multicolumn",
    "settings": {
        "title": "Problem / Symptoms",
        "columns_desktop": 5,
        "color_scheme": "scheme-2"
    },
    "blocks": {
        "s_1": {"type": "column", "settings": {}},
        "s_2": {"type": "column", "settings": {}},
        "s_3": {"type": "column", "settings": {}},
        "s_4": {"type": "column", "settings": {}},
        "s_5": {"type": "column", "settings": {}}
    },
    "block_order": ["s_1", "s_2", "s_3", "s_4", "s_5"]
}

data['sections']['root_cause'] = {
    "type": "custom-liquid",
    "settings": {
        "custom_liquid": "<!-- Symptom-to-Root-Cause table goes here -->\n<div class='page-width'><h2>Root Cause Education</h2></div>"
    }
}

data['sections']['education_science'] = {
    "type": "image-with-text",
    "settings": {
        "layout": "image_first"
    },
    "blocks": {
        "heading": {
            "type": "heading",
            "settings": {
                "heading": "The Science Behind Sculptique"
            }
        },
        "text": {
            "type": "text",
            "settings": {
                "text": "..."
            }
        }
    },
    "block_order": ["heading", "text"]
}

# Update order
order = ["trust_bar", "main", "problem_symptoms", "root_cause", "education_science", "related-products"]
data["order"] = order

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2)

print("Injected top half sections.")
