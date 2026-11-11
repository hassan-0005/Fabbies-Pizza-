"""
FABBIES - Premium Animated Restaurant Menu Website
Framework: Streamlit & Streamlit Cloud compatible
Author: Senior UI/UX & Restaurant Brand Developer
"""

import streamlit as st

st.set_page_config(
    page_title="FABBIES | Food Is My Best Friend",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CENTRALIZED EDITABLE MENU DATA DICTIONARY
MENU_DATA = {
    "brand": {
        "name": "FABBIES",
        "tagline": "FOOD IS MY BEST FRIEND",
        "subtitle": "Taste the Happiness",
        "headline": "The Daily Fabbies Menu",
        "description": "At Fabbies, excellence isn't just a goal — it's a way of life. From our meticulously prepared dishes to our spotless dining area, we strive for perfection in everything we do.",
        "phone": "+92 300 1234567",
        "whatsapp": "923001234567",
        "location": "Main Boulevard, Commercial Center, Pakistan",
        "hours": "Mon - Sun: 12:00 PM - 02:00 AM",
        "facebook_url": "https://facebook.com/fabbiespizza",
        "instagram_url": "https://instagram.com/fabbiespizza",
    },
    "pizzas": {
        "deep_dish": [
            {
                "name": "Peri Peri Deep Dish",
                "desc": "Thick golden deep pan crust loaded with peri peri chicken, molten cheese blend, and signature spicy drizzle.",
                "prices": {"Medium": "1,449", "Large": "1,949"},
                "badge": "Signature",
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "BBQ Texas Deep Dish",
                "desc": "Slow-smoked Texas style BBQ chicken chunks with smoky glaze, double mozzarella, and herbs in deep dish pan.",
                "prices": {"Medium": "1,449", "Large": "1,949"},
                "badge": "Bestseller",
                "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Garlic Butter Deep Dish",
                "desc": "Herb-infused garlic butter dough topped with aromatic shredded chicken, garlic emulsion, and aged cheese.",
                "prices": {"Medium": "1,449", "Large": "1,949"},
                "badge": "Chef Special",
                "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=800&q=80",
            },
        ],
        "extreme": [
            {
                "name": "Mild Extreme",
                "desc": "Loaded with gentle zesty spices, bell peppers, golden corn, and tender chicken chunks over savory marinara.",
                "prices": {'10" Medium': "1,349", '13" Large': "1,749"},
                "badge": "Mild & Cheesy",
                "image": "https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Classic Extreme",
                "desc": "The ultimate party pizza packed with chicken pepperoni, diced capsicum, black olives, onions, and spicy red sauce.",
                "prices": {'10" Medium': "1,349", '13" Large': "1,749"},
                "badge": "Extreme Flavor",
                "image": "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?auto=format&fit=crop&w=800&q=80",
            },
        ],
        "crown_crust": [
            {
                "name": "Royal Crown Crust Pizza",
                "desc": "Hand-pinched crown crust stuffed with melted cream cheese & kebab pockets, topped with chicken fajita and black olives.",
                "prices": {'10" Medium': "1,249", '13" Large': "1,599"},
                "badge": "Crown Special",
                "image": "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?auto=format&fit=crop&w=800&q=80",
            }
        ],
        "stuffed_crust": [
            {
                "name": "Kabab Crust Pizza",
                "desc": "Savory baked shami/seekh kabab roll ringed entirely inside the outer crust for pure indulgence in every bite.",
                "prices": {"Standard": "575"},
                "badge": "Traditional Fusion",
                "image": "https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Cheese Stuffed Crust",
                "desc": "Crust edge bursting with pure melted mozzarella strings and seasoned garlic herb dusting.",
                "prices": {'Medium 10"': "1,075"},
                "badge": "Extra Cheese",
                "image": "https://images.unsplash.com/photo-1594007654729-407eedc4be65?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Mild Stuffed Crust",
                "desc": "Mild spiced cream cheese blend stuffed rim with juicy chicken supreme toppings.",
                "prices": {'Large 13"': "1,499"},
                "badge": "Grand Feast",
                "image": "https://images.unsplash.com/photo-1588315029754-2dd089d39a1a?auto=format&fit=crop&w=800&q=80",
            },
        ],
    },
    "appetizers": [
        {
            "name": "Fried Tender Strips",
            "desc": "Hand-breaded golden crispy chicken breast tenders served piping hot with secret garlic mayo dip.",
            "serving": "5 Pcs",
            "price": "480",
            "image": "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Artisan Garlic Bread",
            "desc": "Freshly toasted baguette slices brushed with garlic parsley butter and melted parmesan.",
            "serving": "5 Pcs / 10 Pcs",
            "price": "250 / 450",
            "image": "https://images.unsplash.com/photo-1619860860774-1e2e17343432?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Oven Baked Wings",
            "desc": "Juicy oven-roasted wings marinated in secret spices, finished to a tender and smokey perfection.",
            "serving": "6 Pcs",
            "price": "349",
            "image": "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy BBQ Wings",
            "desc": "Golden fried wings tossed liberally in sweet and smoky Texas hickory barbecue sauce.",
            "serving": "6 Pcs",
            "price": "380",
            "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Golden Nuggets",
            "desc": "Crispy crumb-coated minced chicken bites seasoned lightly with white pepper and celery salt.",
            "serving": "5 Pcs / 10 Pcs",
            "price": "300 / 550",
            "image": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Classic French Fries",
            "desc": "Golden straight-cut Idaho potatoes tossed with sea salt, crisp on outside and fluffy inside.",
            "serving": "Only Fries",
            "price": "199",
            "image": "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Fully Loaded Fries",
            "desc": "Heaped fries drenched with warm melted cheese, jalapeños, crispy chicken chunks & chipotle mayo.",
            "serving": "Platter Size",
            "price": "649",
            "image": "https://images.unsplash.com/photo-1585109649139-366815a0d713?auto=format&fit=crop&w=800&q=80",
        },
    ],
    "burgers": {
        "fried": [
            {
                "name": "Zinger Chipotle",
                "desc": "Extra crispy whole muscle chicken fillet topped with smokey chipotle sauce, lettuce, and pickles.",
                "price": "399",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Classic Chicken Patty",
                "desc": "Savory seasoned minced chicken patty grilled soft with cream mayonnaise and crunchy iceberg.",
                "price": "249",
                "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Signature Zinger Burger",
                "desc": "The town's favorite spicy fried fillet coated in crunchy batter, crowned with chilled lettuce.",
                "price": "349",
                "image": "https://images.unsplash.com/photo-1625813506062-0aeb1d7a094b?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Crunch Burger",
                "desc": "Double crisp crumbed fillet with tangy dressing, melted cheese slice, and sweet toasted bun.",
                "price": "299",
                "image": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Colossal Tower Burger",
                "desc": "Twin towering zinger fillets stacked high with golden hashbrown, double cheese, and zesty sauce.",
                "price": "499",
                "image": "https://images.unsplash.com/photo-1582196016295-f8c8bd4b3e99?auto=format&fit=crop&w=800&q=80",
            },
        ],
        "grilled": [
            {
                "name": "Grilled Beef Patty",
                "desc": "Flame-seared 100% prime ground beef patty topped with smoked caramelized onions, cheddar, and BBQ glaze.",
                "price": "649",
                "image": "https://images.unsplash.com/photo-1553979459-d2229ba7433b?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Chicken Spark Jalapeno",
                "desc": "Char-grilled spicy breast fillet smothered in fiery jalapeño rings, melted Monterey jack, and chili mayo.",
                "price": "499",
                "image": "https://images.unsplash.com/photo-1520072959219-c595dc870360?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Flamin Cheeto's Fillet",
                "desc": "Crispy chicken breast crust rolled in crushed flaming red Cheetos with warm cheese volcanic drip.",
                "price": "499",
                "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?auto=format&fit=crop&w=800&q=80",
            },
        ],
    },
    "wraps_and_sandwiches": {
        "wraps": {
            "title": "Crispy Tortilla Wraps",
            "flavors": ["Chipotle", "Jalapeno", "Garlic", "Honey Mustard", "Peri Peri"],
            "base_price": "549",
            "addons": [
                {"name": "Black Olives", "price": "60"},
                {"name": "Extra Melted Cheese", "price": "60"},
                {"name": "Pickled Jalapenos", "price": "60"},
                {"name": "Sautéed Mushrooms", "price": "60"},
            ],
            "desc": "Crispy shredded chicken folded inside a warm toasted flour tortilla with fresh greens and choice of artisan drizzle.",
            "image": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=800&q=80",
        },
        "sandwiches": [
            {
                "name": "Grand Club Sandwich",
                "desc": "Triple-decker toasted bread filled with chicken spread, fried egg, cucumber, tomato slice, and cheese.",
                "price": "540",
                "sides": "Served with Golden Fries & Fresh Coleslaw",
                "image": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Cocktail Sandwich",
                "desc": "Zesty shredded chicken dressed in secret cocktail sauce, stacked neatly with crisp greens.",
                "price": "540",
                "sides": "Served with Golden Fries & Fresh Coleslaw",
                "image": "https://images.unsplash.com/photo-1554433607-66b5efe9d304?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "BBQ Grilled Sandwich",
                "desc": "Grilled chicken strips glazed with sweet and spicy hickory sauce, grilled pressed between buttered slices.",
                "price": "540",
                "sides": "Served with Golden Fries & Fresh Coleslaw",
                "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
            },
        ],
    },
    "pastas": [
        {
            "name": "Classic Al-Fredo Pasta",
            "desc": "Fettuccine pasta enrobed in rich parmesan garlic cream sauce, grilled chicken strips, black olives, and melted mozzarella crust.",
            "price": "749",
            "badge": "Creamy Rich",
            "image": "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Flaming Pasta",
            "desc": "Fiery penne pasta simmered in spicy arrabbiata tomato emulsion with crushed red chilies, herbs, and tender chicken.",
            "price": "599",
            "badge": "Hot & Spicy",
            "image": "https://images.unsplash.com/photo-1621996346565-e3d5d6281724?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Tong Twister Pasta",
            "desc": "Our signature tangy-savory fusion pasta baked in clay dish under a blanket of browned golden cheese.",
            "price": "749",
            "badge": "House Favorite",
            "image": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80",
        },
    ],
    "fried_chicken": [
        {
            "name": "Crispy Whole Chicken (8 Pcs)",
            "desc": "Full 8-piece chicken marinated overnight in proprietary spices, pressure fried for ultimate crunch and juiciness.",
            "price": "1,499",
            "serving": "8 Pieces Bucket",
            "image": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy Drum Stick",
            "desc": "Plump and juicy single chicken drumstick with thick, crispy textured outer coating.",
            "price": "249",
            "serving": "1 Piece",
            "image": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy Thai Piece",
            "desc": "Succulent bone-in chicken thigh with delicate golden flaky crust and tender meat.",
            "price": "299",
            "serving": "1 Piece",
            "image": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy Hot Wings",
            "desc": "Deep golden crunchy chicken wings sprinkled with signature spicy dusting.",
            "price": "399",
            "serving": "6 Pieces",
            "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy Hot Shots",
            "desc": "Bite-sized pops of 100% boneless tender chicken breast, fried to an irresistible golden crisp.",
            "price": "499",
            "serving": "10 Pieces Box",
            "image": "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=800&q=80",
        },
    ],
    "platters": [
        {
            "name": "Behari Platter",
            "desc": "4 Pieces of cheese-stuffed Behari Rolls + 6 Pieces of tender Baked Wings + Crispy Fries + Signature Garlic Dip Sauce.",
            "price": "749",
            "includes": "4 Behari Rolls • 6 Baked Wings • Crispy Fries • Dip Sauce",
            "badge": "Best Value Combo",
            "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Sandwich Platter",
            "desc": "1 Grand Club or Grilled Sandwich + 4 Pieces Golden Crispy Wings + Fresh Coleslaw + Heaped Seasoned Fries.",
            "price": "699",
            "includes": "1 Full Sandwich • 4 Crispy Wings • 1 Fries • 1 Coleslaw",
            "badge": "Hunger Buster",
            "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
        },
    ],
    "behari_rolls": {
        "name": "Signature Behari Rolls",
        "desc": "Marinated Behari chicken seasoned with charred spices, tender onions, melted cheese, wrapped carefully in warm flaky pita tortilla bread, baked to perfection and served with house dipping sauce.",
        "serving": "4 Pieces Box",
        "price": "499",
        "badge": "Customer Obsession",
        "image": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=800&q=80",
    },
}

HTML_HEADER = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
#MainMenu, header, footer, .stDeployButton { visibility: hidden !important; display: none !important; }
div.block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
html { scroll-behavior: smooth; background-color: #0c0d0f; }
body { background-color: #0c0d0f; color: #f3f4f6; font-family: 'Montserrat', sans-serif; overflow-x: hidden; }

:root {
  --gold: #F5C518;
  --gold-glow: rgba(245, 197, 24, 0.3);
  --red: #E63932;
  --bg-card: #141519;
  --bg-card-hover: #1b1d22;
}

.hero-screen {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  background: radial-gradient(circle at 50% 50%, #1e2026 0%, #0a0b0d 100%);
  text-align: center;
  padding: 3rem 1.5rem;
}

.brand-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(3.5rem, 9vw, 7rem);
  font-weight: 900;
  color: #fff;
  background: linear-gradient(180deg, #FFFFFF 20%, #F5C518 80%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0;
  letter-spacing: 2px;
}

.brand-tagline {
  font-size: clamp(1rem, 2.5vw, 1.8rem);
  font-weight: 800;
  letter-spacing: 5px;
  color: #fff;
  text-transform: uppercase;
  margin: 1rem 0;
}

.sticky-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(13, 14, 18, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(245, 197, 24, 0.2);
  padding: 0.8rem 1rem;
  display: flex;
  justify-content: center;
  gap: 0.8rem;
  overflow-x: auto;
  white-space: nowrap;
}

.nav-link-btn {
  padding: 0.5rem 1.2rem;
  border-radius: 30px;
  background: rgba(255,255,255,0.06);
  color: #eee;
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 700;
  transition: all 0.25s;
}

.nav-link-btn:hover {
  background: var(--gold);
  color: #000;
  box-shadow: 0 0 15px var(--gold-glow);
}

.menu-wrapper {
  max-width: 1300px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

.category-header {
  text-align: center;
  margin: 4rem 0 2rem 0;
}

.category-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 800;
  color: #fff;
  margin: 0.3rem 0;
}

.grid-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.8rem;
}

.card {
  background: var(--bg-card);
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.08);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s, border-color 0.3s;
}

.card:hover {
  transform: translateY(-6px);
  border-color: var(--gold);
}

.card-img {
  width: 100%;
  height: 220px;
  object-fit: cover;
}

.card-body {
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.card-title {
  font-family: 'Cinzel', serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: #fff;
  margin: 0 0 0.5rem 0;
}

.card-desc {
  font-size: 0.85rem;
  color: #999;
  line-height: 1.6;
  margin-bottom: 1.2rem;
  flex-grow: 1;
}

.card-price {
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--gold);
  border-top: 1px dashed rgba(255,255,255,0.1);
  padding-top: 0.8rem;
}
</style>
"""

st.markdown(HTML_HEADER, unsafe_allow_html=True)

# Render Landing & Sections
b = MENU_DATA["brand"]
st.markdown(
    f"""
<div class="hero-screen" id="hero">
  <div style="color:var(--gold); font-size:0.8rem; font-weight:800; letter-spacing:4px; text-transform:uppercase; margin-bottom:1rem;">Original Gourmet Experience</div>
  <h1 class="brand-title">{b['name']}</h1>
  <div class="brand-tagline">“ {b['tagline']} ”</div>
  <p style="color:#aaa; max-width:600px; margin: 0 auto 2rem auto; font-size:0.95rem; line-height:1.7;">{b['description']}</p>
  <a href="#menu-nav" style="color:var(--gold); font-weight:700; letter-spacing:3px; text-decoration:none; font-size:0.8rem;">
    SCROLL TO EXPLORE MENU <i class="fa-solid fa-chevron-down" style="margin-left:6px;"></i>
  </a>
</div>

<div class="sticky-nav" id="menu-nav">
  <a href="#pizzas" class="nav-link-btn">Pizzas</a>
  <a href="#appetizers" class="nav-link-btn">Appetizers</a>
  <a href="#burgers" class="nav-link-btn">Burgers</a>
  <a href="#wraps" class="nav-link-btn">Wraps & Sandwiches</a>
  <a href="#pastas" class="nav-link-btn">Pastas</a>
  <a href="#fried-chicken" class="nav-link-btn">Fried Chicken</a>
  <a href="#platters" class="nav-link-btn">Platters</a>
  <a href="#behari-rolls" class="nav-link-btn">Behari Rolls</a>
</div>
""",
    unsafe_allow_html=True,
)

# Render Categories
def make_card(item):
    prices_text = ""
    if "prices" in item:
        prices_text = " · ".join([f"{k}: Rs.{v}" for k, v in item["prices"].items()])
    else:
        prices_text = f"Rs. {item.get('price', '')}"
    
    return f"""
    <div class="card">
      <img src="{item['image']}" class="card-img" alt="{item['name']}">
      <div class="card-body">
        <h4 class="card-title">{item['name']}</h4>
        <p class="card-desc">{item['desc']}</p>
        <div class="card-price">{prices_text}</div>
      </div>
    </div>
    """

menu_html = """<div class="menu-wrapper">"""

# Pizzas
menu_html += """
<div id="pizzas" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Hand-Crafted</div>
  <h2 class="category-title">The Legendary Pizzas</h2>
</div>
<div class="grid-cards">
"""
for p in MENU_DATA["pizzas"]["deep_dish"] + MENU_DATA["pizzas"]["extreme"] + MENU_DATA["pizzas"]["crown_crust"] + MENU_DATA["pizzas"]["stuffed_crust"]:
    menu_html += make_card(p)
menu_html += "</div>"

# Appetizers
menu_html += """
<div id="appetizers" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Starters</div>
  <h2 class="category-title">Appetizers</h2>
</div>
<div class="grid-cards">
"""
for a in MENU_DATA["appetizers"]:
    menu_html += make_card(a)
menu_html += "</div>"

# Burgers
menu_html += """
<div id="burgers" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Crunch & Flame</div>
  <h2 class="category-title">Gourmet Burgers</h2>
</div>
<div class="grid-cards">
"""
for b_item in MENU_DATA["burgers"]["fried"] + MENU_DATA["burgers"]["grilled"]:
    menu_html += make_card(b_item)
menu_html += "</div>"

# Wraps & Sandwiches
menu_html += """
<div id="wraps" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Artisanal Layers</div>
  <h2 class="category-title">Wraps & Sandwiches</h2>
</div>
<div class="grid-cards">
"""
for sw in MENU_DATA["wraps_and_sandwiches"]["sandwiches"]:
    menu_html += make_card(sw)
menu_html += "</div>"

# Pastas
menu_html += """
<div id="pastas" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Italian Special</div>
  <h2 class="category-title">Artisanal Pastas</h2>
</div>
<div class="grid-cards">
"""
for pa in MENU_DATA["pastas"]:
    menu_html += make_card(pa)
menu_html += "</div>"

# Fried Chicken
menu_html += """
<div id="fried-chicken" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">11-Spice Batter</div>
  <h2 class="category-title">Crispy Fried Chicken</h2>
</div>
<div class="grid-cards">
"""
for fc in MENU_DATA["fried_chicken"]:
    menu_html += make_card(fc)
menu_html += "</div>"

# Platters
menu_html += """
<div id="platters" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Grand Combos</div>
  <h2 class="category-title">Fabbies Platters</h2>
</div>
<div class="grid-cards">
"""
for pl in MENU_DATA["platters"]:
    menu_html += make_card(pl)
menu_html += "</div>"

# Behari Rolls
menu_html += """
<div id="behari-rolls" class="category-header">
  <div style="color:var(--gold); font-size:0.75rem; font-weight:800; letter-spacing:3px; text-transform:uppercase;">Town Legend</div>
  <h2 class="category-title">Signature Behari Rolls</h2>
</div>
<div class="grid-cards">
"""
menu_html += make_card(MENU_DATA["behari_rolls"])
menu_html += "</div>"

menu_html += f"""
<footer style="margin-top:6rem; padding:3rem 0; border-top:1px solid rgba(245, 197, 24, 0.2); text-align:center;">
  <div style="font-family:'Cinzel', serif; font-size:1.8rem; font-weight:900; color:var(--gold);">{b['name']}</div>
  <p style="color:#aaa; font-size:0.85rem; margin:0.8rem 0 1.5rem 0;">{b['tagline']} · {b['hours']}</p>
  <a href="https://wa.me/{b['whatsapp']}" target="_blank" style="display:inline-block; padding:0.7rem 1.6rem; border-radius:30px; background:#25D366; color:#fff; text-decoration:none; font-weight:700; font-size:0.85rem;">
    Order on WhatsApp
  </a>
</footer>
</div>
"""

st.markdown(menu_html, unsafe_allow_html=True)
