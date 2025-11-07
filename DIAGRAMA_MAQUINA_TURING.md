# DIAGRAMA DE MÁQUINA DE TURING

## Descripción de la Máquina

**Propósito:** Esta máquina de Turing verifica si una cadena binaria tiene un número par de '1's.

- **Acepta:** Cadenas con un número par de '1's (incluyendo cero '1's)
- **Rechaza:** Cadenas con un número impar de '1's
- **Ciclo Infinito:** Cadenas que contengan el símbolo 'x'

---

## Componentes de la Máquina

### Estados (Q)
- **q0**: Estado inicial (conteo par de '1's)
- **q1**: Estado de conteo impar de '1's
- **qloop**: Estado de ciclo infinito
- **qaccept**: Estado de aceptación ✓
- **qreject**: Estado de rechazo ✗

### Alfabeto de Entrada (Σ)
- **{0, 1}**

### Alfabeto de la Cinta (Γ)
- **{0, 1, x, _}**
- Donde '_' es el símbolo blanco

### Estado Inicial
- **q0**

### Símbolo Blanco
- **_**

### Estados de Aceptación (F)
- **{qaccept}**

### Estados de Rechazo (R)
- **{qreject}**

---

## Función de Transición (δ)

| Estado Actual | Símbolo Leído | Estado Siguiente | Símbolo Escrito | Dirección |
|---------------|---------------|------------------|-----------------|-----------|
| q0            | 0             | q0               | 0               | R         |
| q0            | 1             | q1               | 1               | R         |
| q0            | x             | qloop            | x               | R         |
| q0            | _             | qaccept          | _               | R         |
| q1            | 0             | q1               | 0               | R         |
| q1            | 1             | q0               | 1               | R         |
| q1            | x             | qloop            | x               | R         |
| q1            | _             | qreject          | _               | R         |
| qloop         | 0             | qloop            | 0               | R         |
| qloop         | 1             | qloop            | 1               | R         |
| qloop         | x             | qloop            | x               | R         |
| qloop         | _             | qloop            | _               | R         |

---

## Diagrama Visual

```
                    0/0,R
                  ┌───────┐
                  │       │
                  ▼       │
        ┌─────────────────┴─┐
  ───→  │       q0          │  _/_,R
 Inicio │  (par de 1's)     │───────→ (( qaccept ))
        └─────────┬─────────┘           ACEPTA ✓
                  │
            1/1,R │
                  │
                  ▼
        ┌───────────────────┐
        │       q1          │  _/_,R
        │  (impar de 1's)   │───────→ (( qreject ))
        └─────────┬─────────┘           RECHAZA ✗
                  │       ▲
            0/0,R │       │
                  └───────┘
                  
                  
        x/x,R desde q0 o q1
                  │
                  ▼
        ┌───────────────────┐
        │      qloop        │  {0,1,x,_}/{0,1,x,_},R
        │  (ciclo infinito) │◄────────────────────┐
        └───────────────────┘                     │
                  │                               │
                  └───────────────────────────────┘
```

---

## Ejemplos de Ejecución

### Ejemplo 1: ACEPTACIÓN (Número par de 1's)
- **Entrada:** `0110`
- **Configuraciones:**
  1. `q00110` (inicio en q0, lee 0)
  2. `0q0110` (sigue en q0, lee 1)
  3. `01q110` (va a q1, lee 1)
  4. `011q10` (vuelve a q0, lee 0)
  5. `0110q0_` (sigue en q0, lee _)
  6. `0110_qaccept_` (ACEPTA - número par de 1's)

### Ejemplo 2: RECHAZO (Número impar de 1's)
- **Entrada:** `101`
- **Configuraciones:**
  1. `q0101` (inicio en q0, lee 1)
  2. `1q101` (va a q1, lee 0)
  3. `10q11` (sigue en q1, lee 1)
  4. `101q0_` (vuelve a q0, pero hay un solo 1 más)
  
  **Nota:** Corregimos - con 101 hay 2 unos (par)
  
- **Mejor ejemplo:** `001`
- **Configuraciones:**
  1. `q0001` (inicio en q0, lee 0)
  2. `0q001` (sigue en q0, lee 0)
  3. `00q01` (sigue en q0, lee 1)
  4. `001q1_` (va a q1, lee _)
  5. `001_qreject_` (RECHAZA - número impar de 1's)

### Ejemplo 3: CICLO INFINITO
- **Entrada:** `01x`
- **Configuraciones:**
  1. `q001x` (inicio en q0, lee 0)
  2. `0q01x` (sigue en q0, lee 1)
  3. `01q1x` (va a q1, lee x)
  4. `01xqloop_` (va a qloop, lee _)
  5. `01x_qloop_` (sigue en qloop, lee _)
  6. `01x__qloop_` (sigue en qloop infinitamente...)

---

## Notación Utilizada

- **Configuración:** `uqv` donde:
  - `u` = contenido de la cinta a la izquierda del cabezal
  - `q` = estado actual
  - `v` = contenido de la cinta desde el cabezal hacia la derecha

- **Transición:** `δ(q, a) = (p, b, D)` donde:
  - `q` = estado actual
  - `a` = símbolo leído
  - `p` = nuevo estado
  - `b` = símbolo escrito
  - `D` = dirección (L=izquierda, R=derecha)

---

## Propiedades de la Máquina

✓ Determinista (máximo una transición por cada par estado-símbolo)  
✓ Tiene estados de aceptación explícitos  
✓ Tiene estados de rechazo explícitos  
✓ Puede entrar en ciclo infinito con entradas específicas  
✓ Utiliza solo la cinta (sin memoria externa)

---

**Fecha:** Noviembre 2025  
**Curso:** Lenguajes y Máquinas  
**Tema:** Máquinas de Turing Deterministas
