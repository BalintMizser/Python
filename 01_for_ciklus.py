# írjuk ki 1 és 100 között a páros számokat

for i in range(1,101):
    # % -  maradékososztás az osztás maradékát adja vissza pl 9%2->1
    if i % 2==0:
        print(1)


#másik megoldás
for i in range(2,101,2):
    print(i)

# írjuk ki 10 és 100 között a hárommal osztható számokat
for i in range(10,101):
    if i % 3 ==0:
        print(i)

#másik megoldás
for i in range(12,101,3):
    print(i)