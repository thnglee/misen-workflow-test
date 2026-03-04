/**
 * Product Information Section - Interaction JS
 * Vanilla JS replacement for jQuery buy-page.js
 *
 * Handles:
 * - Variant selector block clicks (radio-style selection)
 * - Subscription / One-Time-Purchase toggle
 * - Collapsible accordion tabs
 * - Add to Cart via Shopify AJAX API or Champs redirect
 */

document.addEventListener('DOMContentLoaded', function () {
  /* ========================================
     Variant Selector Block Clicks
     ======================================== */
  document.querySelectorAll('.product-selector_block').forEach(function (block) {
    block.addEventListener('click', function () {
      var outer = this.closest('.product-selector_outer');
      if (outer) {
        outer.querySelectorAll('.product-selector_block').forEach(function (b) {
          b.classList.remove('active');
        });
      }
      this.classList.add('active');

      // Toggle refill frequency notes
      var indexOpt = this.getAttribute('data-index');
      if (indexOpt) {
        document.querySelectorAll('.cta-note.changeble').forEach(function (note) {
          note.classList.add('hided');
        });
        var matchingNote = document.querySelector('.cta-note.changeble[data-id="' + indexOpt + '"]');
        if (matchingNote) {
          matchingNote.classList.remove('hided');
        }
      }
    });
  });

  /* ========================================
     Subscription / OTP Toggle (Autoship checkbox)
     ======================================== */
  document.querySelectorAll('.pp_var_autoship').forEach(function (autoship) {
    autoship.addEventListener('click', function () {
      this.classList.toggle('disabled');

      var subOuter = document.querySelector('.product-selector_outer[data="sub"]');
      var otpOuter = document.querySelector('.product-selector_outer[data="otp"]');

      if (this.classList.contains('disabled')) {
        // Switch to OTP
        if (subOuter) subOuter.classList.remove('active_block');
        if (otpOuter) otpOuter.classList.add('active_block');
      } else {
        // Switch to Subscription
        if (subOuter) subOuter.classList.add('active_block');
        if (otpOuter) otpOuter.classList.remove('active_block');
      }
    });
  });

  /* ========================================
     Collapsible Tabs
     ======================================== */
  document.querySelectorAll('.product_tab-block').forEach(function (tab) {
    tab.addEventListener('click', function () {
      this.classList.toggle('active');
    });
  });

  /* ========================================
     Add to Cart
     ======================================== */
  document.querySelectorAll('.product-selector_atc').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var modeChamps = this.getAttribute('data-mode-champs');

      if (modeChamps === 'true') {
        // Champs checkout redirect
        var activeOuter = document.querySelector('.product-selector_outer.active_block');
        if (activeOuter) {
          var activeBlock = activeOuter.querySelector('.product-selector_block.active');
          if (activeBlock) {
            var newUrl = activeBlock.getAttribute('data-champs-url');
            if (newUrl) {
              window.location.href = newUrl;
              return;
            }
          }
        }
      }

      // Shopify AJAX Cart API fallback
      var activeOuter = document.querySelector('.product-selector_outer.active_block');
      if (activeOuter) {
        var activeBlock = activeOuter.querySelector('.product-selector_block.active');
        if (activeBlock) {
          var variantId = activeBlock.getAttribute('data-id');
          if (variantId) {
            fetch('/cart/add.js', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ items: [{ id: parseInt(variantId), quantity: 1 }] })
            })
              .then(function (response) { return response.json(); })
              .then(function () {
                window.location.href = '/cart';
              })
              .catch(function (err) {
                console.error('Add to cart error:', err);
              });
          }
        }
      }
    });
  });

  /* ========================================
     Delivery Date Calculation
     ======================================== */
  var dateEl = document.querySelector('.col_pp_delivery__Date');
  if (dateEl) {
    var deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 5);
    var options = { weekday: 'long', day: 'numeric', month: 'long' };
    dateEl.textContent = deliveryDate.toLocaleDateString('en-US', options);
  }
});
