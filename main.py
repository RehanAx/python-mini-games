from games import cave_guess, color_guess
from libs import exit_program

def option():
    while True:
        user_option = int(input(f"Menu program :\n1. Tebak Goa\n2. Tebak Warna\n3. Exit Program\nSilahkan pilih menu program :"))
        choice()
        if user_option == 1: 
            cave_guess.start()
            break
        elif user_option == 2:
            color_guess.start()
        elif user_option == 3:
            exit_program()
            exit()
    
def choice():
    user_choice = input(f"Apakah anda yakin? [y/n] :")
    if user_choice == "y":
        print("Program dilanjutkan...")
        print()
    else :
        option()
        
def main():
    option()
    choice()
    
if __name__ == '__main__':
    main()
    































































