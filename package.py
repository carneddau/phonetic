#!/usr/bin/env python
from os import remove
from tempfile import mkstemp
from textwrap import dedent

from PyInstaller.__main__ import run

_, temp_file = mkstemp(suffix=".py")

file_contents = dedent(
    """\
    from phonetic.__main__ import main

    if __name__ == "__main__":
        main()
    """
)

with open(temp_file, "w", encoding="UTF8") as file:
    file.write(file_contents)

run(
    [
        temp_file,
        "--copy-metadata",
        "phonetic",
        "--name",
        "phonetic",
    ]
)

remove(temp_file)
