import newsData from "@/data/news.json";
import { notFound } from "next/navigation";

interface NoticiaPageProps {
  params: { id: string };
}

export default function NoticiaPage({ params }: NoticiaPageProps) {
  const noticia = newsData.find((item) => item.id === Number(params.id));

  if (!noticia) return notFound();

  return (
    <article className="container mx-auto px-4 py-10 max-w-3xl">
      <img
        src={noticia.image}
        alt={noticia.title}
        className="w-full h-72 object-cover rounded-lg mb-6"
      />

      <h1 className="text-3xl font-bold mb-4">{noticia.title}</h1>

      <p className="text-muted-foreground leading-relaxed mb-4">
        {noticia.description}
      </p>

      <p className="text-sm text-muted-foreground">
        Publicado em {new Date().toLocaleDateString("pt-BR")}
      </p>

      <div className="mt-6 text-justify text-muted-foreground">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer
          facilisis erat et nisl varius, ut volutpat felis egestas. Cras sed
          justo sed purus tincidunt suscipit. Sed eget turpis non justo
          efficitur bibendum.
        </p>
        <p className="mt-4">
          Praesent accumsan, sem nec consequat imperdiet, orci lacus sagittis
          nulla, ut tristique leo turpis vitae nulla. Donec vulputate mi sed
          nisl posuere, nec tristique libero laoreet.
        </p>
      </div>
    </article>
  );
}
