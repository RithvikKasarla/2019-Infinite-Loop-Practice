alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
def pheonetic_alphabet(ipt):
    final = []
    for idx, i in enumerate(ipt):
        if i == " ":
            final.append(" ")
        else:
            final.append(alphabet[ord(i.lower()) - 97])
            try:
                if not ipt[idx + 1] == " ":
                    final.append("-")
            except:
                pass
    return "".join(final)
            
if __name__ == "__main__":
    print(pheonetic_alphabet("Hello There"))