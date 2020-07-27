name = 'bob'
greatting = f"Hello, {name}"
print(greatting)

name = 'Rolf'

print(f"Hello, {name}")

# Now using an template

name = 'Marcos'
greatting = "Hello, {}"

with_name = greatting.format(name)

print(with_name)


