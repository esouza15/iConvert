# 📘 iConvert – Conversor de Unidades em Python

Um app de conversão de unidades desenvolvido como atividade acadêmica no curso superior em TI.  
O projeto demonstra modularização, reutilização de componentes e boas práticas de CLI utilizando Python.

---

## 🚀 Funcionalidades Principais

- Conversão de unidades usando a biblioteca **Pint**
- CLI interativo usando **Click**
- Tratamento de erros:
  - Unidades inexistentes
  - Dimensões incompatíveis
  - Valores inválidos
- Conversão rápida via terminal  
  Ex:  
  ```bash
  python iConvert.py converter 10 km m
  ```
- Modo interativo  
  ```bash
  python iConvert.py interativo
  ```

---

## 🧩 Arquitetura dos Componentes

### 🔹 1. Componente Reutilizado — `UnitManager`
- Implementa o padrão **Singleton**
- Gerencia uma instância única do **UnitRegistry** (Pint)
- Facilita a reutilização em outros projetos

### 🔹 2. Componente Desenvolvido — `ConverterService`
- Lógica de conversão encapsulada
- Não usa `input()` ou `print()`
- Reutilizável em:
  - APIs Python
  - Scripts de automação
  - Apps desktop
  - CLI

### 🔹 3. Interface CLI com Click
- Comando `converter` (one-shot)
- Comando `interativo`
- Mensagens coloridas (feedback intuitivo)

---

## 📦 Como executar o projeto

### 1. Instale as dependências
```bash
pip install pint click
```

### 2. Execução direta
```bash
python iConvert.py converter 10 km m
```

### 3. Modo interativo
```bash
python iConvert.py interativo
```

---

## 🧪 Exemplos de Uso

### Conversão simples:
```bash
python iConvert.py converter 100 m cm
```

### No modo interativo:
```
iConvert> 10 km m
iConvert> converter 2 hr min
```

---

## 🗂 Estrutura do Projeto

```
├── iConvert.py
└── README.md
```

---

## 📘 Tecnologias Utilizadas

- **Python 3**
- **Pint** – Biblioteca para unidades físicas
- **Click** – Construção de CLI profissionais

---


## 👨‍💻 Autor

**Esthefison Souza**  
Desenvolvimento do app como parte da atividade acadêmica em Tecnologia da Informação.

---

## 📝 Licença

Este projeto pode ser utilizado livremente para fins acadêmicos, educacionais ou de demonstração.
