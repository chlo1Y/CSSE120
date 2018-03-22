def main():
    input_string = input('What is the Fahrenheit temperature? ')
    fahrenheit = float(input_string)
    celsius = (fahrenheit - 32) * (5 / 9)

    print('That temperature is', celsius, 'degrees Celsius.')

main()
