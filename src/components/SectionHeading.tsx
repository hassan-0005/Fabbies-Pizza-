import React from "react";
import { motion } from "motion/react";
import { LucideIcon } from "lucide-react";

interface SectionHeadingProps {
  kicker: string;
  title: string;
  icon?: LucideIcon;
  subtitle?: string;
}

export const SectionHeading: React.FC<SectionHeadingProps> = ({
  kicker,
  title,
  icon: Icon,
  subtitle,
}) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
      className="text-center mb-10 max-w-2xl mx-auto"
    >
      <span className="text-xs font-extrabold tracking-[0.3em] uppercase text-[#F5C518] block mb-2">
        {kicker}
      </span>
      <h2 className="font-serif-brand text-3xl sm:text-4xl md:text-5xl font-black text-white tracking-wide mb-3">
        {title}
      </h2>

      <div className="flex items-center justify-center gap-4 mt-2">
        <span className="h-[2px] w-16 bg-gradient-to-r from-transparent to-[#F5C518]" />
        {Icon && <Icon className="w-5 h-5 text-[#F5C518]" />}
        <span className="h-[2px] w-16 bg-gradient-to-l from-transparent to-[#F5C518]" />
      </div>

      {subtitle && (
        <p className="text-xs sm:text-sm text-neutral-400 mt-3 font-medium">
          {subtitle}
        </p>
      )}
    </motion.div>
  );
};
