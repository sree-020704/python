def secondlarge(lst):
    if len(lst) < 2:
        return "List must contain at least two elements."
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort(reverse=True)
    return unique_lst[1]  # Second largest

# Taking list input from user
lst = list(map(int, input("Enter list elements (space-separated): ").split()))
print("Second largest element is:", secondlarge(lst))
