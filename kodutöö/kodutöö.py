 
    grade_i_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]                                # Вычисляем сумму произведений первых 10 цифр кода и весовой таблицы Grade I
    sum_products = sum([int(code[i]) * grade_i_weights[i] for i in range(10)])
    remainder = sum_products % 11                                                      # Делим сумму на 11
    if remainder != 10:                                                    # Если остаток не равен 10, то он является контрольным номером
        return remainder == int(code[-1])
    grade_ii_weights = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum_products = sum([int(code[i]) * grade_ii_weights[i] for i in range(10)])
    remainder = sum_products % 11
    return remainder == int(code[-1])
 sum = 0
    weights = [3, 7, 6, 0, 5, 0, 3, 0, 2, 9]
    for i in range(10):
        sum += int(code[i]) * weights[i]
    residue = sum % 11
    if residue == 10:
        residue = 0
    return residue == int(code[10])

code = "37605030299"
if verify_code(code):
    print("Valid code")
else:
    print("Invalid code")