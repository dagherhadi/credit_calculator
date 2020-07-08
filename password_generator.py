from random import choice, sample

def generate_password():
    character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()?'
    word_list = ['nature', 'london', 'building', 'airplane', 'airport']
    pass_strength = input("How strong do you want your password to be? ")
    if pass_strength.lower() == 'weak':
        password = choice(word_list)
    elif pass_strength.lower() == 'strong':
        pass_len = int(input("How long do you want your password to be? "))
        password = "".join(sample(character_list, pass_len))
    print(password)

if __name__ == '__main__':
    generate_password()
