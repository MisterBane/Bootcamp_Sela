import statistics


def split_male_female(data_set):
    """
            A function that get dictionary as a parameter and returns 2 dictionaries -
            one for the elements where the "sex" field is equal to "male" and the other for
            the elements where the "sex" field is equal to "female"
            :param data_set: dictionary
            :return:
        """
    if type(data_set) is not dict:
        print("TypeError: split_male_female's parameter must be a dictionary")
        return {}, {}
    male = {}
    female = {}
    for details in d.values():
        if details['sex'] == 'male':
            male[details['name']] = details
        else:
            female[details['name']] = details
    return female, male


def find_median_average(data_set):
    """
            A function that get a dictionary,  finds the average age and median age of the ages inside the dictionaries
            of the given dictionary and print them
            :param data_set: dictionary
            :return: None
        """
    ages = []
    for key, item in data_set.items():
        ages.append(float(item["age"]))
    avg_age = sum(ages) / len(ages)
    print(f"The average age is: {avg_age}\n")
    print(f"The median age is : {statistics.median(ages)}\n")


def print_values_above(data_set, num=0):
    """
            Function that get a dictionary and a positive number - optional,
            If a number is received - a function will print elements that have an age field greater than the number
            If no - a function will print all the elements of the dictionary
            :param data_set: dictionary
            :param num: integer number
            :return: None
        """
    new_dict = {}
    for key, item in data_set.items():
        if item["age"] > num:
            new_dict[key] = item
        else:
            new_dict[key] = item  #in case no num is entered, num=0

    print(f"{new_dict=}\n")


def main():
    data_set = {651446216: {"name": "Tal", "sex": "male", "age": 22},
                154083593: {"name": "Haim", "sex": "male", "age": 43, "height": 1.72},
                590574215: {"name": "Shira", "sex": "female", "age": 21, "height": 1.64},
                528707765: {"name": "Yarden", "sex": "male", "age": 26}
                }
    female, male = split_male_female(data_set)
    print(female)
    print(male)
    split_male_female(data_set)
    find_median_average(data_set)
    print_values_above(data_set, )


main()
