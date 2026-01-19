from pathlib import Path
import json
from utils import get_domain_name


class JsonExporter:
    """
    Salvestab tulemused JSON faili.
    """

    def export(self, url: str, data: list[dict]) -> None:
        """
        Salvestab andmed JSON faili.

        :param url: Veebilehe aadress
        :param data: Töödeldud tulemused
        """
        base_dir = Path(__file__).resolve().parent.parent
        output_dir = base_dir / "json_files"
        output_dir.mkdir(exist_ok=True)

        filename = get_domain_name(url) + ".json"
        file_path = output_dir / filename

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
