import operator

# Given a dictionary where the keys are the reservation numbers
# and the values are the number of seats for that reservation, find
# an arrangement that fits the theatre and that doesn't split up groups
# between different rows.
FIRST_ROW = 'A'
PAST_LAST_ROW = 'K'
SEAT_SPACING = 3
FOUR_PERFECT = 11
THREE_PERFECT = 14
TWO_PERFECT = 17
ONE_PERFECT = 20

def arrange_seating(reserve_dict):
    # Sort the dictionary by the number of seats.
    sorted_tuples = sorted(reserve_dict.items(), key=operator.itemgetter(1))
    sorted_dict = {k:v for k,v in sorted_tuples}
    # Find sets of four reservations that add up to 11 and put them into
    # the same row then remove those reservations from the dictionary.  Do this
    # until no set of four reservations that add up to 11 are found.

    # Dictionary where the key is the name of the row, i.e. A thru J, and the
    # values are the reservation numbers associated with that row
    row_dict = {}
    # Set the first row as A.
    RowChar = FIRST_ROW

    lessPerfect = 0
    while RowChar != PAST_LAST_ROW and len(sorted_tuples) != 0:
        sorted_tuples, sorted_dict, row_dict, RowChar = setRow(sorted_tuples, sorted_dict, row_dict, RowChar, 4, lessPerfect)
        sorted_tuples, sorted_dict, row_dict, RowChar = setRow(sorted_tuples, sorted_dict, row_dict, RowChar, 3, lessPerfect)
        sorted_tuples, sorted_dict, row_dict, RowChar = setRow(sorted_tuples, sorted_dict, row_dict, RowChar, 2, lessPerfect)
        sorted_tuples, sorted_dict, row_dict, RowChar = setRow(sorted_tuples, sorted_dict, row_dict, RowChar, 1, lessPerfect)
        lessPerfect += 1

    # If there are still tuples left after we get out of the for loop then we
    # didn't find seats for all of the reservations.
    if len(sorted_tuples) != 0:
        print("\n")
        print("Not all reservations were given seats.\n")
    else:
        print("\n")
        print("All reservations were given seats.\n")

    order_dict = {}
    for reservation in row_dict.keys():
        number = int(reservation[1:])
        order_dict[number] = reservation
    return row_dict, order_dict

def setRow(sorted_tuples, sorted_dict, row_dict, RowChar, setNumber, lessPerfect):

    if setNumber == 4:
        foundSet = findFourElements(sorted_tuples, len(sorted_tuples), FOUR_PERFECT - lessPerfect)
    elif setNumber == 3:
        foundSet = findThreeElements(sorted_tuples, len(sorted_tuples), THREE_PERFECT - lessPerfect)
    elif setNumber == 2:
        foundSet = findTwoElements(sorted_tuples, len(sorted_tuples), TWO_PERFECT - lessPerfect)
    else:
        foundSet = findOneElement(sorted_tuples, len(sorted_tuples), ONE_PERFECT - lessPerfect)

    while len(sorted_dict) >= setNumber and foundSet != None and RowChar != PAST_LAST_ROW:
        seatNumber = 1
        for item in foundSet:
            seatListForReservation = []
            for seats in range(item[1]):
                seatListForReservation.append(RowChar + str(seatNumber))
                seatNumber += 1
            row_dict[item[0]] = seatListForReservation
            seatNumber += SEAT_SPACING
            # Remove reservations that have found a seat from the sorted dictionary.
            del(sorted_dict[item[0]])
        RowChar = chr(ord(RowChar) + 1)

        sorted_tuples = sorted(sorted_dict.items(), key = operator.itemgetter(1))

        if setNumber == 4:
            foundSet = findFourElements(sorted_tuples, len(sorted_tuples), FOUR_PERFECT - lessPerfect)
        elif setNumber == 3:
            foundSet = findThreeElements(sorted_tuples, len(sorted_tuples), THREE_PERFECT - lessPerfect)
        elif setNumber == 2:
            foundSet = findTwoElements(sorted_tuples, len(sorted_tuples), TWO_PERFECT - lessPerfect)
        else:
            foundSet = findOneElement(sorted_tuples, len(sorted_tuples), ONE_PERFECT - lessPerfect)

    return sorted_tuples, sorted_dict, row_dict, RowChar

# Below was borrowed from https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/
# Below runtime is n^2 and space is n^2.
def findFourElements(sorted_tuples, n, X):
    # Store sums of all pairs in a hash table
    sum_pairs = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum_pairs[sorted_tuples[i][1] + sorted_tuples[j][1]] = [i, j]

    # Traverse through all pairs and search
    # for X - (current pair sum).
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = sorted_tuples[i][1] + sorted_tuples[j][1]

            # If X - summ is present in hash table,
            if (X - sum) in sum_pairs:

                # Making sure that all elements are
                # distinct array elements and an element
                # is not considered more than once.
                p = sum_pairs[X - sum]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
                    return [sorted_tuples[i], sorted_tuples[j], sorted_tuples[p[0]], sorted_tuples[p[1]]]
    return None

# Below was borrowed from https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
def findThreeElements(sorted_tuples, n, X):
    for i in range(n - 1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to X - A[i]
        s = set()
        dict = {}
        curr_sum = X - sorted_tuples[i][1]
        for j in range(i + 1, n):
            if (curr_sum - sorted_tuples[j][1] in s):
                return [sorted_tuples[i], sorted_tuples[j], dict[curr_sum - sorted_tuples[j][1]]]
            s.add(sorted_tuples[j][1])
            dict[sorted_tuples[j][1]] = sorted_tuples[j]
    return None

# Below was borrowed from https://www.geeksforgeeks.org/count-pairs-with-given-sum/
def findTwoElements(sorted_tuples, n, X):
    count = 0  # Initialize result
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if sorted_tuples[i][1] + sorted_tuples[j][1] == X:
                return [sorted_tuples[i], sorted_tuples[j]]
    return None

def findOneElement(sorted_tuples, n, X):
    for i in range(0, n):
        if sorted_tuples[i][1] == X:
            return [sorted_tuples[i]]
    return None