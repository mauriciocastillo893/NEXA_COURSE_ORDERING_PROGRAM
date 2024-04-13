
def swap_elements(arr1, arr2, percentage):
    # Check if the length of arrays is at least 3
    if len(arr1) < 3 or len(arr2) < 3:
        return False
        # return "Arrays must have at least 3 elements for swapping"

    percentage_per_element = 100 / (len(arr1))
    print("Percentage per element:", percentage_per_element)
    
    if(percentage_per_element <= percentage):
        print("Changing elements... ", len(arr1)-1, "of", len(arr1), "by rule set\n")
    else:
        print("Percentage calculated is below percentage parameter. Changes could not be resolved due it\n")
    change_values = False
    is_there_a_pair = False
    percentage_applied = percentage_per_element
    # Perform swapping based on the rules
    for i in range(len(arr1)):

        if percentage_applied <= percentage:
            # Check if the element at position i is equal in both arrays
            if arr1[i] == arr2[i]:
                if i == 0:
                    is_there_a_pair = True
                else: 
                    if is_there_a_pair:
                        is_there_a_pair = True
                    else:
                        is_there_a_pair = False
                pass
            else:
                if is_there_a_pair:
                    arr1[i], arr2[i] = arr2[i], arr1[i]
                else:
                    pass
                
            print("Percentage completed:", percentage_applied, " %")
            print(f"{arr1[i]} <-> {arr2[i]}, mix each other: {is_there_a_pair}")
            percentage_applied += percentage_per_element
        else:
            break
    if not is_there_a_pair:
        print("There is no pair in the arrays. No changes were made.")
    return arr1, arr2

# Example usage
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [5, 4, 3, 2, 1]
# arr1 = [0, 1, 3, 2, 2]
# arr2 = [2, 2, 3, 1, 0]
# arr1 = [1, 2, 3, 4, 5, 6, 8, 7]
# arr2 = [1, 2, 3, 4, 5, 7, 6, 8]

# print("Initially:")
# print("First pair:", arr1)
# print("Second pair:", arr2)

# arr1, arr2 = swap_elements(arr1, arr2, 100)

# print("\nAt the end:")
# print("First pair:", arr1)
# print("Second pair:", arr2)
