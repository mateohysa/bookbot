from stats import get_words, count_characters, pretty_print
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    num_words = len(get_words(sys.argv[1]).split())
    print(f"Analyzing book found at {sys.argv[1]} ...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    res = count_characters(get_words(sys.argv[1]))
    #print(res)
    print("--------- Character Count -------")


    pretty_print(res)
    print("============= END ===============")


main()