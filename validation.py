class Validation:
    @staticmethod
    def validate_date(date):
        try:
            parts = date.split('-')
            if len(parts) != 3:
                return False
            year, month, day = map(int, parts)
            return 1901 <= year <= 2024 and 1 <= month <= 12 and 1 <= day <= 31
        except ValueError:
            return False

    @staticmethod
    def validate_year(year):
        try:
            year = int(year)
            return 1901 <= year <= 2024
        except ValueError:
            return False
