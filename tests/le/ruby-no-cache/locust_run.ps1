$locustFile = "..\..\..\locust_scripts\locustfile_linkextractor.py"
$qtdUsuarios = @("30", "60", "90")

for ($i = 0; $i -lt $qtdUsuarios.Length; $i++) {
  $qtdUsuario = $qtdUsuarios[$i]
  $outputDir = ".\$qtdUsuario\rst"

  $command = "locust -f $locustFile --csv $outputDir --headless -t5m"

  Invoke-Expression $command *> $null

  Write-Output "Teste com duração de 5 minutos executado com sucesso em $outputDir"
}