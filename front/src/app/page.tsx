import ProductList from "@/components/product-list";


export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <section className="container mx-auto px-4 py-10">
        <h1 className="text-3xl font-bold mb-6 text-center">
          Produtos em Destaque
        </h1>
        <ProductList />
      </section>
    </div>
  );
}
