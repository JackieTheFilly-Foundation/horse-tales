import htlib.basicinfo

entity_name = input("Type in your entity name: ")
entity_type = input("Type in your entity type: ")

#try:
pony = htlib.basicinfo.Entity(entity_name, entity_type)

#print("{} is not an entity type, putting in NoneEn as entity type.".format(ex.entity))
entity_type = "NoneEn"
#pony = htlib.basicinfo.Entity(entity_name, entity_type)

#finally:
input("Press enter to continue.")

print("Your creditentials:\n")
print("Name:", pony.name)
print("Entity:", pony.entity)
