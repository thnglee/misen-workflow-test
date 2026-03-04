# Sculptique Product Page – Implementation Plan

## 1. High-Level Mapping (Markdown Section → Dawn Section/Block)

To adhere strictly to Dawn's native architecture, we will map the requested sections to Dawn's existing global sections where possible, minimizing custom code.

| Markdown Section            | Dawn Section / Block Mapping | Notes                                                                                                                |
| :-------------------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **1. Header**               | `header`                     | Global (Do not modify)                                                                                               |
| **2. Trust / Press Bar**    | `multicolumn`                | Set to 4 columns, no text, images only. Use grayscale CSS filter.                                                    |
| **3. Hero / Product**       | `main-product`               | Uses native `product.media`, custom `variant_picker` block, and `custom_liquid` blocks for trust stars and benefits. |
| **4. Problem / Symptoms**   | `multicolumn` + `rich-text`  | 5-column multicolumn for symptoms. Rich text for the pink callout.                                                   |
| **5. Symptom Root Cause**   | `custom-liquid`              | Custom table using Dawn's `page-width` and table utility classes, or a barebones custom Liquid section.              |
| **6. Education / Science**  | `image-with-text`            | Multiple native `image-with-text` sections alternating layouts.                                                      |
| **7. Hidden Drainage**      | `rich-text`                  | Native rich text, white background.                                                                                  |
| **8. Why Nothing Worked**   | `image-with-text`            | Native image with text.                                                                                              |
| **9. The Missing Piece**    | `rich-text`                  | Pale green background (using Dawn's color schemes).                                                                  |
| **10. Ingredients Section** | `multicolumn`                | 4 columns for ingredients. Can use `collapsible_content` for the accordion details beneath if needed.                |
| **11. Synergistic Effect**  | `rich-text`                  | Native rich text.                                                                                                    |
| **12. Social Proof/Stats**  | `custom-liquid`              | Custom HTML/CSS required for the circular pie-chart stats, wrapped in Dawn's `page-width`.                           |
| **13. Reviews Section**     | App Block / `custom-liquid`  | Standard Shopify product reviews app block or custom metafield loop.                                                 |
| **14. Trust Icons Bar**     | `multicolumn`                | 4 columns, icon + title + text.                                                                                      |
| **15. Expert Advice**       | `image-with-text`            | Portrait image on right, quote on left.                                                                              |
| **16. Transformations**     | `multicolumn`                | 3 columns, before/after images.                                                                                      |
| **17. Bundle Buy Box**      | `main-product`               | Integrated as a custom variant selector block.                                                                       |
| **18. FAQ Section**         | `collapsible_content`        | Native Dawn FAQ section.                                                                                             |
| **19. Footer**              | `footer`                     | Global (Do not modify)                                                                                               |

---

## 2. Liquid Code (`sections/main-product.liquid` modifications)

To achieve the "Spring Sale", Trustpilot stars, Benefits, and Bundle radio cards while keeping theme compatibility, we modify the blocks within `main-product.liquid`.

**Diff / Additions to `main-product.liquid`:**

```liquid
{%- comment -%} Add this inside the main-product block rendering loop, replacing the standard variant picker {%- endcomment -%}

{%- case block.type -%}
  {%- when 'trustpilot_rating' -%}
    <div class="product__trustpilot" {{ block.shopify_attributes }}>
      <span class="trustpilot-stars" style="color: var(--color-trustpilot, #00b67a); letter-spacing: 2px;">★★★★★</span>
      <span class="trustpilot-text caption-large">
        {{ block.settings.rating_score | default: '4.8/5 Excellent' }} | Based on {{ block.settings.review_count | default: '2381' }} Reviews
      </span>
    </div>

  {%- when 'benefits_list' -%}
    <ul class="product__benefits list-unstyled" {{ block.shopify_attributes }}>
      {%- for i in (1..6) -%}
        {%- assign text_key = 'benefit_text_' | append: i -%}
        {%- assign icon_key = 'benefit_icon_' | append: i -%}
        {%- if block.settings[text_key] != blank -%}
          <li class="benefit-item">
            <span class="benefit-item__icon">{{ block.settings[icon_key] }}</span>
            <span class="benefit-item__text">{{ block.settings[text_key] }}</span>
          </li>
        {%- endif -%}
      {%- endfor -%}
    </ul>

  {%- when 'clinicians_badge' -%}
    <div class="product__clinicians-badge" {{ block.shopify_attributes }}>
      <span class="badge-icon">⚕️</span>
      <div class="badge-text">
        <strong>{{ block.settings.clinician_count | default: '521' }} clinicians</strong> share this on <em>FrontrowMD</em>.
      </div>
    </div>

  {%- when 'variant_picker' -%}
    {%- comment -%} Custom Bundle Radio Selector for Sculptique {%- endcomment -%}
    <div class="bundle-selector" {{ block.shopify_attributes }}>
      <variant-radios class="no-js-hidden" data-section="{{ section.id }}" data-url="{{ product.url }}">
        {%- for variant in product.variants -%}
          <div class="bundle-option {% if forloop.index == 2 %}bundle-option--featured{% endif %}">
            <input type="radio"
                   id="bundle-{{ variant.id }}"
                   name="id"
                   value="{{ variant.id }}"
                   form="{{ product_form_id }}"
                   {% if variant.id == product.selected_or_first_available_variant.id %}checked{% endif %}>

            <label for="bundle-{{ variant.id }}" class="bundle-option__label">
              {%- if forloop.index == 2 -%}
                <span class="bundle-option__badge">Spring Sale +</span>
              {%- endif -%}

              <div class="bundle-option__header">
                <span class="bundle-option__title">{{ variant.title }}</span>
                <div class="bundle-option__pricing">
                  <span class="price-item price-item--regular">{{ variant.price | money }}</span>
                  {%- if variant.compare_at_price > variant.price -%}
                    <s class="price-item price-item--sale">{{ variant.compare_at_price | money }}</s>
                  {%- endif -%}
                </div>
              </div>

              <div class="bundle-option__perks caption">
                {%- if variant.compare_at_price > variant.price -%}
                  <div class="perk-save">Save {{ variant.compare_at_price | minus: variant.price | money }}</div>
                {%- endif -%}
                <div class="perk-item">✓ Free USA Shipping</div>
                {%- if forloop.index >= 2 -%}<div class="perk-item">✓ Free Anti-Bloating Protocol E-book</div>{%- endif -%}
                {%- if forloop.index == 3 -%}<div class="perk-item">✓ $20 Gift Card</div>{%- endif -%}
              </div>
            </label>
          </div>
        {%- endfor -%}
      </variant-radios>
    </div>
{%- endcase -%}
```

**Schema Additions in `main-product.liquid`:**
We will append these block types to the schema to maintain Theme Editor compatibility.

```json
{
  "type": "trustpilot_rating",
  "name": "Trustpilot Rating",
  "settings": [
    { "type": "text", "id": "rating_score", "label": "Score Text", "default": "4.8/5" },
    { "type": "text", "id": "review_count", "label": "Review Count", "default": "2381" }
  ]
},
{
  "type": "benefits_list",
  "name": "Benefits List",
  "settings": [
    { "type": "text", "id": "benefit_icon_1", "label": "Icon 1", "default": "🔄" },
    { "type": "text", "id": "benefit_text_1", "label": "Benefit 1" }
    // ... up to 6
  ]
},
{
  "type": "clinicians_badge",
  "name": "Clinicians Badge",
  "settings": [
    { "type": "text", "id": "clinician_count", "label": "Clinician count", "default": "521" }
  ]
}
```

---

## 3. CSS Additions

To be placed inside Dawn's `<style>` block in `main-product.liquid`, scoped tightly to avoid bleeding.

```css
<style>
  /* Base variables mapped to Dawn natively where possible, overrides scoped */
  .product__info-container {
    --color-trustpilot: #00b67a;
    --color-bg-sage: #e8ede8;
    --color-accent-teal: #008b7d;
    --color-accent-gold: #d4a017;
  }

  /* Benefits List */
  .product__benefits {
    margin: 2rem 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .benefit-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    font-size: 1.5rem; /* ~15px aligning with Dawn base size */
  }

  /* Bundle Selector Radio Cards */
  .bundle-selector {
    margin: 2.5rem 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .bundle-option {
    position: relative;
  }
  .bundle-option input[type="radio"] {
    position: absolute;
    opacity: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
    z-index: 2;
  }
  .bundle-option__label {
    display: block;
    padding: 1.5rem;
    border: 1px solid rgba(var(--color-foreground), 0.1);
    border-radius: 1.2rem; /* 12px given in design system */
    background: rgb(var(--color-background));
    transition: all 0.2s ease;
  }
  .bundle-option input[type="radio"]:checked + .bundle-option__label {
    border-color: var(--color-accent-teal);
    background: var(--color-bg-sage);
    box-shadow: 0 0 0 1px var(--color-accent-teal);
  }
  .bundle-option--featured .bundle-option__label {
    border-color: var(--color-accent-gold);
  }
  .bundle-option__badge {
    position: absolute;
    top: -10px;
    right: 20px;
    background: var(--color-accent-gold);
    color: #fff;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: uppercase;
  }
  .bundle-option__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
  }
  .bundle-option__title {
    font-weight: 700;
    font-size: 1.6rem;
  }
  .bundle-option__pricing {
    text-align: right;
  }
  .price-item--regular {
    font-weight: 700;
  }
  .perk-save {
    color: var(--color-accent-teal);
    font-weight: 600;
  }
  .perk-item {
    color: rgba(var(--color-foreground), 0.7);
    margin-top: 0.2rem;
  }
</style>
```

**Justification for CSS:**

- Dawn's native pill/dropdown `variant_picker` does not support rich content (titles, multiple prices, lists of perks, dynamic badges) within the standard DOM without JS modifications. By rebuilding the radio inputs as stacked rich cards, we hit the visual requirement while remaining fully functional via standard form submission logic.
- CSS variables encapsulate the UI's specific greens and golds without altering global `base.css`.
- The flexbox layouts (`bundle-selector`, `product__benefits`) are standard, robust ways to recreate the list alignments shown in the UI.

---

## 4. Notes

**Reused from Dawn:**

1. **Core Layout:** We reuse `header`, `footer`, and the global CSS grid mapping (`page-width`).
2. **Standard Sections:** We heavily rely on `multicolumn`, `image-with-text`, and `rich-text` features (passing via `product.json` blocks) to avoid creating 10+ custom components. We will assemble these natively in the Customizer.
3. **Product Form:** We reuse Dawn;s AJAX add-to-cart logic. Our modified `variant_picker` simply emits a selected `name="id"` radio value which Dawn’s existing JS handles cleanly.

**Limitations / Approximations:**

1. **Paginating Reviews:** Usually requires a third-party app (e.g., Judge.me). We can map the UI of the review section, but native Liquid cannot natively handle AJAX paginated reviews without heavy custom JS/metafields routing.
2. **Stat Circles (Social Proof):** Dawn does not contain pie chart CSS components. We will implement them using a raw CSS `conic-gradient` via a `custom-liquid` section block, ensuring it hits the visual spec.
3. **Mobile Reordering:** Standard Dawn `image-with-text` drops images on top of text on mobile. If the specific UI dictates text-on-top for specific blocks, we may need to inject a `flex-direction: column-reverse` CSS class for mobile queries on those specific instances.
