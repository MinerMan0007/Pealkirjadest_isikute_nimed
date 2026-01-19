from pathlib import Path
from urllib.parse import urlparse


def load_websites() -> list[str]:
    """
    Laeb veebilehtede URL-id konfiguratsioonifailist.

    :return: URL-ide nimekiri
    """
    base_dir = Path(__file__).resolve().parent.parent
    config_file = base_dir / "config" / "websites.txt"

    with open(config_file, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def get_domain_name(url: str) -> str:
    """
    Teisendab URL-i sobivaks failinimeks.

    :param url: Veebilehe aadress
    :return: Domeeni nimi failinime jaoks
    """
    netloc = urlparse(url).netloc.replace("www.", "")
    return netloc.split(".")[0]
