name = input()
salary = float(input())
sales = float(input())
final_salary = salary+((sales/100)*15)

print("TOTAL = R$ {:.2f}".format(final_salary))