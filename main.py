from life_path import LifePath
from luck_colors import LuckyColour
from master_number import MasterNumber
from generation import Generation
from validation import Validation

def main():
    while True:
        print("1. Calculate Life Path Number")
        print("2. Determine Generation")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter birth date (YYYY-MM-DD): ")
            if Validation.validate_date(date):
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

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
