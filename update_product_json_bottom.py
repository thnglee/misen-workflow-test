import json
import os

filepath = 'templates/product.json'

with open(filepath, 'r') as f:
    data = json.load(f)

# Define new sections for Hour 4 & 5
data['sections']['missing_piece'] = {
    "type": "image-with-text",
    "settings": {
        "layout": "text_first"
    },
    "blocks": {
        "heading": {"type": "heading", "settings": {"heading": "The Missing Piece"}},
        "text": {"type": "text", "settings": {"text": "pale green background"}}
    },
    "block_order": ["heading", "text"]
}

data['sections']['ingredients'] = {
    "type": "multicolumn",
    "settings": {
        "title": "8-Ingredient System",
        "columns_desktop": 4
    },
    "blocks": {
        "i_1": {"type": "column", "settings": {}},
        "i_2": {"type": "column", "settings": {}},
        "i_3": {"type": "column", "settings": {}},
        "i_4": {"type": "column", "settings": {}}
    },
    "block_order": ["i_1", "i_2", "i_3", "i_4"]
}

data['sections']['synergistic_effect'] = {
    "type": "rich-text",
    "settings": {},
    "blocks": {
        "heading": {"type": "heading", "settings": {"heading": "Synergistic Effect"}},
        "text": {"type": "text", "settings": {}}
    },
    "block_order": ["heading", "text"]
}

data['sections']['social_proof'] = {
    "type": "custom-liquid",
    "settings": {
         "custom_liquid": "<div class='page-width scroll-trigger animate--slide-in'><div class='stat-circles' style='background: conic-gradient(...)'><h2>87% and 91%</h2></div></div>"
    }
}

data['sections']['reviews'] = {
    "type": "custom-liquid",
    "settings": {
         "custom_liquid": "<!-- Reviews Integration (App Block fallback) -->"
    }
}

data['sections']['trust_icons_footer'] = {
    "type": "multicolumn",
    "settings": {
        "title": "Trust Icons",
        "columns_desktop": 4
    },
    "blocks": {
        "t_1": {"type": "column", "settings": {}},
        "t_2": {"type": "column", "settings": {}},
        "t_3": {"type": "column", "settings": {}},
        "t_4": {"type": "column", "settings": {}}
    },
    "block_order": ["t_1", "t_2", "t_3", "t_4"]
}

data['sections']['expert_advice'] = {
    "type": "image-with-text",
    "settings": {
        "layout": "image_first"
    },
    "blocks": {
        "heading": {"type": "heading", "settings": {"heading": "Expert Advice"}},
        "text": {"type": "text", "settings": {}}
    },
    "block_order": ["heading", "text"]
}

data['sections']['faq'] = {
    "type": "collapsible_content",
    "settings": {
        "heading": "Frequently Asked Questions"
    },
    "blocks": {
        "f_1": {"type": "collapsible_row", "settings": {"heading": "Question 1"}},
        "f_2": {"type": "collapsible_row", "settings": {"heading": "Question 2"}},
        "f_3": {"type": "collapsible_row", "settings": {"heading": "Question 3"}}
    },
    "block_order": ["f_1", "f_2", "f_3"]
}

# Update order
order = data.get("order", [])
# Remove related-products temporarily to append
if "related-products" in order:
    order.remove("related-products")

order.extend(["missing_piece", "ingredients", "synergistic_effect", "social_proof", "reviews", "trust_icons_footer", "expert_advice", "faq", "related-products"])
data["order"] = order

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2)

print("Injected bottom half and footer sections.")
