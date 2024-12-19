from project import get_word, check_input, check_answer, format_validated_answer
import requests,re


def main():
    test_get_word()
    test_check_input()
    test_check_answer()
    test_format_validated_answer()


def test_get_word():

    word_list = requests.get("https://gist.github.com/shmookey/b28e342e1b1756c4700f42f17102c2ff")
    list = re.findall(r'class=\"blob-code blob-code-inner js-file-line\">(\w+)<\/td>', word_list.text)
    assert get_word() in list


def test_check_input():

    assert check_input("12345") == "Only alphabets are allowed"
    assert check_input("arc") == "Must be five letters"
    assert check_input("Territory") == "Must be five letters"
    assert check_input("Acorn") == True


def test_check_answer():

    assert check_answer("acorn","about","_____") == "A_o__"
    assert check_answer("count","acorn","_____") == "_____"


def test_format_validated_answer():

    assert format_validated_answer("A_on_","__o__") == "A_on_"
    assert format_validated_answer("_____","__o__") == "__o__"




if __name__ == "__main__":
    main()
