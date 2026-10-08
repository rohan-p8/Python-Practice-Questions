class Sample:
    a = 10

obj = Sample()

print("Class attribute before:", Sample.a)
print("Object attribute before:", obj.a)

obj.a = 20

print("Class attribute after:", Sample.a)

print("Object attribute after:", obj.a)