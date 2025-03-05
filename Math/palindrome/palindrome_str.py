def isPalindrome(s):
    p1 = 0
    p2 = len(s) -1

    while p1 < p2:
        if not s[p1].isalnum():
            p1 += 1
        elif not s[p2].isalnum():
            p2 -= 1
        elif s[p1].lower() != s[p2].lower():
            return False
        else: 
            p1 += 1
            p2 -= 1
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama".strip()
    ans =isPalindrome(s)

    if ans:
        print("YES")
    else: print("NO")
