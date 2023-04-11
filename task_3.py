import requests

def main():
    response = requests.get("http://www.python.org/")

    char_dict = {}
    for char in response.text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    output_text = ""
    for char in char_dict:
        output_text += f"{repr(char)} : {char_dict[char]}\n"

    with open("readme.md",'w') as file:
        file.write(output_text)

if __name__ == "__main__":
    main()