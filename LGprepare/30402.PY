def main():
    photo = [list(input().split()) for _ in range(15)]
    for row in photo:
        if 'w' in row:
            return 'chunbae'
        elif 'b' in row:
            return 'nabi'
        elif 'g' in row:
            return 'yeongcheol'

print(main())