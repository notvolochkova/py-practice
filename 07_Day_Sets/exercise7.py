
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#ex1.1
num_companies = len(it_companies)
print(num_companies)

#ex1.2
it_companies.add('Twitter')
print(it_companies)

#ex1.3
it_companies.update(['Anthropic', 'DELL', 'NVIDIA'])
print(it_companies)

#ex1.4 + 1.5 - if element not exist in remove() raises KeyError
# it_companies.remove('Mellanox') #raises an error
it_companies.discard('Mellanox') # no error

#ex2.1
C = A.union(B)
print(C)

#ex2.2
print(A & B)

#ex2.3
print(A.issubset(B))
print(B.issuperset(A))

#ex2.4
print(A.isdisjoint(B))
print(B.isdisjoint(A))

#ex2.5
D = (A | B).union(B | A)
print(D)

#ex2.6
print(A.symmetric_difference(B)) 
print(B.difference(A))

#ex2.7
del A
del B

#ex3.1
age_tp = set(age)
print(age_tp)
print(age)

if len(age) > len(age_tp):
    print("The list is bigger")
else:
    print("The tuple is bigger")

#ex3.3
statement = "I am a teacher and I love to inspire and teach people"
statement_lst = statement.split()
print(statement_lst)
num_unique_words = len(set(statement_lst))
print(num_unique_words)
print(set(statement_lst))

