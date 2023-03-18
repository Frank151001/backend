from about import me

name = me["name"]
last = me["last_name"]
print(name +" "+ last)

me["age"] = me["age"]+1
print(me)


me["preferredColor"]="blue/gray"
print(me)

age=me["age"]
print(name +":" + str(age))

print(f"{name}:{age}")
print(f"    {age} - .,  {name}")
