from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

s = input().strip()
sl = len(s)

st = []

res = ''

for i in range(sl):
    if s[i]=='(':
        st.append(s[i])
    elif s[i]==')':
        while len(st) and st[-1]!='(':
            res += st.pop()
        st.pop()
    elif s[i].isalpha():
        res += s[i]
    elif s[i]=='*' or s[i]=='/':
        while len(st) and (st[-1]=='*' or st[-1]=='/'):
            res += st.pop()
        st.append(s[i])
    else:
        while len(st) and st[-1]!='(':
            res += st.pop()
        st.append(s[i])
    # print(i, res)

while len(st):
    res += st.pop()
print(res)

