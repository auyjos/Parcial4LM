# EJEMPLOS ADICIONALES - CASOS DE PRUEBA

Este archivo contiene ejemplos adicionales que puedes usar para probar el simulador durante la presentación o demostración.

---

## Ejemplo 4: Cadena Vacía (ACEPTACIÓN)

**Archivo:** `input_empty.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 
```

**Resultado Esperado:** ACEPTA (0 es par)

**Ejecución:**
```powershell
python turing_machine_simulator.py input_empty.txt output_empty.txt
```

---

## Ejemplo 5: Solo Ceros (ACEPTACIÓN)

**Archivo:** `input_zeros.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 0000
```

**Resultado Esperado:** ACEPTA (0 unos = par)

---

## Ejemplo 6: Cuatro Unos (ACEPTACIÓN)

**Archivo:** `input_four_ones.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 11001100
```

**Resultado Esperado:** ACEPTA (4 unos = par)

---

## Ejemplo 7: Tres Unos (RECHAZO)

**Archivo:** `input_three_ones.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 111
```

**Resultado Esperado:** RECHAZA (3 unos = impar)

---

## Ejemplo 8: Alternando (RECHAZO)

**Archivo:** `input_alternating.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 10101
```

**Resultado Esperado:** RECHAZA (3 unos = impar)

---

## Ejemplo 9: X al Final (CICLO INFINITO)

**Archivo:** `input_x_end.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 1111x
```

**Resultado Esperado:** CICLO_INFINITO

---

## Ejemplo 10: Solo X (CICLO INFINITO)

**Archivo:** `input_only_x.txt`

```
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: x
```

**Resultado Esperado:** CICLO_INFINITO

---

## Tabla Resumen de Ejemplos

| # | Entrada | Descripción | Resultado Esperado | Unos |
|---|---------|-------------|-------------------|------|
| 1 | `0110` | Básico par | ACEPTA | 2 |
| 2 | `001` | Básico impar | RECHAZA | 1 |
| 3 | `01x` | Con ciclo | CICLO_INFINITO | 1 |
| 4 | `` (vacío) | Cadena vacía | ACEPTA | 0 |
| 5 | `0000` | Solo ceros | ACEPTA | 0 |
| 6 | `11001100` | Cuatro unos | ACEPTA | 4 |
| 7 | `111` | Tres unos | RECHAZA | 3 |
| 8 | `10101` | Alternando | RECHAZA | 3 |
| 9 | `1111x` | X al final | CICLO_INFINITO | 4 |
| 10 | `x` | Solo X | CICLO_INFINITO | 0 |

---

## Script para Crear Ejemplos Adicionales

```powershell
# Crear ejemplo de cadena vacía
@"
Q: q0,q1,qloop,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,x,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q0,0,R
q0,1,q1,1,R
q0,x,qloop,x,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q0,1,R
q1,x,qloop,x,R
q1,_,qreject,_,R
qloop,0,qloop,0,R
qloop,1,qloop,1,R
qloop,x,qloop,x,R
qloop,_,qloop,_,R
Input: 
"@ | Out-File -Encoding UTF8 input_empty.txt

# Ejecutar
python turing_machine_simulator.py input_empty.txt output_empty.txt
```

---

## Análisis de Configuraciones

### Ejemplo: Entrada "0110"

```
Paso 0: q00110       (Inicio - lee 0)
Paso 1: 0q0110       (q0 → q0, escribe 0, va derecha, lee 1)
Paso 2: 01q110       (q0 → q1, escribe 1, va derecha, lee 1)
Paso 3: 011q00       (q1 → q0, escribe 1, va derecha, lee 0)
Paso 4: 0110q0_      (q0 → q0, escribe 0, va derecha, lee _)
Paso 5: 0110_qaccept_ (q0 → qaccept, escribe _, va derecha)
```

**Análisis:**
- Comienza en q0 (contador par)
- Primer 1 → pasa a q1 (contador impar)
- Segundo 1 → vuelve a q0 (contador par)
- Lee blanco en q0 → ACEPTA ✓

---

## Preguntas de Demostración

Durante la presentación, puedes responder:

### P1: ¿Qué pasa con una cadena vacía?
**Demostrar:** Ejemplo 4 - ACEPTA (0 es par)

### P2: ¿Qué pasa si todos son ceros?
**Demostrar:** Ejemplo 5 - ACEPTA (0 unos)

### P3: ¿Funciona con cadenas más largas?
**Demostrar:** Ejemplo 6 - ACEPTA (8 caracteres, 4 unos)

### P4: ¿Cómo se ve el ciclo infinito?
**Demostrar:** Ejemplo 3 o 10 - Mostrar archivo de salida con 10,000 pasos

---

## Notas para la Demostración

1. **Empezar simple:** Usa los ejemplos básicos (1, 2, 3)
2. **Casos especiales:** Muestra vacío y solo ceros
3. **Cadenas largas:** Demuestra escalabilidad con ejemplo 6
4. **Ciclo infinito:** Muestra que se detecta correctamente

---

**Estos ejemplos te permiten tener más material para la presentación y demostrar la versatilidad del simulador.**
