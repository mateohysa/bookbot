def get_words(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        

def count_characters(file_contents):

    character_dict = {}

    for char in file_contents:
        low_char = char.lower()
        if low_char not in character_dict:
            character_dict[low_char] = 1
        elif low_char in character_dict:
            character_dict[low_char] += 1
    return character_dict

def pretty_print(character_dict):
    final_list = []
    for char in character_dict:
        if char.isalpha():
            fin_dict = {
                "char": char,
                "num" : character_dict[char]
            }
            final_list.append(fin_dict)
    final_list.sort(key=num_helper, reverse=True)

    for i in range(0, len(final_list)):
        print(f"{final_list[i]["char"]}: {final_list[i]["num"]}")
    #return final_list

def num_helper(dict):
    return dict["num"]     

