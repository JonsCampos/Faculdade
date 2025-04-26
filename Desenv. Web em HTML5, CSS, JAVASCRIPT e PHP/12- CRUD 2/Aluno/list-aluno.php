<?php
require_once("../Service/Database.php");

$db = new Database();

try {

  
  /*
  $sql = "insert into user (email, password, name) values ('admin@teste', '123', 'usuario administrador')";
  $db->exec($sql);
*/
  $sql = "select distinct * from aluno";
  $result = $db->query($sql);

  echo "<table border='1'>";
  echo "<tr>
  <td>Matricula</td>
  <td>Nome</td>
  <td> Disciplina </td>
  <td>Nota Final</td>
  <td>Data criação</td>
  <td></td><td></td></tr>";
  foreach($result as $row) {
    echo "<tr>";
    echo "<td>".$row['matricula']."</td>";
    echo "<td>".$row['nome']."</td>";
    echo "<td>".$row['disciplina']."</td>";
    echo "<td>".$row['nota_final']."</td>";
    echo "<td>".$row['data_criacao']."</td>";
  
    echo "<td><a href=delete-aluno.php?id=".$row['id'].">Deletar</a></td>";

     echo "<td><a href=update-aluno-form.php?id=".$row['id'].">Atualizar</a></td>";
    
    echo "</tr>";
  
  }
  echo "</table>";
  echo "<br>";
  echo "<a href='../index.php'>Voltar</a>";
  echo "<br>";
  echo "<a href='add-aluno-form.php'>Novo Aluno</a>";
  
}catch (PDOException $e) {
   echo $ex->getMessage();
}






?>