#function that adds 3 to every value in a variable
def encoder1(input_value):
    #setting the variables needed
    int(input_value)
    real_list = []
    final_value = ''
    #adds every value that is provided into a list
    for i in range(len(input_value)):
        real_list.append(int(input_value[i]))
    #adds three to every index in list
    for i in range(len((real_list))):
        real_list[i] = 3 + real_list[i]
        #if the result is greater than 9 you transfer it instead of going over ten
        if real_list[i] > 9:
            real_list[i] = real_list[i] -10
    #add all the indexes into a list
    for i in range(len(real_list)):
        final_value = final_value + str(real_list[i])
    return final_value
#function that subtracts 3 to every value in a variable
def decoder(input_value):
    #setting the variables needed
    int(input_value)
    real_list = []
    final_value = ''
    #making the input into a list
    for i in range(len(input_value)):
        real_list.append(int(input_value[i]))
    #subtracting three from every index
    for i in range(len((real_list))):
        real_list[i] = real_list[i] - 3
        #if it becomes less then zero you transfer it be under 10
        if real_list[i] < 0:
            real_list[i] = real_list[i] + 10
    #take the index and make it into a string
    for i in range(len(real_list)):
        final_value = final_value + str(real_list[i])
    return final_value

def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = input("Please enter an option:")
        if option == '1':
            encoded_input = input("Please enter your password to encode:")
            encoded_input = encoder1((encoded_input))
            print("Your password has been encoded and stored!")
            print()
            continue
        if option == '2':
            print("The encoded password is " + encoded_input + " and the original password is " + decoder(encoded_input))
            print()
            continue
        if option == '3':
            break
if __name__ == '__main__':
    main()
