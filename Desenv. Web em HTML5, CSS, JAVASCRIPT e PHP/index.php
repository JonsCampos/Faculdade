<?php
/**
Criar um sistema para ler nome, duas notas e calcular a media de um aluno.
Conceito SOLID.
https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530

*/

class Pessoa {
  private $nome;
  private $nota1;
  private $nota2;
  private $nota3;
  
  public function getNome(){
    return $this->nome;
  }
  public function  setNome($nome){
    $this->nome = $nome;
  }
  public function  getNota1(){
    return $this->nota1;
  }
  public function  setNota1($nota){
    $this->nota1 = $nota;
  }

  public function  getNota2(){
    return $this->nota2;
  }
  
  public function  setNota2($nota){
    $this->nota2 = $nota;
  }

  public function  getNota3(){
    return $this->nota3;
  }
  public function  setNota3($nota){
    $this->nota3 = $nota;
  }
  
  public function getMedia() {
   return (($this->nota1+$this->nota2)/2);
  }
  public function getMedia2() {
   return (($this->nota1+$this->nota2+$this->nota3)/3);
  }
}
$aluno = new Pessoa() ;
$aluno->setNome('Andre');
$aluno->setNota1(2.5);
$aluno->setNota2(5);
  //echo "<br>" . $aluno->getMedia();

$aluno2 = new Pessoa() ;
  $aluno2->setNome('Lucas');
  $aluno2->setNota1(10);
  $aluno2->setNota2(8);
//echo "<br>" .$aluno2->getMedia();

//----------------------------
//principio manter a classe simples
class Pessoa2 {
  private $nome;
  public function getNome(){
    return $this->nome;
  }
  public function setNome($nome){
    $this->nome = $nome;
  }
}
//4-principio de segregação
interface MediaTemplate {
  public function getMedia();
  public function getNota1();
  public function getNota2();
  public function setNota1($nota);
  public function setNota2($nota);
} 

class Media implements MediaTemplate {
  private $nota1;
  private $nota2;

  public function getNota1(){
    return $this->nota1;
  }
  public function setNota1($nota){
    $this->nota1 = $nota;
  }

  public function getNota2(){
    return $this->nota2;
  }

  public function setNota2($nota){
    $this->nota2 = $nota;
  }
  
  public function getMedia() {
   return (($this->nota1+$this->nota2)/2);
  }

}

class MediaCliente2 extends Media {
   private $nota3;

  public function setNota3($nota){
    $this->nota3 = $nota;
  }

  public function getNota3(){
    return $this->nota3;
  }

  public function getMedia() {
   return (($this->nota1+$this->nota2+$this->nota3)/3);
  }
  
}

class Aluno extends Pessoa2{
 private $media;
  private $tipoCliente;
 
  function __construct($tipoCliente){
   $this->tipoCliente = $tipoCliente;
  //padrao de desenvolvimento chamado estrategia
    //design patterns strategy 
   if ($tipoCliente=='cliente1') {
     //principio de markov
      $this->media = new Media();
   }else if ($tipoCliente=='cliente2') {
     $this->media = new MediaCliente2();
   }
  
 }
  public function getMedia(){
    return $this->media->getMedia();
  }
  public function notas($notas) {
    if ($this->tipoCliente=='cliente1') {
      $this->media->setNota1($notas[0]);
      $this->media->setNota2($notas[1]);
    }else if ($this->tipoCliente=='cliente2') {
      $this->media->setNota1($notas[0]);
      $this->media->setNota2($notas[1]);
      $this->media->setNota3($notas[2]);
      
    }
   
  }
}

$aluno1 = new Aluno("cliente1");
$aluno1->setNome('Juca');
echo "Nome:".$aluno1->getNome();
$aluno1->notas([8,9]);
echo "<br>" .$aluno1->getMedia();

$aluno2 = new Aluno("cliente2");
$aluno2->setNome('Juninho');
echo "Nome:".$aluno2->getNome();
$aluno2->notas([8,9, 10]);
echo "<br>" .$aluno2->getMedia()







?>