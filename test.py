import csv
import textwrap
import re
import yaml
from collections import defaultdict
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
from pathlib import Path


with open("colors.tsv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    each_row = list(reader)

    hex_codes = {row["hex"].strip('# '): row['number']  for row in each_row}

    # colors = defaultdict(list)
    # seen = set()
    # dupes = set()
    # for row in each_row:
    #     if row["name"] in seen:
    #         dupes.add(row["name"])
    #     seen.add(row["name"])

    new_dupes = set()
    seen = set()
    results = {}
    for hex_code, number in hex_codes.items():
        # Get color name from https://https://encycolorpedia.com/{hex}
        url = f'https://encycolorpedia.com/{hex_code}'.strip()
        # print(f"Fetching {url}")
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        info = soup.select("#information > h1", first=True)[0].text

        if "/" in info:
            name = info.split("/")[0].strip()
        else:
            name = (
                soup.select("#named > ul > li > ol > li > a", first=True)[0]
                .text.strip()
                .split("#")[0]
            )

        results[hex_code] = {"name": name, "ansi": number}
        if name in seen:
            new_dupes.add(name)
        seen.add(name)

        # print(f"Another name for {row['name']} {row['hex']} " f"is {name}")


    Path("colors.yaml").write_text(yaml.safe_dump(results, sort_keys=True))

    print(f"dupes {new_dupes}")

    # for row in each_row:
    #     if row['name'] in dupes:

    # for each_dupe in dupes:
    #     # Get a better color name from online
    #     print(f"{each_dupe} is duplicated")

    # colors = {row.pop("name"): row for row in sorted(reader, key=lambda i: i["name"])}

    # for name, info in colors.items():
    #     ansi = info["number"]
    #     print(
    #         textwrap.dedent(
    #             f"""
    #             def in_{name}(text: str): -> "StyledStr":
    #                 return _change_text_color(text, "{ansi}")
    #             """
    #         )
    #     )

    # for row in sorted(reader, key=lambda i: i["name"]):
    #     name = re.sub("(?<!^)(?=[A-Z0-9])", "_", row["name"]).lower()
    #     ansi = row["number"]
    #     print(
    #         textwrap.dedent(
    #             f"""
    #             def in_{name}(text: str): -> "StyledStr":
    #                 return _change_text_color(text, "{ansi}")
    #             """
    #         )
    #     )
