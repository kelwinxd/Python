#chart the data in list comprehension
#MAP
products = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
new_products = [
    #if the price was bigger than 20, rise 5% 
    {**pd, 'preco': pd['preco'] * 1.05} 
    if pd['preco'] > 20 else {**pd}
    for pd in products
    
]

print(*new_products, sep='\n')
