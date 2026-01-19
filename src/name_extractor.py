import re


class NameExtractor:
    """
    Leiab inimeste nimed pealkirjadest.
    """

    NAME_PATTERN = re.compile(
        r"[A-ZÕÄÖÜ][a-zõäöü]+(?:\s+[A-ZÕÄÖÜ][a-zõäöü]+)+"
    )

    def extract(self, headlines: list[dict]) -> list[dict]:
        """
        Leiab pealkirjadest nimed ja eemaldab duplikaadid.

        :param headlines: Pealkirjade ja URL-ide nimekiri
        :return: Unikaalsed tulemused
        """
        results = []
        seen = set()

        for item in headlines:
            names = self.NAME_PATTERN.findall(item["headline"])

            if not names:
                continue

            names_str = ", ".join(names)
            key = (names_str, item["headline"], item["url"])

            if key in seen:
                continue

            seen.add(key)

            results.append({
                "names": names_str,
                "headline": item["headline"],
                "url": item["url"]
            })

        return results
