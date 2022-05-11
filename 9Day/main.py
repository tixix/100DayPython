import os
from logo import logo


def clear_console(): return os.system('cls')


def blind_auction():
    another_bid = True
    bids = {}
    print(logo)
    print("Welcome to the blind auction.")
    while another_bid:
        name = input("Whats your name? \n")
        bid = int(input("Whats your bid price? \n"))
        bids[name] = bid
        another = input("Is there another user who wants to bid (Y/N): \n")
        if another == "Y":
            continue
        else:
            print("The winner is " + next(iter(sort_dict_by_values(bids))) +
                  " with a bid of $" + str(bids[next(iter(sort_dict_by_values(bids)))]))
            break


def sort_dict_by_values(dict_to_check):
    sorted_dict = {}
    sorted_keys = sorted(dict_to_check, key=dict_to_check.get, reverse=True)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = dict_to_check[w]

    return sorted_dict


blind_auction()
