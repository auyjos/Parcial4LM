"""
Simulador de Máquina de Turing Determinista
Autor: [Tu Nombre]
Fecha: Noviembre 2025

Este programa simula una máquina de Turing determinista según la notación vista en clase.
"""

import sys
from typing import Dict, List, Optional, Set, Tuple


class TuringMachine:
    """
    Clase que representa una Máquina de Turing Determinista.
    
    Notación:
    - M = (Q, Σ, Γ, δ, q0, B, F, R)
    - Q: conjunto de estados
    - Σ: alfabeto de entrada
    - Γ: alfabeto de la cinta
    - δ: función de transición Q × Γ → Q × Γ × {L, R}
    - q0: estado inicial
    - B: símbolo blanco
    - F: estados de aceptación
    - R: estados de rechazo
    """
    
    def __init__(self):
        self.Q: Set[str] = set()  # Estados
        self.sigma: Set[str] = set()  # Alfabeto de entrada
        self.gamma: Set[str] = set()  # Alfabeto de la cinta
        self.delta: Dict[Tuple[str, str], Tuple[str, str, str]] = {}  # Función de transición
        self.q0: str = ""  # Estado inicial
        self.B: str = "_"  # Símbolo blanco
        self.F: Set[str] = set()  # Estados de aceptación
        self.R: Set[str] = set()  # Estados de rechazo
        self.tape: List[str] = []  # Cinta
        self.head_position: int = 0  # Posición del cabezal
        self.current_state: str = ""  # Estado actual
        self.configurations: List[str] = []  # Configuraciones
        self.max_steps: int = 10000  # Límite para detectar ciclos infinitos
        
    def load_from_file(self, filename: str) -> bool:
        """
        Carga la especificación de la máquina de Turing desde un archivo.
        
        Formato del archivo:
        Q: q0,q1,q2,...
        Sigma: a,b,c,...
        Gamma: a,b,c,_,...
        q0: estado_inicial
        B: _
        F: qf1,qf2,...
        R: qr1,qr2,...
        Delta:
        q0,a,q1,b,R
        q1,b,q2,c,L
        ...
        Input: cadena_entrada
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            i = 0
            while i < len(lines):
                line = lines[i]
                
                if line.startswith('Q:'):
                    self.Q = set(line[2:].strip().split(','))
                
                elif line.startswith('Sigma:'):
                    self.sigma = set(line[6:].strip().split(','))
                
                elif line.startswith('Gamma:'):
                    self.gamma = set(line[6:].strip().split(','))
                
                elif line.startswith('q0:'):
                    self.q0 = line[3:].strip()
                
                elif line.startswith('B:'):
                    self.B = line[2:].strip()
                
                elif line.startswith('F:'):
                    states = line[2:].strip()
                    self.F = set(states.split(',')) if states else set()
                
                elif line.startswith('R:'):
                    states = line[2:].strip()
                    self.R = set(states.split(',')) if states else set()
                
                elif line.startswith('Delta:'):
                    i += 1
                    while i < len(lines) and not lines[i].startswith('Input:'):
                        delta_line = lines[i].strip()
                        if delta_line:
                            parts = delta_line.split(',')
                            if len(parts) == 5:
                                q_current, symbol_read, q_next, symbol_write, direction = parts
                                self.delta[(q_current.strip(), symbol_read.strip())] = (
                                    q_next.strip(), 
                                    symbol_write.strip(), 
                                    direction.strip()
                                )
                        i += 1
                    i -= 1
                
                elif line.startswith('Input:'):
                    input_str = line[6:].strip()
                    self.initialize_tape(input_str)
                
                i += 1
            
            return self.validate_specification()
            
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return False
    
    def validate_specification(self) -> bool:
        """Valida que la especificación de la máquina sea correcta."""
        errors = []
        
        # Validar que Q no esté vacío
        if not self.Q:
            errors.append("El conjunto de estados Q está vacío")
        
        # Validar que el estado inicial esté en Q
        if self.q0 not in self.Q:
            errors.append(f"El estado inicial '{self.q0}' no está en Q")
        
        # Validar que Sigma esté contenido en Gamma
        if not self.sigma.issubset(self.gamma):
            errors.append("El alfabeto de entrada Σ no está contenido en Γ")
        
        # Validar que el símbolo blanco esté en Gamma
        if self.B not in self.gamma:
            errors.append(f"El símbolo blanco '{self.B}' no está en Γ")
        
        # Validar que F y R estén contenidos en Q
        if not self.F.issubset(self.Q):
            errors.append("Los estados de aceptación F no están contenidos en Q")
        
        if not self.R.issubset(self.Q):
            errors.append("Los estados de rechazo R no están contenidos en Q")
        
        # Validar que F y R sean disjuntos
        if self.F.intersection(self.R):
            errors.append("Los conjuntos F y R no son disjuntos")
        
        # Validar función de transición
        for (q, symbol), (q_next, symbol_write, direction) in self.delta.items():
            if q not in self.Q:
                errors.append(f"Estado '{q}' en δ no está en Q")
            if symbol not in self.gamma:
                errors.append(f"Símbolo '{symbol}' en δ no está en Γ")
            if q_next not in self.Q:
                errors.append(f"Estado siguiente '{q_next}' en δ no está en Q")
            if symbol_write not in self.gamma:
                errors.append(f"Símbolo a escribir '{symbol_write}' en δ no está en Γ")
            if direction not in ['L', 'R']:
                errors.append(f"Dirección '{direction}' debe ser 'L' o 'R'")
        
        if errors:
            print("Errores en la especificación:")
            for error in errors:
                print(f"  - {error}")
            return False
        
        print("✓ Especificación válida")
        return True
    
    def initialize_tape(self, input_str: str):
        """Inicializa la cinta con la cadena de entrada."""
        if input_str:
            self.tape = list(input_str)
        else:
            self.tape = [self.B]
        self.head_position = 0
        self.current_state = self.q0
        self.configurations = []
    
    def get_configuration(self) -> str:
        """
        Retorna la configuración actual en la notación de clase.
        Formato: q0w (estado + contenido de la cinta desde el cabezal)
        o bien: uqv donde u es lo leído, q es el estado, v es lo que falta por leer
        """
        # Asegurar que hay suficiente cinta
        while len(self.tape) <= self.head_position:
            self.tape.append(self.B)
        
        # Construir la configuración: parte_izquierda + estado + parte_derecha
        left_part = ''.join(self.tape[:self.head_position])
        right_part = ''.join(self.tape[self.head_position:])
        
        # Eliminar blancos innecesarios al final
        right_part = right_part.rstrip(self.B)
        if not right_part:
            right_part = self.B
        
        configuration = f"{left_part}{self.current_state}{right_part}"
        return configuration
    
    def step(self) -> bool:
        """
        Ejecuta un paso de la máquina de Turing.
        Retorna True si puede continuar, False si debe detenerse.
        """
        # Asegurar que hay suficiente cinta
        while len(self.tape) <= self.head_position:
            self.tape.append(self.B)
        
        # Leer símbolo actual
        current_symbol = self.tape[self.head_position]
        
        # Verificar si estamos en un estado de aceptación o rechazo
        if self.current_state in self.F:
            return False  # Estado de aceptación
        
        if self.current_state in self.R:
            return False  # Estado de rechazo
        
        # Buscar transición
        key = (self.current_state, current_symbol)
        if key not in self.delta:
            # No hay transición definida -> estado de rechazo implícito
            return False
        
        # Aplicar transición
        next_state, write_symbol, direction = self.delta[key]
        
        # Escribir en la cinta
        self.tape[self.head_position] = write_symbol
        
        # Cambiar estado
        self.current_state = next_state
        
        # Mover cabezal
        if direction == 'R':
            self.head_position += 1
        elif direction == 'L':
            self.head_position -= 1
            if self.head_position < 0:
                # Expandir cinta a la izquierda
                self.tape.insert(0, self.B)
                self.head_position = 0
        
        return True
    
    def run(self) -> Tuple[str, List[str]]:
        """
        Ejecuta la máquina de Turing y retorna el resultado.
        Retorna: (resultado, configuraciones)
        - resultado: "ACEPTA", "RECHAZA", o "CICLO_INFINITO"
        """
        self.configurations = []
        steps = 0
        
        # Agregar configuración inicial
        self.configurations.append(self.get_configuration())
        
        while steps < self.max_steps:
            can_continue = self.step()
            
            # Agregar configuración actual
            self.configurations.append(self.get_configuration())
            
            if not can_continue:
                # Determinar si aceptó o rechazó
                if self.current_state in self.F:
                    return "ACEPTA", self.configurations
                else:
                    return "RECHAZA", self.configurations
            
            steps += 1
        
        # Se alcanzó el límite de pasos
        return "CICLO_INFINITO", self.configurations
    
    def save_output(self, filename: str, result: str):
        """Guarda las configuraciones en un archivo de salida."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("SIMULACIÓN DE MÁQUINA DE TURING\n")
                f.write("=" * 60 + "\n\n")
                
                f.write("ESPECIFICACIÓN DE LA MÁQUINA:\n")
                f.write(f"Q = {{{', '.join(sorted(self.Q))}}}\n")
                f.write(f"Σ = {{{', '.join(sorted(self.sigma))}}}\n")
                f.write(f"Γ = {{{', '.join(sorted(self.gamma))}}}\n")
                f.write(f"q0 = {self.q0}\n")
                f.write(f"B = {self.B}\n")
                f.write(f"F = {{{', '.join(sorted(self.F))}}}\n")
                f.write(f"R = {{{', '.join(sorted(self.R))}}}\n\n")
                
                f.write("FUNCIÓN DE TRANSICIÓN δ:\n")
                for (q, symbol), (q_next, symbol_write, direction) in sorted(self.delta.items()):
                    f.write(f"  δ({q}, {symbol}) = ({q_next}, {symbol_write}, {direction})\n")
                f.write("\n")
                
                f.write("=" * 60 + "\n")
                f.write("CONFIGURACIONES:\n")
                f.write("=" * 60 + "\n\n")
                
                for i, config in enumerate(self.configurations):
                    f.write(f"Paso {i}: {config}\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write(f"RESULTADO: {result}\n")
                f.write("=" * 60 + "\n")
                
                if result == "CICLO_INFINITO":
                    f.write(f"\nNOTA: Se detectó un posible ciclo infinito después de {self.max_steps} pasos.\n")
                    f.write("Se muestran las primeras configuraciones.\n")
            
            print(f"✓ Archivo de salida guardado: {filename}")
            
        except Exception as e:
            print(f"Error al guardar el archivo de salida: {e}")


def main():
    """Función principal del programa."""
    print("=" * 60)
    print("SIMULADOR DE MÁQUINA DE TURING DETERMINISTA")
    print("=" * 60)
    print()
    
    # Verificar argumentos
    if len(sys.argv) < 2:
        print("Uso: python turing_machine_simulator.py <archivo_entrada> [archivo_salida]")
        print("\nEjemplo:")
        print("  python turing_machine_simulator.py inputs/input_accept.txt outputs/output_accept.txt")
        print("  python turing_machine_simulator.py inputs\\input_accept.txt outputs\\output_accept.txt")
        return
    
    input_filename = sys.argv[1]
    
    # Si no se proporciona archivo de salida, inferir del nombre de entrada
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
    else:
        # Inferir nombre de salida basado en entrada
        import os
        base_name = os.path.basename(input_filename)
        if base_name.startswith('input_'):
            output_name = base_name.replace('input_', 'output_')
            output_filename = os.path.join('outputs', output_name)
        else:
            output_filename = "outputs/output.txt"
    
    # Crear máquina de Turing
    tm = TuringMachine()
    
    # Cargar especificación
    print(f"Cargando especificación desde: {input_filename}")
    if not tm.load_from_file(input_filename):
        print("❌ Error: La especificación no es válida")
        return
    
    print()
    print("Ejecutando máquina de Turing...")
    print()
    
    # Ejecutar máquina
    result, configurations = tm.run()
    
    # Mostrar resultado
    print(f"Resultado: {result}")
    print(f"Número de pasos: {len(configurations) - 1}")
    
    # Guardar salida
    tm.save_output(output_filename, result)
    
    print()
    print("✓ Simulación completada")


if __name__ == "__main__":
    main()
