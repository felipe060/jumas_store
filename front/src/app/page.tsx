import ProductCard from "@/components/product-card";

const mockProducts = [
  {
    id: 1,
    name: "Camiseta Jumas Classic",
    price: 89.9,
    image: "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600",
  },
  {
    id: 2,
    name: "Boné Jumas Explorer",
    price: 69.9,
    image: "https://images.unsplash.com/photo-1528701800489-20be3c2ea33d?w=600",
  },
  {
    id: 3,
    name: "Mochila Aventura",
    price: 199.9,
    image: "https://images.unsplash.com/photo-1503341455253-b2e723bb3dbb?w=600",
  },
];

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <section>
      <h1 className="text-3xl font-bold mb-6 text-center">
        Produtos em Destaque
      </h1>
      <div className="grid gap-6 sm:grid-cols-2 md:grid-cols-3">
        {mockProducts.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </section>
    </div>
  );
}
