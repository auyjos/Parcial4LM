# Simulador de Máquina de Turing - Parcial 4

**Estudiante:** [Tu Nombre]  
**Curso:** Lenguajes y Máquinas  
**Fecha:** Noviembre 2025

---

## 📋 Descripción del Proyecto

Este proyecto implementa un **simulador de Máquina de Turing Determinista** en Python, según la notación vista en clase. El simulador puede:

- ✅ Cargar especificaciones de máquinas de Turing desde archivos de texto
- ✅ Validar que las especificaciones sean correctas
- ✅ Ejecutar la simulación y generar configuraciones
- ✅ Detectar estados de aceptación, rechazo y ciclos infinitos
- ✅ Guardar los resultados automáticamente en la carpeta `outputs/`

---

## 📁 Estructura del Proyecto

```
Parcial4LM/
├── turing_machine_simulator.py    # Simulador principal
├── README.md                       # Este archivo
├── DIAGRAMA_MAQUINA_TURING.md     # Diagrama y especificación
├── EJEMPLOS_ADICIONALES.md        # Documentación de ejemplos
├── inputs/                         # Carpeta de entradas
│   ├── input_accept.txt           # ✅ Caso aceptación
│   ├── input_reject.txt           # ❌ Caso rechazo
│   ├── input_infinite.txt         # ♾️ Caso ciclo infinito
│   ├── input_empty.txt            # ✅ Cadena vacía
│   ├── input_zeros.txt            # ✅ Solo ceros
│   ├── input_four_ones.txt        # ✅ 4 unos (par)
│   ├── input_three_ones.txt       # ❌ 3 unos (impar)
│   ├── input_alternating.txt      # ❌ Alternante (impar)
│   ├── input_x_end.txt            # ♾️ X al final
│   └── input_only_x.txt           # ♾️ Solo X
└── outputs/                        # Carpeta de salidas (generada)
    ├── output_accept.txt
    ├── output_reject.txt
    ├── output_infinite.txt
    └── ... (10 archivos de salida)
```

---

## 🚀 Cómo Usar el Simulador

### Requisitos
- Python 3.6 o superior
- No requiere librerías externas (usa solo la librería estándar)

### Ejecución Básica

```bash
# Forma simple (salida automática en outputs/)
python turing_machine_simulator.py inputs\input_accept.txt

# Forma explícita (especificar archivo de salida)
python turing_machine_simulator.py inputs\input_accept.txt outputs\output_accept.txt
```

### Ejecutar Todos los Casos de Prueba

```bash
# Caso 1: Aceptación (0110 - dos 1's)
python turing_machine_simulator.py inputs\input_accept.txt

# Caso 2: Rechazo (001 - un 1)
python turing_machine_simulator.py inputs\input_reject.txt

# Caso 3: Ciclo Infinito (01x - contiene 'x')
python turing_machine_simulator.py inputs\input_infinite.txt

# Caso 4: Cadena vacía (acepta - cero 1's)
python turing_machine_simulator.py inputs\input_empty.txt

# Caso 5: Solo ceros (acepta - cero 1's)
python turing_machine_simulator.py inputs\input_zeros.txt

# Caso 6: Cuatro unos (acepta - par)
python turing_machine_simulator.py inputs\input_four_ones.txt

# Caso 7: Tres unos (rechaza - impar)
python turing_machine_simulator.py inputs\input_three_ones.txt

# Caso 8: Alternante (rechaza - impar)
python turing_machine_simulator.py inputs\input_alternating.txt

# Caso 9: X al final (ciclo infinito)
python turing_machine_simulator.py inputs\input_x_end.txt

# Caso 10: Solo X (ciclo infinito)
python turing_machine_simulator.py inputs\input_only_x.txt
```

---

## 📊 Casos de Prueba Incluidos

### ✅ Casos de ACEPTACIÓN (5 casos)

| # | Archivo | Entrada | Resultado | Explicación |
|---|---------|---------|-----------|-------------|
| 1 | `input_accept.txt` | `0110` | ✅ ACEPTA | 2 unos (par) |
| 4 | `input_empty.txt` | `""` (vacío) | ✅ ACEPTA | 0 unos (par) |
| 5 | `input_zeros.txt` | `0000` | ✅ ACEPTA | 0 unos (par) |
| 6 | `input_four_ones.txt` | `11001100` | ✅ ACEPTA | 4 unos (par) |

### ❌ Casos de RECHAZO (3 casos)

| # | Archivo | Entrada | Resultado | Explicación |
|---|---------|---------|-----------|-------------|
| 2 | `input_reject.txt` | `001` | ❌ RECHAZA | 1 uno (impar) |
| 7 | `input_three_ones.txt` | `111` | ❌ RECHAZA | 3 unos (impar) |
| 8 | `input_alternating.txt` | `10101` | ❌ RECHAZA | 3 unos (impar) |

### ♾️ Casos de CICLO INFINITO (3 casos)

| # | Archivo | Entrada | Resultado | Explicación |
|---|---------|---------|-----------|-------------|
| 3 | `input_infinite.txt` | `01x` | ♾️ CICLO | Contiene 'x' |
| 9 | `input_x_end.txt` | `1111x` | ♾️ CICLO | 'x' al final |
| 10 | `input_only_x.txt` | `x` | ♾️ CICLO | Solo 'x' |

---

## 📝 Formato del Archivo de Entrada

```
# Comentarios comienzan con #

Q: estado1,estado2,estado3,...
Sigma: simbolo1,simbolo2,...
Gamma: simbolo1,simbolo2,simbolo_blanco,...
q0: estado_inicial
B: simbolo_blanco
F: estado_aceptacion1,estado_aceptacion2,...
R: estado_rechazo1,estado_rechazo2,...
Delta:
estado_actual,simbolo_leido,estado_siguiente,simbolo_escrito,direccion
...
Input: cadena_de_entrada
```

### Ejemplo Completo:
```
# Máquina que verifica número par de 1's
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
Input: 0110
```

---

## 🔍 Descripción de la Máquina Implementada

La máquina de Turing diseñada **verifica si una cadena binaria tiene un número PAR de 1's**.

### Comportamiento Detallado:

#### ✅ ACEPTA (5 ejemplos)
Cadenas con número par de 1's (incluyendo cero):
- `""` (vacío) → 0 unos es par ✓
- `0000` → 0 unos es par ✓
- `0110` → 2 unos es par ✓
- `11001100` → 4 unos es par ✓
- `000000` → 0 unos es par ✓

#### ❌ RECHAZA (3 ejemplos)
Cadenas con número impar de 1's:
- `001` → 1 uno es impar ✗
- `111` → 3 unos es impar ✗
- `10101` → 3 unos es impar ✗

#### ♾️ CICLO INFINITO (3 ejemplos)
Cadenas que contienen el símbolo 'x':
- `01x` → Contiene 'x', entra en bucle
- `1111x` → Contiene 'x', entra en bucle
- `x` → Solo 'x', entra en bucle

### Estados de la Máquina:

| Estado | Descripción |
|--------|-------------|
| `q0` | Estado inicial - Ha visto un número PAR de 1's |
| `q1` | Ha visto un número IMPAR de 1's |
| `qloop` | Estado de bucle infinito (al encontrar 'x') |
| `qaccept` | Estado de aceptación |
| `qreject` | Estado de rechazo |

### Tabla de Transiciones Simplificada:

```
En q0 (par de 1's):
  - Lee '0' → Mantiene q0, escribe '0', mueve R
  - Lee '1' → Cambia a q1, escribe '1', mueve R
  - Lee 'x' → Va a qloop (ciclo infinito)
  - Lee '_' → Va a qaccept (ACEPTA)

En q1 (impar de 1's):
  - Lee '0' → Mantiene q1, escribe '0', mueve R
  - Lee '1' → Cambia a q0, escribe '1', mueve R
  - Lee 'x' → Va a qloop (ciclo infinito)
  - Lee '_' → Va a qreject (RECHAZA)

En qloop (bucle):
  - Cualquier símbolo → Mantiene qloop, mueve R
```

Ver el archivo **`DIAGRAMA_MAQUINA_TURING.md`** para el diagrama completo.

---

## 📊 Formato de Salida

El archivo de salida contiene:

1. **Especificación de la máquina** (Q, Σ, Γ, δ, q0, B, F, R)
2. **Función de transición** (todas las reglas δ)
3. **Configuraciones paso a paso** (notación: uqv)
4. **Resultado final** (ACEPTA, RECHAZA, o CICLO_INFINITO)
5. **Estadísticas** (número de pasos)

### Ejemplo de Configuraciones:

```
=== EJECUCIÓN ===
Input: 0110

Configuraciones:
Paso 0: q00110
Paso 1: 0q0110
Paso 2: 01q110
Paso 3: 011q10
Paso 4: 0110q0_
Paso 5: 0110_qaccept_

RESULTADO: ACEPTA
Número de pasos: 5
```

**Notación de configuración (uqv):**
- `u` = parte de la cinta ya procesada (a la izquierda)
- `q` = estado actual de la máquina
- `v` = parte de la cinta por procesar (a la derecha, empezando con el símbolo actual)

### Ejemplo Detallado:
En la configuración `01q110`:
- `01` = ya procesó estos símbolos
- `q1` = está en el estado q1
- `10` = por procesar (cabezal apunta al primer '1')

---

## ✅ Validaciones Implementadas

El simulador valida automáticamente:
- ✓ **Q no vacío**: Conjunto de estados tiene al menos un elemento
- ✓ **q0 ∈ Q**: Estado inicial pertenece a Q
- ✓ **Σ ⊆ Γ**: Alfabeto de entrada es subconjunto del alfabeto de cinta
- ✓ **B ∈ Γ**: Símbolo blanco pertenece al alfabeto de cinta
- ✓ **B ∉ Σ**: Símbolo blanco NO está en alfabeto de entrada
- ✓ **F ⊆ Q**: Estados de aceptación pertenecen a Q
- ✓ **R ⊆ Q**: Estados de rechazo pertenecen a Q
- ✓ **F ∩ R = ∅**: Estados de aceptación y rechazo son disjuntos
- ✓ **Función determinista**: Máximo una transición por (estado, símbolo)
- ✓ **Direcciones válidas**: Solo 'L' (izquierda) o 'R' (derecha)
- ✓ **Estados alcanzables**: Todos los estados en δ pertenecen a Q
- ✓ **Símbolos válidos**: Todos los símbolos en δ pertenecen a Γ

---

## 🎯 Entregables del Parcial

### ✅ Completados (8 archivos principales):

- [x] **a)** Programa simulador (`turing_machine_simulator.py`)
- [x] **b)** Diagrama de máquina de Turing (`DIAGRAMA_MAQUINA_TURING.md`)
- [x] **c)** Archivo de entrada - caso aceptación (`inputs/input_accept.txt`)
- [x] **d)** Archivo de salida - caso aceptación (`outputs/output_accept.txt`)
- [x] **e)** Archivo de entrada - caso rechazo (`inputs/input_reject.txt`)
- [x] **f)** Archivo de salida - caso rechazo (`outputs/output_reject.txt`)
- [x] **g)** Archivo de entrada - caso ciclo infinito (`inputs/input_infinite.txt`)
- [x] **h)** Archivo de salida - caso ciclo infinito (`outputs/output_infinite.txt`)

### ✅ Extras (7 casos adicionales de prueba):

- [x] Caso 4: Cadena vacía → Aceptación
- [x] Caso 5: Solo ceros → Aceptación
- [x] Caso 6: Cuatro unos → Aceptación
- [x] Caso 7: Tres unos → Rechazo
- [x] Caso 8: Alternante → Rechazo
- [x] Caso 9: X al final → Ciclo infinito
- [x] Caso 10: Solo X → Ciclo infinito

### Pendiente (para el día del parcial):
- [ ] **i)** Ejecución del programa el día asignado (**22.5 puntos**)
- [ ] **j)** Revisión de archivos en Canvas (**22.5 puntos**)

---

## 💡 Características Adicionales

### Detección de Ciclos Infinitos
- **Límite configurado**: 10,000 pasos máximo
- **Detección automática**: Si excede el límite → marca como CICLO_INFINITO
- **Todas las configuraciones**: Se guardan en el archivo de salida

### Manejo Automático de Cinta
- **Expansión dinámica**: Agrega blancos automáticamente cuando es necesario
- **Sin límites artificiales**: La cinta crece según necesidad
- **Movimiento bidireccional**: Puede moverse a izquierda y derecha

### Sistema de Archivos
- **Carpetas organizadas**: `inputs/` y `outputs/` separadas
- **Salida automática**: Si no especificas archivo de salida, usa `outputs/output_X.txt`
- **Sin sobrescrituras**: Genera nombres únicos si el archivo existe

### Comentarios y Formato
- **Líneas de comentario**: Usa `#` al inicio para comentarios
- **Espacios flexibles**: Ignora espacios extra
- **Validación estricta**: Detecta errores de formato

---

## 🧪 Pruebas Completas

### Script para Ejecutar Todos los Casos

```bash
# Windows PowerShell
foreach ($i in 1..10) {
    $files = @(
        "accept", "reject", "infinite", "empty", "zeros",
        "four_ones", "three_ones", "alternating", "x_end", "only_x"
    )
    $file = $files[$i-1]
    python turing_machine_simulator.py "inputs\input_$file.txt"
}
```

### Verificar Resultados

```bash
# Ver todos los outputs generados
dir outputs\

# Ver contenido de un output específico
type outputs\output_accept.txt

# Buscar resultados en todos los outputs
findstr "RESULTADO:" outputs\*.txt
```

### Resultados Esperados

```
✅ output_accept.txt       → RESULTADO: ACEPTA (5 pasos)
❌ output_reject.txt       → RESULTADO: RECHAZA (4 pasos)
♾️ output_infinite.txt     → RESULTADO: CICLO_INFINITO (10,000 pasos)
✅ output_empty.txt        → RESULTADO: ACEPTA (1 paso)
✅ output_zeros.txt        → RESULTADO: ACEPTA (5 pasos)
✅ output_four_ones.txt    → RESULTADO: ACEPTA (9 pasos)
❌ output_three_ones.txt   → RESULTADO: RECHAZA (4 pasos)
❌ output_alternating.txt  → RESULTADO: RECHAZA (6 pasos)
♾️ output_x_end.txt        → RESULTADO: CICLO_INFINITO (10,000 pasos)
♾️ output_only_x.txt       → RESULTADO: CICLO_INFINITO (10,000 pasos)
```

---

## 📚 Referencias Teóricas

### Definición Formal

Una **Máquina de Turing** es una 7-tupla:

**M = (Q, Σ, Γ, δ, q₀, B, F, R)**

Donde:
- **Q**: Conjunto finito de estados
- **Σ**: Alfabeto de entrada (Σ ⊂ Γ)
- **Γ**: Alfabeto de la cinta
- **δ**: Q × Γ → Q × Γ × {L, R} (función de transición)
- **q₀**: Estado inicial (q₀ ∈ Q)
- **B**: Símbolo blanco (B ∈ Γ, B ∉ Σ)
- **F**: Conjunto de estados de aceptación (F ⊆ Q)
- **R**: Conjunto de estados de rechazo (R ⊆ Q, F ∩ R = ∅)

### Notación de Configuraciones

Una **configuración** se representa como: **uqv**

Donde:
- **u** ∈ Γ* (contenido a la izquierda del cabezal)
- **q** ∈ Q (estado actual)
- **v** ∈ Γ* (contenido desde el cabezal hacia la derecha)

### Movimientos (⊢)

La relación de transición **⊢** se define:
- **uaqibv ⊢ uacqjbv** si δ(qi, b) = (qj, c, R)
- **uaqibv ⊢ uqjacbv** si δ(qi, b) = (qj, c, L)

---

## ✨ Notas Importantes

### Cumplimiento de Requisitos
- ✅ **Notación de clase**: Usa exactamente la notación vista en clase
- ✅ **Sin buffer externo**: Solo usa la cinta (no memorias adicionales)
- ✅ **Configuraciones estándar**: Formato uqv
- ✅ **Determinista**: Máximo una transición por (estado, símbolo)
- ✅ **Estados explícitos**: Tiene estados de aceptación y rechazo definidos
- ✅ **Ciclos detectados**: Puede identificar ciclos infinitos

### Para la Presentación
1. **Llevar laptop** con Python instalado
2. **Tener los archivos** en la carpeta correcta
3. **Conocer los casos**: Poder explicar cada uno
4. **Entender el código**: Revisar el simulador
5. **Probar antes**: Ejecutar todos los casos

### Troubleshooting Común

**Error: "No se encuentra el archivo"**
```bash
# Verificar que estás en la carpeta correcta
cd d:\UVG\Parcial4LM
dir inputs\
```

**Error: "Python no reconocido"**
```bash
# Usar py en lugar de python
py turing_machine_simulator.py inputs\input_accept.txt
```

**Archivo de salida no se genera**
```bash
# Crear carpeta outputs si no existe
mkdir outputs
```

---

## 🎓 Documentación Adicional

Para más información, consultar:
- **`DIAGRAMA_MAQUINA_TURING.md`** - Diagrama detallado y tabla de transiciones
- **`EJEMPLOS_ADICIONALES.md`** - Explicación de los 10 casos de prueba
- **`INSTRUCCIONES_PRESENTACION.md`** - Guía para el día del parcial
- **`REFERENCIA_RAPIDA.txt`** - Hoja de referencia para imprimir

---

## 📞 Contacto y Ayuda

Si tienes problemas durante la ejecución:
1. Verificar que Python está instalado: `python --version`
2. Revisar que los archivos están en las carpetas correctas
3. Consultar la sección de troubleshooting
4. Revisar los ejemplos en `EJEMPLOS_ADICIONALES.md`

---

**¡Éxito en el parcial! 🎓🚀**

*Última actualización: Noviembre 2025*