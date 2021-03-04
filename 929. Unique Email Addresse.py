a = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]

def numUniqueEmails(emails) -> int:
    ans = []
    for email in emails:
        email = email.split("@")
        if "+" in email[0]:
            ans.append(email[0][:email[0].index("+")].replace(".", "") + "@" + email[1])
        else:
            ans.append(email[0].replace(".", "") + "@" + email[1])
    return len(set(ans))

print(numUniqueEmails(a))


def numUniqueEmails(emails) -> int:
    ans = []
    for email in emails:
        email = email.split("@")
        if "+" in email[0]:
            ans.append(email[0][:email[0].index("+")].replace(".", "") + "@" + email[1])
        else:
            ans.append(email[0].replace(".", "") + "@" + email[1])
    return len(set(ans))

print(numUniqueEmails(a))