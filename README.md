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
- ✅ Guardar los resultados en archivos de salida

---

## 📁 Archivos del Proyecto

### Programa Principal
- **`turing_machine_simulator.py`** - Simulador de Máquina de Turing

### Documentación
- **`DIAGRAMA_MAQUINA_TURING.md`** - Diagrama y especificación de la máquina diseñada
- **`README.md`** - Este archivo (instrucciones de uso)

### Archivos de Entrada (Casos de Prueba)
- **`inputs/input_accept.txt`** - Caso que llega a estado de ACEPTACIÓN
- **`inputs/input_reject.txt`** - Caso que llega a estado de RECHAZO
- **`inputs/input_infinite.txt`** - Caso que entra en CICLO INFINITO

### Archivos de Salida (Configuraciones)
- **`outputs/output_accept.txt`** - Configuraciones del caso de aceptación
- **`outputs/output_reject.txt`** - Configuraciones del caso de rechazo
- **`outputs/output_infinite.txt`** - Configuraciones del caso de ciclo infinito

---

## 🚀 Cómo Usar el Simulador

### Requisitos
- Python 3.6 o superior
- No requiere librerías externas (usa solo la librería estándar)

### Ejecución

```bash
python turing_machine_simulator.py <archivo_entrada> [archivo_salida]
```

**Ejemplos:**

```bash
# Caso de aceptación
python turing_machine_simulator.py inputs\input_accept.txt outputs\output_accept.txt

# Caso de rechazo
python turing_machine_simulator.py inputs\input_reject.txt outputs\output_reject.txt

# Caso de ciclo infinito
python turing_machine_simulator.py inputs\input_infinite.txt outputs\output_infinite.txt
```

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

### Ejemplo:
```
Q: q0,q1,qaccept,qreject
Sigma: 0,1
Gamma: 0,1,_
q0: q0
B: _
F: qaccept
R: qreject
Delta:
q0,0,q1,0,R
q0,1,q1,1,R
q0,_,qaccept,_,R
q1,0,q1,0,R
q1,1,q1,1,R
q1,_,qreject,_,R
Input: 010
```

---

## 🔍 Descripción de la Máquina Implementada

La máquina de Turing diseñada **verifica si una cadena binaria tiene un número PAR de 1's**.

### Comportamiento:
- **ACEPTA** ✅ - Cadenas con número par de 1's (incluyendo cero 1's)
  - Ejemplo: `0110` (dos 1's - par)
  - Ejemplo: `0000` (cero 1's - par)
  - Ejemplo: `11001100` (cuatro 1's - par)

- **RECHAZA** ❌ - Cadenas con número impar de 1's
  - Ejemplo: `001` (un 1 - impar)
  - Ejemplo: `111` (tres 1's - impar)

- **CICLO INFINITO** ♾️ - Cadenas que contienen el símbolo 'x'
  - Ejemplo: `01x`
  - El estado `qloop` se queda iterando infinitamente

### Estados:
- `q0` - Estado inicial (contador par)
- `q1` - Estado contador impar
- `qloop` - Estado de ciclo infinito
- `qaccept` - Estado de aceptación
- `qreject` - Estado de rechazo

Ver el archivo **`DIAGRAMA_MAQUINA_TURING.md`** para más detalles.

---

## 📊 Formato de Salida

El archivo de salida contiene:

1. **Especificación de la máquina** (Q, Σ, Γ, δ, q0, B, F, R)
2. **Función de transición** (todas las reglas δ)
3. **Configuraciones paso a paso** (notación: uqv)
4. **Resultado final** (ACEPTA, RECHAZA, o CICLO_INFINITO)

### Ejemplo de configuración:
```
Paso 0: q00110
Paso 1: 0q0110
Paso 2: 01q110
Paso 3: 011q10
Paso 4: 0110q0_
Paso 5: 0110_qaccept_
```

Donde:
- La parte antes del estado = contenido leído
- El estado = estado actual
- La parte después del estado = contenido por leer

---

## ✅ Validaciones Implementadas

El simulador valida:
- ✓ Q no está vacío
- ✓ q0 ∈ Q
- ✓ Σ ⊆ Γ
- ✓ B ∈ Γ
- ✓ F ⊆ Q
- ✓ R ⊆ Q
- ✓ F ∩ R = ∅
- ✓ Función de transición bien definida
- ✓ Direcciones válidas (L o R)

---

## 🎯 Entregables del Parcial

### ✅ Completados:

- [x] **a)** Programa simulador (`turing_machine_simulator.py`)
- [x] **b)** Diagrama de máquina de Turing (`DIAGRAMA_MAQUINA_TURING.md`)
- [x] **c)** Archivo de entrada - caso aceptación (`input_accept.txt`)
- [x] **d)** Archivo de salida - caso aceptación (`output_accept.txt`)
- [x] **e)** Archivo de entrada - caso rechazo (`input_reject.txt`)
- [x] **f)** Archivo de salida - caso rechazo (`output_reject.txt`)
- [x] **g)** Archivo de entrada - caso ciclo infinito (`input_infinite.txt`)
- [x] **h)** Archivo de salida - caso ciclo infinito (`output_infinite.txt`)

### Pendiente:
- [ ] **i)** Ejecución del programa el día asignado
- [ ] **j)** Revisión de archivos en Canvas

---

## 💡 Características Adicionales

- **Detección de ciclos infinitos**: Límite de 10,000 pasos
- **Expansión dinámica de cinta**: Se agregan blancos automáticamente
- **Comentarios en archivos**: Líneas con `#` son ignoradas
- **Validación completa**: Verifica la correctitud antes de ejecutar
- **Salida detallada**: Muestra todas las configuraciones paso a paso

---

## 🧪 Pruebas Rápidas

Para verificar que todo funciona:

```bash
# Ejecutar los tres casos
python turing_machine_simulator.py inputs\input_accept.txt outputs\output_accept.txt
python turing_machine_simulator.py inputs\input_reject.txt outputs\output_reject.txt
python turing_machine_simulator.py inputs\input_infinite.txt outputs\output_infinite.txt

# Verificar los archivos de salida
type outputs\output_accept.txt
type outputs\output_reject.txt
type outputs\output_infinite.txt
```

---

## 📚 Referencias

- Notación de configuraciones según visto en clase
- Definición formal de Máquina de Turing: M = (Q, Σ, Γ, δ, q0, B, F, R)
- Función de transición: δ: Q × Γ → Q × Γ × {L, R}

---

## ✨ Notas Finales

Este simulador implementa fielmente la notación y definiciones vistas en clase:
- **No usa buffer ni memoria externa** (solo la cinta)
- **Configuraciones en notación estándar** (uqv)
- **Función de transición determinista** (máximo una transición por par estado-símbolo)
- **Estados de aceptación y rechazo explícitos**
- **Capacidad de detectar ciclos infinitos**

---

**¡Éxito en el parcial! 🎓**
