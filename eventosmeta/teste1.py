from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")


┌─────────────────────────────────────────────────────────────┐
│                 FLUXO DE STATUS - INSCRIÇÕES                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Pendente (código 1)                                     │
│     └─> PARTICIPA da classificação ✅                       │
│                                                             │
│  2. Classificado (código 2)                                 │
│     └─> PARTICIPA da reclassificação ✅                     │
│                                                             │
│  3. Lista de Espera (código 3)                              │
│     └─> PARTICIPA da reclassificação ✅                     │
│                                                             │
│  4. Confirmada (código 4)                                   │
│     └─> NÃO participa ❌ (já confirmou vaga)                │
│                                                             │
│  5. Cancelada (código 5)                                    │
│     └─> NÃO participa ❌                                    │
│                                                             │
│  6. Expirada (código 6)                                     │
│     └─> NÃO participa ❌                                    │
│                                                             │
│  7. Desistente (código 7)                                   │
│     └─> NÃO participa ❌                                    │
│                                                             │
│  8. Não localizado para confirmar inscrição (código 8)      │
│     └─> NÃO participa ❌                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘

APÓS CLASSIFICAÇÃO:
├─> Se posição <= total_vagas → Status: "Classificado" (2)
└─> Se posição > total_vagas → Status: "Lista de Espera" (3)

APÓS CLASSIFICAÇÃO (EVENTO):
└─> Status do evento → "Resultado Divulgado"