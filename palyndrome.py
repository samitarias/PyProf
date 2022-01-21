def is_palyndrome(string: str) -> bool :
    string= string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palyndrome(1000))


if __name__ == '__main__':
    run()