<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
  <body>

<div class="container">
  <form action="login.php" method="post">
    <div class="mb-3">
      <label for="login" class="form-label">Login</label>
      <input type="email" class="form-control" 
        id="login" placeholder="name@example.com"
        name="campoLogin">
    </div>
  <div class="mb-3">
    <label for="senha" class="form-label">Senha</label>
    <input type="password" class="form-control" 
      id="senha" 
      name="campoSenha"
      >
  </div>
   <input type="submit" class="btn btn-primary">
  </form>
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  </body>
</html>
