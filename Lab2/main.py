from vector import Vector
v1 = Vector()
print(f"{v1 = }")

print(f"{v1.length() = }")

print(f"{v1.contains(0) = }")

print(f"{v1.getitem(0) = }")

v1.setitem(index = 0, item = 2)
print(f"setitem: {v1 = }")

v1.append(10)
print(f"append: {v1 = }")

v1.insert(index = 1, item = 1)
print(f"insert: {v1 = }")

v1.remove(0)
print(f"remove: {v1 = }")

print(f"{v1.indexOf(10) = }")

v2 = Vector([1, 2, 3, 4, 5, 6, 7, 8])
v1.extend(v2)
print(f"extend: {v1 = }")

sub = v1.subVector(1, 6)
print(f"subVector: {sub = }")