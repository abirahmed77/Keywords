a = input("Enter a word: ")

for i in a:
    
    if i =='A' or i == "a":
        print ("A is found")
        break
    
    else:
        print(f"Anot found at {i}")