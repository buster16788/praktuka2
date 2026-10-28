def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0: raise ZeroDivisionError("Деление на ноль!")
    return a / b

ops = {'+': add, '-': sub, '*': mul, '/': div}

print("Вводите числа и операции по одной в строке, конец — '='")
tokens = []
while (inp := input().strip()) != '=':
    if inp: tokens.append(inp)

if not tokens:
    print("Ввод пуст.")
else:
    # Парсим: чередование число-операция-число...
    nums = []
    ops_seq = []
    for t in tokens:
        if t in ops:
            ops_seq.append(t)
        else:
            nums.append(float(t) if '.' in t else int(t))

    if len(nums) != len(ops_seq) + 1:
        print("Некорректная последовательность.")
    else:
        res = nums[0]
        for i, op in enumerate(ops_seq):
            nxt = nums[i + 1]
            res = ops[op](res, nxt)
            out = int(res) if isinstance(res, float) and res.is_integer() else res
            print(f"{nums[i]} {op} {nxt} = {out}")
        print(f"Итоговый результат: {out}")
