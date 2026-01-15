import json
from pathlib import Path


class JsonExporter:
    """
    Salvestab tulemused JSON faili.
    """

    def export(self, domain: str, data: list[dict]) -> None:
        """
        Salvestab nimekirja JSON faili.

        :param domain: Domeeni nimi
        :param data: Tulemused
        """
        base_dir = Path(__file__).resolve().parent.parent
        output_dir = base_dir / "output"
        output_dir.mkdir(exist_ok=True)

        file_path = output_dir / f"{domain}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
