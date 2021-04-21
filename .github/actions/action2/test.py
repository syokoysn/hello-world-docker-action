
import os
if __name__ == '__main__':
    print("Github Actions test")
    check = os.environ.get('SECRET_KEY_TEST')
    print("check => ",check)
    print(check == "SECRET_KEY_TEST")
    print('done')