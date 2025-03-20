lines = [int(_) for _ in open(0).read().splitlines()]
print('part 1:', sum(lines))
print('part 2:', sum(sorted(lines, reverse=True)[20:]))
print('part 3:', sum([n if i % 2 == 0 else -n for i,n in enumerate(lines)]))
