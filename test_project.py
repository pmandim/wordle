import pytest
import project
import csv

def main():
    test_check_word()
    test_select_level()
    test_get_word()

def test_check_word():
    # Test if the attempt == answer
    assert project.check_word("house", "house") == True
    # Test if the attempt != answer
    assert project.check_word("field", "house") == False
    # Test if the regex is working
    with pytest.raises(NameError):
        project.check_word("box", "!=-")
    # Test if the len(attempt) != len(answer)
    with pytest.raises(ValueError):
        project.check_word("field", "box")

def test_select_level(monkeypatch):
    # Test input of "3"
    monkeypatch.setattr('builtins.input', lambda _: "3")
    level = project.select_level()
    assert level == 3
    # Test input of "2"
    monkeypatch.setattr('builtins.input', lambda _: "2")
    level = project.select_level()
    assert level == 2

def test_get_word():
    # Test with get_word(1)
    rows = []
    with open("wordle.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    stripped_row = []
    for i in rows[1]:
        stripped_row.append(i.strip())
    word = project.get_word(1)
    assert word in stripped_row

    # Test with get_word(2)
    rows = []
    with open("wordle.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    stripped_row = []
    for i in rows[2]:
        stripped_row.append(i.strip())
    word = project.get_word(2)
    assert word in stripped_row

if __name__ == "__main__":
    main()
