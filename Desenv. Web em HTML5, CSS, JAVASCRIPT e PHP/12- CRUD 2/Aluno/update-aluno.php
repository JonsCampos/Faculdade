<?php
require_once("../Service/Database.php");

$db = new Database();

$id = $_GET['id'];
$matricula = $_GET['matricula'];
$nome = $_GET['nome'];
$disciplina = $_GET['disciplina'];
$nota_final = $_GET['nota_final'];

//var_dump($_GET);
try {

  $sql = "update aluno set nome='$nome', matricula='$matricula',
              disciplina='$disciplina',
              nota_final='$nota_final'
              where id = '$id'
              ";
//echo "$sql";
  
 $db->exec($sql);
  
 echo "<script>
  window.location.replace('list-aluno.php');
  </script>";
  
}catch(PDOException $e ) {
  var_dump($e->getMessage());
}


