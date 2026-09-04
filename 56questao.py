

total_casas = 64
grao = 1
total_graos = 0

for casa in range(1, total_casas + 1):
    total_graos += grao
    print(f"Casa {casa}: {grao} grão(s)")
    grao = grao * 2

print("\nTotal de grãos que o monge esperava receber:", total_graos)