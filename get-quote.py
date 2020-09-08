import random


def add_quote():
    file_w = open('quotes.txt', 'a')
    file_w.write('\nThis is a new quote')

def primary():


# print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0,last)

    print(quotes[rnd])
    print(quotes[rnd + 1])

if __name__ == "__main__":
    primary()

    #Uncomment this function call it and add a quote. Update this function accordingly with a new quote.
    #add_quote()
