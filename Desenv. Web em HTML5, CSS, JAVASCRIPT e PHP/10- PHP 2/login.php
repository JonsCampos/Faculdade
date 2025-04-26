<?php
session_start();

//var_dump($_POST);

$login=$_POST['campoLogin'];
$senha=$_POST["campoSenha"];

/*
echo "
<p>Login: $login</p>

<p>Senha: $senha</p>

";
*/

if ($login=='admin@teste' && $senha==123) {
  $_SESSION['autenticado']=true;
  echo '<script>
  window.location.replace("menu.php");
  </script>';
}else{
  unset($_SESSION['autenticado']);
  echo '<script>
  window.location.replace("index.php");
  </script>';
}

?>