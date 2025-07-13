from time import sleep

def welcome_message(title1,title2):
    line1 = (title1)
    line2 = (title2)
    style = "*" * max(len(line1),len(line2))
    
    print(style)
    print(line1)
    print(line2)
    print(style)
    
def exit_program():
    print("Program akan dihentikan...")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    print("Program berhasil dihentikan!")
    
if __name__ == '__main__':
    exit_program()
    