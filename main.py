def tip(bill: float, percent: float, people: int):
    """
    This function takes a bill amount and percentage, both floats, and the
    number of people, an integer, and calculates the tip by multiplying the
    bill amount by the percentage. The function then checks the number of
    people, and determines the individual amount basedon this number.
    """

    tip = bill * percent
    total = bill + tip
    if int(people) < 2:
        print(f"Your bill was {bill}.")
        print(f"{percent} of the bill is {tip}.")
        print(f"Your total is {total}.")

    elif int(people) > 1:
        print(f"The bill was {bill}.")
        print(f"{percent} of the bill is {tip}.")
        print(f"Your total is {total / people}.")
