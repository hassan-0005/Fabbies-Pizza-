import React, { useState } from "react";
import { Plus, Check } from "lucide-react";

interface FoodCardProps {
  name: string;
  description: string;
  image: string;
  price?: string;
  prices?: Record<string, string>;
  serving?: string;
  badge?: string;
  onAddToCart?: (item: { name: string; price: string; variant?: string }) => void;
}

export const FoodCard: React.FC<FoodCardProps> = ({
  name,
  description,
  image,
  price,
  prices,
  serving,
  badge,
  onAddToCart,
}) => {
  const [selectedSize, setSelectedSize] = useState<string>(
    prices ? Object.keys(prices)[0] : ""
  );
  const [isAdded, setIsAdded] = useState(false);

  const currentPrice = prices ? prices[selectedSize] : price || "0";

  const handleAdd = () => {
    if (onAddToCart) {
      onAddToCart({
        name,
        price: currentPrice,
        variant: prices ? selectedSize : serving,
      });
      setIsAdded(true);
      setTimeout(() => setIsAdded(false), 1200);
    }
  };

  return (
    <div className="group relative flex flex-col bg-[#141519] border border-white/8 hover:border-[#F5C518]/50 rounded-2xl overflow-hidden shadow-xl shadow-black/50 hover:shadow-2xl hover:shadow-[#F5C518]/10 transition-all duration-300 hover:-translate-y-1.5">
      {/* Visual media container */}
      <div className="relative w-full h-52 sm:h-56 overflow-hidden bg-neutral-900">
        <img
          src={image}
          alt={name}
          loading="lazy"
          referrerPolicy="no-referrer"
          className="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-108"
          onError={(e) => {
            // Elegant image fallback
            (e.target as HTMLElement).style.display = "none";
          }}
        />
        <div className="absolute inset-0 bg-gradient-to-t from-[#141519] via-transparent to-transparent opacity-80" />

        {/* Subtle Badge */}
        {badge && (
          <div className="absolute top-3 right-3 px-3 py-1 rounded-full text-[11px] font-bold tracking-wider uppercase bg-[#E63932] text-white shadow-lg shadow-black/60">
            {badge}
          </div>
        )}

        {/* Serving micro-label */}
        {serving && (
          <div className="absolute bottom-3 left-3 px-2.5 py-0.5 rounded-md text-[11px] font-semibold tracking-wider uppercase bg-black/75 text-[#F5C518] backdrop-blur-sm border border-[#F5C518]/20">
            {serving}
          </div>
        )}
      </div>

      {/* Card Content Details */}
      <div className="flex flex-col flex-1 p-5">
        <h3 className="font-serif-brand text-lg sm:text-xl font-bold text-white group-hover:text-[#F5C518] transition-colors mb-2 tracking-wide line-clamp-1">
          {name}
        </h3>
        
        <p className="text-xs sm:text-sm text-neutral-400 leading-relaxed mb-4 flex-1 line-clamp-3">
          {description}
        </p>

        {/* Multi-size selector if item has size variations */}
        {prices && (
          <div className="mb-4">
            <span className="text-[11px] font-bold uppercase tracking-wider text-neutral-400 block mb-2">
              Select Size
            </span>
            <div className="flex flex-wrap gap-1.5">
              {Object.entries(prices).map(([size, p]) => (
                <button
                  key={size}
                  onClick={() => setSelectedSize(size)}
                  className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all whitespace-nowrap cursor-pointer ${
                    selectedSize === size
                      ? "bg-[#F5C518] text-black shadow-md shadow-[#F5C518]/20"
                      : "bg-white/5 hover:bg-white/10 text-neutral-300 border border-white/5"
                  }`}
                >
                  {size} <span className="opacity-80">· Rs.{p}</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Price & Action Row */}
        <div className="flex items-center justify-between pt-3 border-t border-white/10 mt-auto">
          <div>
            <span className="text-[10px] font-semibold text-neutral-400 uppercase tracking-widest block">
              {prices ? selectedSize : "Price"}
            </span>
            <div className="text-xl font-extrabold text-[#F5C518] tracking-tight tabular-nums">
              <span className="text-xs font-bold text-white mr-1">Rs.</span>
              {currentPrice}
            </div>
          </div>

          <button
            onClick={handleAdd}
            className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-bold transition-all shadow-md cursor-pointer whitespace-nowrap ${
              isAdded
                ? "bg-emerald-500 text-white"
                : "bg-white/10 hover:bg-[#F5C518] text-white hover:text-black border border-white/10 hover:border-[#F5C518]"
            }`}
          >
            {isAdded ? (
              <>
                <Check className="w-3.5 h-3.5" />
                <span>Added</span>
              </>
            ) : (
              <>
                <Plus className="w-3.5 h-3.5" />
                <span>Add Item</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
