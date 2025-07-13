import random
import main
from libs import exit_program

def start():
    while True :
        color_option = ["merah", "kuning", "hijau", "biru", "ungu"]
            
        name_user = input("Silahkan masukkan nama anda :")
        while name_user == "" :    
            name_user = input("Masukkan nama anda :")
        print()
        print(f"Halo {name_user} Selamat datang di di game Tebak Warna🎨")
        print()
        print("Aturan :\nSaya akan memilih 1 warna dari daftar berikut:\n[Merah, Biru, Kuning, Hijau, Ungu]\n\nTugas kamu: Tebak warna yang saya pilih!\nNote: Kamu punya 3 kesempatan.")
        print()
        choice1 = input("Tebakan ke -1 adalah :")
        
        color_pick = random.choice(color_option)
        if choice1 == color_pick :
            print(f"Selamat {name_user} kamu benar warna yang saya pilih {color_pick}")
            
            play_again = input(f"Apakah {name_user} ingin melanjutkan gamenya lagi? [Y/N] :")
            if play_again == 'n':
                exit_program()
                exit()
            if play_again == 'y':
                continue
        else:
            print(f"Sayang sekali kamu salah warna yang saya pilih {color_pick} masih ada 2 kesempatan")

        color_pick = random.choice(color_option)
        choice2 = input("Tebakan ke -2 adalah :")
        if choice2 == color_pick :
            print(f"Selamat {name_user} kamu benar warna yang saya pilih {color_pick}")
            
            play_again = input(f"Apakah {name_user} ingin melanjutkan gamenya lagi? [Y/N] :")
            if play_again == 'n':
                exit_program()
                exit()                                                 
            if play_again == 'y':
                continue
        else:
            print(f"Sayang sekali kamu salah warna yang saya pilih {color_pick} masih ada 1 kesempatan")
            
        color_pick = random.choice(color_option)
        choice3 = input("Tebakan ke -3 adalah :")
        if choice3 == color_pick :
            print(f"Selamat {name_user} kamu benar warna yang saya pilih {color_pick}")
            
            play_again = input(f"Apakah {name_user} ingin melanjutkan gamenya lagi? [Y/N] :")
            if play_again == 'n':
                exit_program()
                exit()
            if play_again == 'y':
                continue
        else:
            print(f"Sayang sekali kamu salah lagi warna yang saya pilih {color_pick}. Silahkan ulangin permainan jika masih ingin bermain")
        
        play_again = input(f"Apakah {name_user} ingin melanjutkan gamenya lagi? [Y/N] :")
        if play_again == 'n':
            exit_program()
            print()
            main.option()
    
if __name__ == '__main__':
    start()
