<?php
session_start();
if (! isset($_SESSION['autenticado'])) {
  echo '<script>
  window.location.replace("index.php");
  </script>';
}

?>
<html>
  <head>
    <title>Tela de menu</title>
  </head>
  <body>
    <h1>Parabéns vc foi autenticado e está na tela de menu</h1>
  </body>
</html>

