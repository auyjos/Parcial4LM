# INSTRUCCIONES PARA LA PRESENTACIÓN

## 📋 Checklist Pre-Presentación

### Archivos a Cargar en Canvas
- [ ] `turing_machine_simulator.py` - Simulador (inciso a)
- [ ] `DIAGRAMA_MAQUINA_TURING.md` - Diagrama (inciso b)
- [ ] `input_accept.txt` - Entrada caso aceptación (inciso c)
- [ ] `output_accept.txt` - Salida caso aceptación (inciso d)
- [ ] `input_reject.txt` - Entrada caso rechazo (inciso e)
- [ ] `output_reject.txt` - Salida caso rechazo (inciso f)
- [ ] `input_infinite.txt` - Entrada caso ciclo infinito (inciso g)
- [ ] `output_infinite.txt` - Salida caso ciclo infinito (inciso h)

### Verificar antes de la presentación
- [ ] Python está instalado (`python --version`)
- [ ] Todos los archivos están en el mismo directorio
- [ ] Los archivos de salida se generan correctamente
- [ ] El código está bien comentado y es legible

---

## 🎯 Demostración en Clase

### Paso 1: Preparación
```bash
# Navegar al directorio del proyecto
cd d:\UVG\Parcial4LM

# Verificar que Python funciona
python --version

# Listar archivos disponibles
dir
```

### Paso 2: Demostración - Caso de Aceptación
```bash
python turing_machine_simulator.py inputs\input_accept.txt outputs\output_accept.txt
```

**Explicar:**
- Entrada: `0110` (dos 1's - número par)
- Se espera: **ACEPTA**
- Configuraciones muestran el recorrido de q0 ↔ q1 hasta qaccept

**Mostrar el archivo de salida:**
```bash
type outputs\output_accept.txt
```

### Paso 3: Demostración - Caso de Rechazo
```bash
python turing_machine_simulator.py inputs\input_reject.txt outputs\output_reject.txt
```

**Explicar:**
- Entrada: `001` (un 1 - número impar)
- Se espera: **RECHAZA**
- Configuraciones muestran que termina en qreject

**Mostrar el archivo de salida:**
```bash
type outputs\output_reject.txt
```

### Paso 4: Demostración - Caso de Ciclo Infinito
```bash
python turing_machine_simulator.py inputs\input_infinite.txt outputs\output_infinite.txt
```

**Explicar:**
- Entrada: `01x` (contiene símbolo 'x')
- Se espera: **CICLO_INFINITO**
- El simulador detecta el ciclo después de 10,000 pasos
- El estado qloop se repite indefinidamente

**Mostrar el archivo de salida (primeras líneas):**
```bash
type outputs\output_infinite.txt | Select-Object -First 50
```

---

## 💡 Puntos Clave para Explicar

### 1. Sobre el Simulador
- **Lenguaje:** Python (fácil de leer y entender)
- **No usa memoria externa:** Solo la cinta de la máquina
- **Validación completa:** Verifica que la especificación sea correcta antes de ejecutar
- **Notación de clase:** Configuraciones en formato `uqv`

### 2. Sobre la Máquina de Turing Diseñada
- **Propósito:** Verificar si una cadena binaria tiene número par de 1's
- **5 estados:** q0, q1, qloop, qaccept, qreject
- **Determinista:** Una sola transición por cada par (estado, símbolo)
- **Completa:** Maneja aceptación, rechazo y ciclo infinito

### 3. Sobre las Configuraciones
```
Formato: uqv
- u: parte leída de la cinta (izquierda del cabezal)
- q: estado actual
- v: parte por leer (desde el cabezal hacia la derecha)

Ejemplo: 011q00
- Ya se leyó: "011"
- Estado actual: q0
- Falta por leer: "0"
```

### 4. Sobre la Función de Transición
```
δ(q0, 1) = (q1, 1, R)

Significa:
- Si estamos en q0 y leemos 1
- Cambiamos a q1
- Escribimos 1 (no cambiamos el símbolo)
- Movemos el cabezal a la derecha (R)
```

---

## 🔍 Posibles Preguntas y Respuestas

### P: ¿Por qué elegiste verificar número par de 1's?
**R:** Es un problema sencillo pero completo que permite demostrar:
- Estados de aceptación y rechazo
- Alternancia entre estados (q0 ↔ q1)
- Ciclo infinito con un caso especial (símbolo 'x')

### P: ¿Cómo detectas el ciclo infinito?
**R:** El simulador tiene un límite de 10,000 pasos. Si la máquina no termina antes de este límite, se asume que está en un ciclo infinito. El estado `qloop` está diseñado específicamente para esto: todas sus transiciones regresan a sí mismo.

### P: ¿Qué pasa si la cinta se queda sin espacio?
**R:** La cinta se expande dinámicamente. Si el cabezal necesita moverse más allá del final, se agregan blancos automáticamente. Si se mueve a la izquierda del inicio, se inserta un blanco al principio.

### P: ¿Por qué no usas buffer o memoria externa?
**R:** Según la definición formal de máquina de Turing, la única memoria disponible es la cinta infinita. El simulador respeta esta restricción.

### P: ¿Cómo validas la especificación?
**R:** El simulador verifica:
- Los conjuntos estén bien definidos
- Las relaciones entre conjuntos (Σ ⊆ Γ, F ⊆ Q, etc.)
- F y R sean disjuntos
- La función de transición esté correctamente definida

---

## 📝 Explicación del Código (Revisión)

### Estructura Principal

```python
class TuringMachine:
    def __init__(self):
        # Componentes de la MT: Q, Σ, Γ, δ, q0, B, F, R
        
    def load_from_file(self, filename):
        # Carga la especificación desde un archivo
        
    def validate_specification(self):
        # Valida que la especificación sea correcta
        
    def step(self):
        # Ejecuta un paso de la máquina
        
    def run(self):
        # Ejecuta la máquina completa
        
    def save_output(self, filename, result):
        # Guarda las configuraciones en un archivo
```

### Métodos Clave

1. **`load_from_file`**: Lee el archivo y parsea cada sección (Q, Σ, Γ, etc.)
2. **`validate_specification`**: Verifica todas las condiciones formales
3. **`step`**: Implementa la transición δ(q, a) = (p, b, D)
4. **`get_configuration`**: Genera la notación `uqv`
5. **`run`**: Bucle principal que ejecuta pasos hasta terminar o detectar ciclo

---

## ⚠️ Errores Comunes a Evitar

### Durante la demostración:
- ❌ No estar en el directorio correcto
- ❌ Nombres de archivos incorrectos
- ❌ Python no instalado o no en PATH
- ❌ Archivos de entrada con formato incorrecto

### En el código:
- ❌ Olvidar validar la entrada
- ❌ No manejar la expansión de la cinta
- ❌ Configuraciones en formato incorrecto
- ❌ No detectar ciclos infinitos

---

## ✅ Lista de Verificación Final

Antes de la presentación, ejecutar:

```bash
# Test completo
python turing_machine_simulator.py inputs\input_accept.txt outputs\output_accept.txt
python turing_machine_simulator.py inputs\input_reject.txt outputs\output_reject.txt
python turing_machine_simulator.py inputs\input_infinite.txt outputs\output_infinite.txt

# Verificar que los archivos de salida existen
dir outputs\output_*.txt

# Revisar que el código no tiene errores de sintaxis
python -m py_compile turing_machine_simulator.py
```

Si todo ejecuta sin errores: **¡Estás listo! 🎉**

---

## 📚 Material de Apoyo

### Definición Formal de Máquina de Turing
```
M = (Q, Σ, Γ, δ, q0, B, F, R)

Donde:
- Q: conjunto finito de estados
- Σ: alfabeto de entrada (Σ ⊂ Γ)
- Γ: alfabeto de la cinta
- δ: Q × Γ → Q × Γ × {L, R} (función de transición)
- q0 ∈ Q: estado inicial
- B ∈ Γ: símbolo blanco
- F ⊆ Q: estados de aceptación
- R ⊆ Q: estados de rechazo (F ∩ R = ∅)
```

### Notación de Configuraciones
```
Configuración instantánea: uqv
- u ∈ Γ*: contenido a la izquierda del cabezal
- q ∈ Q: estado actual
- v ∈ Γ*: contenido desde el cabezal hacia la derecha
```

---

**¡Mucha suerte en tu presentación! 🚀**
