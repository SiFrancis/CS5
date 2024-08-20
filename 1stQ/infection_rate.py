POPULATION = 109674895

def main():
    """
    Asks the user to provide an infection rate and the loop checks when the disease will overrun the population.
    The population is stored in the constant POPULATION.
    """

    # initializations
    total_sick:float = 1
    number_of_days:int = 0
    starting:bool = False

    while not starting:
        infection_rate = float(input("infection_rate: "))
        if (infection_rate > 0): starting = True
        else: print("Please enter an infection rate greater than 0.\n")

    # loop
    while (total_sick < POPULATION) and starting:
        # at the start of the day, show the number of sick people
        print("Day {}: {:.4f} persons sick".format(number_of_days, total_sick))
        # infect others and update the number of sick
        new_sick = total_sick * infection_rate
        total_sick = total_sick + new_sick
        # at the end of the day, increase the accumulator for days
        number_of_days += 1

    # off by one error, display again
    # outside the loop
    print("Day {}: {:.4f} persons sick".format(number_of_days, total_sick))
    # display the final count of days
    print("With an infection rate of {}, it will take {} days to infect everyone.".format(infection_rate, number_of_days))

if __name__ == "__main__":
    main()