import requests


class PageDownloader:
    """
    Vastutab veebilehe HTML-i allalaadimise eest.
    """

    def download(self, url: str) -> str:
        """
        Laeb etteantud URL-i HTML sisu.

        :param url: Veebilehe aadress
        :return: HTML sisu stringina
        """
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text