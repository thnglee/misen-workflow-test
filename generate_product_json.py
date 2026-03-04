import json

with open('templates/product.json', 'r') as f:
    data = json.load(f)

# Modify the main product block order to include our custom blocks
data['sections']['main']['block_order'] = [
    'trustpilot',
    'title',
    'price',
    'clinicians',
    'benefits',
    'variant_picker',
    'quantity_selector',
    'buy_buttons',
    'description'
]

data['sections']['main']['blocks']['trustpilot'] = {
    "type": "trustpilot_rating",
    "settings": {
        "rating_score": "4.8/5 Excellent",
        "review_count": "2381"
    }
}

data['sections']['main']['blocks']['clinicians'] = {
    "type": "clinicians_badge",
    "settings": {
        "clinician_count": "521"
    }
}

data['sections']['main']['blocks']['benefits'] = {
    "type": "benefits_list",
    "settings": {
        "benefit_text_1": "Supports Healthy Lymph Flow",
        "benefit_text_2": "Reduces Water Retention",
        "benefit_text_3": "Boosts Energy",
        "benefit_text_4": "Natural Ingredients",
        "benefit_text_5": "Clinically Tested",
        "benefit_text_6": "Fast Acting"
    }
}

with open('templates/product.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated templates/product.json")
