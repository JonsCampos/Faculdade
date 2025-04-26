<html>
  <head>
    <title>Cadastro de Alunos </title>
  </head>
  <body>

    <form action="add-aluno.php" method="get">
      <label for="matricula" >Matricula</label>
      <input type="matricula" name="matricula" id="matricula" required>
      <br>
      <br>
      <label for="nome" >Nome</label>
      <input type="nome" name="nome" id="nome" required>
      <br>
      <br>
      <label for="disciplina" >Disciplina</label>
      <input type="disciplina" name="disciplina" id="disciplina" required>
      <br>
      <br>
      <label for="nota_final" >Nota final</label>
      <input type="nota_final" name="nota_final" id="nota_final" required>
      <br>
      <br>
      <input type="submit" value="Adicionar">
    </form>
  </body>
  
</html>