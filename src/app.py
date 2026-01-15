from downloader import PageDownloader
from parser import HeadlineParser
from name_extractor import NameExtractor
from exporter import JsonExporter


class NewsApp:
    """
    Rakenduse põhilogika.
    """

    PORTALS = {
        "delfi": "https://www.delfi.ee",
        "postimees": "https://www.postimees.ee",
        "ohtuleht": "https://www.ohtuleht.ee"
    }

    def run(self):
        """
        Käivitab rakenduse.
        """
        print("Vali portaal: delfi, postimees, ohtuleht")
        choice = input(">>> ").strip().lower()

        if choice not in self.PORTALS:
            print("Tundmatu portaal!")
            return

        downloader = PageDownloader()
        parser = HeadlineParser()
        extractor = NameExtractor()
        exporter = JsonExporter()

        html = downloader.download(self.PORTALS[choice])
        headlines = parser.extract_headlines(html, self.PORTALS[choice])

        names = extractor.extract(headlines)
        exporter.export(choice, names)

        print(f"Leitud {len(names)} nime. Tulemus salvestatud {choice}.json faili.")


if __name__ == "__main__":
    NewsApp().run()
