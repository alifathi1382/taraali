def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    bt = [-1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):

            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                bt[i] = j
                break

    if not dp[n]:
        return False, ""

    result = []
    idx = n
    while idx > 0:
        result.append(s[bt[idx]:idx])
        idx = bt[idx]

    result.reverse()
    return True, " ".join(result)


dictionary = {"i", "like", "sam", "sung", "samsung", "ice", "mobile", "cream", "ice cream", "go", "man", "mango"}
input_string = input('enter your word:')
can_break, segmented_string = word_break(input_string, dictionary)
if can_break:
    print(f'yes, the string can be seqmented as "{segmented_string}"')
else:
    print("Cannot be segmented")
