a = "Let's take LeetCode contest"



def reverseWords(s: str) -> str:
    temp =map(lambda a: a[::-1],  s.split(" "))
    return " ".join(temp)

reverseWords(a)
