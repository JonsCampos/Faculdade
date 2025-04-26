<?php
session_start();
if (!isset($_SESSION["autenticado"])) {
    echo '
    <script>
    window.location.replace("index.php");
    </script>
    ';
}
?>
<h1> Parabéns voce está autenticado</h1>