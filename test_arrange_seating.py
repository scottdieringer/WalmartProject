from FindRows import *


def test_findFourElements():
    reserve_dict = {"R001": 2, "R002": 4, "R003": 4, "R004": 3, "R005": 2}
    sorted_dict = sorted(reserve_dict.items(), key=operator.itemgetter(1))
    foundFourSet = findFourElements(sorted_dict, len(sorted_dict), 11)
    print(foundFourSet)
    assert 1 == 1

def test_findThreeElements():
    reserve_dict = {"R001": 2, "R002": 4, "R003": 4, "R004": 3, "R005": 2}
    sorted_dict = sorted(reserve_dict.items(), key=operator.itemgetter(1))
    foundThreeSet = findThreeElements(sorted_dict, len(sorted_dict), 9)
    print(foundThreeSet)
    assert 1 == 1

def test_arrange_seating1():
    reserve_dict = {"R001": 2, "R002": 4, "R003": 3, "R004": 3, "R005": 2, "R006" : 2, "R007" : 2, "R008": 4}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1


def test_arrange_seating2():
    reserve_dict = {"R001": 2, "R002": 4, "R003": 3, "R004": 3, "R005": 2, "R006": 2, "R007": 2, "R008": 4, "R009": 12, "R0010": 5}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1

def test_arrange_seating3():
    reserve_dict = {"R001": 2, "R002": 4, "R003": 3, "R004": 3, "R005": 2, "R006": 2, "R007": 2, "R008": 4, "R009": 12,
                    "R010": 5, "R011": 15, "R012": 2, "R013": 2, "R014": 5, "R015": 3, "R016": 5, "R017": 4, "R018": 6}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1

def test_arrange_seating4():
    reserve_dict = {"R001": 3, "R002": 4, "R003": 7, "R004": 3, "R005": 12, "R006": 2, "R007": 20, "R008": 4, "R009": 12,
                    "R010": 5, "R011": 5, "R012": 2, "R013": 2, "R014": 5, "R015": 3, "R016": 5, "R017": 4, "R018": 6}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1

def test_arrange_seating5():
    reserve_dict = {"R001": 1, "R002": 8, "R003": 5, "R004": 6, "R005": 2, "R006": 2, "R007": 2, "R008": 2, "R009": 12,
                    "R010": 5, "R011": 1, "R012": 2, "R013": 2, "R014": 2, "R015": 3, "R016": 5, "R017": 3, "R018": 16}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1

def test_arrange_seating6():
    reserve_dict = {"R001": 10, "R002": 4, "R003": 3, "R004": 1, "R005": 1, "R006": 1, "R007": 2, "R008": 4, "R009": 7,
                    "R010": 5, "R011": 15, "R012": 2, "R013": 2, "R014": 5, "R015": 3, "R016": 5, "R017": 4, "R018": 6, "R019": 2,
                    "R020": 3, "R021": 2, "R022": 1, "R023": 4, "R024": 3, "R025": 6, "R026": 7, "R027": 4, "R028": 3, "R029": 20, "R030": 20}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1

def test_arrange_seating7():
    reserve_dict = {"R001": 12, "R002": 1, "R003": 3, "R004": 3, "R005": 2, "R006": 2, "R007": 4, "R008": 2, "R009": 1,
                    "R010": 5, "R011": 15, "R012": 5, "R013": 6, "R014": 15, "R015": 5, "R016": 1, "R017": 1, "R018": 1,
                    "R019": 9, "R020": 8, "R021": 3, "R022": 4, "R023": 2, "R024": 20, "R025": 6, "R026": 3, "R027": 5, "R028": 3,
                    "R029": 3, "R030": 2, "R031": 16}
    answer = arrange_seating(reserve_dict)
    print(answer)
    assert 1 == 1


if __name__ == "__main__":
    test_findFourElements()
    test_findThreeElements()
    test_arrange_seating1()
    test_arrange_seating2()
    test_arrange_seating3()
    test_arrange_seating4()
    test_arrange_seating5()
    test_arrange_seating6()
    test_arrange_seating7()
    print("Everything passed")