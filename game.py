
import getpass
import time
import re
import os

static_delay = 2.5

def check_again():
    valid_res = ['yes', 'no']
    try:
        user_res = input("Do you check password again? Enter(Yes/No): ")
        if user_res.lower() not in valid_res:
            raise ValueError("Yes or No not else.")

        if user_res.lower() == "yes":
            time.sleep(static_delay)
            os.system( "cls" if os.name == "nt" else "clear")
            return True
        else:
            print("GoodLuck, Sir :)")
            time.sleep(5)
            os.system( "cls" if os.name == "nt" else "clear")
            return False
    except ValueError as err:
        print(err)

def start_check():

    play = True

    while play:
        word_User = getpass.getpass(prompt="Enter Password: ")
        lower_case = re.findall(r"[a-z]", word_User, re.DOTALL)
        upper_case = re.findall(r"[A-Z]", word_User, re.DOTALL)
        digit_case = re.findall(r"[\d]", word_User, re.DOTALL)
        white_space = re.findall(r"[\s]", word_User, re.DOTALL)
        special_chars = re.findall(r"[^a-z0-9]", word_User, re.I)

        strength = len(lower_case) + len(upper_case) + len(digit_case) + len(white_space)+ len(special_chars)

        print(f"Content with LowerCase: {len(lower_case)}")
        print(f"Content with UpperCase: {len(upper_case)}")
        print(f"Content with Digits: {len(digit_case)}")
        print(f"Content with WhiteSpace: {len(white_space)}")
        print(f"Content with Special Characters: {len(special_chars)}")
        print(f"Password Score: {strength / 5}")

        # Remark print
        if strength == 1:
            print("'That\'s a very bad password. Change it as soon as possible.'")
            time.sleep(static_delay)
            os.system( "cls" if os.name == "nt" else "clear")
            start_check()

        elif strength <= 3:
            print("Are you kidding me that number is so weak, Try another stronger.")
            time.sleep(static_delay)
            os.system( "cls" if os.name == "nt" else "clear")
            start_check()

        elif strength <= 6:
            print("Still too early, that's not good and not bad, You Should make it Stronger.")
            time.sleep(static_delay)
            play = check_again()

        elif strength <= 9:
            print("Okay, But it is better to make it stronger than that.")
            time.sleep(static_delay)
            play = check_again()

        elif strength > 13 :
            print("GoodWork, I think Sir that this is so Strong.")
            time.sleep(static_delay)
            play = check_again()

        else:
            print("Okay, Good Strength even now.")
            time.sleep(static_delay)
            play = check_again()

if __name__ == "__main__":
    print("Let's Check your strength password, Let's begin.")
    start_check()
