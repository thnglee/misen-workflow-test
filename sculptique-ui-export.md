# Sculptique – Lymphatic Drainage Capsules: UI Export for Shopify Liquid Cloning

**Source URL:** `https://trysculptique.com/products/lymph-cc-select`
**Page Type:** Long-form Product Landing Page (VSL-style, single product)
**Exported:** 2026-03-04

---

## 🎨 Design System

### Color Palette

| Token                  | HEX       | Usage                                                               |
| ---------------------- | --------- | ------------------------------------------------------------------- |
| `--color-bg-primary`   | `#f1f4f1` | Main page background (sage/off-white green)                         |
| `--color-bg-secondary` | `#ffffff` | Card/section backgrounds                                            |
| `--color-bg-pink`      | `#f8e7e7` | Accent callout boxes, "Here's what nobody's telling you" blocks     |
| `--color-bg-sage-card` | `#e8ede8` | Ingredient/symptom explanation cards                                |
| `--color-accent-teal`  | `#008b7d` | Primary CTA buttons, checkmarks, highlighted text, icon backgrounds |
| `--color-accent-gold`  | `#d4a017` | "Spring Sale" badge, sale labels                                    |
| `--color-text-dark`    | `#1a1a1a` | Headings, body text                                                 |
| `--color-text-muted`   | `#6b6b6b` | Secondary text, captions                                            |
| `--color-star`         | `#e8a045` | Star rating icons                                                   |
| `--color-trustpilot`   | `#00b67a` | Trustpilot star color                                               |
| `--color-border`       | `#e0e0e0` | Card borders, dividers                                              |

### Typography

| Role                 | Font                             | Size    | Weight | Notes                                  |
| -------------------- | -------------------------------- | ------- | ------ | -------------------------------------- |
| Logo                 | Serif (custom)                   | ~28px   | 400    | `sculptique.` lowercase with period    |
| H1 / Hero Headline   | Serif (Georgia/Playfair Display) | 36–48px | 700    | Dark text                              |
| H2 / Section Heading | Serif                            | 28–36px | 700    | Mix: teal highlight on key word        |
| H3 / Card Heading    | Sans-serif (Inter/DM Sans)       | 18–22px | 600    |                                        |
| Body Text            | Sans-serif                       | 15–17px | 400    | Line-height ~1.6                       |
| Badge/Label          | Sans-serif                       | 11–13px | 700    | All caps or bold                       |
| Price                | Sans-serif                       | 24–28px | 700    | Dark green primary, strikethrough gray |

### Spacing

- Section vertical padding: `80px` desktop / `48px` mobile
- Card border-radius: `12px`
- Button border-radius: `8px` (pill-adjacent)
- Max content width: `1200px` page-width

---

## 🗺️ Page Structure (Section Order)

```
1.  [HEADER]               → Logo + Nav (minimal)
2.  [TRUST BAR]            → Media logos (Vogue, BuzzFeed, Vogue, Allure)
3.  [HERO / PRODUCT]       → Product image + headline + benefits list + pricing bundles + social proof
4.  [PROBLEM SECTION]      → "Your Body Has A Hidden Drainage System" – symptoms grid
5.  [CONNECTION SECTION]   → Symptoms → Root Cause table
6.  [EDUCATION SECTION]    → Body anatomy diagram, why lymphatic system fails after 35
7.  [SOLUTION SECTION]     → "Your Hidden Drainage System" explanation
8.  [BEFORE/AFTER SECTION] → Why Nothing Has Worked Until Now (comparison charts)
9.  [THE MISSING PIECE]    → Comprehensive lymphatic restoration explanation
10. [INGREDIENTS SECTION]  → "8-Ingredient System" – ingredient grid cards
11. [SYNERGISTIC EFFECT]   → How ingredients work together
12. [RESULTS SECTION]      → "93,000+ Transformations" – stat circles, social proof images
13. [REVIEWS SECTION]      → Star rating breakdown + paginated review feed
14. [TRUST ICONS BAR]      → 4 icons: Free Shipping / Natural / 100% Natural / 60-Day Guarantee
15. [EXPERT SECTION]       → Quote from Dr. Emily Chen + image + "Try Risk-Free" CTA
16. [TRANSFORMATION STORIES] → "See The Stories..." – customer testimonials with images
17. [PRICING / BUY BOX]    → Bundle selector + Add to Cart (also appears in hero)
18. [FAQ SECTION]          → Collapsible accordion FAQ
19. [FOOTER]               → Minimal footer (links, copyright)
```

---

## Section-by-Section Liquid Implementation Guide

---

### 1. HEADER

**Layout:** Centered logo, minimal navigation.

```liquid
{%- comment -%} sections/header.liquid — use standard Dawn header, minimized {%- endcomment -%}
<header class="site-header">
  <div class="page-width header-inner">
    <a href="{{ routes.root_url }}" class="header__logo">
      {{ shop.name }}
    </a>
  </div>
</header>
```

**Notes:**

- No mega menu needed — this is a landing page
- Logo is `sculptique.` in elegant serif, all lowercase with trailing period
- Header is NOT sticky on this page (simple print/PDF export shows no sticky)

---

### 2. TRUST / PRESS BAR

**Type:** Static horizontal logo strip

**Content:** Vogue, BuzzFeed, Vogue (UK), Allure logos in grayscale

**Liquid Snippet:**

```liquid
{%- comment -%} snippets/press-bar.liquid {%- endcomment -%}
<section class="press-bar">
  <div class="page-width press-bar__inner">
    {%- for block in section.blocks -%}
      {%- if block.type == 'logo' -%}
        <div class="press-bar__item">
          {%- if block.settings.logo != blank -%}
            {{ block.settings.logo | image_url: width: 120 | image_tag: loading: 'lazy' }}
          {%- else -%}
            <span class="press-bar__text">{{ block.settings.label }}</span>
          {%- endif -%}
        </div>
      {%- endif -%}
    {%- endfor -%}
  </div>
</section>
```

**Schema blocks:**

```json
{
  "type": "logo",
  "name": "Press logo",
  "settings": [
    { "type": "image_picker", "id": "logo", "label": "Logo image" },
    { "type": "text", "id": "label", "label": "Text fallback" }
  ]
}
```

---

### 3. HERO / PRODUCT SECTION

**Layout:** 2-column (60% left: image gallery | 40% right: product info)

**Left column — Product Image:**

- Large product photo with sage-green textured background (reeds/botanicals)
- Yellow/gold `Spring Sale` badge overlaid top-right of image (absolute positioned)
- Below image: pill-shaped CTA button → `🌿 Nutritional Information`
- Below that: 3 small preview images (educational cards: lymphatic system, why after 35)

**Right column — Product Info:**

- Trustpilot stars: `★★★★★ 4.8/5 Excellent | Based on 2381 Reviews` (teal stars)
- `H1`: "New Maximum Potency Formula - Lymphatic Drainage Capsules by Sculptique™"
- Benefits list (icon + text, 6 items):
  - 👥 Join over 93 Thousand who say - it WORKS!
  - 🔄 Restores your body's natural 24-hour lymphic cycle
  - 💧 Helps reduce fluid retention and the appearance of puffiness and bloating
  - 😴 Helps fall asleep faster, stay asleep longer and wake up energized
  - 🦴 Eliminates joint stiffness, pain, morning creakiness and feel more grounded
  - ⚡ Boosts energy, mental clarity and emotional balance
- `Clinicians' Choice` seal — "521 clinicians, including dermatologists share this on FrontrowMD. Learn more | Read their reviews"
- **Pricing Bundle Selector** (radio-style cards, see Section 17)

**Liquid:**

```liquid
{%- comment -%} sections/main-product.liquid — adapt Dawn's main-product section {%- endcomment -%}
<section class="product-hero" id="ProductSection-{{ section.id }}">
  <div class="page-width">
    <div class="product-hero__grid">

      {%- comment -%} LEFT: Media Gallery {%- endcomment -%}
      <div class="product-hero__media">
        {%- if section.settings.show_sale_badge and product.compare_at_price > product.price -%}
          <div class="product-hero__badge badge--sale">
            {{ section.settings.sale_badge_text | default: 'Spring Sale' }}
          </div>
        {%- endif -%}
        {% render 'product-media-gallery', product: product, section: section %}
        <a href="#nutritional-info" class="btn btn--outline btn--nutritional">
          🌿 Nutritional Information
        </a>
      </div>

      {%- comment -%} RIGHT: Product Info {%- endcomment -%}
      <div class="product-hero__info">

        {%- comment -%} Trustpilot / Star Rating {%- endcomment -%}
        <div class="product-hero__rating">
          <div class="stars stars--trustpilot">★★★★★</div>
          <span>{{ section.settings.review_score }} | Based on {{ section.settings.review_count }} Reviews</span>
        </div>

        {%- if request.page_type == 'product' -%}
          <h1 class="product-hero__title">{{ product.title }}</h1>
        {%- else -%}
          <h2 class="product-hero__title">{{ product.title }}</h2>
        {%- endif -%}

        {%- comment -%} Benefits List {%- endcomment -%}
        <ul class="product-hero__benefits">
          {%- for block in section.blocks -%}
            {%- if block.type == 'benefit' -%}
              <li class="benefit-item" {{ block.shopify_attributes }}>
                <span class="benefit-item__icon">{{ block.settings.icon }}</span>
                <span class="benefit-item__text">{{ block.settings.text }}</span>
              </li>
            {%- endif -%}
          {%- endfor -%}
        </ul>

        {%- comment -%} Clinicians Badge {%- endcomment -%}
        {%- if section.settings.show_clinicians_badge -%}
          <div class="clinicians-badge">
            <img src="{{ 'clinicians-choice-seal.png' | asset_url }}" alt="Clinicians Choice" width="48">
            <div>
              <strong>{{ section.settings.clinicians_count }} clinicians</strong>, including dermatologists
              share this on <em>FrontrowMD</em>.
              <a href="{{ section.settings.clinicians_url }}">Learn more</a>
            </div>
          </div>
        {%- endif -%}

        {%- comment -%} Variant / Bundle Picker — see Section 17 {%- endcomment -%}
        {% render 'product-variant-picker', product: product, section: section %}

        {%- comment -%} Delivery estimate {%- endcomment -%}
        <div class="delivery-estimate">
          🚚 Delivered on <strong>{{ 'now' | date: '%A, %-d %B' | plus: 5 }}</strong> with Express Shipping
        </div>

      </div>
    </div>
  </div>
</section>
```

**Schema settings to add:**

```json
{ "type": "text", "id": "review_score", "label": "Review score", "default": "4.8/5 Excellent" },
{ "type": "text", "id": "review_count", "label": "Review count", "default": "2381" },
{ "type": "checkbox", "id": "show_sale_badge", "label": "Show sale badge", "default": true },
{ "type": "text", "id": "sale_badge_text", "label": "Sale badge text", "default": "Spring Sale" },
{ "type": "checkbox", "id": "show_clinicians_badge", "label": "Show Clinicians badge", "default": true },
{ "type": "text", "id": "clinicians_count", "label": "Clinician count", "default": "521" },
{ "type": "url", "id": "clinicians_url", "label": "Clinicians link" }
```

---

### 4. PROBLEM / SYMPTOMS SECTION

**Type:** Educational section, sage-green background
**Headline:** _"Why Your Bloating, Brain Fog & Swollen Legs Are Actually Connected"_

**Layout — 5-column symptom grid:**
| Image | Caption |
|---|---|
| Woman with bloated stomach | "Your stomach is flat in the morning, but by evening you look six months pregnant." |
| Swollen ankle photo | "Your ankles disappear into 'kankles' by the end of the day." |
| Cellulite on thighs | "That dimpled, cottage cheese texture on your thighs won't go away no matter what you try." |
| Woman tired in bed | "You feel foggy and exhausted even after a full night's sleep." |
| Woman waking up stiff | "You wake up stiff and achy, like your body aged overnight." |

**Below grid:** Curved arrows pointing to a **pink callout box**:

- `Here's what nobody's telling you:`
- _"These aren't separate problems. They're all symptoms of the same root cause."_

**Then a large pink/rose banner (full width):**

- `Here's what nobody's telling you:`
- _"These aren't separate problems. They're all symptoms of the same root cause."_

**Liquid:**

```liquid
{%- comment -%} sections/lp-symptoms.liquid {%- endcomment -%}
<section class="lp-symptoms section-{{ section.id }}-padding" style="background: {{ section.settings.bg_color }}">
  <div class="page-width">
    <h2 class="lp-symptoms__heading">{{ section.settings.heading }}</h2>
    <p class="lp-symptoms__subheading">{{ section.settings.subheading }}</p>

    <div class="symptoms-grid">
      {%- for block in section.blocks -%}
        {%- if block.type == 'symptom' -%}
          <div class="symptom-card" {{ block.shopify_attributes }}>
            {%- if block.settings.image != blank -%}
              {{ block.settings.image | image_url: width: 300 | image_tag: loading: 'lazy', class: 'symptom-card__image' }}
            {%- endif -%}
            <p class="symptom-card__caption">{{ block.settings.caption }}</p>
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>

    {%- comment -%} Arrow connectors (decorative SVG arrows) {%- endcomment -%}
    <div class="symptoms-arrows" aria-hidden="true">
      {%- for i in (1..5) -%}<span class="arrow-down">↷</span>{%- endfor -%}
    </div>

    <div class="symptoms-callout symptoms-callout--small">
      <p class="callout__label">{{ section.settings.callout_label }}</p>
      <p>{{ section.settings.callout_text }}</p>
    </div>

    <div class="symptoms-callout symptoms-callout--hero">
      <h3>{{ section.settings.callout_label }}</h3>
      <p>{{ section.settings.callout_text }}</p>
    </div>
  </div>
</section>
```

---

### 5. SYMPTOM-TO-ROOT-CAUSE TABLE

**Type:** Two-column comparison table
**Columns:** "Your Symptom" | "The Real Cause"

| Your Symptom           | The Real Cause                                                |
| ---------------------- | ------------------------------------------------------------- |
| Bloating & puffiness   | 4-5 liters of lymphatic fluid backing up in tissue            |
| Swollen legs           | Gravity pulling backed-up lymph to lower extremities          |
| Cellulite appearance   | Fluid and toxins trapped between fat cells, creating dimpling |
| Brain fog & exhaustion | Glymphatic system can't clear metabolic waste from brain      |
| Morning stiffness      | Overnight lymph accumulation in joints and tissues            |

**Below table:** Section transition: `"Your Hidden Drainage System"` with chevron `»` icon

**Liquid:**

```liquid
{%- comment -%} sections/lp-root-cause.liquid {%- endcomment -%}
<section class="lp-root-cause">
  <div class="page-width">
    <h2>{{ section.settings.heading }}</h2>
    <div class="root-cause-table">
      <div class="root-cause-table__header">
        <span>{{ section.settings.col1_label | default: 'Your Symptom' }}</span>
        <span>{{ section.settings.col2_label | default: 'The Real Cause' }}</span>
      </div>
      {%- for block in section.blocks -%}
        {%- if block.type == 'row' -%}
          <div class="root-cause-table__row" {{ block.shopify_attributes }}>
            <div class="root-cause__symptom">
              <span class="root-cause__icon">{{ block.settings.icon }}</span>
              <span>{{ block.settings.symptom }}</span>
            </div>
            <div class="root-cause__cause">{{ block.settings.cause }}</div>
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>
    <div class="section-transition">
      <span class="chevron-icon">»</span>
      <h3>{{ section.settings.transition_heading }}</h3>
    </div>
  </div>
</section>
```

---

### 6. EDUCATION / SCIENCE SECTION

**Type:** Image + text, multi-part explanation
**Headline:** _"Why This Happens After 35"_

**Content blocks:**

- Medical diagram of lymph nodes (human body silhouette)
- Graph showing lymphatic efficiency declining sharply after age 35
- Side-by-side: "Healthy Lymphatic Flow" vs "Congested Lymphatic Flow" (cross-section diagram)
- Explanatory text about estrogen/progesterone decline affecting lymphatics

**Layout:** Alternating image-left / text-right two-column rows

**Liquid:**

```liquid
{%- comment -%} sections/lp-science.liquid {%- endcomment -%}
<section class="lp-science">
  <div class="page-width">
    {%- for block in section.blocks -%}
      <div class="science-row science-row--{{ block.settings.layout | default: 'image-left' }}" {{ block.shopify_attributes }}>
        {%- if block.settings.image != blank -%}
          <div class="science-row__media">
            {{ block.settings.image | image_url: width: 600 | image_tag: loading: 'lazy' }}
          </div>
        {%- endif -%}
        <div class="science-row__content">
          {%- if block.settings.label != blank -%}
            <span class="science-row__label">{{ block.settings.label }}</span>
          {%- endif -%}
          <h3>{{ block.settings.heading }}</h3>
          <div class="rte">{{ block.settings.text }}</div>
        </div>
      </div>
    {%- endfor -%}
  </div>
</section>
```

---

### 7. "YOUR HIDDEN DRAINAGE SYSTEM" SECTION

**Type:** Text-dominant educational block
**Background:** White (#ffffff)

**Content:**

- Small double-chevron icon `»` above heading
- `H2`: "Your **Hidden** Drainage System" (`Hidden` in teal color)
- Body text: _"Your lymphatic system is your body's internal cleaning crew—a network of vessels that processes **3-4 liters of cellular waste and excess fluid every single day.**"_
- Continuation: _"When it's working properly, you don't even know it exists."_
- Then: _"But after 35, as hormones shift, your lymphatic system becomes fundamentally compromised."_
- Bulleted causes:
  - Lymphatic pumping slows by 40%
  - Protein clogs form in lymph vessels
  - Inflammation impairs drainage
  - Metabolism of lymph fluid slows
  - Waste clearance becomes inefficient
- Callout text (bordered box, subtle green): _"This isn't symptom masking. This is root cause restoration."_

---

### 8. WHY NOTHING HAS WORKED – COMPARISON SECTION

**Type:** "Before vs After discovery" section
**Layout:** Text left + image right

**Content:**

- Section label: _"Why Nothing Has Worked Until Now"_
- Contrast panels showing why typical approaches fail (dieting, exercise, topical creams)
- Explanation of why lymphatic health was the missing piece

---

### 9. THE MISSING PIECE / SOLUTION INTRO

**Background:** Pale green (`#e8f0e8`)
**Content:**

- Heading: _"The Missing Piece:"_
- Subheading: _"Comprehensive lymphatic restoration that addresses vessel pumping, protein clearance, inflammation, and metabolism—all at once."_
- 5-point bulleted feature list with teal checkmarks

---

### 10. INGREDIENTS SECTION

**Type:** Product ingredient showcase grid
**Headline (H2):**
_"The **8-Ingredient System** That Restores What Hormones Once Maintained"_
_("`8-Ingredient System`" in teal)_

**Subtext:** _"Sculptique is the only formula that addresses ALL 6 mechanisms of lymphatic dysfunction simultaneously—not with symbolic doses, but with therapeutic amounts based on clinical research."_

**Mechanism Grid (4-column):**

- ✓ Reactivate Lymphatic [Pumps]
- ✓ Flush Excess Fluid
- ✓ Break Down Protein Clogs
- ✓ Strengthen Vessel Walls

**Ingredient Cards (4-column grid, each card has image + name + dose + accordion):**

| Ingredient        | Dose  | Key Action                  |
| ----------------- | ----- | --------------------------- |
| Cleavers Extract  | —     | Lymphatic pump reactivation |
| Dandelion Extract | 250mg | Flush excess fluid          |
| Bromelain Powder  | 100mg | Break down protein clogs    |
| Rutin             | 100mg | Strengthen vessel walls     |
| Burdock Root      | —     | Anti-inflammation           |
| Echinacea         | —     | Immune support              |
| Kelp              | —     | Metabolic support           |
| Lemon Powder      | —     | Antioxidant / cleansing     |

**Liquid:**

```liquid
{%- comment -%} sections/lp-ingredients.liquid {%- endcomment -%}
<section class="lp-ingredients">
  <div class="page-width">
    <h2 class="lp-ingredients__heading">{{ section.settings.heading }}</h2>
    <p class="lp-ingredients__subtext">{{ section.settings.subtext }}</p>

    <div class="mechanism-grid">
      {%- for block in section.blocks -%}
        {%- if block.type == 'mechanism' -%}
          <div class="mechanism-item" {{ block.shopify_attributes }}>
            <span class="mechanism-item__check">✓</span>
            {{ block.settings.text }}
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>

    <div class="ingredients-grid">
      {%- for block in section.blocks -%}
        {%- if block.type == 'ingredient' -%}
          <div class="ingredient-card" {{ block.shopify_attributes }}>
            {%- if block.settings.image != blank -%}
              {{ block.settings.image | image_url: width: 200 | image_tag: loading: 'lazy', class: 'ingredient-card__image' }}
            {%- endif -%}
            <h4 class="ingredient-card__name">{{ block.settings.name }}</h4>
            {%- if block.settings.dose != blank -%}
              <span class="ingredient-card__dose">({{ block.settings.dose }})</span>
            {%- endif -%}
            <details class="ingredient-card__accordion">
              <summary>Learn more ↓</summary>
              <div class="ingredient-card__detail rte">{{ block.settings.detail }}</div>
            </details>
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>
  </div>
</section>
```

---

### 11. SYNERGISTIC EFFECT SECTION

**Background:** Very pale green
**Headline:** _"The Synergistic Effect"_
**Content:**

- Explanatory text about how the 8 ingredients work together in 6 stages
- Bulleted list:
  - Together, they address all 6 failure points simultaneously
  - These herbs work synergistically, making each other more effective
  - Begins working efficiently, moving waste out
  - Builds momentum over time
  - Reaches full restoration (marking end of vicious cycle)
- Closing italic quote: _"This isn't symptom masking. This is root cause restoration."_

---

### 12. SOCIAL PROOF / RESULTS SECTION

**Headline:** _"Real Women, Real Results: 93,000+ Transformations"_
**Trustpilot badge** inline: `★★★★★ 93,000+ Customers Worldwide`

**Two Stat Circles (side by side):**

- Circle 1: **87%** – _"reported less bloating and tiredness in the first 4 weeks\*"_
- Circle 2: **91%** – _"reported less puffiness and firmer skin in the first 4 weeks\*"_
- _"Based on a four-week independent customer panel"_ (footnote)

**Also in this area:**

- 3 thumbnail images showing social media posts / before-after photos
- Carousel arrows `‹ ›` for swiping

**Liquid:**

```liquid
{%- comment -%} sections/lp-social-proof.liquid {%- endcomment -%}
<section class="lp-social-proof">
  <div class="page-width">
    <div class="trustpilot-badge">
      <span class="trustpilot-stars">★★★★★</span>
      <span>{{ section.settings.trustpilot_count }} Customers Worldwide</span>
    </div>
    <h2>{{ section.settings.heading }}</h2>

    <div class="stat-circles">
      {%- for block in section.blocks -%}
        {%- if block.type == 'stat' -%}
          <div class="stat-circle" {{ block.shopify_attributes }}>
            <div class="stat-circle__ring" style="--pct: {{ block.settings.percentage }}">
              <span class="stat-circle__number">{{ block.settings.percentage }}%</span>
            </div>
            <p class="stat-circle__label">{{ block.settings.label }}</p>
            <small class="stat-circle__footnote">{{ block.settings.footnote }}</small>
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>

    {%- comment -%} Social proof image carousel {%- endcomment -%}
    <div class="social-carousel">
      {%- for block in section.blocks -%}
        {%- if block.type == 'social_image' -%}
          <div class="social-carousel__item" {{ block.shopify_attributes }}>
            {{ block.settings.image | image_url: width: 300 | image_tag: loading: 'lazy' }}
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>
  </div>
</section>
```

**CSS for stat circles (use CSS conic-gradient):**

```css
.stat-circle__ring {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: conic-gradient(
    var(--color-accent-teal) calc(var(--pct) * 1%),
    #e0e0e0 0
  );
  display: flex;
  align-items: center;
  justify-content: center;
}
```

---

### 13. REVIEWS SECTION

**Headline:** _"Customer Reviews"_
**Rating Summary:**

- `4.75 out of 5` — Based on 167 reviews ✅
- Star breakdown:
  - ★★★★★: 136
  - ★★★★☆: 22
  - ★★★☆☆: 8
  - ★★☆☆☆: 1
  - ★☆☆☆☆: 0
- "Diamond Authenticity 100.0" badge (blue wreath icon)

**Review feed (paginated, 3 pages shown):**

- Sort by: "Most Recent ▾"
- Each review card:
  - ★★★★★ stars + date (e.g., `02/27/2026`)
  - Avatar icon + Name + "Verified" badge
  - Review text body

**"Write a review" button:** Outlined red/coral border, white background

**Liquid** — Use a review app metafield or Shopify native product reviews:

```liquid
{%- comment -%} sections/lp-reviews.liquid {%- endcomment -%}
<section class="lp-reviews" id="Reviews">
  <div class="page-width">
    <h2>Customer Reviews</h2>

    <div class="review-summary">
      <div class="review-summary__score">{{ product.metafields.reviews.rating }}</div>
      <div class="review-summary__bars">
        {%- for i in (1..5) reversed -%}
          <div class="rating-bar">
            <span>{{ i }} ★</span>
            <div class="rating-bar__track">
              <div class="rating-bar__fill" style="width: {{ product.metafields.reviews['rating_' | append: i] }}%"></div>
            </div>
            <span>{{ product.metafields.reviews['count_' | append: i] }}</span>
          </div>
        {%- endfor -%}
      </div>
      <a href="#review-form" class="btn btn--outline btn--write-review">Write a review</a>
    </div>

    {%- comment -%} Review items — populated by review app (e.g. Yotpo, Judge.me) {%- endcomment -%}
    <div class="review-list">
      {%- paginate product.metafields.reviews.reviews by 5 -%}
        {%- for review in product.metafields.reviews.reviews -%}
          <div class="review-item">
            <div class="review-item__header">
              <div class="stars">{{ review.rating | times: '★' }}</div>
              <span class="review-item__date">{{ review.created_at | date: '%m/%d/%Y' }}</span>
            </div>
            <div class="review-item__author">
              <span class="avatar-icon">👤</span>
              <strong>{{ review.author }}</strong>
              {%- if review.verified -%}<span class="verified-badge">Verified</span>{%- endif -%}
            </div>
            <p class="review-item__body">{{ review.body }}</p>
          </div>
        {%- endfor -%}
        {% render 'pagination', paginate: paginate %}
      {%- endpaginate -%}
    </div>
  </div>
</section>
```

---

### 14. TRUST ICONS BAR

**Layout:** 4-column icon grid (centered, white background)
**Items:**

| Icon                   | Title                          | Subtitle                                 |
| ---------------------- | ------------------------------ | ---------------------------------------- |
| 🚚 Free shipping truck | "Free Shipping from USA"       | "On all orders"                          |
| 🌿 Leaf/plant          | "Naturally Supports Your Body" | "Promotes healthy immune cell functions" |
| 🍃 Natural leaf        | "100% Natural Ingredients"     | "8 active, natural ingredients"          |
| 📅 60-day calendar     | "Try it Risk Free for 60 Days" | "60-day money-back guarantee"            |

**Liquid:**

```liquid
{%- comment -%} sections/lp-trust-icons.liquid {%- endcomment -%}
<section class="lp-trust-icons">
  <div class="page-width">
    <div class="trust-icons-grid">
      {%- for block in section.blocks -%}
        {%- if block.type == 'trust_item' -%}
          <div class="trust-item" {{ block.shopify_attributes }}>
            {%- if block.settings.icon_image != blank -%}
              {{ block.settings.icon_image | image_url: width: 64 | image_tag: loading: 'lazy', class: 'trust-item__icon' }}
            {%- elsif block.settings.icon_svg != blank -%}
              <div class="trust-item__icon">{{ block.settings.icon_svg }}</div>
            {%- endif -%}
            <h4 class="trust-item__title">{{ block.settings.title }}</h4>
            <p class="trust-item__subtitle">{{ block.settings.subtitle }}</p>
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>
  </div>
</section>
```

---

### 15. EXPERT ADVICE SECTION

**Layout:** Text left (60%) + Image right (40%)
**Background:** White

**Content:**

- Small label: _"Expert Advice From:"_
- Name: _"Dr. Emily Chen of a New York Skin Clinic"_
- Long expert quote about cellulite and lymphatic drainage (3–4 paragraphs)
- Includes quote: _"...breaks down the fat cells in your skin."_
- CTA (text link, subtle): _"Try Lymphatic Drainage Risk-Free"_
- Below CTA: 🔒 _"60-Day Money-Back Guarantee"_ (badge icon)

**Right:** Professional photo of woman (Dr. Emily Chen) in black top

---

### 16. TRANSFORMATION STORIES SECTION

**Background:** Off-white sage (`#f1f4f1`)
**Trustpilot bar:** `★★★★★ 93,000+ Customers Worldwide`
**Headline:** _"See The Stories of Sculptique™ Women Firsthand"_

**Layout:** Customer story cards with before/after photos

---

### 17. PRICING / BUNDLE BUY BOX

This appears both **in the hero sidebar** and as a **dedicated CTA section** further down the page.

**Bundle Options (radio-button selector cards):**

| Option      | Bundle                       | Price      | Original    | Notes                                                          |
| ----------- | ---------------------------- | ---------- | ----------- | -------------------------------------------------------------- | --------------------- |
| Option 1    | 1 Bottle                     | **$31.96** | ~~$59.95~~  | Save $27.99 / Free USA Shipping                                |
| Option 2 ⭐ | Buy 2 Get 1 Free (3 bottles) | **$63.92** | ~~$179.85~~ | Save $115.93 / Free USA Shipping / Free E-book                 | "Spring Sale +" badge |
| Option 3    | Buy 3 Get 2 Free (5 bottles) | **$95.88** | ~~$299.75~~ | Save $203.87 / Free USA Shipping / Free E-book / $20 Gift Card |

**Add-ons shown for Options 2 & 3:**

- ☐ Free Anti-Bloating Protocol E-book
- ☐ $20 Gift Card (option 3 only)

**Delivery estimate:** _"Delivered on Monday, 9 March with Express Shipping"_

**Liquid:**

```liquid
{%- comment -%} snippets/bundle-buy-box.liquid {%- endcomment -%}
<div class="bundle-buy-box" id="BundleBuyBox">
  <div class="bundle-options">
    {%- for variant in product.variants -%}
      <label class="bundle-option {% if forloop.index == 2 %}bundle-option--featured{% endif %}"
             for="bundle-{{ variant.id }}">
        {%- if forloop.index == 2 -%}
          <span class="bundle-option__badge">Spring Sale +</span>
        {%- endif -%}
        <input type="radio"
               id="bundle-{{ variant.id }}"
               name="bundle-variant"
               value="{{ variant.id }}"
               {% if forloop.first %}checked{% endif %}>
        <div class="bundle-option__content">
          <div class="bundle-option__title">{{ variant.title }}</div>
          <div class="bundle-option__pricing">
            <span class="bundle-option__price">{{ variant.price | money }}</span>
            {%- if variant.compare_at_price > variant.price -%}
              <span class="bundle-option__compare">{{ variant.compare_at_price | money }}</span>
              <span class="bundle-option__save">Save {{ variant.compare_at_price | minus: variant.price | money }}</span>
            {%- endif -%}
          </div>
          <div class="bundle-option__perks">
            <span>✓ Free USA Shipping</span>
            {%- if forloop.index >= 2 -%}
              <span>✓ Free Anti-Bloating Protocol E-book</span>
            {%- endif -%}
            {%- if forloop.index == 3 -%}
              <span>✓ $20 Gift Card</span>
            {%- endif -%}
          </div>
        </div>
      </label>
    {%- endfor -%}
  </div>

  <button type="submit"
          name="add"
          class="btn btn--primary btn--full-width"
          id="AddToCart">
    {{ 'products.product.add_to_cart' | t }}
  </button>

  <div class="buy-box__delivery">
    <span class="delivery-icon">🚚</span>
    Delivered on <strong>{{ 'now' | date: '%A, %-d %B' }}</strong> with Express Shipping
  </div>
</div>
```

---

### 18. FAQ SECTION

**Type:** Collapsible accordion
**Typical Shopify section:** `collapsible-content.liquid`

**Suggested schema structure:**

```json
{
  "name": "FAQ",
  "type": "faq_item",
  "settings": [
    { "type": "text", "id": "question", "label": "Question" },
    { "type": "richtext", "id": "answer", "label": "Answer" }
  ]
}
```

---

### 19. FOOTER

**Minimal footer layout:**

- Links: Privacy Policy | Terms of Service | Refund Policy | Contact
- Copyright: `© 2026, Sculptique`
- Payment icons (Visa, Mastercard, PayPal, etc.)

---

## 📋 Shopify Template Recommendation

**Template file:** `templates/product.json`

```json
{
  "sections": {
    "trust_bar": { "type": "lp-trust-bar" },
    "main_product": { "type": "main-product" },
    "symptoms": { "type": "lp-symptoms" },
    "root_cause": { "type": "lp-root-cause" },
    "science": { "type": "lp-science" },
    "hidden_system": { "type": "lp-hidden-system" },
    "why_failed": { "type": "lp-why-failed" },
    "missing_piece": { "type": "lp-missing-piece" },
    "ingredients": { "type": "lp-ingredients" },
    "synergistic": { "type": "lp-synergistic" },
    "social_proof": { "type": "lp-social-proof" },
    "reviews": { "type": "lp-reviews" },
    "trust_icons": { "type": "lp-trust-icons" },
    "expert": { "type": "lp-expert" },
    "transformations": { "type": "lp-transformations" },
    "faq": { "type": "lp-faq" }
  },
  "order": [
    "trust_bar",
    "main_product",
    "symptoms",
    "root_cause",
    "science",
    "hidden_system",
    "why_failed",
    "missing_piece",
    "ingredients",
    "synergistic",
    "social_proof",
    "reviews",
    "trust_icons",
    "expert",
    "transformations",
    "faq"
  ]
}
```

---

## 🖼️ Screenshot Reference

Captured screenshots from the original PDF (24 screenshots across 17 pages):

| File                  | Content                                                              |
| --------------------- | -------------------------------------------------------------------- |
| `pdf_ui_01_top`       | Page 1 – Hero (product image + headline + benefits + Trustpilot)     |
| `pdf_ui_02_mid`       | Page 1 – Pricing bundle selector cards                               |
| `pdf_ui_03_bottom`    | Page 1–2 – Lower hero / Press logos (Vogue, BuzzFeed, Allure)        |
| `pdf_ui_04_p2_bot`    | Page 2–3 – Problem intro                                             |
| `pdf_ui_05_p3_top`    | Page 3 – 5-column symptom grid with images and captions              |
| `pdf_ui_06_p3_mid`    | Page 3 – Arrow callout + pink "Here's what nobody's telling you" box |
| `pdf_ui_07_p4_top`    | Page 4 – Symptom / Root cause explanation table                      |
| `pdf_ui_08_p5_top`    | Page 5 – Symptom table + "Your Hidden Drainage System" section intro |
| `pdf_ui_09_p5_bot_p6` | Pages 5-6 – Science diagram, lymph vessel explanation                |
| `pdf_ui_10_p6_mid`    | Page 6 – Anatomy diagram + post-35 lymph failure chart               |
| `pdf_ui_11_p7`        | Page 7 – "Why Nothing Has Worked"                                    |
| `pdf_ui_12_p7_p8`     | Pages 7–8 – Missing piece section                                    |
| `pdf_ui_13_p8`        | Page 8 – 8-Ingredient System heading + 4-mechanism grid              |
| `pdf_ui_14_p9`        | Page 9 – Ingredient cards (Cleavers, Dandelion, Bromelain, Rutin)    |
| `pdf_ui_15_p9_p10`    | Pages 9–10 – More ingredient cards (Burdock, Echinacea, Kelp, Lemon) |
| `pdf_ui_16_p10_p11`   | Pages 10–11 – Synergistic Effect section                             |
| `pdf_ui_17_p11`       | Page 11 – Real Women results section + stat circles (87%, 91%)       |
| `pdf_ui_18_p12`       | Page 12 – Social proof image carousel                                |
| `pdf_ui_19_p12_p13`   | Pages 12–13 – Review star breakdown + paginated reviews              |
| `pdf_ui_20_p13_p14`   | Pages 13–14 – Trustpilot + "See The Stories" heading                 |
| `pdf_ui_21_p14_p15`   | Pages 14–15 – Expert Dr. Emily Chen section                          |
| `pdf_ui_22_p15_p16`   | Pages 15–16 – Review feed + Trust Icons bar                          |
| `pdf_ui_23_p16_p17`   | Pages 16–17 – More reviews                                           |
| `pdf_ui_24_end`       | Page 17 – End of page / footer                                       |

> **Screenshot directory:** `/Users/thanglee/.gemini/antigravity/brain/2d4eb6e0-331f-4eb9-9c71-7838fe30217b/`

---

## 🛠️ Implementation Notes for Shopify Liquid Devs

1. **New custom sections needed:** All `lp-*` sections are custom (not in Dawn base theme). Create each in `/sections/`.
2. **Product variant structure:** Set up 3 variants (1-bottle, 3-bottle, 5-bottle) in Shopify admin. Use variant titles for display.
3. **Metafields needed:**
   - `product.metafields.custom.review_score` → Trustpilot score string
   - `product.metafields.custom.review_count` → Review count
   - `product.metafields.custom.clinicians_count` → Clinician count
4. **Review app:** This page uses a third-party review system. Recommend **Judge.me** or **Yotpo** for the review breakdown + paginated feed.
5. **Bundle pricing:** Recommend **Shopify Bundles app** or custom variant approach. The bundle selector UI is fully custom — not default Shopify.
6. **Fonts:** Add Google Fonts import to `theme.liquid`:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com" />
   <link
     href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@400;500;600&display=swap"
     rel="stylesheet"
   />
   ```
7. **Colors:** Set as CSS variables in `base.css` or `theme.liquid`:
   ```css
   :root {
     --color-bg-primary: #f1f4f1;
     --color-accent-teal: #008b7d;
     --color-accent-gold: #d4a017;
     --color-bg-pink: #f8e7e7;
   }
   ```
8. **Mobile:** All sections must stack single-column on mobile. The symptom grid (5-col) should scroll horizontally on mobile or collapse to 2-col.
9. **Performance:** Lazy-load all images except hero product image (use `preload: true` on hero).
10. **Trustpilot widget:** The Trustpilot star bar is a direct embed. Add Trustpilot TrustBox widget script to `theme.liquid`.
