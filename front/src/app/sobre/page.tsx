export default function SobrePage() {
  return (
    <section className="container mx-auto px-4 py-10 max-w-4xl">
      <h1 className="text-3xl font-bold mb-6 text-center">Sobre a Jumas Store</h1>

      <p className="text-muted-foreground mb-6 text-justify">
        A <strong>Jumas Store</strong> nasceu com o propósito de unir propósito e comunidade.
        Nosso e-commerce foi criado para apoiar as ações sociais e culturais do
        movimento <strong>Jumas Olinda</strong>, promovendo o bem através de produtos de
        qualidade e valores que fazem a diferença.
      </p>

      <div className="grid sm:grid-cols-2 gap-4 mb-10">
        <img
          src="https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?w=600"
          alt="Ação social Jumas"
          className="rounded-lg object-cover h-64 w-full"
        />
        <img
          src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600"
          alt="Equipe Jumas"
          className="rounded-lg object-cover h-64 w-full"
        />
      </div>

      <h2 className="text-2xl font-semibold mb-4">Entre em contato</h2>
      <ul className="space-y-2 text-muted-foreground">
        <li>Email: <a href="mailto:contato@jumasstore.com" className="text-primary">contato@jumasstore.com</a></li>
        <li>Instagram: <a href="https://instagram.com/jumasolinda" target="_blank" className="text-primary">@jumasolinda</a></li>
        <li>Telefone: (81) 99999-9999</li>
      </ul>
    </section>
  );
}
