"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ThemeToggle } from "./theme-toggle";
import { ShoppingCart, Menu } from "lucide-react";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { useState } from "react";

export default function Header() {
  const [open, setOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 w-full border-b bg-background/80 backdrop-blur-md">
      <div className="container mx-auto flex h-16 items-center justify-between px-4">
        {/* LOGO */}
        <Link href="/" className="text-xl font-semibold">
          Jumas<span className="text-primary">Store</span>
        </Link>

        {/* NAV DESKTOP */}
        <nav className="hidden md:flex items-center gap-10">
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

        {/* AÇÕES */}
        <div className="flex items-center gap-2">
          <Button size="sm" variant="outline" className="hidden sm:flex items-center gap-2">
            <ShoppingCart size={16} />
            Carrinho
          </Button>
          <ThemeToggle />

          {/* MENU MOBILE */}
          <Sheet open={open} onOpenChange={setOpen}>
            <SheetTrigger asChild>
              <Button size="icon" variant="ghost" className="md:hidden">
                <Menu className="h-5 w-5" />
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-64 sm:w-80">
              <SheetHeader>
                <SheetTitle className="text-left text-xl font-semibold mb-4">
                  Menu
                </SheetTitle>
              </SheetHeader>
              <nav className="flex flex-col gap-4 px-3">
                <Link
                  href="/produtos"
                  className="text-base hover:text-primary"
                  onClick={() => setOpen(false)}
                >
                  Produtos
                </Link>
                <Link
                  href="/noticias"
                  className="text-base hover:text-primary"
                  onClick={() => setOpen(false)}
                >
                  Notícias
                </Link>
                <Link
                  href="/sobre"
                  className="text-base hover:text-primary"
                  onClick={() => setOpen(false)}
                >
                  Sobre
                </Link>
                <Button
                  size="sm"
                  variant="outline"
                  className="flex items-center gap-2 mt-6"
                  onClick={() => setOpen(false)}
                >
                  <ShoppingCart size={16} />
                  Carrinho
                </Button>
              </nav>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  );
}
