"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ThemeToggle } from "./theme-toggle";
import { ShoppingCart } from "lucide-react";

export default function Header() {
  return (
    <header className="sticky top-0 z-40 w-full border-b bg-background/80 backdrop-blur-md">
      <div className="container mx-auto flex h-16 items-center justify-between px-4">
        <Link href="/" className="text-xl font-semibold">
          Jumas<span className="text-primary">Store</span>
        </Link>

        <nav className="flex items-center gap-4">
          <Link href="/produtos" className="text-sm font-medium hover:text-primary">
            Produtos
          </Link>
          <Link href="/noticias" className="text-sm font-medium hover:text-primary">
            Notícias
          </Link>
          <Link href="/sobre" className="text-sm font-medium hover:text-primary">
            Sobre
          </Link>
        </nav>

        <div className="flex items-center gap-2">
          <Button size="sm" variant="outline" className="flex items-center gap-2">
            <ShoppingCart size={16} />
            Carrinho
          </Button>
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
