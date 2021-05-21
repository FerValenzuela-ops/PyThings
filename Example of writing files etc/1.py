# import sys
# from random import randint


# def continue_game():
#     answer = str(
#         input('Enter yes if you want to continue or no if you not: \n'))
#     if answer == "Yes":
#         print(f'Ok, there we go again')
#         return True
#     else:
#         print(f'Ok, we are done')
#         return False

    


# sys_num = randint(int(sys.argv[1]), int(sys.argv[2]))

# play = True
# while play:
#     try:
#         user_num = int(input('Please enter a number between 0 and 10: \n'))

#         print(sys_num)
#         if 0 < sys_num < 11:
#             if user_num == sys_num:
#                 print('You are a genius')
#                 play = continue_game()
#             elif user_num != sys_num:
#                 print('Ups, that is not the number') 
#                 play =continue_game()   
#         else:
#             print('Hey, I said 1~10')
#     except ValueError:
#         print('Please enter a number 1~10')
#         continue
