lines=[]
while True:
    s=input()
    if s:
        lines.append(s.upper())
    else:
        break

        
print('\n'.join(lines))