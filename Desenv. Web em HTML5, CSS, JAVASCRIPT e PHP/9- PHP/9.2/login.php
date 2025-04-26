<?php
//var_dump($_GET);
$login=$_GET['campoLogin'];
$senha=$_GET["campoSenha"];


/*
echo "
<p>Login: $login</p>

<p>Senha: $senha</p>

";
*/

if ($login=='admin@teste' && $senha==123) {
  echo "<p> Parabéns vc foi autenticado</p>";
}else{
  echo "<p>Ocorreu um erro</p>";
}

?>