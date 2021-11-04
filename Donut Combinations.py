from itertools import combinations_with_replacement


def rSubset(array, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list)
    different_combo = list(combinations_with_replacement(array, r))
    return different_combo


if __name__ == "__main__":
    arr = ["glazed", "chocolate", "sprinkled", "yeast", "caked", "sugar", "powder", "crumb",
           "fruit filled", "cream filled", "jelly",
           "sour cream", "boston cream", "apple fritter", "cinnamon twist", "crullers",
           "cronuts", "spudnuts", "cocunut", "long john", "mapple bar"]
    #arr = ["glazed", "chocolate", "sprinkled"]

    r = 12

    number_of_combos = len(rSubset(arr, r))
    diff_combos = rSubset(arr, r)

    print(number_of_combos)
    #for combo in diff_combos:
       #print(combo)
