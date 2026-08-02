from constants import UNDER_20, TENS, ABOVE_100


def num_to_word(num: int) -> str:

    """
    Function converts an integer into words.

    :param int num: The number to be converted to words.
    :return: The word representation of the number.
    :rtype: str
    """

    if num < 20:
        return UNDER_20 [num]
    
    elif num  < 100 : 
        remain = num % 10
        if remain == 0 :
            return TENS[num//10]
        return TENS[num//10] + " " + UNDER_20[remain]

    pivot = max([key for key in ABOVE_100 if key <= num ])
    p1 = num // pivot
    p2 = ABOVE_100[pivot]

    if num % pivot == 0:
        return f"{num_to_word(p1)} {p2}"

    return f"{num_to_word(p1)} {p2} {num_to_word(num % pivot)}"

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    if num >= 0 and num <= 999999999999:
        print(num_to_word(num))
        
    else:
        print("Number out of range")