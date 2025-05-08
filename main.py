import sys 
from stats import get_num_words, get_char_count, sorted_dict

def get_book_text(file_path):
  with open(file_path) as f:
    text = f.read()
  return text

def main():
  # Check if the file path is provided as a command line argument
  if len(sys.argv) > 1:
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    # print(f"{get_num_words(book_text)} words found in the document.")
    # print(f"dictionary of characters and their counts: {get_char_count(book_text)}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("----------- Character Count -----------")
    sorted_dict_list = sorted_dict(get_char_count(book_text))
    for d in sorted_dict_list:
      if d["char"].isalpha():
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
  else:
    print("Please provide a file path as a command line argument.")
    print("Usage: python3 main.py <file_path>")
    sys.exit(1)
  
if __name__ == "__main__":
  main()
 