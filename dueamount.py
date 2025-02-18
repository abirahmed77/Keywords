def due(b,g):
    return g-b

bill = int(input("Enter Bill amount: "))
given = int(input("Enter Given amount: "))

dueAmount = due(bill, given)

print(f"Due Amount : {dueAmount}")