def palindrome(string):
    upstring = str.upper(string).replace(" ","")
    revstring = upstring[::-1]
    return upstring == revstring



def main():
    pali = input("Input a string: ")
    return palindrome(pali)


if __name__ == '__main__':
    main()
