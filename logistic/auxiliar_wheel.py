
def swap_elements(arr1, arr2, p_mut_cruza, p_mut_ind):
    if len(arr1) < 3 or len(arr2) < 3 or p_mut_cruza < 50:
        if p_mut_cruza < 50:
            print("\n[AUXILIAR WHEEL]\n\tThe cross mutation percentage is below 50%. No changes were made.")
        else:
            print("\n[AUXILIAR WHEEL]\n\tArrays must have at least 3 elements for swapping")
        return arr1, arr2

    percentage_per_element = 100 // (len(arr1))
    print("\n\t[AUXILIAR WHEEL]\n\tPercentage per element:", percentage_per_element, "%")
    
    if(percentage_per_element <= p_mut_ind):
        print("\tRULE SET:", len(arr1), "elements could be crossed\n")
    else:
        print(f"\tPercentage calculated [{percentage_per_element} %] is below individual mutation percentage parameter [{p_mut_ind} %]. Changes could not be resolved due it\n")
        return arr1, arr2
    
    is_there_a_pair = False
    pairs_found = 0
    percentage_applied = percentage_per_element

    for i in range(len(arr1)):

        if percentage_applied <= p_mut_ind:
            # Check if the element at position i is equal in both arrays
            if arr1[i] == arr2[i]:
                if i == 0:
                    is_there_a_pair = True
                    pairs_found += 1
                    print(f"\tPair, posicion: {i}")
                else: 
                    if is_there_a_pair:
                        is_there_a_pair = True
                        pairs_found += 1
                        print(f"\tPair, posicion: {i}")
                    else:
                        is_there_a_pair = False
                pass
            else:
                if is_there_a_pair:
                    arr1[i], arr2[i] = arr2[i], arr1[i]
                else:
                    pass
                
            print("\tPercentage completed:", percentage_applied, " %")
            print(f"\t{arr1[i]} <-> {arr2[i]}, mix each other: {'Same value' if arr1[i] == arr2[i] else is_there_a_pair}\n")
            percentage_applied += percentage_per_element
        else:
            break
    if not is_there_a_pair:
        print("\tThere is no pair in the arrays. No changes were made.")
    print("\n\tPairs found:", pairs_found)
    return arr1, arr2

# Example usage
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [5, 4, 3, 2, 1]
# arr1 = [0, 1, 3, 2, 2]
# arr2 = [2, 2, 3, 1, 0]
# arr1 = [1, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11]
# arr2 = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11]
# arr1 = ['1-P1', '2-P2', '3-P3', '5-P4', '0-P5', '4-P6']
# arr2 = ['1-P1', '2-P2', '0-P3', '3-P4', '5-P5', '4-P6']

# print("Initially:")
# print("First pair:", arr1)
# print("Second pair:", arr2)

# arr1, arr2 = swap_elements(arr1, arr2, 50, 100)

# print("\nAt the end:")
# print("First pair:", arr1)
# print("Second pair:", arr2)

def define_operator(selected_option):
    if selected_option == 'a' or selected_option == 'c' or selected_option == 'e':
        print("[MUTATION] RULE SET: Ordening from lower to greater")
        return "<"
    else:
        print("[MUTATION] RULE SET: Ordening from greater to lower")
        return ">"

def mutation_for_first_array(first_pair, operator, p_mut_gen, percentage_per_element):
    percentage_applied = 0
    changed_applies = 0
    
    print("\n\t[MUTATION] Mutation for FIRST ARRAY initialized")
    
    for i in range(len(first_pair)):
        condition = "{} {} {}".format(first_pair[i-changed_applies].split("-")[0], operator, first_pair[len(first_pair)-1].split('-')[0])
            
        percentage_applied += percentage_per_element
            
        if percentage_applied <= p_mut_gen:
            print("\n\t[MUTATION] Condition:", condition)
            if eval(condition):
                print(f"\t[MUTATION] [X] No changes needed in {first_pair[i-changed_applies]} <-> {first_pair[len(first_pair)-1]}")
                pass
            else:
                if i-changed_applies >= len(first_pair)-1:
                    print(f"\t[MUTATION] [X] No changes made in {first_pair[i-changed_applies]} <-> {first_pair[len(first_pair)-1]}")
                else:
                    print(f"\t[MUTATION] [✔] Changing {first_pair[i-changed_applies]} <-> {first_pair[len(first_pair)-1]}")
                    first_pair.append(first_pair[i-changed_applies])
                    first_pair.pop(i-changed_applies)
                    changed_applies += 1
                    print("\t[MUTATION] [N] New first_array got:\n\t\t", first_pair)
                    
            print("\t[MUTATION] Percentage completed:", percentage_applied, " %")
        else:
            break
        
    print(f"\n\t[MUTATION] >> Mutation process completed by reaching the mutation percentage parameter [{p_mut_gen} %]. \n\t[MUTATION] >> Completed percentage:", percentage_applied, "% from", "100 % (default)" )
    