import re

with open('/Users/thanglee/shopify/MISENtest-0304/markdownexport/Sculptique-nonLIQUID/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Extract lines 1830 to 2086 (index 1829 to 2086 is exactly 257 lines)
ticker_lines = lines[1829:2086]
ticker_html = "".join(ticker_lines)

# Apply liquid asset_url filter
ticker_html = re.sub(r'src="assets/([^"]+)"', r'src="{{ \'\1\' | asset_url }}"', ticker_html)

# Read product-information.liquid
file_path = '/Users/thanglee/shopify/MISENtest-0304/markdownexport/sections/product-information.liquid'
with open(file_path, 'r', encoding='utf-8') as f:
    liquid_content = f.read()

badge_html = """
                <style>
                  .clinicians-choice {
                    display: flex;
                    align-items: center;
                    gap: 15px;
                    background: #fbfbfb;
                    border: 1px solid #eee;
                    border-radius: 8px;
                    padding: 16px;
                    margin-top: 24px;
                    margin-bottom: 24px;
                  }
                  .clinicians-choice-badge {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    flex-shrink: 0;
                    text-align: center;
                    width: 80px;
                  }
                  .clinicians-choice-badge svg {
                    width: 40px;
                    height: 40px;
                    margin-bottom: 5px;
                  }
                  .clinicians-choice-badge span {
                    font-size: 11px;
                    font-weight: bold;
                    line-height: 1.1;
                  }
                  .clinicians-choice-text {
                    font-size: 14px;
                    line-height: 1.4;
                  }
                  .clinicians-choice-text strong {
                    font-weight: bold;
                  }
                  .clinicians-choice-text a {
                    text-decoration: underline;
                    color: #000;
                  }
                  .clinicians-choice-footer {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    margin-top: 8px;
                  }
                  .clinicians-avatars {
                    display: flex;
                  }
                  .clinicians-avatars img {
                    width: 24px;
                    height: 24px;
                    border-radius: 50%;
                    margin-left: -8px;
                    border: 2px solid #fff;
                  }
                  .clinicians-avatars img:first-child {
                    margin-left: 0;
                  }
                </style>
                <div class="clinicians-choice">
                  <div class="clinicians-choice-badge">
                    <svg viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5">
                      <path d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 8.843 5.3m-8.843-5.3a8.997 8.997 0 0 0-8.843 5.3" />
                      <circle cx="12" cy="12" r="3" fill="#000"/>
                    </svg>
                    <span>Clinicians' Choice</span>
                  </div>
                  <div class="clinicians-choice-text">
                    <strong>521 clinicians</strong>, including dermatologists, share this on <em>FrontrowMD</em>. <a href="#">Learn more</a>
                    <div class="clinicians-choice-footer">
                      <div class="clinicians-avatars">
                        <img src="https://ui-avatars.com/api/?name=J&background=random" />
                        <img src="https://ui-avatars.com/api/?name=A&background=random" />
                        <img src="https://ui-avatars.com/api/?name=M&background=random" />
                      </div>
                      <small>Read their reviews</small>
                    </div>
                  </div>
                </div>
"""

# Replace the iframe completely
iframe_pattern = re.compile(r'<script\s+async=""[^>]*src="https://app.thefrontrowhealth.com[^>]*></script>\s*<iframe[^>]*src="https://app.thefrontrowhealth.com[^>]*></iframe>\s*<style>\s*.iframe.frontrow[^}]*}\s*</style>', re.DOTALL)
liquid_content = iframe_pattern.sub(badge_html, liquid_content)

# Insert ticker right before {% schema %}
if "{% schema %}" in liquid_content:
    liquid_content = liquid_content.replace("{% schema %}", ticker_html + "\n\n{% schema %}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(liquid_content)

print("Replacement complete")
