def insert_string_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_string_middle("(())","Tops"))
print(insert_string_middle("[[]]","Career"))
print(insert_string_middle("{{}}","Center"))

