class LuckyColour:
    COLOURS = {
        1: "Red",
        2: "Orange",
        3: "Yellow",
        4: "Green",
        5: "Blue",
        6: "Indigo",
        7: "Violet",
        8: "Pink",
        9: "Gold",
        11: "Silver",
        22: "Brown",
        33: "White"
    }

    @staticmethod
    def get_lucky_colour(life_path_number):
        return LuckyColour.COLOURS.get(life_path_number, "Unknown")
