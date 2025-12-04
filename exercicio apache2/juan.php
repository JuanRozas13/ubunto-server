<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Desafio Linux Ubunto</title>
<style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .box { border: 1px solid #ccc; padding: 20px; margin: 20px auto; max-width: 600px; background-color: #f9f9f9; }
        h1 { color: #4B0082; }
</style>
</head>
<body>
 
    <h1> Página PHP do Juan</h1>
 
    <div class="box">
<h3>Teste das Funções PHP</h3>
<?php 
            // FUNÇÃO 1 (NOVA): DATE - Mostra a data e hora do servidor
            // O formato 'd/m/Y H:i:s' significa Dia/Mês/Ano Hora:Minuto:Segundo
            echo "<p><strong>Data e Hora atual:</strong> " . date('d/m/Y H:i:s') . "</p>";
            echo "<hr>";
 
            // FUNÇÃO 2: Converte texto para Maiúsculo
            $nome = "Juan Rozas ";
            echo "<p>Meu nome em minúsculo: $nome</p>";
            echo "<p>Meu nome com <strong>strtoupper</strong>: " . strtoupper($nome) . "</p>";
        ?>
</div>
 
    <br>
<button onclick="window.location.href='index.html'">⬅️ Voltar para o Site Principal (HTML)</button>
 
</body>
</html>
