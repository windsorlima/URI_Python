uni_price = 0
for i in range(2):
    p_id, p_qtd, p_price = input().split()
    uni_price += float(p_price) * int(p_qtd)

print("VALOR A PAGAR: R$ {:.2f}".format(uni_price))
