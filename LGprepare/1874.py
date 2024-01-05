from sys import stdin
input = stdin.readline


def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    given_stack = list(range(n, 0, -1))
    making_stack = []
    answer = []
    while numbers:
        # print(numbers, given_stack, making_stack, answer)
        must_number = numbers[0]
        if making_stack and making_stack[-1] == must_number:
            making_stack.pop()
            answer.append("-")
            numbers.pop(0)
        else:
            if given_stack:
                given_number = given_stack.pop()
                answer.append("+")
                making_stack.append(given_number)
                if must_number == given_number:
                    making_stack.pop()
                    answer.append("-")
                    numbers.pop(0)
            else:
                print("NO")
                return
    print("\n".join(answer))


main()