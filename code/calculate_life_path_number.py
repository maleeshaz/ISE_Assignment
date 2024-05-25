class LifePath:
    @staticmethod
    def calculate_life_path_number(date):
        total = sum(int(digit) for digit in date.replace("-", "") if digit.isdigit())
        while total > 9 and total not in {11, 22, 33}:
            total = sum(int(digit) for digit in str(total))
        return total
