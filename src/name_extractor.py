import re


class NameExtractor:
    """
    Leiab inimeste nimed pealkirjadest.
    """

    NAME_PATTERN = re.compile(
        r"\b([A-ZÕÄÖÜ][a-zõäöü]+(?:-[A-ZÕÄÖÜ][a-zõäöü]+)?"
        r"(?:\s+[A-ZÕÄÖÜ][a-zõäöü]+|\s+[A-Z]\.){1,3})\b"
    )

    def extract(self, headlines: list[dict]) -> list[dict]:
        """
        Tagastab nime, pealkirja ja URL-i.

        :param headlines: Pealkirjad koos URL-idega
        :return: List objektidest (name, headline, url)
        """
        results = []

        for item in headlines:
            matches = self.NAME_PATTERN.findall(item["headline"])
            for name in matches:
                results.append({
                    "name": name,
                    "headline": item["headline"],
                    "url": item["url"]
                })

        return results
