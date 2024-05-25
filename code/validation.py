from datetime import datetime

class Validation:
    @staticmethod
    def validate_date(date):
        try:
            # Attempt to parse the date string to ensure it is in the correct format
            parsed_date = datetime.strptime(date, '%Y-%m-%d')
            # print(parsed_date)
            # Extract the year to perform additional range check
            year = parsed_date.year
            return 1901 <= year <= 2024
        except ValueError:
            return False

    @staticmethod
    def validate_year(year):
        try:
            year = int(year)
            return 1901 <= year <= 2024
        except ValueError:
            return False
        
# print(Validation.validate_date("2020-12-25"))  # True
# print(Validation.validate_date("2020-02-29"))  # True (2020 is a leap year)
# print(Validation.validate_date("2021-02-29"))  # False (2021 is not a leap year)
# print(Validation.validate_date("2020-13-01"))  # False (Invalid month)
# print(Validation.validate_date("2020-11-31"))  # False (November has 30 days)
# print(Validation.validate_date("1899-05-20"))  # False (Year out of range)
# print(Validation.validate_date("2025-05-20"))  # False (Year out of range)
# print(Validation.validate_date("2020-10-12"))  # True
# print(Validation.validate_date("2020-12-10"))