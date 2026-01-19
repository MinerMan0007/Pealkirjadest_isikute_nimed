from downloader import PageDownloader
from parser import HeadlineParser
from name_extractor import NameExtractor
from exporter import JsonExporter
from utils import load_websites


class NewsApp:
    """
    Rakenduse põhilogika, mis juhib andmete kogumist ja töötlemist.
    """

    def run(self) -> None:
        """
        Käivitab rakenduse ja töötleb kõik konfigureeritud veebilehed.
        """
        print("Uudiste nimede koguja käivitub...\n")

        websites = load_websites()

        downloader = PageDownloader()
        parser = HeadlineParser()
        extractor = NameExtractor()
        exporter = JsonExporter()

        for url in websites:
            print(f"Töötlen veebilehte: {url}")

            html = downloader.download(url)
            headlines = parser.extract_headlines(html, url)
            results = extractor.extract(headlines)

            exporter.export(url, results)

            print(f"Leitud {len(results)} kirjet.\n")
if __name__ == "__main__":
    app = NewsApp()
    app.run()
