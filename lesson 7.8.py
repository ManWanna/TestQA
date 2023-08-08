total = 0
for n in range(1, 101):
    for k in range(1, 101):
        for m in range(1, 101):
            if 10 * n + 5 * k + 0.5 * m == 100  and n + k + m == 100:
                print('n =', n, 'k =', k, 'm =', m)
