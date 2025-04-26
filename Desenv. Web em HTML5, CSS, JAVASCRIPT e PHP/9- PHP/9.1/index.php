<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
   teste
    <script>
      //javascript
      let senha = 123;
      let valor1=5;
      let valor2 = 6;
      let media = (valor1+valor2)/2;
      if (media>2) {
        alert('Media = '+media);
      }
    </script>
    <?php
      //linguagem php
      $senha=456;

      echo "<h1>oi mundo</h1>";
      echo "<p> sua senha é $senha </p>";
      $v1=8;
      $v2=9;
      $media=($v1+$v2)/2;
      if ($media>2) {
        echo "<p>Media = $media</p>";
      }
     ?>
  </body>
  </body>
</html>
