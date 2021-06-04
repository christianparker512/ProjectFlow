shopping_list = ["apples", "grapefruit", "coffee", "brisket", "tortillas", "peppers", "onions"]

#for item in shopping_list:
 #   if item != "onions":
  #      print("Buy " + item)

for item in shopping_list:
    if item == "onions":
        continue

    print("Buy " + item)