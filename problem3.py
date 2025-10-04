"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = 0
    list_numbers = []
   

        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
    while numbers != "done":
        numbers = input("Choose a number")   #demander à la personne de choisir un nombre
        if numbers == "done":
            print("You have written done")
        else:
            try:
                float_numbers = float(numbers)  # essaie de convertir
                print(f"You have chosen : {float_numbers}")
                list_numbers.append(float_numbers)
            except ValueError:
                print("Error: You have to chose a valid number.")
            

    return list_numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    

    average = sum(numbers) / len(numbers)
    

    count_even = 0
    count_odd = 0
    for number in numbers:
        if number % 2 == 0:
            count_even = count_even+1
        else: 
            count_odd = count_odd+1



    analysis = {
    "Number of elements": len(numbers),
    "Sum of elements": sum(numbers),
    "Average value": average,
    "Smallest value": min(numbers),
    "Largest number": max(numbers),
    "Even count": count_even,
    "Odd count": count_odd,

}


    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers



    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    print(f"count: {analysis["Number of elements"]}")
    print(f"sum: {analysis["Sum of elements"]}")
    print(f"Average: {analysis["Average value"]}")
    print(f"minimum: {analysis["Smallest value"]}")
    print(f"maximum: {analysis["Largest number"]}")
    print(f"even numbers: {analysis["Even count"]}")
    print(f"odd numbers: {analysis["Odd count"]}")



def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()