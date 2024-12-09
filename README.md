# **Cálculo do IMC (Índice de Massa Corporal)**

Este repositório contém um programa em Python desenvolvido como parte da disciplina **Linguagem de Programação**, do 1º semestre do curso de **Engenharia de Software**. O objetivo do projeto é calcular o IMC (Índice de Massa Corporal) de uma pessoa e classificá-lo com base em faixas pré-definidas.

---

## **Descrição do Projeto**

O cálculo do IMC é uma aplicação prática para consolidar conceitos básicos de programação, incluindo:

- Estruturação do código.
- Uso de **classes** e **métodos** na Programação Orientada a Objetos (POO).
- Entrada e saída de dados (interação com o usuário).
- Aplicação de validações e lógica condicional.

O programa permite que o usuário insira seu peso e altura e, com base nesses dados:

- Calcule o IMC.
- Classifique o resultado como **magro**, **normal**, **sobrepeso**, **obesidade**, ou **obesidade grave**.

> **Nota Importante:** Um relatório detalhado sobre o projeto foi criado seguindo as normas ABNT e inclui imagens e explicações sobre o desenvolvimento. Contudo, tanto o relatório quanto as imagens estão **desatualizados** em relação ao código atual, que foi reescrito usando o paradigma de Programação Orientada a Objetos (POO).

---

## **Funcionalidades**

### **Cálculo do IMC**
- Fórmula usada:
  \[
  IMC = peso/(altura*altura)
  \]

### **Classificação do IMC**
- **Magro:** IMC < 18.5.
- **Normal:** 18.5 ≤ IMC ≤ 24.9.
- **Sobrepeso:** 25.0 ≤ IMC ≤ 29.9.
- **Obesidade:** 30.0 ≤ IMC ≤ 39.9.
- **Obesidade grave:** IMC ≥ 40.0.

### **Validação de Entradas**
- Garante que o peso e a altura sejam valores numéricos positivos.

---

## **Estrutura do Código**

O programa segue o paradigma de Programação Orientada a Objetos (POO). A classe `Pessoa` é usada para encapsular os dados e as operações relacionadas ao IMC.

### **Classe `Pessoa`**
- **Atributos:** `peso`, `altura`.
- **Métodos:**
  - `calcular_imc`: Calcula o IMC com base nos atributos.
  - `classificar_imc`: Classifica o IMC conforme as faixas definidas.

### **Função `main`**
- Responsável por interagir com o usuário, criar um objeto `Pessoa` e exibir os resultados.

---

## **Relatório em ABNT**

Um relatório detalhado foi elaborado seguindo as normas ABNT, apresentando:

- O contexto e objetivo do projeto.
- Estrutura do código.
- Imagens explicativas.

> **Aviso:** O relatório e as imagens estão **desatualizados** em relação à versão atual do código, que foi reestruturado para utilizar **Programação Orientada a Objetos (POO)**.

---

## **Aprendizados**

Durante o desenvolvimento deste projeto, foram consolidados os seguintes conceitos:

- Utilização de **classes** e **métodos** para estruturar o código.
- Boas práticas na organização do programa e validação de dados.
- Aplicação de lógica condicional para resolver problemas reais.
- Interação com o usuário por meio de entrada e saída de dados.
