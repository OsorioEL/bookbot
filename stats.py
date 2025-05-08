def get_num_words(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  low_text=text.lower()
  letter_dict={}
  for char in low_text:
    if char not in letter_dict:
      letter_dict[char]=1
    else:
      letter_dict[char] += 1
  return letter_dict

def sorted_dict(d):
  dict_list = []
  for key in d:
    char_dict={"char":key, "num":d[key]}
    dict_list.append(char_dict)
  dict_list.sort(key=lambda x: x["num"], reverse=True)
  return dict_list

      
