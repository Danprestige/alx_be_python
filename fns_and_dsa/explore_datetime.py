from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()  # Save current datetime
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # return the datetime object for future use


def calculate_future_date(current_date, days_to_add):
    """Calculate and display the future date after adding given days"""
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Ask user for number of days to add
    while True:
        try:
            days_input = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer number of days.")

    calculate_future_date(current_date, days_input)


if __name__ == "__main__":
    main()
