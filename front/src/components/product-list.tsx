import products from "@/data/products.json";
import ProductCard from "@/components/product-card";

export default function ProductList() {
  return (
    <div className="grid gap-6 sm:grid-cols-2 md:grid-cols-3">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
