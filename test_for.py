def cc(digits):
    conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    product = ['']
    for k in digits:
        product = [i + j for i in product for j in conversion[k]]
    return product


if __name__ == '__main__':
    print(cc('23'))
