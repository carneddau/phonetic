from typer import Exit, Option, Typer

from .utils import console, version

# Allow invocation without subcommand so --version option does not produce an error
interface = Typer()


def version_callback(print_version: bool):
    if print_version:
        console.print(version())
        raise Exit()


NATO_PHONETIC_LETTERS = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

NATO_PHONETIC_NUMBERS = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Tree",
    "4": "Fower",
    "5": "Fife",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Niner",
}


@interface.command()
def phonetic(
    input: str = Option(
        ...,
        "--input",
        "-i",
        help="Input string to map to phonetic code words",
    ),
    map_numbers: bool = Option(
        False,
        "--numbers",
        "-n",
        help="Map numeric characters to code words",
    ),
    _: bool = Option(
        False,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
    ),
):
    mapping = (
        NATO_PHONETIC_LETTERS | NATO_PHONETIC_NUMBERS
        if map_numbers
        else NATO_PHONETIC_LETTERS
    )

    for character in input:
        phonetic_name = mapping.get(character.upper())
        if phonetic_name is not None:
            console.print(phonetic_name, style="green")
        else:
            console.print(character, style="red")
