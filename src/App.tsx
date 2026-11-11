import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import {
  Pizza,
  UtensilsCrossed,
  Flame,
  Layers,
  Soup,
  Drumstick,
  ShoppingBag,
  ArrowUp,
  MapPin,
  Clock,
  Phone,
  MessageCircle,
  Sparkles,
} from "lucide-react";

import { MENU_DATA } from "./data/menuData";
import { HeroSection } from "./components/HeroSection";
import { FoodCard } from "./components/FoodCard";
import { SectionHeading } from "./components/SectionHeading";
import { CartDrawer, CartItem } from "./components/CartDrawer";

export default function App() {
  const {
    brand,
    pizzas,
    appetizers,
    burgers,
    wrapsAndSandwiches,
    pastas,
    friedChicken,
    platters,
    behariRolls,
  } = MENU_DATA;

  // Cart state
  const [cartItems, setCartItems] = useState<CartItem[]>([]);
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [showScrollTop, setShowScrollTop] = useState(false);
  const [activeSection, setActiveSection] = useState<string>("brand-hero");

  // Selected wrap customization
  const [selectedWrapFlavor, setSelectedWrapFlavor] = useState<string>(
    wrapsAndSandwiches.wraps.flavors[0]
  );
  const [selectedAddons, setSelectedAddons] = useState<string[]>([]);

  // Listen to scroll for Back-To-Top button & active section highlight
  useEffect(() => {
    const handleScroll = () => {
      setShowScrollTop(window.scrollY > 450);

      const sections = [
        "brand-hero",
        "pizzas",
        "appetizers",
        "burgers",
        "wraps-sandwiches",
        "pastas",
        "fried-chicken",
        "platters",
        "behari-rolls",
      ];

      for (const sectionId of sections) {
        const el = document.getElementById(sectionId);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= 200 && rect.bottom >= 200) {
            setActiveSection(sectionId);
            break;
          }
        }
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: "smooth" });
    }
  };

  const handleAddToCart = (item: {
    name: string;
    price: string;
    variant?: string;
  }) => {
    setCartItems((prev) => {
      const existingKey = `${item.name}-${item.variant || ""}`;
      const found = prev.find((i) => i.id === existingKey);

      if (found) {
        return prev.map((i) =>
          i.id === existingKey ? { ...i, quantity: i.quantity + 1 } : i
        );
      }
      return [
        ...prev,
        {
          id: existingKey,
          name: item.name,
          price: item.price,
          variant: item.variant,
          quantity: 1,
        },
      ];
    });
  };

  const handleUpdateQuantity = (id: string, delta: number) => {
    setCartItems((prev) =>
      prev
        .map((item) => {
          if (item.id === id) {
            const newQty = item.quantity + delta;
            return newQty > 0 ? { ...item, quantity: newQty } : null;
          }
          return item;
        })
        .filter(Boolean) as CartItem[]
    );
  };

  const handleRemoveItem = (id: string) => {
    setCartItems((prev) => prev.filter((i) => i.id !== id));
  };

  const handleClearCart = () => setCartItems([]);

  const toggleAddon = (addonName: string) => {
    setSelectedAddons((prev) =>
      prev.includes(addonName)
        ? prev.filter((name) => name !== addonName)
        : [...prev, addonName]
    );
  };

  // Add customized wrap to order
  const handleAddCustomWrap = () => {
    let wrapPrice = parseInt(wrapsAndSandwiches.wraps.basePrice, 10);
    const addonDetails: string[] = [];

    selectedAddons.forEach((addonName) => {
      const match = wrapsAndSandwiches.wraps.addons.find(
        (a) => a.name === addonName
      );
      if (match) {
        wrapPrice += parseInt(match.price, 10);
        addonDetails.push(match.name);
      }
    });

    const variantDesc = `${selectedWrapFlavor} sauce${
      addonDetails.length > 0 ? ` + ${addonDetails.join(", ")}` : ""
    }`;

    handleAddToCart({
      name: wrapsAndSandwiches.wraps.title,
      price: wrapPrice.toString(),
      variant: variantDesc,
    });
  };

  const totalCartCount = cartItems.reduce((sum, item) => sum + item.quantity, 0);

  return (
    <div className="min-h-screen bg-[#0a0b0d] text-neutral-100 font-sans selection:bg-[#F5C518] selection:text-black">
      {/* 1. SCREEN ONE: BRAND INTRODUCTION ONLY */}
      <HeroSection onExploreClick={() => scrollToSection("menu-nav-anchor")} />

      {/* 2. STICKY INTERACTIVE QUICK-NAV BAR */}
      <nav
        id="menu-nav-anchor"
        className="sticky top-0 z-40 bg-[#0d0e12]/90 backdrop-blur-md border-y border-white/8 px-4 py-2.5 shadow-xl shadow-black/60 overflow-x-auto no-scrollbar"
      >
        <div className="max-w-6xl mx-auto flex items-center justify-between gap-4">
          <div className="flex items-center gap-1.5 shrink-0">
            <span className="font-serif-brand font-black text-sm text-[#F5C518] tracking-widest uppercase mr-2">
              FABBIES
            </span>
          </div>

          {/* Category Navigation Pills */}
          <div className="flex items-center gap-1 overflow-x-auto py-1">
            {[
              { id: "pizzas", label: "Pizzas", icon: Pizza },
              { id: "appetizers", label: "Appetizers", icon: UtensilsCrossed },
              { id: "burgers", label: "Burgers", icon: Flame },
              { id: "wraps-sandwiches", label: "Wraps & Sandwiches", icon: Layers },
              { id: "pastas", label: "Pastas", icon: Soup },
              { id: "fried-chicken", label: "Fried Chicken", icon: Drumstick },
              { id: "platters", label: "Platters", icon: Sparkles },
              { id: "behari-rolls", label: "Behari Rolls", icon: Flame },
            ].map(({ id, label, icon: Icon }) => (
              <button
                key={id}
                onClick={() => scrollToSection(id)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition-all cursor-pointer ${
                  activeSection === id
                    ? "bg-[#F5C518] text-black shadow-md shadow-[#F5C518]/25 font-bold"
                    : "text-neutral-400 hover:text-white hover:bg-white/5"
                }`}
              >
                <Icon className="w-3.5 h-3.5" />
                <span>{label}</span>
              </button>
            ))}
          </div>

          {/* Quick Cart Trigger */}
          <button
            onClick={() => setIsCartOpen(true)}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#F5C518] text-black font-extrabold text-xs shadow-lg shadow-[#F5C518]/20 hover:scale-105 active:scale-95 transition-all cursor-pointer shrink-0"
          >
            <ShoppingBag className="w-4 h-4" />
            <span className="hidden sm:inline">Order Platter</span>
            <span className="bg-black text-[#F5C518] px-1.5 py-0.2 rounded-full text-[10px]">
              {totalCartCount}
            </span>
          </button>
        </div>
      </nav>

      {/* 3. MAIN STORYTELLING MENU BODY */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20 space-y-24 md:space-y-32">
        {/* ========================================================
            SECTION 1: PIZZAS (Deep Dish, Extreme, Crown Crust, Stuffed Crust)
           ======================================================== */}
        <section id="pizzas" className="scroll-mt-20">
          <SectionHeading
            kicker="Stone Baked & Golden Crusted"
            title="The Legendary Pizzas"
            icon={Pizza}
            subtitle="Prepared using slow-fermented artisanal dough, 100% whole mozzarella, and signature sauces."
          />

          {/* Subcategory: Deep Dish */}
          <div className="mb-14">
            <div className="flex items-center gap-3 mb-6 pb-2 border-b border-white/8">
              <span className="w-2.5 h-2.5 rounded-full bg-[#F5C518]" />
              <h3 className="text-xl font-extrabold uppercase tracking-widest text-white">
                Deep Dish Pan Pizzas
              </h3>
              <span className="text-xs text-neutral-400 hidden sm:inline">
                · Packed with thick cheese & savory sauce
              </span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {pizzas.deepDish.map((pizza) => (
                <FoodCard
                  key={pizza.id}
                  name={pizza.name}
                  description={pizza.description}
                  image={pizza.image}
                  prices={pizza.prices}
                  badge={pizza.badge}
                  onAddToCart={handleAddToCart}
                />
              ))}
            </div>
          </div>

          {/* Subcategory: Extreme Pizzas */}
          <div className="mb-14">
            <div className="flex items-center gap-3 mb-6 pb-2 border-b border-white/8">
              <span className="w-2.5 h-2.5 rounded-full bg-[#E63932]" />
              <h3 className="text-xl font-extrabold uppercase tracking-widest text-white">
                Extreme Pizzas
              </h3>
              <span className="text-xs text-neutral-400 hidden sm:inline">
                · High intensity flavor loaded with supreme toppings
              </span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
              {pizzas.extreme.map((pizza) => (
                <FoodCard
                  key={pizza.id}
                  name={pizza.name}
                  description={pizza.description}
                  image={pizza.image}
                  prices={pizza.prices}
                  badge={pizza.badge}
                  onAddToCart={handleAddToCart}
                />
              ))}
            </div>
          </div>

          {/* Subcategory: Crown Crust Pizza */}
          <div className="mb-14">
            <div className="flex items-center gap-3 mb-6 pb-2 border-b border-white/8">
              <span className="w-2.5 h-2.5 rounded-full bg-[#F5C518]" />
              <h3 className="text-xl font-extrabold uppercase tracking-widest text-white">
                Royal Crown Crust
              </h3>
              <span className="text-xs text-neutral-400 hidden sm:inline">
                · Hand-pinched pockets stuffed with molten cheese and kebab
              </span>
            </div>
            <div className="max-w-2xl mx-auto">
              {pizzas.crownCrust.map((pizza) => (
                <FoodCard
                  key={pizza.id}
                  name={pizza.name}
                  description={pizza.description}
                  image={pizza.image}
                  prices={pizza.prices}
                  badge={pizza.badge}
                  onAddToCart={handleAddToCart}
                />
              ))}
            </div>
          </div>

          {/* Subcategory: Stuffed Crust */}
          <div>
            <div className="flex items-center gap-3 mb-6 pb-2 border-b border-white/8">
              <span className="w-2.5 h-2.5 rounded-full bg-[#F5C518]" />
              <h3 className="text-xl font-extrabold uppercase tracking-widest text-white">
                Stuffed Crust Series
              </h3>
              <span className="text-xs text-neutral-400 hidden sm:inline">
                · Kebab, cheese, and mild seasoned fillings inside every crust rim
              </span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {pizzas.stuffedCrust.map((pizza) => (
                <FoodCard
                  key={pizza.id}
                  name={pizza.name}
                  description={pizza.description}
                  image={pizza.image}
                  prices={pizza.prices}
                  badge={pizza.badge}
                  onAddToCart={handleAddToCart}
                />
              ))}
            </div>
          </div>
        </section>

        {/* ========================================================
            SECTION 2: APPETIZERS
           ======================================================== */}
        <section id="appetizers" className="scroll-mt-20">
          <SectionHeading
            kicker="Get Munchin Before The Main Course"
            title="Appetizers & Starters"
            icon={UtensilsCrossed}
            subtitle="Golden fried breast tenders, artisan garlic bread, crunchy nuggets, and loaded fries."
          />
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {appetizers.map((item) => (
              <FoodCard
                key={item.id}
                name={item.name}
                description={item.description}
                image={item.image}
                price={item.price}
                prices={item.prices}
                serving={item.serving}
                badge={item.badge}
                onAddToCart={handleAddToCart}
              />
            ))}
          </div>
        </section>

        {/* ========================================================
            SECTION 3: BURGERS (Fried Burgers & Grilled Burgers)
           ======================================================== */}
        <section id="burgers" className="scroll-mt-20">
          <SectionHeading
            kicker="Pure Crunch & Flame-Seared Goodness"
            title="Gourmet Burgers"
            icon={Flame}
            subtitle="Crispy deep-fried zinger fillets, tower burgers, flame-grilled beef, and fiery Cheetos specialties."
          />

          {/* Fried Burgers */}
          <div className="mb-14">
            <div className="flex items-center gap-3 mb-6 pb-2 border-b border-white/8">
              <span className="w-2.5 h-2.5 rounded-full bg-[#F5C518]" />
              <h3 className="text-xl font-extrabold uppercase tracking-widest text-white">
                Golden Fried Burgers
              </h3>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {burgers.fried.map((item) => (
                <FoodCard
                  key={item.id}
                  name={item.name}
                  description={item.description}
                  image={item.image}
                  price={item.price}
                  badge={item.badge}
                  onAddToCart={handleAddToCart}
                />
              ))}
            </div>
          </div>

          {/* Grilled Burgers */}
          <div>
            <div className="flex items-center gap-3 mb-6 pb-2 border-b border-white/8">
              <span className="w-2.5 h-2.5 rounded-full bg-[#E63932]" />
              <h3 className="text-xl font-extrabold uppercase tracking-widest text-white">
                Char-Grilled & Specialty Fillets
              </h3>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {burgers.grilled.map((item) => (
                <FoodCard
                  key={item.id}
                  name={item.name}
                  description={item.description}
                  image={item.image}
                  price={item.price}
                  badge={item.badge}
                  onAddToCart={handleAddToCart}
                />
              ))}
            </div>
          </div>
        </section>

        {/* ========================================================
            SECTION 4: TORTILLA WRAPS & SANDWICHES
           ======================================================== */}
        <section id="wraps-sandwiches" className="scroll-mt-20">
          <SectionHeading
            kicker="Rolled Fresh & Layered Deep"
            title="Tortilla Wraps & Sandwiches"
            icon={Layers}
            subtitle="Customize your crispy chicken wrap or relish our signature triple-decker club sandwiches."
          />

          {/* Interactive Feature Wrap Builder */}
          <div className="mb-12 rounded-3xl bg-gradient-to-br from-[#16171d] to-[#0f1013] border border-[#F5C518]/30 overflow-hidden shadow-2xl">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 p-6 sm:p-8 lg:p-10 items-center">
              <div className="lg:col-span-7 space-y-5">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-widest bg-[#F5C518]/15 text-[#F5C518] border border-[#F5C518]/30">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Tortilla Wrap Feature</span>
                </div>

                <h3 className="font-serif-brand text-2xl sm:text-3xl font-bold text-white">
                  {wrapsAndSandwiches.wraps.title}
                </h3>

                <p className="text-sm text-neutral-300 leading-relaxed">
                  {wrapsAndSandwiches.wraps.description}
                </p>

                {/* Flavor choices */}
                <div>
                  <span className="text-xs uppercase font-extrabold tracking-wider text-[#F5C518] block mb-2">
                    1. Select Artisan Drizzle Flavor:
                  </span>
                  <div className="flex flex-wrap gap-2">
                    {wrapsAndSandwiches.wraps.flavors.map((fl) => (
                      <button
                        key={fl}
                        onClick={() => setSelectedWrapFlavor(fl)}
                        className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                          selectedWrapFlavor === fl
                            ? "bg-[#F5C518] text-black shadow-md shadow-[#F5C518]/25"
                            : "bg-white/5 hover:bg-white/10 text-neutral-300 border border-white/5"
                        }`}
                      >
                        {fl}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Optional Add-ons */}
                <div>
                  <span className="text-xs uppercase font-extrabold tracking-wider text-[#F5C518] block mb-2">
                    2. Add Extra Indulgence (+Rs.60 each):
                  </span>
                  <div className="flex flex-wrap gap-2">
                    {wrapsAndSandwiches.wraps.addons.map((addon) => {
                      const isSelected = selectedAddons.includes(addon.name);
                      return (
                        <button
                          key={addon.name}
                          onClick={() => toggleAddon(addon.name)}
                          className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
                            isSelected
                              ? "bg-white/20 text-white border border-[#F5C518]"
                              : "bg-white/5 hover:bg-white/10 text-neutral-400 border border-white/5"
                          }`}
                        >
                          {addon.name} · +Rs.{addon.price}
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Add to Order Action */}
                <div className="flex items-center gap-6 pt-3 border-t border-white/10">
                  <div>
                    <span className="text-[10px] uppercase font-bold text-neutral-400 block tracking-widest">
                      Customized Price
                    </span>
                    <span className="text-2xl font-black text-[#F5C518] tabular-nums">
                      <span className="text-xs font-bold text-white mr-1">Rs.</span>
                      {parseInt(wrapsAndSandwiches.wraps.basePrice, 10) +
                        selectedAddons.length * 60}
                    </span>
                  </div>

                  <button
                    onClick={handleAddCustomWrap}
                    className="px-6 py-2.5 rounded-xl bg-[#F5C518] hover:bg-[#ffe169] text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-[#F5C518]/20 transition-all hover:scale-105 active:scale-95 cursor-pointer"
                  >
                    Add Custom Wrap
                  </button>
                </div>
              </div>

              <div className="lg:col-span-5 h-64 lg:h-80 rounded-2xl overflow-hidden border border-white/10">
                <img
                  src={wrapsAndSandwiches.wraps.image}
                  alt={wrapsAndSandwiches.wraps.title}
                  referrerPolicy="no-referrer"
                  className="w-full h-full object-cover"
                />
              </div>
            </div>
          </div>

          {/* Sandwiches Cards */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {wrapsAndSandwiches.sandwiches.map((item) => (
              <FoodCard
                key={item.id}
                name={item.name}
                description={item.description}
                image={item.image}
                price={item.price}
                serving={item.serving}
                badge={item.badge}
                onAddToCart={handleAddToCart}
              />
            ))}
          </div>
        </section>

        {/* ========================================================
            SECTION 5: PASTAS
           ======================================================== */}
        <section id="pastas" className="scroll-mt-20">
          <SectionHeading
            kicker="Oven-Baked Mozzarella & Velvety Cream"
            title="Artisanal Pastas"
            icon={Soup}
            subtitle="Indulgent fettuccine and penne dishes baked hot in clay skillets."
          />
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {pastas.map((item) => (
              <FoodCard
                key={item.id}
                name={item.name}
                description={item.description}
                image={item.image}
                price={item.price}
                badge={item.badge}
                onAddToCart={handleAddToCart}
              />
            ))}
          </div>
        </section>

        {/* ========================================================
            SECTION 6: FRIED CHICKEN
           ======================================================== */}
        <section id="fried-chicken" className="scroll-mt-20">
          <SectionHeading
            kicker="Secret 11-Spice Golden Batter"
            title="Crispy Fried Chicken"
            icon={Drumstick}
            subtitle="Pressure fried for extraordinary crunch and juicy tenderness in every bite."
          />
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {friedChicken.map((item) => (
              <FoodCard
                key={item.id}
                name={item.name}
                description={item.description}
                image={item.image}
                price={item.price}
                serving={item.serving}
                badge={item.badge}
                onAddToCart={handleAddToCart}
              />
            ))}
          </div>
        </section>

        {/* ========================================================
            SECTION 7: GRAND PLATTERS
           ======================================================== */}
        <section id="platters" className="scroll-mt-20">
          <SectionHeading
            kicker="Ultimate Sharing Deals"
            title="Fabbies Grand Platters"
            icon={Sparkles}
            subtitle="Handcrafted platter combinations featuring rolls, wings, sandwiches, and seasoned fries."
          />
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {platters.map((platter) => (
              <div
                key={platter.id}
                className="group relative flex flex-col bg-[#14151a] border border-[#F5C518]/30 rounded-3xl overflow-hidden shadow-2xl hover:border-[#F5C518] transition-all duration-300"
              >
                <div className="relative h-64 sm:h-72 overflow-hidden bg-neutral-900">
                  <img
                    src={platter.image}
                    alt={platter.name}
                    referrerPolicy="no-referrer"
                    className="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#14151a] via-transparent to-transparent" />
                  <div className="absolute top-4 right-4 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-[#F5C518] text-black shadow-lg">
                    {platter.badge}
                  </div>
                </div>

                <div className="p-6 sm:p-8 flex flex-col flex-1">
                  <h3 className="font-serif-brand text-2xl font-bold text-white mb-2">
                    {platter.name}
                  </h3>
                  <p className="text-sm text-neutral-400 mb-6 leading-relaxed">
                    {platter.description}
                  </p>

                  {/* Included Items Tag Strip */}
                  <div className="mb-6 p-4 rounded-xl bg-white/5 border border-white/5">
                    <span className="text-[11px] font-extrabold uppercase tracking-wider text-[#F5C518] block mb-2">
                      Platter Includes:
                    </span>
                    <div className="grid grid-cols-2 gap-2">
                      {platter.itemsIncluded.map((item) => (
                        <div
                          key={item}
                          className="flex items-center gap-2 text-xs font-semibold text-neutral-300"
                        >
                          <span className="w-1.5 h-1.5 rounded-full bg-[#F5C518]" />
                          <span>{item}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="flex items-center justify-between pt-4 border-t border-white/10 mt-auto">
                    <div>
                      <span className="text-[10px] font-bold text-neutral-400 uppercase tracking-widest block">
                        Complete Platter Deal
                      </span>
                      <span className="text-2xl font-black text-[#F5C518] tabular-nums">
                        <span className="text-xs font-bold text-white mr-1">Rs.</span>
                        {platter.price}
                      </span>
                    </div>

                    <button
                      onClick={() =>
                        handleAddToCart({
                          name: platter.name,
                          price: platter.price,
                          variant: "Complete Combo Platter",
                        })
                      }
                      className="px-5 py-2.5 rounded-xl bg-[#F5C518] hover:bg-[#ffe066] text-black font-extrabold text-xs uppercase tracking-wider shadow-md hover:scale-105 active:scale-95 transition-all cursor-pointer"
                    >
                      Add Platter
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* ========================================================
            SECTION 8: BEHARI ROLLS
           ======================================================== */}
        <section id="behari-rolls" className="scroll-mt-20">
          <SectionHeading
            kicker="The Town's Number One Roll"
            title="Signature Behari Rolls"
            icon={Flame}
            subtitle="Charred aromatic Behari spices, mozzarella, and flaky tortilla."
          />

          <div className="rounded-3xl bg-gradient-to-br from-[#181921] to-[#0c0d10] border-2 border-[#F5C518] p-6 sm:p-10 shadow-2xl relative overflow-hidden">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
              <div className="lg:col-span-7 space-y-4">
                <div className="inline-block px-3 py-1 rounded-full text-xs font-bold uppercase tracking-widest bg-[#E63932] text-white">
                  {behariRolls.badge}
                </div>
                <div className="text-xs font-bold tracking-widest text-[#F5C518] uppercase">
                  {behariRolls.serving}
                </div>
                <h3 className="font-serif-brand text-3xl sm:text-4xl font-extrabold text-[#F5C518]">
                  {behariRolls.name}
                </h3>
                <p className="text-sm sm:text-base text-neutral-300 leading-relaxed">
                  {behariRolls.description}
                </p>

                <div className="flex items-center gap-6 pt-4 border-t border-white/10">
                  <div>
                    <span className="text-[10px] font-bold text-neutral-400 uppercase tracking-widest block">
                      Special Box Price
                    </span>
                    <span className="text-3xl font-black text-white tabular-nums">
                      <span className="text-xs font-bold text-[#F5C518] mr-1">Rs.</span>
                      {behariRolls.price}
                    </span>
                  </div>

                  <button
                    onClick={() =>
                      handleAddToCart({
                        name: behariRolls.name,
                        price: behariRolls.price,
                        variant: behariRolls.serving,
                      })
                    }
                    className="px-6 py-3 rounded-xl bg-[#F5C518] hover:bg-[#ffe169] text-black font-extrabold text-xs uppercase tracking-wider shadow-lg shadow-[#F5C518]/25 hover:scale-105 active:scale-95 transition-all cursor-pointer"
                  >
                    Add 4 Pcs Box
                  </button>
                </div>
              </div>

              <div className="lg:col-span-5 h-72 rounded-2xl overflow-hidden border border-white/10 shadow-2xl">
                <img
                  src={behariRolls.image}
                  alt={behariRolls.name}
                  referrerPolicy="no-referrer"
                  className="w-full h-full object-cover"
                />
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* ========================================================
          FOOTER SECTION & RESTAURANT INFO
         ======================================================== */}
      <footer className="bg-[#070709] border-t border-[#F5C518]/20 mt-24 py-16 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-10">
          <div>
            <h4 className="font-serif-brand text-2xl font-black text-[#F5C518] mb-2 tracking-wider">
              {brand.name}
            </h4>
            <p className="text-xs font-extrabold uppercase tracking-widest text-neutral-400 mb-4">
              &ldquo;{brand.tagline}&rdquo;
            </p>
            <p className="text-xs text-neutral-400 leading-relaxed max-w-sm mb-6">
              {brand.description}
            </p>
            <div className="flex items-center gap-3">
              <a
                href={brand.facebookUrl}
                target="_blank"
                rel="noreferrer"
                className="w-10 h-10 rounded-full bg-white/5 hover:bg-[#F5C518] hover:text-black flex items-center justify-center text-neutral-300 transition-all border border-white/5"
                title="Facebook"
              >
                FB
              </a>
              <a
                href={brand.instagramUrl}
                target="_blank"
                rel="noreferrer"
                className="w-10 h-10 rounded-full bg-white/5 hover:bg-[#F5C518] hover:text-black flex items-center justify-center text-neutral-300 transition-all border border-white/5"
                title="Instagram"
              >
                IG
              </a>
              <a
                href={`https://wa.me/${brand.whatsapp}`}
                target="_blank"
                rel="noreferrer"
                className="w-10 h-10 rounded-full bg-[#25D366]/20 hover:bg-[#25D366] text-[#25D366] hover:text-white flex items-center justify-center transition-all border border-[#25D366]/30"
                title="WhatsApp Order"
              >
                <MessageCircle className="w-5 h-5" />
              </a>
            </div>
          </div>

          <div>
            <h4 className="font-serif-brand text-lg font-bold text-white mb-4 tracking-wider">
              Restaurant Details
            </h4>
            <ul className="space-y-3 text-xs text-neutral-400">
              <li className="flex items-start gap-3">
                <MapPin className="w-4 h-4 text-[#F5C518] shrink-0 mt-0.5" />
                <span>{brand.location}</span>
              </li>
              <li className="flex items-center gap-3">
                <Clock className="w-4 h-4 text-[#F5C518] shrink-0" />
                <span>{brand.hours}</span>
              </li>
              <li className="flex items-center gap-3">
                <Phone className="w-4 h-4 text-[#F5C518] shrink-0" />
                <span>{brand.phone}</span>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-serif-brand text-lg font-bold text-white mb-4 tracking-wider">
              Instant WhatsApp Order
            </h4>
            <p className="text-xs text-neutral-400 leading-relaxed mb-4">
              Have special dietary requests or a custom catering order? Connect with our kitchen team directly.
            </p>
            <a
              href={`https://wa.me/${brand.whatsapp}?text=Hi%20FABBIES!%20I%20would%20like%20to%20place%20an%20order.`}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-[#25D366] text-white text-xs font-bold hover:brightness-110 shadow-lg shadow-[#25D366]/20 transition-all"
            >
              <MessageCircle className="w-4 h-4" />
              <span>Chat with Kitchen</span>
            </a>
          </div>
        </div>

        <div className="max-w-7xl mx-auto mt-12 pt-6 border-t border-white/5 text-center text-neutral-400 text-xs">
          &copy; {new Date().getFullYear()} {brand.name} Restaurant. All Rights Reserved. Crafted with passion for good food.
        </div>
      </footer>

      {/* Floating Action Buttons: WhatsApp & Scroll to top */}
      <div className="fixed bottom-6 right-6 z-40 flex flex-col gap-3">
        <a
          href={`https://wa.me/${brand.whatsapp}?text=Hi%20Fabbies!%20I%20want%20to%20order.`}
          target="_blank"
          rel="noreferrer"
          className="w-13 h-13 rounded-full bg-[#25D366] text-white flex items-center justify-center shadow-2xl shadow-black/80 hover:scale-110 active:scale-95 transition-all"
          title="Direct WhatsApp Order"
        >
          <MessageCircle className="w-6 h-6" />
        </a>

        <AnimatePresence>
          {showScrollTop && (
            <motion.button
              initial={{ opacity: 0, scale: 0.5 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.5 }}
              onClick={() => scrollToSection("brand-hero")}
              className="w-13 h-13 rounded-full bg-[#F5C518] text-black flex items-center justify-center shadow-2xl shadow-black/80 hover:scale-110 active:scale-95 transition-all cursor-pointer font-bold"
              title="Scroll To Top"
            >
              <ArrowUp className="w-5 h-5" />
            </motion.button>
          )}
        </AnimatePresence>
      </div>

      {/* Cart & WhatsApp Checkout Drawer */}
      <CartDrawer
        isOpen={isCartOpen}
        onClose={() => setIsCartOpen(false)}
        items={cartItems}
        onUpdateQuantity={handleUpdateQuantity}
        onRemoveItem={handleRemoveItem}
        onClearCart={handleClearCart}
        whatsappNumber={brand.whatsapp}
      />
    </div>
  );
}
