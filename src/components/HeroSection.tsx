import React from "react";
import { motion } from "motion/react";
import { ChevronDown } from "lucide-react";
import { MENU_DATA } from "../data/menuData";

interface HeroSectionProps {
  onExploreClick: () => void;
}

export const HeroSection: React.FC<HeroSectionProps> = ({ onExploreClick }) => {
  const { brand } = MENU_DATA;

  return (
    <section
      id="brand-hero"
      className="relative min-h-screen w-full flex flex-col items-center justify-center overflow-hidden px-4 py-16 bg-radial from-[#1e2026] via-[#101115] to-[#070709]"
    >
      {/* Golden atmospheric glow */}
      <div className="absolute w-[360px] md:w-[680px] h-[360px] md:h-[680px] rounded-full bg-[#F5C518]/10 blur-[100px] pointer-events-none animate-pulse" />
      <div className="absolute -top-24 -right-24 w-96 h-96 rounded-full bg-[#E63932]/10 blur-[90px] pointer-events-none" />

      {/* Floating food visual satellites on sides (Desktop view) */}
      <motion.div
        animate={{ y: [0, -18, 0], rotate: [0, 4, 0] }}
        transition={{ duration: 7, repeat: Infinity, ease: "easeInOut" }}
        className="hidden lg:block absolute top-16 left-12 w-44 h-44 rounded-full overflow-hidden border-2 border-[#F5C518]/30 shadow-2xl shadow-black/80 pointer-events-none z-10"
      >
        <img
          src="/src/assets/images/deep_dish_pizza_1794423163785.jpg"
          alt="Deep dish pizza"
          referrerPolicy="no-referrer"
          className="w-full h-full object-cover scale-110"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
      </motion.div>

      <motion.div
        animate={{ y: [0, 20, 0], rotate: [0, -4, 0] }}
        transition={{ duration: 8.5, repeat: Infinity, ease: "easeInOut" }}
        className="hidden lg:block absolute bottom-20 left-16 w-48 h-48 rounded-full overflow-hidden border-2 border-[#F5C518]/30 shadow-2xl shadow-black/80 pointer-events-none z-10"
      >
        <img
          src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=500&q=80"
          alt="Gourmet Burger"
          referrerPolicy="no-referrer"
          className="w-full h-full object-cover scale-110"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
      </motion.div>

      <motion.div
        animate={{ y: [0, -22, 0], rotate: [0, -3, 0] }}
        transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
        className="hidden lg:block absolute top-20 right-14 w-44 h-44 rounded-full overflow-hidden border-2 border-[#F5C518]/30 shadow-2xl shadow-black/80 pointer-events-none z-10"
      >
        <img
          src="https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=500&q=80"
          alt="Crispy Fried Chicken"
          referrerPolicy="no-referrer"
          className="w-full h-full object-cover scale-110"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
      </motion.div>

      <motion.div
        animate={{ y: [0, 18, 0], rotate: [0, 5, 0] }}
        transition={{ duration: 7.2, repeat: Infinity, ease: "easeInOut" }}
        className="hidden lg:block absolute bottom-16 right-20 w-48 h-48 rounded-full overflow-hidden border-2 border-[#F5C518]/30 shadow-2xl shadow-black/80 pointer-events-none z-10"
      >
        <img
          src="https://images.unsplash.com/photo-1585109649139-366815a0d713?auto=format&fit=crop&w=500&q=80"
          alt="Loaded Fries"
          referrerPolicy="no-referrer"
          className="w-full h-full object-cover scale-110"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
      </motion.div>

      {/* Hero Central Identity Content */}
      <div className="relative z-20 max-w-3xl mx-auto text-center flex flex-col items-center">
        {/* Newspaper / Brand Badge */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="inline-flex items-center gap-2 px-5 py-1.5 rounded-full bg-[#F5C518]/10 border border-[#F5C518]/30 text-[#F5C518] text-xs font-bold tracking-[0.3em] uppercase mb-6 shadow-lg shadow-[#F5C518]/5"
        >
          <span>Original Recipe & Craft</span>
          <span className="text-[#F5C518]/40">·</span>
          <span>Since Day One</span>
        </motion.div>

        {/* Brand Logo & Name */}
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="mb-3"
        >
          <div className="flex items-center justify-center gap-3 mb-2">
            <span className="h-[2px] w-12 bg-gradient-to-r from-transparent to-[#F5C518]" />
            <span className="text-xs font-semibold tracking-[0.35em] text-[#d6d8df] uppercase">
              {brand.headline}
            </span>
            <span className="h-[2px] w-12 bg-gradient-to-l from-transparent to-[#F5C518]" />
          </div>

          <h1 className="text-6xl sm:text-7xl md:text-8xl lg:text-9xl font-black tracking-wider text-transparent bg-clip-text bg-gradient-to-b from-white via-[#F5C518] to-[#b88c07] drop-shadow-[0_15px_35px_rgba(0,0,0,0.9)]">
            {brand.name}
          </h1>
        </motion.div>

        {/* Primary Tagline */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="mb-2"
        >
          <h2 className="text-xl sm:text-2xl md:text-3xl font-extrabold tracking-[0.25em] text-white uppercase">
            &ldquo;<span className="text-[#F5C518]">FOOD</span> IS MY BEST FRIEND&rdquo;
          </h2>
        </motion.div>

        {/* Subtitle */}
        <motion.p
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          className="font-script-brand italic text-xl sm:text-2xl text-[#F5C518] mb-6 tracking-wide"
        >
          {brand.subtitle}
        </motion.p>

        {/* Brand Philosophy Bio */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="text-sm sm:text-base text-neutral-400 max-w-xl leading-relaxed mb-10 text-balance"
        >
          {brand.description}
        </motion.p>

        {/* Scroll CTA & Trigger */}
        <motion.button
          onClick={onExploreClick}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.5 }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.96 }}
          className="group flex flex-col items-center gap-3 text-[#F5C518] hover:text-white transition-colors cursor-pointer focus:outline-none"
        >
          <span className="text-xs font-bold tracking-[0.3em] uppercase">
            Scroll To Explore Menu
          </span>
          <div className="w-6 h-10 rounded-full border-2 border-[#F5C518] p-1 flex justify-center shadow-lg shadow-[#F5C518]/20 group-hover:border-white transition-colors">
            <motion.div
              animate={{ y: [0, 12, 0], opacity: [1, 0.2, 1] }}
              transition={{ duration: 1.8, repeat: Infinity, ease: "easeInOut" }}
              className="w-1.5 h-2.5 rounded-full bg-[#F5C518] group-hover:bg-white transition-colors"
            />
          </div>
          <ChevronDown className="w-4 h-4 animate-bounce text-[#F5C518] group-hover:text-white transition-colors" />
        </motion.button>
      </div>
    </section>
  );
};
