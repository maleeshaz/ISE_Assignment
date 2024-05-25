class Generation:
    GENERATIONS = [
        (1901, 1927, "G.I. Generation"),
        (1928, 1945, "Silent Generation"),
        (1946, 1964, "Baby Boomers"),
        (1965, 1980, "Generation X"),
        (1981, 1996, "Millennials"),
        (1997, 2012, "Generation Z"),
        (2013, 2024, "Generation Alpha"),
    ]

    @staticmethod
    def determine_generation(year):
        for start, end, generation in Generation.GENERATIONS:
            if start <= year <= end:
                return generation
        return "Unknown Generation"
