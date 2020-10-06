# Team WAK -- William Yin, Anya Zorin, Kelly Huang
# SoftDev
# K07 -- StI/O: Divine your Destiny!
# 2020-10-01


def build_dict(file_name):
    """
    Takes a str parameter representing name of the csv file to be opened, and
    creates a dictionary where for each pair, the key is the occupation name in
    the first column, and the value is the percentage in the second column.
    """
    file = open(file_name, 'r')
    # Skips the first line in the file which is the heading.
    file.readline()
    occupation_dict = {}
    # Reads the file line-by-line.
    for line in file:
        # Splits each line by their commas so we can separate the values.
        values = line.split(',')
        # The occupation name is all the values except for the last one on
        # that line joined together into a string (handles names with commas).
        occupation_name = ''.join(values[:-1])
        # Occupation percentage will always be the last value on that line.
        # Value will be a str so it must be converted to a float.
        occupation_percentage = float(values[-1])
        occupation_dict[occupation_name] = occupation_percentage
    file.close()
    return occupation_dict


def select_occupation(occupation_dict):
    """
    Takes a parameter of type dict and selects a random occupation weighted by
    the percentage given.
    """
    # From Python docs:
    # Returns the next random floating point number in the range [0.0, 1.0).
    from random import random
    # Sum of all percentages does not sum to exactly 100, so the number chosen
    # must be on the interval [0, occupation_dict['Total']).
    num = random() * occupation_dict['Total']

    # The variable counter will be accumulated by adding the percentages to it
    # until it is greater than or equal to the value in num, at which point the
    # chosen occupation is the one whose percentage pushed counter above num.
    # This creates intervals for each occupation where the length of each
    # interval is equal to that occupation's percentage.
    # For example, "Computer and Mathematical" have a percentage of 2.7, and
    # "Management" and "Business and Financial operations" have a percentage of
    # 6.1 and 5 respectively. This means for Computer and Mathematical to be
    # chosen, a number on the interval (11.1, 13.8] must be chosen. Since each
    # number on the interval [0, occupation_dict['Total']) has an equal chance
    # of being picked, this gives Computer and Mathematical a 2.7% chance of
    # being picked
    counter = 0
    # Converts each key-value pair in occupation_dict to a tuple where name is
    # the first value and percentage is the second.
    for name, percentage in occupation_dict.items():
        counter += percentage
        if counter >= num:
            return name


def main():
    """
    Main function.
    """
    file_name = 'occupations.csv'
    occupation_dict = build_dict(file_name)
    occupation = select_occupation(occupation_dict)
    print(occupation)

main()
