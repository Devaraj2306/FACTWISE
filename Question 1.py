ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def number_to_words(n):
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ones[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + number_to_words(n % 100)
    elif n == 1000:
        return "onethousand"

# Calculate total letters used
total_letters = sum(len(number_to_words(i)) for i in range(1, 1001))

print(total_letters)