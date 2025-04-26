<?php
require_once("../Service/Database.php");

$db = new Database();

try {

  
  /*
  $sql = "insert into user (email, password, name) values ('admin@teste', '123', 'usuario administrador')";
  $db->exec($sql);
*/
  $sql = "select distinct * from user";
  $result = $db->query($sql);

  echo "<table border='1'>";
  echo "<tr><td>Email</td><td>Senha</td><td>Nome</td><td></td><td></td></tr>";
  foreach($result as $row) {
    echo "<tr>";
    echo "<td>".$row['email']."</td>";
    echo "<td>".$row['password']."</td>";
    echo "<td>".$row['name']."</td>";
  
    echo "<td><a href=delete-user.php?id=".$row['id'].">Deletar</a></td>";

     echo "<td><a href=update-user-form.php?id=".$row['id'].">Atualizar</a></td>";
    
    echo "</tr>";
  
  }
  echo "</table>";
  echo "<br>";
  echo "<a href='../index.php'>Voltar</a>";
  echo "<br>";
  echo "<a href='add-user-form.php'>Novo Usuário</a>";
  
}catch (PDOException $e) {
   echo $ex->getMessage();
}






?>