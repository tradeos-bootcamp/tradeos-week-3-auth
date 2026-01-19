
Скрипт проверки структуры проекта
Write-Host "Проверка структуры проекта..." -ForegroundColor Cyan

$requiredFiles = @(
"app_init_.py",
"app\main.py",
"app\database.py",
"app\models_init_.py",
"app\models\user.py",
"app\models\product.py",
"app\schemas_init_.py",
"app\schemas\user.py",
"app\schemas\product.py",
"app\crud_init_.py",
"app\crud\user.py",
"app\crud\product.py",
"app\core_init_.py",
"app\core\config.py",
"app\core\security.py",
"app\api_init_.py",
"app\api\deps.py",
"app\api\v1_init_.py",
"app\api\v1\api.py",
"app\api\v1\endpoints_init_.py",
"app\api\v1\endpoints\auth.py",
"app\api\v1\endpoints\products.py",
"requirements.txt",
".env.example",
"docker-compose.yml",
"README.md",
"tests_init_.py",
"tests\test_auth.py",
"scripts\create_admin.py"
)

$missingFiles = @()

foreach ($file in $requiredFiles) {
if (!(Test-Path $file)) {
$missingFiles += $file
Write-Host "✗ Отсутствует: $file" -ForegroundColor Red
} else {
Write-Host "✓ Найден: $file" -ForegroundColor Green
}
}

if ($missingFiles.Count -eq 0) {
Write-Host "n✅ Все файлы на месте! Структура проекта корректна." -ForegroundColor Green } else { Write-Host "n⚠️ Отсутствуют файлы: $($missingFiles.Count)" -ForegroundColor Yellow
Write-Host "Создайте отсутствующие файлы:" -ForegroundColor White
foreach ($file in $missingFiles) {
Write-Host " - $file" -ForegroundColor Cyan
}
}
