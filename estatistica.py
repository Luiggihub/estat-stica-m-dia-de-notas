import statistics as stats

notas_turma_a = [7.0, 8.0, 7.5, 7.5]
notas_turma_b = [5.0, 10.0, 6.0, 9.0]

media_a = stats.mean(notas_turma_a)
media_b = stats.mean(notas_turma_b)

desvio_a = stats.stdev(notas_turma_a)
desvio_b = stats.stdev(notas_turma_b)

print("-" * 45)
print("RESULTADOS DA ANÁLISE ESTATÍSTICA")
print("-" * 45)

print(f"Turma A -> Média: {media_a:.2f} | Desvio Padrão: {desvio_a:.2f}")
print(f"Turma B -> Média: {media_b:.2f} | Desvio Padrão: {desvio_b:.2f}")

print("-" * 45)

if desvio_a < desvio_b:
    print("Conclusão: A Turma A é mais homogênea (regular).")
else:
    print("Conclusão: A Turma B é mais homogênea (regular).")
print("-" * 45)

