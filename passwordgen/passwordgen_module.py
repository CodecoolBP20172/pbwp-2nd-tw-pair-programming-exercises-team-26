import random
import string

def passwordgen():
    phase1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    phase2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    phase3 = ''.join(random.choice(string.digits) for _ in range(3))
    phase4 = ''.join(random.choice('!@#$%^&*') for _ in range(3))
    password = phase1 + phase2 + phase3 + phase4
    return password

def main():
    return

if __name__ == '__main__':
    main()
