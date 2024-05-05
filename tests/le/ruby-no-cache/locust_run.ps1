$OutputEncoding = [System.Text.Encoding]::UTF8

$locustFile = "..\..\..\locust_scripts\locustfile_linkextractor.py"
$qtdUsuarios = @("30", "60", "90")

for ($i = 0; $i -lt $qtdUsuarios.Length; $i++) {
  $qtdUsuario = $qtdUsuarios[$i]
  $outputDir = ".\$qtdUsuario\rst"
  $spawnRate = [int]::Parse($qtdUsuario) / 10

  $command = "locust -f $locustFile --csv $outputDir -u $qtdUsuario -r $spawnRate --headless -t5m"
  Write-Output "Executando teste com $qtdUsuario usuários: $command"

  Invoke-Expression $command *> $null

  Write-Output "Teste com duração de 5 minutos executado com sucesso em $outputDir"
}