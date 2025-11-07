# 📚 ÍNDICE GENERAL DEL PROYECTO

**Parcial 4 - Simulador de Máquina de Turing Determinista**  
**Fecha:** Noviembre 6, 2025

---

## 🎯 Inicio Rápido

### Para ejecutar el proyecto inmediatamente:
```powershell
# 1. Ejecutar pruebas automáticas
powershell -ExecutionPolicy Bypass -File test_simulator.ps1

# 2. Ejecutar casos individuales
python turing_machine_simulator.py inputs\input_accept.txt outputs\output_accept.txt
python turing_machine_simulator.py inputs\input_reject.txt outputs\output_reject.txt
python turing_machine_simulator.py inputs\input_infinite.txt outputs\output_infinite.txt
```

---

## 📋 ARCHIVOS DEL PROYECTO

### 🔧 Archivos Principales (ENTREGAR EN CANVAS)

| Archivo | Descripción | Inciso | Tamaño |
|---------|-------------|--------|--------|
| `turing_machine_simulator.py` | Simulador en Python | a) | 13.7 KB |
| `DIAGRAMA_MAQUINA_TURING.md` | Diagrama y especificación de la MT | b) | 5.7 KB |
| `inputs/input_accept.txt` | Entrada - caso aceptación | c) | 959 B |
| `outputs/output_accept.txt` | Salida - caso aceptación | d) | 1.1 KB |
| `inputs/input_reject.txt` | Entrada - caso rechazo | e) | 960 B |
| `outputs/output_reject.txt` | Salida - caso rechazo | f) | 1.1 KB |
| `inputs/input_infinite.txt` | Entrada - caso ciclo infinito | g) | 977 B |
| `outputs/output_infinite.txt` | Salida - caso ciclo infinito | h) | ~50 MB |

**TOTAL DE ARCHIVOS A ENTREGAR: 8**

---

### 📖 Documentación de Apoyo (NO ENTREGAR, SOLO CONSULTA)

| Archivo | Propósito | Leer Antes De |
|---------|-----------|---------------|
| `README.md` | Documentación completa del proyecto | Empezar a trabajar |
| `RESUMEN_EJECUTIVO.md` | Vista rápida del estado del proyecto | La presentación |
| `INSTRUCCIONES_PRESENTACION.md` | Guía paso a paso para presentar | La clase |
| `EJEMPLOS_ADICIONALES.md` | Casos de prueba extra | La demostración |
| `INDICE.md` | Este archivo - navegación | Cualquier momento |

---

### 🧪 Archivos de Prueba

| Archivo | Propósito |
|---------|-----------|
| `test_simulator.ps1` | Script de pruebas automáticas |

---

## 📊 ESTRUCTURA DE LECTURA RECOMENDADA

### Para Entender el Proyecto:
1. **`RESUMEN_EJECUTIVO.md`** ← Empieza aquí (5 min)
2. **`README.md`** ← Documentación completa (10 min)
3. **`DIAGRAMA_MAQUINA_TURING.md`** ← Detalles de la MT (15 min)
4. **`turing_machine_simulator.py`** ← Código fuente (30 min)

### Para Preparar la Presentación:
1. **`INSTRUCCIONES_PRESENTACION.md`** ← Guía de presentación (20 min)
2. **`RESUMEN_EJECUTIVO.md`** ← Checklist (5 min)
3. Ejecutar **`test_simulator.ps1`** ← Verificar funcionamiento (2 min)

### Para la Demostración en Clase:
- Tener abierto: **`INSTRUCCIONES_PRESENTACION.md`**
- Tener a mano: **`EJEMPLOS_ADICIONALES.md`** (por si piden más casos)

---

## 🎓 CONTENIDO POR ARCHIVO

### 1. `turing_machine_simulator.py`
**Contenido:**
- Clase `TuringMachine` completa
- Método `load_from_file()` - Carga especificaciones
- Método `validate_specification()` - Valida componentes
- Método `step()` - Ejecuta un paso de la MT
- Método `run()` - Ejecuta la simulación completa
- Método `save_output()` - Guarda configuraciones
- Función `main()` - Programa principal

**Lo que hace:**
- Simula una Máquina de Turing determinista
- Carga especificaciones desde archivo
- Valida la correctitud formal
- Genera configuraciones paso a paso
- Detecta aceptación, rechazo y ciclos infinitos

**Líneas de código:** ~400

---

### 2. `DIAGRAMA_MAQUINA_TURING.md`
**Contenido:**
- Descripción de la máquina diseñada
- Componentes formales (Q, Σ, Γ, δ, q0, B, F, R)
- Tabla de función de transición
- Diagrama visual en ASCII
- Ejemplos de ejecución paso a paso
- Explicación de la notación

**Máquina implementada:**
- Verifica si una cadena binaria tiene número PAR de 1's
- 5 estados: q0, q1, qloop, qaccept, qreject
- Alfabeto de entrada: {0, 1}
- Alfabeto de cinta: {0, 1, x, _}

---

### 3. Archivos de Entrada (`input_*.txt`)

#### `input_accept.txt`
```
Entrada: 0110
Resultado esperado: ACEPTA
Razón: 2 unos (par)
```

#### `input_reject.txt`
```
Entrada: 001
Resultado esperado: RECHAZA
Razón: 1 uno (impar)
```

#### `input_infinite.txt`
```
Entrada: 01x
Resultado esperado: CICLO_INFINITO
Razón: Símbolo 'x' causa ciclo
```

---

### 4. Archivos de Salida (`output_*.txt`)

Cada archivo contiene:
1. Especificación completa de la MT
2. Función de transición δ
3. Configuraciones paso a paso (formato: uqv)
4. Resultado final

**Formato de configuración:**
```
Paso 0: q00110
Paso 1: 0q0110
Paso 2: 01q110
...
```

---

### 5. `README.md`
**Secciones:**
- Descripción del proyecto
- Listado de archivos
- Instrucciones de uso
- Formato de entrada
- Descripción de la máquina
- Formato de salida
- Validaciones implementadas
- Checklist de entregables
- Características adicionales
- Pruebas rápidas

**Ideal para:** Documentación técnica completa

---

### 6. `RESUMEN_EJECUTIVO.md`
**Secciones:**
- Estado del proyecto
- Tabla de entregables
- Descripción del simulador
- Casos de prueba
- Resultados de pruebas
- Checklist de presentación
- Puntos clave para explicar
- Estructura de archivos
- Comandos rápidos

**Ideal para:** Vista rápida antes de presentar

---

### 7. `INSTRUCCIONES_PRESENTACION.md`
**Secciones:**
- Checklist pre-presentación
- Demostración paso a paso
- Puntos clave para explicar
- Configuraciones y transiciones
- Preguntas y respuestas
- Explicación del código
- Errores comunes a evitar
- Lista de verificación final
- Material de apoyo

**Ideal para:** Preparar la presentación en clase

---

### 8. `EJEMPLOS_ADICIONALES.md`
**Contiene:**
- 10 ejemplos de prueba diferentes
- Archivos de entrada completos
- Resultados esperados
- Tabla resumen
- Script para crear ejemplos
- Análisis de configuraciones
- Preguntas de demostración

**Ideal para:** Tener más casos de prueba listos

---

### 9. `test_simulator.ps1`
**Funciones:**
- Verifica instalación de Python
- Valida existencia de archivos
- Ejecuta los 3 casos principales
- Verifica resultados automáticamente
- Genera reporte de éxito/falla

**Uso:**
```powershell
powershell -ExecutionPolicy Bypass -File test_simulator.ps1
```

---

## 🎯 RUTA DE APRENDIZAJE

### Si tienes 1 hora:
1. Lee `RESUMEN_EJECUTIVO.md` (5 min)
2. Lee `README.md` (10 min)
3. Ejecuta `test_simulator.ps1` (2 min)
4. Revisa el código Python (20 min)
5. Lee `INSTRUCCIONES_PRESENTACION.md` (15 min)
6. Practica la demostración (8 min)

### Si tienes 30 minutos:
1. Lee `RESUMEN_EJECUTIVO.md` (5 min)
2. Ejecuta `test_simulator.ps1` (2 min)
3. Lee `INSTRUCCIONES_PRESENTACION.md` (15 min)
4. Practica comandos (8 min)

### Si tienes 10 minutos:
1. Lee `RESUMEN_EJECUTIVO.md` (5 min)
2. Ejecuta `test_simulator.ps1` (2 min)
3. Revisa checklist en `INSTRUCCIONES_PRESENTACION.md` (3 min)

---

## 📝 CHECKLIST FINAL

### Antes de Subir a Canvas:
- [ ] Los 8 archivos principales están listos
- [ ] Los archivos de salida se generaron correctamente
- [ ] El simulador ejecuta sin errores
- [ ] El código está comentado

### Antes de la Presentación:
- [ ] Python funciona (`python --version`)
- [ ] Todos los archivos en el directorio correcto
- [ ] `test_simulator.ps1` pasa todas las pruebas
- [ ] Laptop con batería cargada
- [ ] Backup en USB (opcional)

### Durante la Presentación:
- [ ] Explicar la máquina diseñada
- [ ] Ejecutar caso de aceptación
- [ ] Ejecutar caso de rechazo
- [ ] Ejecutar caso de ciclo infinito
- [ ] Mostrar archivos de salida
- [ ] Explicar configuraciones
- [ ] Responder preguntas sobre el código

---

## 🔍 BÚSQUEDA RÁPIDA

### ¿Cómo ejecutar el simulador?
→ Ver `README.md` sección "Cómo Usar el Simulador"

### ¿Cómo funciona la máquina?
→ Ver `DIAGRAMA_MAQUINA_TURING.md`

### ¿Qué decir en la presentación?
→ Ver `INSTRUCCIONES_PRESENTACION.md`

### ¿Qué archivos entregar?
→ Ver `RESUMEN_EJECUTIVO.md` tabla de entregables

### ¿Cómo crear más ejemplos?
→ Ver `EJEMPLOS_ADICIONALES.md`

### ¿Cómo probar todo funciona?
→ Ejecutar `test_simulator.ps1`

---

## 📞 RESOLUCIÓN DE PROBLEMAS

### Error: "Python no se reconoce..."
**Solución:** Instalar Python y agregarlo al PATH

### Error: "No se encuentra el archivo..."
**Solución:** Verificar que estás en el directorio correcto (`cd d:\UVG\Parcial4LM`)

### El simulador no termina
**Solución:** Normal para caso de ciclo infinito (espera hasta 10,000 pasos)

### Los archivos de salida no se generan
**Solución:** Verificar permisos de escritura y nombres correctos

---

## 🎉 ESTADO ACTUAL

✅ **PROYECTO 100% COMPLETO**

- Total de archivos creados: 14
- Archivos para entregar: 8
- Documentación de apoyo: 5
- Scripts de prueba: 1
- Todas las pruebas: PASANDO ✓

---

## 📚 REFERENCIAS RÁPIDAS

### Definición Formal
```
M = (Q, Σ, Γ, δ, q0, B, F, R)
```

### Notación de Configuraciones
```
uqv (ejemplo: 011q00)
```

### Función de Transición
```
δ(q, a) = (p, b, D)
```

### Comandos Principales
```powershell
# Ejecutar simulador
python turing_machine_simulator.py input.txt output.txt

# Pruebas automáticas
powershell -ExecutionPolicy Bypass -File test_simulator.ps1

# Ver salida
type output.txt
```

---

**¡Todo está listo para la presentación!** 🚀

**Última actualización:** Noviembre 6, 2025  
**Versión:** 1.0  
**Estado:** COMPLETO ✅
