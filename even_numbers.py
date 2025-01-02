def create_even_number_list(start,end):
    even_numbers=[]
    for num in range(start,end+1):
        if num%2==0:
            even_numbers.append(num)
    return even_numbers
start_range = int(input("Enter the starting number of the range:"))
end_range = int(input("Enter the ending number of the range:"))

even_number_list = create_even_number_list(start_range,end_range)

print("List of even numbers:",even_number_list)