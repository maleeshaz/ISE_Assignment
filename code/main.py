from calculate_life_path_number import LifePath
from identify_luck_color import LuckyColour
from check_master_number import MasterNumber
from determine_generation import Generation
from validation import Validation

def main():
    while True:
        print("1. Calculate Life Path Number")
        print("2. Determine Generation")
        print("3. Compare Life Path Numbers of Two Birthdays")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter birth date (YYYY-MM-DD): ")
            suit = Validation.validate_date(date)
            print(suit)
            if suit:
                life_path_number = LifePath.calculate_life_path_number(date)
                lucky_colour = LuckyColour.get_lucky_colour(life_path_number)
                is_master = MasterNumber.is_master_number(life_path_number)
                print(f"Life Path Number: {life_path_number}")
                print(f"Lucky Colour: {lucky_colour}")
                print(f"Master Number: {'Yes' if is_master else 'No'}")
            else:
                print("Invalid date. Please try again.")

        elif choice == '2':
            year = input("Enter birth year: ")
            if Validation.validate_year(year):
                generation = Generation.determine_generation(int(year))
                print(f"Generation: {generation}")
            else:
                print("Invalid year. Please try again.")

        elif choice == '3':
            date1 = input("Enter the first birth date (YYYY-MM-DD): ")
            date2 = input("Enter the second birth date (YYYY-MM-DD): ")
            if Validation.validate_date(date1) and Validation.validate_date(date2):
                life_path_number1 = LifePath.calculate_life_path_number(date1)
                life_path_number2 = LifePath.calculate_life_path_number(date2)
                if life_path_number1 == life_path_number2:
                    print("The Life Path Numbers are the same.")
                else:
                    print("The Life Path Numbers are different.")
                print(f"Life Path Number for {date1}: {life_path_number1}")
                print(f"Life Path Number for {date2}: {life_path_number2}")
            else:
                print("One or both dates are invalid. Please try again.")

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
