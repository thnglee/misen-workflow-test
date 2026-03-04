# 5-Hour Development Plan: Sculptique Product Page

Based on the `instructions.md` mapping for the Shopify Dawn theme, here is a structured 5-hour development sprint to implement the Sculptique Product Page.

---

## 🕒 Hour 1: Environment Setup & Data Prep (0:00 - 1:00)

**Goal: Prepare the theme environment and Shopify backend data.**

- **0:00 - 0:15 | Theme Setup:** Duplicate the live Dawn theme for development (Name it "Sculptique Product Page Dev").
- **0:15 - 0:30 | CSS Variables:** Add the required color variables (`--color-trustpilot`, `--color-bg-sage`, `--color-accent-teal`, `--color-accent-gold`) to `base.css` or as a `<style>` block scoped to the new sections.
- **0:30 - 1:00 | Product Data Configuration:** In the Shopify Admin, create/update the "Lymph-CC-Select" product. Set up the 3 variant options (1 Bottle, Buy 2 Get 1 Free, Buy 3 Get 2 Free) with appropriate prices and compare-at prices to match the UI bundle options.

## 🕒 Hour 2: Core Product Section & Schema Mods (1:00 - 2:00)

**Goal: Implement the custom `main-product.liquid` modifications.**

- **1:00 - 1:15 | Block Schema:** Modify the `main-product.liquid` schema to register new blocks: `trustpilot_rating`, `benefits_list`, and `clinicians_badge`.
- **1:15 - 1:30 | Liquid Code Injection:** Insert the corresponding Liquid `{% when '...' %}` snippet code for the Trustpilot, Benefits, and Clinicians Badge inside the `main-product.liquid` rendering loop.
- **1:30 - 2:00 | Custom Bundle Selector (Variant Picker):** Rebuild the `variant_picker` block as specified in instructions to use radio-style cards. Inject the associated CSS for `.bundle-selector` and `.bundle-option` specifically handling the "Spring Sale +" badge and active states. Test the `variant-radios` change events to ensure native Dawn AJAX add-to-cart still functions.

## 🕒 Hour 3: Theme Editor Assembly - Top Half (2:00 - 3:00)

**Goal: Map Markdown sections 1-7 using native Dawn sections via Theme Editor.**

- **2:00 - 2:15 | Header & Trust/Press Bar:** Configure standard `header`. Add a `multicolumn` section (4 columns, images only, grayscale via custom CSS) for the Press logos (Vogue, Buzzfeed, etc.).
- **2:15 - 2:35 | Hero, Problem & Symptoms:** Hook up the `main-product` hero section in the theme editor using the new blocks. For the Problem section, use a `multicolumn` (5 columns) for symptoms, followed by a `rich-text` block for the pink callout.
- **2:35 - 3:00 | Root Cause & Education:** Build the Symptom-to-Root-Cause table using a barebones `custom-liquid` block and layout utility classes. For the Science section, alternate layouts of native `image-with-text` sections.

## 🕒 Hour 4: Theme Editor Assembly - Bottom Half (3:00 - 4:00)

**Goal: Map Markdown sections 8-12 using native Dawn sections via Theme Editor.**

- **3:00 - 3:20 | Missing Piece & Ingredients:** Use `image-with-text` for the "Nothing Worked" section and pale green `rich-text` for the Missing Piece. Map the 8-Ingredient system to a `multicolumn` (4 columns), optionally utilizing Dawn's `collapsible_content` for ingredient details.
- **3:20 - 3:45 | Synergistic Effect & Social Proof:** Add `rich-text` for the Synergistic Effect. For the Social Proof results, create a `custom-liquid` block utilizing CSS `conic-gradient` to build the stat circles (87% and 91%) within `page-width`.
- **3:45 - 4:00 | Reviews Integration:** Add the app block for Shopify Product Reviews (or Judge.me/Yotpo) to handle the star breakdown and paginated review feed.

## 🕒 Hour 5: Trust Icons, Footer, Polish & QA (4:00 - 5:00)

**Goal: Finish remaining sections, verify mobile responsiveness, and QA the UX.**

- **4:00 - 4:20 | Trust Icons, Expert Advice & FAQ:** Use `multicolumn` (4 columns) for Trust Icons (Shipping, Natural, Guarantee). Map Expert Advice to `image-with-text`. Build the FAQ section using Dawn's native `collapsible_content`. Let `footer` remain global.
- **4:20 - 4:40 | Mobile & Layout Polish:** Review the page on mobile. If native `image-with-text` sections stack image-on-top on mobile where text-on-top is needed, inject target CSS (`flex-direction: column-reverse;`) for those specific Section IDs.
- **4:40 - 5:00 | Final QA & Testing:**
  - Test the add-to-cart button from both the Hero and the lower Buy Box.
  - Check that bundle pricing matches selections dynamically.
  - Ensure all images load correctly and use `loading="lazy"` where appropriate.
  - Validate cross-browser styling for flexbox layouts and the CSS pie charts.
