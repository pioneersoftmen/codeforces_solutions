for _ in range(int(input())):
    ab = input()
    for i in range(1, len(ab)):
        if ab[i] != '0' and int(ab[:i]) < int(ab[i:]):
            print(ab[:i], ab[i:])
            break
    else:
        print(-1)