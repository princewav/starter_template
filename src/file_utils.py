import csv
import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional


class File:
    def __init__(self, root: Path):
        self.root = root
        if not self.root.exists():
            raise ValueError(f"{str(self.root)} doesn't exists")


class JSON(File):
    def load(self, filename_no_ext: str) -> Any:
        with (self.root / f"{filename_no_ext}.json").open() as f:
            return json.load(f)

    def dump(self, filename_no_ext: str, data: Any, **kwargs) -> None:
        with (self.root / f"{filename_no_ext}.json").open("w") as f:
            json.dump(data, f, **kwargs)


class TXT(File):
    def read(self, filename_no_ext: str) -> str:
        with (self.root / f"{filename_no_ext}.txt").open() as f:
            return f.read()

    def write(self, filename_no_ext: str, text: str) -> None:
        with (self.root / f"{filename_no_ext}.txt").open("w") as f:
            f.write(text)

    def parse_table(self, filename_no_ext: str) -> List[Dict[str, Optional[str]]]:
        text = self.read(filename_no_ext)
        header, *lines = (line.split("\t") for line in text.split("\n"))
        return [
            dict(zip(header, [x if x != "NULL" else None for x in line]))
            for line in lines
        ]


class CSV(File):
    def make_csv(self, filename_no_ext: str, data: List[Dict]):
        filepath = self.root / f"{filename_no_ext}.csv"
        with filepath.open("w") as f:
            fields = sorted(data, key=len)[-1].keys()
            dict_writer = csv.DictWriter(f, list(fields), extrasaction="ignore")
            dict_writer.writerow(dict(zip(fields, fields)))  # header
            dict_writer.writerows(data)
            print(f'CSV "{filepath}" generated.')

    def load_csv(self, filename: str, delimiter=";") -> List[Dict[str, str]]:
        filepath = self.root / f"{filename}.csv"
        with filepath.open() as f:
            info = list(csv.reader(f, delimiter=delimiter))
            header = [x.strip() for x in info.pop(0)]
            return [
                {field: value.replace("\xa0", "") for field, value in zip(header, item)}
                for item in info
            ]
