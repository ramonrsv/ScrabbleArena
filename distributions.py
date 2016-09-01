class LetterDistribution:
    def __init__(self, blank, distribution):
        self.BLANK = blank
        self.distribution = distribution
        if not isinstance(distribution, dict):
            raise TypeError("distribution has to be a dictionary")
        if self.BLANK not in distribution:
            raise ValueError("BLANK has to be in distribution")

English_letter_distribution = LetterDistribution(
    blank=None,
    distribution={
        None: 0,
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10})
