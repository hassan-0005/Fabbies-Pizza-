import React from "react";
import { X, Trash2, Send, ShoppingBag } from "lucide-react";

export interface CartItem {
  id: string;
  name: string;
  price: string;
  variant?: string;
  quantity: number;
}

interface CartDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  items: CartItem[];
  onUpdateQuantity: (id: string, delta: number) => void;
  onRemoveItem: (id: string) => void;
  onClearCart: () => void;
  whatsappNumber: string;
}

export const CartDrawer: React.FC<CartDrawerProps> = ({
  isOpen,
  onClose,
  items,
  onUpdateQuantity,
  onRemoveItem,
  onClearCart,
  whatsappNumber,
}) => {
  if (!isOpen) return null;

  const totalAmount = items.reduce((sum, item) => {
    const raw = parseInt(item.price.replace(/,/g, ""), 10) || 0;
    return sum + raw * item.quantity;
  }, 0);

  const handleCheckoutWhatsApp = () => {
    if (items.length === 0) return;

    let text = `*New Order - FABBIES Restaurant*\n\n`;
    items.forEach((item, index) => {
      text += `${index + 1}. *${item.name}* ${item.variant ? `(${item.variant})` : ""}\n`;
      text += `   Qty: ${item.quantity} x Rs.${item.price} = Rs.${
        (parseInt(item.price.replace(/,/g, ""), 10) || 0) * item.quantity
      }\n`;
    });
    text += `\n*Total Bill: Rs.${totalAmount.toLocaleString()}*\n`;
    text += `\nPlease confirm my order and delivery time!`;

    const encoded = encodeURIComponent(text);
    window.open(`https://wa.me/${whatsappNumber}?text=${encoded}`, "_blank");
  };

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/75 backdrop-blur-sm animate-fade-in">
      <div className="w-full max-w-md bg-[#111215] border-l border-white/10 h-full flex flex-col shadow-2xl">
        {/* Header */}
        <div className="flex items-center justify-between p-5 border-b border-white/10 bg-[#16171c]">
          <div className="flex items-center gap-3">
            <ShoppingBag className="w-5 h-5 text-[#F5C518]" />
            <h3 className="font-serif-brand text-lg font-bold text-white tracking-wide">
              Your Food Order
            </h3>
            <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-[#F5C518]/15 text-[#F5C518]">
              {items.reduce((acc, i) => acc + i.quantity, 0)} items
            </span>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-neutral-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Items List */}
        <div className="flex-1 overflow-y-auto p-5 space-y-4">
          {items.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center py-12 text-neutral-400">
              <ShoppingBag className="w-16 h-16 text-neutral-700 mb-4" />
              <p className="text-base font-semibold text-neutral-300 mb-1">
                Your platter is empty
              </p>
              <p className="text-xs text-neutral-400 max-w-xs">
                Explore our legendary deep-dish pizzas, crispy zinger burgers, and loaded platters to build your feast.
              </p>
            </div>
          ) : (
            items.map((item) => (
              <div
                key={item.id}
                className="flex items-center justify-between p-3.5 rounded-xl bg-white/5 border border-white/5 hover:border-white/10 transition-colors"
              >
                <div className="flex-1 pr-3">
                  <h4 className="text-sm font-bold text-white line-clamp-1">
                    {item.name}
                  </h4>
                  {item.variant && (
                    <span className="text-[11px] text-[#F5C518] font-medium block">
                      {item.variant}
                    </span>
                  )}
                  <span className="text-xs font-semibold text-neutral-400">
                    Rs. {item.price} each
                  </span>
                </div>

                <div className="flex items-center gap-3">
                  {/* Quantity Stepper */}
                  <div className="flex items-center gap-2 bg-black/40 rounded-lg p-1 border border-white/10">
                    <button
                      onClick={() => onUpdateQuantity(item.id, -1)}
                      className="w-6 h-6 rounded flex items-center justify-center text-xs font-bold text-neutral-300 hover:bg-white/10 hover:text-white"
                    >
                      -
                    </button>
                    <span className="text-xs font-bold text-white w-4 text-center tabular-nums">
                      {item.quantity}
                    </span>
                    <button
                      onClick={() => onUpdateQuantity(item.id, 1)}
                      className="w-6 h-6 rounded flex items-center justify-center text-xs font-bold text-neutral-300 hover:bg-white/10 hover:text-white"
                    >
                      +
                    </button>
                  </div>

                  <button
                    onClick={() => onRemoveItem(item.id)}
                    className="p-1.5 text-neutral-400 hover:text-red-400 transition-colors"
                    title="Remove item"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>

        {/* Summary & Checkout Action */}
        {items.length > 0 && (
          <div className="p-5 border-t border-white/10 bg-[#16171c] space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-xs uppercase tracking-wider text-neutral-400 font-semibold">
                Estimated Total
              </span>
              <span className="text-2xl font-black text-[#F5C518] tabular-nums">
                <span className="text-xs font-bold text-white mr-1">Rs.</span>
                {totalAmount.toLocaleString()}
              </span>
            </div>

            <div className="flex gap-2">
              <button
                onClick={onClearCart}
                className="px-3 py-2.5 rounded-xl border border-white/10 hover:border-red-500/30 text-xs font-semibold text-neutral-400 hover:text-red-400 transition-colors cursor-pointer"
              >
                Clear
              </button>
              <button
                onClick={handleCheckoutWhatsApp}
                className="flex-1 flex items-center justify-center gap-2 py-3 px-4 rounded-xl bg-gradient-to-r from-[#25D366] to-[#1ebe5b] text-white font-bold text-sm shadow-lg shadow-[#25D366]/20 hover:brightness-110 transition-all cursor-pointer"
              >
                <Send className="w-4 h-4" />
                <span>Confirm Order on WhatsApp</span>
              </button>
            </div>

            <p className="text-[11px] text-center text-neutral-400">
              Fast delivery within 35–45 minutes · Cash on Delivery available
            </p>
          </div>
        )}
      </div>
    </div>
  );
};
