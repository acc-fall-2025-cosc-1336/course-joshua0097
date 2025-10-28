
def get_dna_complement(dna: str) -> str:
    """
    Return the reverse complement of a DNA string using explicit loops only.
    No string slicing or other high-level built-ins for reversing are used.

    Raises:
    - TypeError if dna is not a string
    - ValueError if dna contains characters other than A, T, C, G (case-insensitive)
    """
    if not isinstance(dna, str):
        raise TypeError("dna must be a string")

    complement = {
        "A": "T", "T": "A", "C": "G", "G": "C",
        "a": "t", "t": "a", "c": "g", "g": "c",
    }

    result = ""
    i = len(dna) - 1
    while i >= 0:
        nuc = dna[i]
        if nuc in complement:
            result += complement[nuc]
        else:
            raise ValueError(f"Invalid nucleotide: {nuc!r}")
        i -= 1

    return result

def get_hamming_distance(dna1: str, dna2: str) -> int:
    """
    Compute Hamming distance using explicit loops only.
    Prints the two sequences with mismatched symbols colored red.
    """
    if not isinstance(dna1, str) or not isinstance(dna2, str):
        raise TypeError("Both dna1 and dna2 must be strings")
    if len(dna1) != len(dna2):
        raise ValueError("Sequences must be of equal length")

    RED = "\033[31m"
    RESET = "\033[0m"

    distance = 0
    colored1 = ""
    colored2 = ""

    i = 0
    n = len(dna1)
    while i < n:
        a = dna1[i]
        b = dna2[i]
        if a != b:
            distance += 1
            colored1 += RED + a + RESET
            colored2 += RED + b + RESET
        else:
            colored1 += a
            colored2 += b
        i += 1

    print("s:", colored1)
    print("t:", colored2)
    return distance