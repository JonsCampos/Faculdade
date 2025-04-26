<html>
  <head>
    <title>Cadastro de Alunos </title>
  </head>
  <body>

    <form action="update-aluno.php" method="get">
      <?php
      
      $id = $_GET['id'];
      echo "<input type='hidden' name='id' value='$id'>";

      require_once("../Service/Database.php");

      $db = new Database();
      $sql = "select distinct * from aluno where id = '$id'";
      $result = $db->query($sql);
      $data = $result->fetch();

     echo '<label for="matricula" >Matricula</label>
      <input type="matricula" name="matricula" id="matricula" 
      value="'.$data['matricula'].'" required>
      <br>
      <br>
      <label for="nome" >Nome</label>
      <input type="nome" name="nome" id="nome"
       value="'.$data['nome'].'"
      required>
      <br>
      <br>
      <label for="disciplina" >Disciplina</label>
      <input type="disciplina" name="disciplina" id="disciplina" 
       value="'.$data['disciplina'].'"
      required>
      <br>
      <br>
      <label for="nota_final" >Nota final</label>
      <input type="nota_final" name="nota_final" id="nota_final"
       value="'.$data['nota_final'].'"
      required>
      <br>
      <br>
      <input type="submit" value="Atualizar">
    </form>';

       ?>
      
  </body>
  
</html>