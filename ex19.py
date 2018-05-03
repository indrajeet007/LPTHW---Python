def tea_and_biscuits(tea_count, biscuits):
    print("You can have {} cups of tea!".format(tea_count))
    print("You also seem to have {} biscuits..".format(biscuits))
    print("Man that's enough for a day!")

# # provide direct inputs
# tea_and_biscuits(2, 8)
#
# # provide variables from this script
# amt_of_tea = 3
# amt_of_biscuits = 10
# tea_and_biscuits(amt_of_tea, amt_of_biscuits)
#
# # Do math inside the function inputs
# tea_and_biscuits(1 + 1, 5 + 3)
# tea_and_biscuits(amt_of_tea + 1, amt_of_biscuits + 5)

# user terminal inputs
amt_of_tea = input("Enter cups of tea: ")
amt_of_biscuits = input("Enter number of biscuits: ")

tea_and_biscuits(amt_of_tea, amt_of_biscuits)
