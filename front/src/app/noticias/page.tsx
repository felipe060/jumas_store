import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import newsData from "@/data/news.json";

export default function NoticiasPage() {
  return (
    <section className="container mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-6 text-center">Últimas Notícias</h1>

      <div className="grid gap-6 sm:grid-cols-2 md:grid-cols-3">
        {newsData.map((news) => (
          <Card
            key={news.id}
            className="overflow-hidden transition-all hover:scale-[1.02] hover:shadow-lg"
          >
            <CardHeader className="p-0">
              <img
                src={news.image}
                alt={news.title}
                className="w-full h-48 object-cover"
              />
            </CardHeader>

            <CardContent className="p-4">
              <h3 className="font-semibold text-lg mb-2">{news.title}</h3>
              <p className="text-sm text-muted-foreground line-clamp-3">
                {news.description}
              </p>
            </CardContent>

            <CardFooter className="p-4">
              <Link href={`/noticias/${news.id}`} className="w-full">
                <Button className="w-full" variant="outline">
                  Ler mais
                </Button>
              </Link>
            </CardFooter>
          </Card>
        ))}
      </div>
    </section>
  );
}
