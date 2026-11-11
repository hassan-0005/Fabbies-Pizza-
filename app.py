"""
FABBIES - Premium Animated Restaurant Menu Website
Framework: Streamlit & Streamlit Community Cloud Compatible
Deploy: streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FABBIES | Food Is My Best Friend",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 1. CENTRALIZED EDITABLE RESTAURANT DATA
MENU_DATA = {
    "brand": {
        "name": "FABBIES",
        "tagline": "FOOD IS MY BEST FRIEND",
        "subtitle": "Taste the Happiness",
        "headline": "The Daily Fabbies Menu",
        "description": "At Fabbies, excellence isn't just a goal — it's a way of life. From our meticulously prepared dishes to our spotless dining atmosphere, we strive for perfection in every bite.",
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
            "badge": "Top Starter",
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
            "badge": "Smoky Baked",
            "image": "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy BBQ Wings",
            "desc": "Golden fried wings tossed liberally in sweet and smoky Texas hickory barbecue sauce.",
            "serving": "6 Pcs",
            "price": "380",
            "badge": "Sweet & Smoky",
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
            "badge": "Crowd Favorite",
            "image": "https://images.unsplash.com/photo-1585109649139-366815a0d713?auto=format&fit=crop&w=800&q=80",
        },
    ],
    "burgers": {
        "fried": [
            {
                "name": "Zinger Chipotle",
                "desc": "Extra crispy whole muscle chicken fillet topped with smokey chipotle sauce, lettuce, and pickles.",
                "price": "399",
                "badge": "Spicy & Smokey",
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
                "badge": "Fabbies Icon",
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
                "badge": "Monster Stack",
                "image": "https://images.unsplash.com/photo-1582196016295-f8c8bd4b3e99?auto=format&fit=crop&w=800&q=80",
            },
        ],
        "grilled": [
            {
                "name": "Grilled Beef Patty",
                "desc": "Flame-seared 100% prime ground beef patty topped with smoked caramelized onions, cheddar, and BBQ glaze.",
                "price": "649",
                "badge": "Flame Grilled",
                "image": "https://images.unsplash.com/photo-1553979459-d2229ba7433b?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Chicken Spark Jalapeno",
                "desc": "Char-grilled spicy breast fillet smothered in fiery jalapeño rings, melted Monterey jack, and chili mayo.",
                "price": "499",
                "badge": "Extra Hot",
                "image": "https://images.unsplash.com/photo-1520072959219-c595dc870360?auto=format&fit=crop&w=800&q=80",
            },
            {
                "name": "Flamin Cheeto's Fillet",
                "desc": "Crispy chicken breast crust rolled in crushed flaming red Cheetos with warm cheese volcanic drip.",
                "price": "499",
                "badge": "Trending Hit",
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
                "badge": "All-Day Classic",
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
                "badge": "Chef Special",
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
            "badge": "Family Bucket",
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
            "badge": "Spicy Crunch",
            "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?auto=format&fit=crop&w=800&q=80",
        },
        {
            "name": "Crispy Hot Shots",
            "desc": "Bite-sized pops of 100% boneless tender chicken breast, fried to an irresistible golden crisp.",
            "price": "499",
            "serving": "10 Pieces Box",
            "badge": "Snack Favorite",
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

# 2. RENDER CARD HELPER (Single-line HTML string to avoid Streamlit Markdown indentation/code block bugs)
def build_card(item):
    badge_html = f'<div class="card-badge">{item["badge"]}</div>' if "badge" in item else ""
    serving_html = f'<div class="card-serving">{item["serving"]}</div>' if "serving" in item else ""
    
    if "prices" in item:
        price_tags = "".join([f'<span class="price-chip">{k}: Rs.{v}</span>' for k, v in item["prices"].items()])
        price_html = f'<div class="card-prices-multi">{price_tags}</div>'
    else:
        price_html = f'<div class="card-price"><span class="rs">Rs.</span>{item.get("price", "")}</div>'

    return (
        f'<div class="food-card">'
        f'<div class="img-box">{badge_html}<img src="{item["image"]}" alt="{item["name"]}" loading="lazy"></div>'
        f'<div class="card-content">{serving_html}<h4 class="card-title">{item["name"]}</h4>'
        f'<p class="card-desc">{item["desc"]}</p>'
        f'<div class="card-bottom">{price_html}</div></div></div>'
    )

# 3. BUILD COMPLETE HTML STRING
b = MENU_DATA["brand"]

pizzas_all = (
    MENU_DATA["pizzas"]["deep_dish"]
    + MENU_DATA["pizzas"]["extreme"]
    + MENU_DATA["pizzas"]["crown_crust"]
    + MENU_DATA["pizzas"]["stuffed_crust"]
)
pizza_cards = "".join([build_card(p) for p in pizzas_all])
appetizer_cards = "".join([build_card(a) for a in MENU_DATA["appetizers"]])
burger_cards = "".join([build_card(b_item) for b_item in MENU_DATA["burgers"]["fried"] + MENU_DATA["burgers"]["grilled"]])
sandwich_cards = "".join([build_card(s) for s in MENU_DATA["wraps_and_sandwiches"]["sandwiches"]])
pasta_cards = "".join([build_card(pa) for pa in MENU_DATA["pastas"]])
chicken_cards = "".join([build_card(c) for c in MENU_DATA["fried_chicken"]])
platter_cards = "".join([build_card(pl) for pl in MENU_DATA["platters"]])
behari_cards = build_card(MENU_DATA["behari_rolls"])

wrap_data = MENU_DATA["wraps_and_sandwiches"]["wraps"]
wrap_addons = "".join([f'<span class="addon-chip">{a["name"]} (+Rs.{a["price"]})</span>' for a in wrap_data["addons"]])
wrap_flavors = " • ".join(wrap_data["flavors"])

COMPLETE_APP_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Montserrat:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; background: #0c0d0f; }}
body {{ background: #0c0d0f; color: #f3f4f6; font-family: 'Montserrat', sans-serif; overflow-x: hidden; }}

:root {{
  --gold: #F5C518;
  --gold-glow: rgba(245, 197, 24, 0.35);
  --red: #E63932;
  --bg-card: #141519;
  --bg-card-hover: #1c1d24;
}}

/* SCREEN 1 - FULLSCREEN BRAND HERO */
.hero-screen {{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  background: radial-gradient(circle at 50% 50%, #20222a 0%, #0a0b0d 100%);
  text-align: center;
  padding: 2.5rem 1rem;
  overflow: hidden;
}}

.hero-glow {{
  position: absolute;
  width: 550px;
  height: 550px;
  background: radial-gradient(circle, var(--gold-glow) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
  animation: pulse 6s infinite alternate;
}}

@keyframes pulse {{
  from {{ transform: scale(0.9); opacity: 0.6; }}
  to {{ transform: scale(1.15); opacity: 0.9; }}
}}

.floating-food {{
  position: absolute;
  border-radius: 50%;
  border: 2px solid rgba(245, 197, 24, 0.3);
  box-shadow: 0 15px 35px rgba(0,0,0,0.8), 0 0 20px var(--gold-glow);
  object-fit: cover;
  pointer-events: none;
  z-index: 2;
}}

.float-top-left {{ width: 160px; height: 160px; top: 8%; left: 4%; animation: float1 7s infinite ease-in-out; }}
.float-bot-left {{ width: 180px; height: 180px; bottom: 10%; left: 5%; animation: float2 8s infinite ease-in-out; }}
.float-top-right {{ width: 170px; height: 170px; top: 10%; right: 4%; animation: float2 7.5s infinite ease-in-out; }}
.float-bot-right {{ width: 190px; height: 190px; bottom: 8%; right: 5%; animation: float1 8.5s infinite ease-in-out; }}

@keyframes float1 {{
  0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
  50% {{ transform: translateY(-18px) rotate(3deg); }}
}}
@keyframes float2 {{
  0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
  50% {{ transform: translateY(18px) rotate(-3deg); }}
}}

.hero-content {{
  position: relative;
  z-index: 5;
  max-width: 820px;
}}

.brand-kicker {{
  display: inline-block;
  padding: 0.4rem 1.6rem;
  border-radius: 30px;
  background: rgba(245, 197, 24, 0.12);
  border: 1px solid var(--gold);
  color: var(--gold);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 4px;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}}

.brand-title {{
  font-family: 'Cinzel', serif;
  font-size: clamp(3.8rem, 10vw, 7.5rem);
  font-weight: 900;
  color: #fff;
  background: linear-gradient(180deg, #FFFFFF 20%, #F5C518 80%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1;
  letter-spacing: 3px;
  text-shadow: 0 10px 30px rgba(0,0,0,0.8);
}}

.brand-tagline {{
  font-size: clamp(1.1rem, 2.8vw, 1.9rem);
  font-weight: 800;
  letter-spacing: 5px;
  color: #fff;
  text-transform: uppercase;
  margin: 1.2rem 0 0.5rem 0;
}}

.brand-subtitle {{
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: clamp(1.1rem, 2.2vw, 1.4rem);
  color: var(--gold);
  margin-bottom: 1.8rem;
}}

.brand-bio {{
  font-size: 0.95rem;
  color: #a3a3a3;
  line-height: 1.7;
  max-width: 620px;
  margin: 0 auto 2.5rem auto;
}}

.scroll-prompt {{
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--gold);
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 3px;
  transition: all 0.3s;
}}
.scroll-prompt:hover {{ color: #fff; }}

.mouse-indicator {{
  width: 24px;
  height: 38px;
  border: 2px solid var(--gold);
  border-radius: 14px;
  position: relative;
}}
.mouse-dot {{
  width: 4px;
  height: 8px;
  background: var(--gold);
  border-radius: 2px;
  position: absolute;
  top: 6px;
  left: 50%;
  transform: translateX(-50%);
  animation: wheel 1.8s infinite;
}}
@keyframes wheel {{
  0% {{ transform: translate(-50%, 0); opacity: 1; }}
  80% {{ transform: translate(-50%, 14px); opacity: 0; }}
  100% {{ transform: translate(-50%, 0); opacity: 0; }}
}}

/* STICKY QUICK NAV */
.sticky-nav {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(12, 13, 16, 0.94);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid rgba(245, 197, 24, 0.25);
  padding: 0.8rem 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.6rem;
  overflow-x: auto;
  white-space: nowrap;
}}

.nav-pill {{
  padding: 0.5rem 1.1rem;
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #ddd;
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 700;
  transition: all 0.25s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}}
.nav-pill i {{ color: var(--gold); font-size: 0.75rem; }}
.nav-pill:hover {{
  background: var(--gold);
  color: #000;
  border-color: var(--gold);
  box-shadow: 0 0 15px var(--gold-glow);
  transform: translateY(-2px);
}}
.nav-pill:hover i {{ color: #000; }}

/* MENU CONTAINER */
.menu-container {{
  max-width: 1320px;
  margin: 0 auto;
  padding: 4rem 1.5rem 6rem 1.5rem;
}}

.category-section {{
  margin-bottom: 6rem;
  scroll-margin-top: 5rem;
}}

.section-header {{
  text-align: center;
  margin-bottom: 3rem;
}}
.section-tag {{
  display: inline-block;
  color: var(--gold);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 4px;
  text-transform: uppercase;
  margin-bottom: 0.4rem;
}}
.section-title {{
  font-family: 'Cinzel', serif;
  font-size: clamp(2.2rem, 4.5vw, 3.2rem);
  font-weight: 800;
  color: #fff;
  letter-spacing: 1.5px;
}}
.section-divider {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  margin-top: 0.8rem;
}}
.divider-line {{
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold));
}}
.divider-line.right {{
  background: linear-gradient(90deg, var(--gold), transparent);
}}
.section-divider i {{ color: var(--gold); font-size: 0.9rem; }}

/* GRID & CARDS */
.cards-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
  gap: 1.8rem;
}}

.food-card {{
  background: var(--bg-card);
  border-radius: 18px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: all 0.35s ease;
  box-shadow: 0 10px 25px rgba(0,0,0,0.5);
  position: relative;
}}
.food-card:hover {{
  transform: translateY(-8px);
  border-color: var(--gold);
  background: var(--bg-card-hover);
  box-shadow: 0 20px 40px rgba(0,0,0,0.7), 0 0 20px rgba(245, 197, 24, 0.2);
}}

.img-box {{
  width: 100%;
  height: 220px;
  position: relative;
  overflow: hidden;
  background: #1e2025;
}}
.img-box img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}}
.food-card:hover .img-box img {{
  transform: scale(1.08);
}}

.card-badge {{
  position: absolute;
  top: 12px;
  right: 12px;
  padding: 0.35rem 0.85rem;
  border-radius: 30px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  background: linear-gradient(135deg, var(--red), #b91c14);
  color: #fff;
  box-shadow: 0 4px 12px rgba(0,0,0,0.6);
  z-index: 2;
}}

.card-serving {{
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--gold);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 0.35rem;
}}

.card-content {{
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}}

.card-title {{
  font-family: 'Cinzel', serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.5rem;
}}

.card-desc {{
  font-size: 0.85rem;
  color: #a3a3a3;
  line-height: 1.55;
  margin-bottom: 1.2rem;
  flex-grow: 1;
}}

.card-bottom {{
  border-top: 1px dashed rgba(255, 255, 255, 0.12);
  padding-top: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.card-price {{
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--gold);
}}
.card-price .rs {{
  font-size: 0.8rem;
  color: #fff;
  margin-right: 2px;
}}

.card-prices-multi {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}}
.price-chip {{
  background: rgba(245, 197, 24, 0.12);
  border: 1px solid rgba(245, 197, 24, 0.3);
  border-radius: 6px;
  padding: 0.3rem 0.6rem;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--gold);
}}

/* WRAP SPECIAL BANNER */
.wrap-banner {{
  background: linear-gradient(135deg, #181920 0%, #101114 100%);
  border: 1px solid rgba(245, 197, 24, 0.3);
  border-radius: 22px;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  overflow: hidden;
  margin-bottom: 2rem;
  box-shadow: 0 20px 45px rgba(0,0,0,0.6);
}}
.wrap-banner-body {{
  padding: 2.5rem;
}}
.wrap-banner-img {{
  width: 100%;
  height: 100%;
  min-height: 300px;
  object-fit: cover;
}}
.addon-chip {{
  display: inline-block;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 8px;
  padding: 0.35rem 0.75rem;
  font-size: 0.78rem;
  color: #e5e5e5;
  margin: 0.3rem 0.3rem 0 0;
}}

/* FOOTER & FLOATING ACTIONS */
.footer-wrap {{
  background: #070709;
  border-top: 1px solid rgba(245, 197, 24, 0.25);
  padding: 4.5rem 1.5rem 2rem 1.5rem;
}}
.footer-grid {{
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 3rem;
}}
.footer-col h4 {{
  font-family: 'Cinzel', serif;
  font-size: 1.2rem;
  color: #fff;
  margin-bottom: 1.2rem;
}}
.footer-col p {{
  color: #999;
  font-size: 0.88rem;
  line-height: 1.7;
  margin-bottom: 0.8rem;
}}
.wa-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 0.75rem 1.6rem;
  border-radius: 30px;
  background: #25D366;
  color: #fff;
  text-decoration: none;
  font-weight: 800;
  font-size: 0.85rem;
  box-shadow: 0 10px 25px rgba(37, 211, 102, 0.3);
  transition: all 0.3s;
}}
.wa-btn:hover {{ transform: scale(1.05); }}

.floating-fabs {{
  position: fixed;
  bottom: 25px;
  right: 25px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  z-index: 999;
}}
.fab {{
  width: 52px;
  height: 52px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-size: 1.3rem;
  box-shadow: 0 10px 25px rgba(0,0,0,0.8);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}
.fab.wa {{ background: #25D366; color: #fff; }}
.fab.up {{ background: var(--gold); color: #000; }}
.fab:hover {{ transform: scale(1.15) translateY(-3px); }}

@media (max-width: 900px) {{
  .floating-food {{ display: none !important; }}
  .wrap-banner {{ grid-template-columns: 1fr; }}
  .wrap-banner-img {{ min-height: 220px; }}
  .sticky-nav {{ justify-content: flex-start; }}
}}
</style>
</head>
<body>

<!-- SCREEN 1: BRAND INTRODUCTION -->
<section class="hero-screen" id="home">
  <div class="hero-glow"></div>
  <img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=400&q=80" class="floating-food float-top-left" alt="Pizza">
  <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=400&q=80" class="floating-food float-bot-left" alt="Burger">
  <img src="https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=400&q=80" class="floating-food float-top-right" alt="Fried Chicken">
  <img src="https://images.unsplash.com/photo-1585109649139-366815a0d713?auto=format&fit=crop&w=400&q=80" class="floating-food float-bot-right" alt="Loaded Fries">

  <div class="hero-content">
    <div class="brand-kicker">Original Gourmet Craft</div>
    <h1 class="brand-title">{b['name']}</h1>
    <div class="brand-tagline">“ {b['tagline']} ”</div>
    <div class="brand-subtitle">{b['subtitle']}</div>
    <p class="brand-bio">{b['description']}</p>
    
    <a href="#menu-nav" class="scroll-prompt">
      <span>SCROLL TO EXPLORE</span>
      <div class="mouse-indicator"><div class="mouse-dot"></div></div>
      <i class="fa-solid fa-chevron-down"></i>
    </a>
  </div>
</section>

<!-- STICKY SPEED NAV -->
<nav class="sticky-nav" id="menu-nav">
  <a href="#pizzas" class="nav-pill"><i class="fa-solid fa-pizza-slice"></i> Pizzas</a>
  <a href="#appetizers" class="nav-pill"><i class="fa-solid fa-cookie-bite"></i> Appetizers</a>
  <a href="#burgers" class="nav-pill"><i class="fa-solid fa-burger"></i> Burgers</a>
  <a href="#wraps" class="nav-pill"><i class="fa-solid fa-bread-slice"></i> Wraps & Sandwiches</a>
  <a href="#pastas" class="nav-pill"><i class="fa-solid fa-bowl-food"></i> Pastas</a>
  <a href="#fried-chicken" class="nav-pill"><i class="fa-solid fa-drumstick-bite"></i> Fried Chicken</a>
  <a href="#platters" class="nav-pill"><i class="fa-solid fa-utensils"></i> Platters</a>
  <a href="#behari-rolls" class="nav-pill"><i class="fa-solid fa-fire"></i> Behari Rolls</a>
</nav>

<!-- MENU CONTENT SECTIONS -->
<div class="menu-container">

  <!-- 1. PIZZAS -->
  <section class="category-section" id="pizzas">
    <div class="section-header">
      <span class="section-tag">Stone Baked & Pan Perfection</span>
      <h2 class="section-title">The Legendary Pizzas</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-pizza-slice"></i><span class="divider-line right"></span></div>
    </div>
    <div class="cards-grid">{pizza_cards}</div>
  </section>

  <!-- 2. APPETIZERS -->
  <section class="category-section" id="appetizers">
    <div class="section-header">
      <span class="section-tag">Get Munchin Before The Main Course</span>
      <h2 class="section-title">Appetizers & Starters</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-cookie-bite"></i><span class="divider-line right"></span></div>
    </div>
    <div class="cards-grid">{appetizer_cards}</div>
  </section>

  <!-- 3. BURGERS -->
  <section class="category-section" id="burgers">
    <div class="section-header">
      <span class="section-tag">Pure Crunch & Char-Grilled Bliss</span>
      <h2 class="section-title">Gourmet Burgers</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-burger"></i><span class="divider-line right"></span></div>
    </div>
    <div class="cards-grid">{burger_cards}</div>
  </section>

  <!-- 4. WRAPS & SANDWICHES -->
  <section class="category-section" id="wraps">
    <div class="section-header">
      <span class="section-tag">Handcrafted & Rolled Fresh</span>
      <h2 class="section-title">Tortilla Wraps & Sandwiches</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-bread-slice"></i><span class="divider-line right"></span></div>
    </div>

    <div class="wrap-banner">
      <div class="wrap-banner-body">
        <div class="card-badge" style="position:static; display:inline-block; margin-bottom:1rem;">Feature Special</div>
        <h3 style="font-family:'Cinzel', serif; font-size:2rem; color:#fff; margin-bottom:0.5rem;">{wrap_data['title']}</h3>
        <p style="font-size:0.9rem; color:#a3a3a3; line-height:1.6; margin-bottom:1rem;">{wrap_data['desc']}</p>
        <div style="font-size:0.78rem; font-weight:800; color:var(--gold); text-transform:uppercase; margin-bottom:0.4rem;">Choice of Drizzle:</div>
        <div style="font-size:0.85rem; color:#fff; font-weight:600; margin-bottom:1rem;">{wrap_flavors}</div>
        <div style="font-size:0.75rem; font-weight:700; color:#888; text-transform:uppercase; margin-bottom:0.4rem;">Add-ons:</div>
        <div>{wrap_addons}</div>
        <div style="margin-top:1.5rem; font-size:1.4rem; font-weight:900; color:var(--gold);">
          <span style="font-size:0.85rem; color:#fff;">Base Price: Rs.</span>{wrap_data['base_price']}
        </div>
      </div>
      <div><img src="{wrap_data['image']}" class="wrap-banner-img" alt="Tortilla Wrap"></div>
    </div>

    <div class="cards-grid">{sandwich_cards}</div>
  </section>

  <!-- 5. PASTAS -->
  <section class="category-section" id="pastas">
    <div class="section-header">
      <span class="section-tag">Oven Baked Cheese & Savory Cream</span>
      <h2 class="section-title">Italian Pastas</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-bowl-food"></i><span class="divider-line right"></span></div>
    </div>
    <div class="cards-grid">{pasta_cards}</div>
  </section>

  <!-- 6. FRIED CHICKEN -->
  <section class="category-section" id="fried-chicken">
    <div class="section-header">
      <span class="section-tag">Secret 11-Spice Recipe</span>
      <h2 class="section-title">Southern Fried Chicken</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-drumstick-bite"></i><span class="divider-line right"></span></div>
    </div>
    <div class="cards-grid">{chicken_cards}</div>
  </section>

  <!-- 7. PLATTERS -->
  <section class="category-section" id="platters">
    <div class="section-header">
      <span class="section-tag">Value Sharing Feasts</span>
      <h2 class="section-title">Fabbies Grand Platters</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-utensils"></i><span class="divider-line right"></span></div>
    </div>
    <div class="cards-grid">{platter_cards}</div>
  </section>

  <!-- 8. BEHARI ROLLS -->
  <section class="category-section" id="behari-rolls">
    <div class="section-header">
      <span class="section-tag">The Town's Famous Roll</span>
      <h2 class="section-title">Signature Behari Rolls</h2>
      <div class="section-divider"><span class="divider-line"></span><i class="fa-solid fa-fire"></i><span class="divider-line right"></span></div>
    </div>
    <div style="max-w:800px; margin:0 auto;">{behari_cards}</div>
  </section>

</div>

<!-- FOOTER -->
<footer class="footer-wrap">
  <div class="footer-grid">
    <div class="footer-col">
      <h4>{b['name']}</h4>
      <p style="color:var(--gold); font-weight:700;">{b['tagline']}</p>
      <p>{b['description']}</p>
    </div>
    <div class="footer-col">
      <h4>Location & Hours</h4>
      <p><i class="fa-solid fa-location-dot" style="color:var(--gold); margin-right:8px;"></i> {b['location']}</p>
      <p><i class="fa-solid fa-clock" style="color:var(--gold); margin-right:8px;"></i> {b['hours']}</p>
      <p><i class="fa-solid fa-phone" style="color:var(--gold); margin-right:8px;"></i> {b['phone']}</p>
    </div>
    <div class="footer-col">
      <h4>Instant Order</h4>
      <p>Hot, crispy, and fresh delivery directly to your doorstep in 35-45 minutes.</p>
      <a href="https://wa.me/{b['whatsapp']}?text=Hi%20Fabbies!%20I%20would%20like%20to%20order." target="_blank" class="wa-btn">
        <i class="fa-brands fa-whatsapp" style="font-size:1.1rem;"></i> Order on WhatsApp
      </a>
    </div>
  </div>
  <div style="text-align:center; color:#555; font-size:0.8rem; margin-top:3.5rem; border-top:1px solid #1a1b22; padding-top:1.5rem;">
    &copy; {b['name']} Restaurant. All Rights Reserved. Food is my best friend.
  </div>
</footer>

<!-- FLOATING ACTIONS -->
<div class="floating-fabs">
  <a href="https://wa.me/{b['whatsapp']}?text=Hi%20Fabbies!%20I%20want%20to%20order." target="_blank" class="fab wa" title="Chat on WhatsApp">
    <i class="fa-brands fa-whatsapp"></i>
  </a>
  <a href="#home" class="fab up" title="Scroll To Top">
    <i class="fa-solid fa-arrow-up"></i>
  </a>
</div>

</body>
</html>
"""

# Render with components.html to ensure 100% isolated, bulletproof HTML/CSS/JS execution on Streamlit Community Cloud
components.html(COMPLETE_APP_HTML, height=3600, scrolling=True)
