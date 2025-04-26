function calcular(){
  console.log('entrou na funcao');
  let valor1= document.getElementById('valor1').value;
  console.log(valor1);
  
  let valor2= document.getElementById('valor2').value;
  console.log(valor2);

  let media=( parseFloat(valor1)+parseFloat(valor2) ) / 2;
  console.log(media);

  document.getElementById("resultado").innerHTML = "Media = "+media;
}

function soma() {
  let valor1 = parseInt(document.getElementById("valor1").value);
  let valor2 = parseInt(document.getElementById("valor2").value);
  let resultado = valor1+valor2;
  document.getElementById("resultado").value = resultado;
}

function subtracao() {
  let valor1 = parseInt(document.getElementById("valor1").value);
  let valor2 = parseInt(document.getElementById("valor2").value);
  let resultado = valor1-valor2;
  document.getElementById("resultado").value = resultado;

}

function multiplicacao() {
  let valor1 = parseInt(document.getElementById("valor1").value);
  let valor2 = parseInt(document.getElementById("valor2").value);
  let resultado = valor1*valor2;
  document.getElementById("resultado").value = resultado;

}

function divisao() {
  let valor1 = parseInt(document.getElementById("valor1").value);
  let valor2 = parseInt(document.getElementById("valor2").value);
  let resultado = valor1/valor2;
  document.getElementById("resultado").value = resultado;

}

