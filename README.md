# **Projeto Ransomware - Encriptador e Decriptador de Arquivos**

Este projeto demonstra o funcionamento básico de um **ransomware** em Python. Ele possui dois scripts: um para **criptografar** um arquivo e outro para **descriptografá-lo**.

> **⚠️ Aviso Importante**  
> Este projeto faz parte dos projetos propostos no Santander Bootcamp Cibersegurança e seu propósito é apenas educativo

---

## **Descrição dos Arquivos**

1. **`encrypter.py`**  
   Este script lê um arquivo (`file.txt`), criptografa seu conteúdo usando **AES** com uma chave fixa e, em seguida, remove o arquivo original. O arquivo criptografado é salvo com a extensão `.ransomware`.

2. **`decrypter.py`**  
   Este script lê o arquivo criptografado (`file.txt.ransomware`), descriptografa o conteúdo usando a mesma chave AES, recria o arquivo original e remove o arquivo criptografado.

---

## **Requisitos**

Para executar o projeto, você precisa de:

- **Python 3** instalado  
- Biblioteca `pyaes` para criptografia  

## **Como executar**

1. **Criptografar o arquivo**
    1. Crie um arquivo chamado (`file.txt`) no mesmo diretório do script.
    2. Execute o script (`encrypter.py`)
    ```bash
        python3 encrypter.py
    ```
    3. O arquivo original será substituido pelo arquivo (`file.txt.ransomware`) e seu conteúdo estará criptografado

2. **Descriptografar o arquivo**
    1. Execute o script (`decrypter.py`)
    ```bash
        python3 decrypter.py
    ```
    2. O arquivo criptografado será substituido pelo arquivo (`file.txt`) e seu conteúdo estará descriptografado