def decode(code):
    if not code or code[0] == "0":
        return 0

    n = len(code)
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        # Single digit decode (1–9)
        one_digit = int(code[i - 1])
        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        # Two digit decode (10–26)
        two_digits = int(code[i - 2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]



assert (decode('12106')) == 2
assert (decode('339')) == 1
assert (decode('306')) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
