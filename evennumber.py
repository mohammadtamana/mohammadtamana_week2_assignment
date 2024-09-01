def filter_even_numbers(numbers):
    # Use a tuple comprehension to filter even numbers
    even_numbers = tuple(num for num in numbers if num % 2 == 0)
    return even_numbers


if __name__ == "_main_":
    # Sample tuple input
    numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # Get the tuple with even numbers only
    even_numbers_tuple = filter_even_numbers(numbers_tuple)

    # Display the result
    print("Original tuple:", numbers_tuple)
    print("Tuple with even numbers only:", even_numbers_tuple)