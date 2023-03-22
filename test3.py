colors =['teal','PINCK','PURPLE','ORANGE','green','BLUE','YELLOW','red','pink','TeAl']
print(len(colors))

results=[]
for color in colors:
    color_lower = color.lower()
    if color_lower not in results:
        results.append(color_lower)
print(results)


color="red"
count=0
for c in colors:
    if color==c.lower():
        count= count+1
print(count)