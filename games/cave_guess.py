import random
import main
from libs import welcome_message, exit_program


def start():
    welcome_message ("   WELCOME TO","STAR GETE GAMES")

    
    while True:    
        name_user = input("Silahkan masukkan nama anda :")
        while name_user == "" :
            name_user = input("Masukkan nama anda :")
        print()
        print(f"Halo {name_user} coba perhatikan goa dibawah ini 👇")

        bentuk_goa = "|_|"
        goa = [bentuk_goa]*10
        goa_kosong = goa.copy()
        
        gete_position = random.randint (1,10)
        
        goa[gete_position-1] = "|0_0|"
        print (' '.join(goa_kosong))
        print()

        while True:
            gete_position = random.randint (1,10)
            
            confirm_answer = 0
            while confirm_answer not in range (1,11):
                try:
                    confirm_answer = int(input(f"Ayo {name_user} coba tebak di goa berapa GETE bersembunyi? [1/ 2/ 3/ 4/ 5/ 6/ 7/ 8/ 9/ 10] : " if confirm_answer == 0 else "Masukkan angka yang valid 1-10 :")) 
                except ValueError:
                    confirm_answer = 0
            
            confirm_user = input(f"Apakah {name_user} yakin dengan jawabannya? [y/n] :")
            print()
            if confirm_user == "y" :
                if confirm_answer == gete_position :
                    print(' '.join(goa) + f"\nSelamat {name_user} kamu benar GETE ada di goa nomor {gete_position}. Terimakasih telah bermain\n")
                else :
                    print(' '.join(goa) + f"\nSayang sekali {name_user} kamu salah GETE ada di nomor {gete_position}. Silahkan ulangin permainan\n") 
            elif confirm_user == "n":
                print(f"Silahkan {name_user} ulangin pilihan jawabannya")
                
            play_again = input(f"Apakah {name_user} ingin melanjutkan gamenya lagi? [y/n] :")
            if play_again == 'n':
                exit_program()
                print()
                main.option()
                
if __name__ == '__main__':
    start()

            
            
            
