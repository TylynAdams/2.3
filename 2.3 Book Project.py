#question one
#the molecular weight of a carbohydrate

def main():
    hydrogen = eval(input('Please enter the amount of hydrogen atoms:  '))
    carbon = eval(input('Please enter the amount of carbon atoms: '))
    oxygen = eval(input('Please enter the amount of oxygen atoms: '))

    weight = hydrogen + carbon + oxygen

    print('The molecular weight of the carbohydrate in grams per mole is: ', weight)

main()

#Question two
#the cost of a coffee order

def main():
    amount = float(input('How many pounds of Konditorei Coffee would you like to buy? '))
    price = ((10.50 * amount) + (0.86 * amount)) + 1.50
    print('Your total will be: $', price)

main()

# Question three
# What's the average of the numbers the user inputs?

def main():
    amount = eval(input('How many numbers are you going to enter? '))
    sum = 0
    for i in range(amount):
        number = eval(input('Enter the number: '))
        sum = sum + number
        print(sum)
    average = sum / number
    print('The average is: ', average)

main()
#
# Question four
# 5-point quiz program

def main():
    numbers = '12345'
    n = int(input('Enter the quiz score (1-5): '))
    pos = n + 1
    print('Your grade is: ', pos)

main()

# Question five
# acronym

def main():
    words = input('Write your phrase: ')
    words.split()

    x= ''
    for i in words.split():
        x = x + i[0] + '.'
    print(x.upper())

main()







