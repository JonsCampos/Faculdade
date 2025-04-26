<html>
  <head>
    <title>Cadastro de usuários </title>
  </head>
  <body>

    <form action="update-user.php" method="get">
      <?php
      
      $id = $_GET['id'];
      echo "<input type='hidden' name='id' value='$id'>";

      require_once("../Service/Database.php");

      $db = new Database();
      $sql = "select distinct * from user where id = '$id'";
      $result = $db->query($sql);
      $data = $result->fetch();

     echo '<label for="email" >Email</label>
      
      <input type="email" name="email" id="email" 
      value='.$data['email'].' required>
      <br>
      <br>
      <label for="name" >Nome</label>
      <input type="name" name="name" id="name"
      value='.$data['name'].' required>
      <br>
      <br>
      <label for="password" >Senha</label>
      <input type="password" name="password" id="password"
      value='.$data['password'].' required>
      <br>
      <br>
      <input type="submit" value="Atualizar">
      </form>';

       ?>
      
  </body>
  
</html>