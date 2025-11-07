# Script para ejecutar todos los ejemplos de prueba

Write-Host '============================================================' -ForegroundColor Cyan
Write-Host 'EJECUTAR TODOS LOS EJEMPLOS' -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''

# Lista de todos los archivos de entrada
$ejemplos = @(
    @{Nombre = 'Aceptacion - 0110'; Input = 'input_accept.txt'; Esperado = 'ACEPTA' },
    @{Nombre = 'Rechazo - 001'; Input = 'input_reject.txt'; Esperado = 'RECHAZA' },
    @{Nombre = 'Ciclo Infinito - 01x'; Input = 'input_infinite.txt'; Esperado = 'CICLO_INFINITO' },
    @{Nombre = 'Cadena Vacia'; Input = 'input_empty.txt'; Esperado = 'ACEPTA' },
    @{Nombre = 'Solo Ceros - 0000'; Input = 'input_zeros.txt'; Esperado = 'ACEPTA' },
    @{Nombre = 'Cuatro Unos - 11001100'; Input = 'input_four_ones.txt'; Esperado = 'ACEPTA' },
    @{Nombre = 'Tres Unos - 111'; Input = 'input_three_ones.txt'; Esperado = 'RECHAZA' },
    @{Nombre = 'Alternando - 10101'; Input = 'input_alternating.txt'; Esperado = 'RECHAZA' },
    @{Nombre = 'X al Final - 1111x'; Input = 'input_x_end.txt'; Esperado = 'CICLO_INFINITO' },
    @{Nombre = 'Solo X'; Input = 'input_only_x.txt'; Esperado = 'CICLO_INFINITO' }
)

$total = 0
$exitosos = 0

foreach ($ejemplo in $ejemplos) {
    $total++
    $inputPath = "inputs\$($ejemplo.Input)"
    $outputPath = "outputs\$($ejemplo.Input.Replace('input_', 'output_'))"
    
    Write-Host "[$total/$($ejemplos.Count)] $($ejemplo.Nombre)" -ForegroundColor Yellow
    Write-Host "  Archivo: $inputPath" -ForegroundColor Gray
    
    if (-not (Test-Path $inputPath)) {
        Write-Host "  ERROR: Archivo de entrada no existe" -ForegroundColor Red
        Write-Host ''
        continue
    }
    
    # Ejecutar simulador
    Write-Host "  Ejecutando..." -ForegroundColor Gray
    python turing_machine_simulator.py $inputPath $outputPath 2>&1 | Out-Null
    
    if (Test-Path $outputPath) {
        $content = Get-Content $outputPath -Raw
        if ($content -match "RESULTADO: $($ejemplo.Esperado)") {
            Write-Host "  OK Resultado: $($ejemplo.Esperado)" -ForegroundColor Green
            $exitosos++
        }
        else {
            Write-Host "  ERROR: Resultado incorrecto" -ForegroundColor Red
        }
    }
    else {
        Write-Host "  ERROR: No se genero archivo de salida" -ForegroundColor Red
    }
    
    Write-Host ''
}

Write-Host '============================================================' -ForegroundColor Cyan
Write-Host 'RESUMEN FINAL' -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''
Write-Host "Total de ejemplos: $total" -ForegroundColor White
Write-Host "Exitosos: $exitosos" -ForegroundColor Green
Write-Host "Fallidos: $($total - $exitosos)" -ForegroundColor Red
Write-Host ''

if ($exitosos -eq $total) {
    Write-Host 'TODOS LOS EJEMPLOS PASARON EXITOSAMENTE' -ForegroundColor Green
    Write-Host ''
    Write-Host 'Archivos generados en: outputs\' -ForegroundColor Cyan
}
else {
    Write-Host 'ALGUNOS EJEMPLOS FALLARON' -ForegroundColor Red
}
Write-Host ''
