input_tree_height = int(input("Wie hoch soll dein Baum sein? - "))

for i in range(1, input_tree_height+1):
    count = 2*i-1

    zeile = ""

    for _ in range(count):
        zeile += "*"


    print(zeile.strip().center(2*input_tree_height*2))

trunk_size = input_tree_height // 2
for i in range(trunk_size):
    print("*".center(2*input_tree_height*2))