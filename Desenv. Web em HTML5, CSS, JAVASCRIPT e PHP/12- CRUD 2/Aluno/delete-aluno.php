<?php
require_once("../Service/Database.php");

$db = new Database();

$id = $_GET['id'];

$sql = "delete from aluno where id = $id";

$db->exec($sql);

echo "<script>
window.location.replace('list-aluno.php');
</script>";