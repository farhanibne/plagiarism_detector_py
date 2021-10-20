from difflib import SequenceMatcher

with open("file.txt") as file_1,open('file_2.txt') as file_2:
    file_1_data = file_1.read()
    file_2_data = file_2.read()

    similarity_ratio = SequenceMatcher(None,file_1_data,file_2_data).ratio()
    print(similarity_ratio)