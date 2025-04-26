<?php
require_once("../Service/Database.php");

$db = new Database();

$matricula = $_GET['matricula'];
$nome = $_GET['nome'];
$disciplina = $_GET['disciplina'];
$nota_final = $_GET['nota_final'];
$data_criacao = date('Y-m-d H:i:s');

//var_dump($_GET);
try {

  // SQL 
  $res = $db->exec(
    "CREATE TABLE IF NOT EXISTS aluno (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      matricula TEXT, 
      nome TEXT,
      disciplina TEXT,
      nota_final numeric,
      data_criacao time
    )"
  );

  $sql = "INSERT INTO aluno (matricula, nome, disciplina, nota_final, data_criacao) 
          VALUES ('$matricula', '$nome',  '$disciplina', '$nota_final', '$data_criacao')";

 $db->exec($sql);
  
  echo "<script>
  window.location.replace('list-aluno.php');
  </script>";
  
}catch(PDOException $e ) {
  var_dump($e->getMessage());
}


