def create_month_dictionary():
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return months


def get_days_in_month(months):
    month_name = input("Enter a month name: ")
    if month_name in months:
        days = months[month_name]
        print(f"There are {days} days in {month_name}.")
    else:
        print(f"Invalid month name.")


def print_month_names(months):
    sorted_months = sorted(months.keys())
    print("Month names in alphabetical order:")
    for month in sorted_months:
        print(month)


def print_months_with_31_days(months):
    month_names = [month for month, days in months.items() if days == 31]
    print("Months with 31 days:")
    for month in month_names:
        print(month)


def print_sorted_by_days(months):
    sorted_months = sorted(months.items(), key=lambda x: x[1])
    print("Months sorted by number of days:")
    for month, days in sorted_months:
        print(f"{month}: {days} days")


month_dict = create_month_dictionary()
get_days_in_month(month_dict)
print()
print_month_names(month_dict)
print()
print_months_with_31_days(month_dict)
print()
print_sorted_by_days(month_dict)
print()