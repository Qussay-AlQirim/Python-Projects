def main():
    # Request Input
    name = str(input('Please input a sentence that includes a smily or frowning face emoticon:'))
    # Convert emoticon to emoji
    result = convert(name)
    # Print the converted sentence
    print(result)

def convert(sentence):
    # replace the emoticons with emojis
    sentence = sentence.replace(':)', '\U0001F642')
    sentence = sentence.replace(':(', '\U0001F641')
    return sentence


main()