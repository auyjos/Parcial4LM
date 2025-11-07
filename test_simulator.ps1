# Script de Prueba Automatica del Simulador de Maquina de Turing

Write-Host '============================================================' -ForegroundColor Cyan
Write-Host 'PRUEBA AUTOMATICA - SIMULADOR DE MAQUINA DE TURING' -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''

$totalTests = 0
$passedTests = 0

function Test-TuringMachine {
    param(
        [string]$inputFile,
        [string]$outputFile,
        [string]$expectedResult,
        [string]$testName
    )
    
    $script:totalTests++
    
    Write-Host "Test $totalTests : $testName" -ForegroundColor Yellow
    Write-Host "  Entrada: $inputFile" -ForegroundColor Gray
    Write-Host "  Esperado: $expectedResult" -ForegroundColor Gray
    
    python turing_machine_simulator.py $inputFile $outputFile 2>&1 | Out-Null
    
    if (Test-Path $outputFile) {
        Write-Host '  OK Archivo generado' -ForegroundColor Green
        $content = Get-Content $outputFile -Raw
        
        if ($content -match "RESULTADO: $expectedResult") {
            Write-Host "  OK Resultado correcto" -ForegroundColor Green
            $script:passedTests++
            Write-Host '  PASS' -ForegroundColor Green
        }
        else {
            Write-Host '  ERROR Resultado incorrecto' -ForegroundColor Red
            Write-Host '  FAIL' -ForegroundColor Red
        }
    }
    else {
        Write-Host '  ERROR Archivo no generado' -ForegroundColor Red
        Write-Host '  FAIL' -ForegroundColor Red
    }
    Write-Host ''
}

Write-Host 'Verificando Python...' -ForegroundColor Cyan
python --version
Write-Host ''

if (Test-Path 'turing_machine_simulator.py') {
    Write-Host 'OK Simulador encontrado' -ForegroundColor Green
}
else {
    Write-Host 'ERROR Simulador no encontrado' -ForegroundColor Red
    exit 1
}
Write-Host ''

Write-Host '============================================================' -ForegroundColor Cyan
Write-Host 'EJECUTANDO PRUEBAS' -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''

Test-TuringMachine 'inputs\input_accept.txt' 'outputs\output_accept.txt' 'ACEPTA' 'Caso de Aceptacion'
Test-TuringMachine 'inputs\input_reject.txt' 'outputs\output_reject.txt' 'RECHAZA' 'Caso de Rechazo'
Test-TuringMachine 'inputs\input_infinite.txt' 'outputs\output_infinite.txt' 'CICLO_INFINITO' 'Caso Ciclo Infinito'

Write-Host '============================================================' -ForegroundColor Cyan
Write-Host 'RESUMEN' -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''
Write-Host "Total: $totalTests" -ForegroundColor White
Write-Host "Exitosas: $passedTests" -ForegroundColor Green
Write-Host "Fallidas: $($totalTests - $passedTests)" -ForegroundColor Red
Write-Host ''

if ($passedTests -eq $totalTests) {
    Write-Host 'TODAS LAS PRUEBAS PASARON' -ForegroundColor Green
}
else {
    Write-Host 'ALGUNAS PRUEBAS FALLARON' -ForegroundColor Red
}
Write-Host ''
