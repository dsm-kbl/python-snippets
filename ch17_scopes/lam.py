def maker(N):
    return lambda X: X ** N

h = maker(3)
print(h(2))
