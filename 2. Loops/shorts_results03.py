results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Toad")
#it will add these elemnts to the end of the list.

#to append multiple elements at once we can try
results.append(["Bowser", "Yoshi"]) 
# but it will put this list inside our list but we want just these elements in our list so
results.remove(["Bowser", "Yoshi"]) 
results.extend(["Bowser", "Yoshi"]) 

results.remove("Bowser")

# To insert an element at a particular decided position in the list
results.insert(0, "Bowser")

# To reverse a list
results.reverse()


print(results)