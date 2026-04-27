print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(temperature_list):
    return sum(temperature_list / len(temperature_list))

def get_user_input():
    user_input = input("Enter temperatures: ")
    string_list = user_input.split(",")
    temperature_list = [float(x.strip()) for x in string_list] 
    return float_list

def find_min_max():
    return [min(temperature_list), max(temperature_list)]

def sort_temperature():
    return sorted(temperature_list)

def calc_median_temperature():
    sorted_list = sorted(temperature_list)
    n - len(sorted_list)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        return sorted_list[middle]
    
def main():
    display_main_menu()
    temperature_list = get_user_input()

    print("Temperature List:", temperature_list)
    print("Average Temperature:", calc_average(temperature_list))

    min_max = find_min_max(temperature_list)
    print("Minimum Temperature:", min_max[0])
    print("Maximum Temperature:", min_max[1])

    print("Sorted Temperatures:", sort_temperature(temperature_list))
    print("Median Temperature:", calc_median_temperature(temperature_list))


if __name__ == "__main__":
    main()
