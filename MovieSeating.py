import sys
import os
import re
import itertools
from FindRows import *
import csv

if __name__ == "__main__":

    # Read the file and make a dictionary where the keys are
    # the reservation numbers and the values are the number of seats reserved
    # for that reservation number.
    reserve_dict = {}
    with open(sys.argv[1], 'r') as input_file:
        line = input_file.readline().rstrip()
        while line != "":
            linedata = re.split(" ", line)
            reserve_dict[linedata[0]] = int(linedata[1])
            line = input_file.readline().rstrip()

    row_dict, order_dict = arrange_seating(reserve_dict)
    sorted_tuples = sorted(order_dict.items(), key=operator.itemgetter(0))
    sorted_dict = {}
    for tuple in sorted_tuples:
        sorted_dict[tuple[1]] = row_dict[tuple[1]]

    with open('output.txt', 'w') as outputfile:
        for reservation, seatList in sorted_dict.items():
            outputfile.write(reservation)
            outputfile.write(" ")
            numberSeats = len(seatList)
            seatNumber = 0
            for seat in seatList:
                outputfile.write(seat)
                if seatNumber < numberSeats - 1:
                    outputfile.write(", ")
                seatNumber += 1
            outputfile.write("\n")

    print("output.txt")