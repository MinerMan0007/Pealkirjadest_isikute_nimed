from bs4 import BeautifulSoup


class HeadlineParser:
    """
    Leiab HTML-ist uudiste pealkirjad ja URL-id.
    """

    def extract_headlines(self, html: str, base_url: str) -> list[dict]:
        """
        Tagastab pealkirjad koos URL-idega.

        :param html: HTML sisu
        :param base_url: Portaali baas-URL
        :return: List sõnastikest (headline, url)
        """
        soup = BeautifulSoup(html, "html.parser")
        results = []

        for link in soup.find_all("a", href=True):
            headline = link.get_text(strip=True)
            href = link["href"]

            if not headline or len(headline.split()) < 3:
                continue

            if not href.startswith("http"):
                href = base_url.rstrip("/") + "/" + href.lstrip("/")

            results.append({
                "headline": headline,
                "url": href
            })

        return results
