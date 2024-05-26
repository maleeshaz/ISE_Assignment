import re
class LifePath:
    MONTHS = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "octomober": "10",
        "november": "11",
        "december": "12"
    }
    
    @staticmethod
    def calculate_life_path_number(date):
        # convert any string formated date to numeric type
        date = LifePath.convert_date_to_numeric(date)

        total = sum(int(digit) for digit in date.replace("-", "") if digit.isdigit())
        while total > 9 and total not in {11, 22, 33}:
            total = sum(int(digit) for digit in str(total))
        return total
    
    @staticmethod
    def convert_date_to_numeric(date):
        # Convert date formats "09 July 2005" and "09-July-2005" to "2005-07-09"
        date = date.lower()
        for month, num in LifePath.MONTHS.items():
            date = date.replace(month, num)
        
        # Use regex to capture and rearrange the date parts
        match = re.match(r'(\d{1,2})[-\s](\d{1,2})[-\s](\d{4})', date)
        if match:
            day, month, year = match.groups()
            return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        
        # If date is already in "YYYY-MM-DD" format
        if re.match(r'\d{4}-\d{2}-\d{2}', date):
            return date

        raise ValueError("Invalid date format")


# date1 = "10 July 2005"
# date2 = "09-July-2005"
# date3 = "2005-07-09"

# print(LifePath.calculate_life_path_number(date1))  
# print(LifePath.calculate_life_path_number(date2))
# print(LifePath.calculate_life_path_number(date3))