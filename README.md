# 📘 iConvert – Conversor de Unidades em Python

Um app de conversão de unidades desenvolvido para atividade acadêmica do curso superior em TI.  
O projeto aplica princípios de modularização, reutilização de componentes e boas práticas de CLI com Python.

---

## 🚀 Funcionalidades Principais

- Conversão de unidades usando a biblioteca **Pint**
- CLI interativo e inteligente usando **Click**
- Tratamento robusto de erros:
  - Unidades inexistentes
  - Incompatibilidade dimensional (ex: metros → quilos)
  - Valores inválidos
- Modo de conversão rápida:
  - `python iConvert.py converter 10 km m`
- Modo interativo:
  - `python iConvert.py interativo`

---

## 🧩 Arquitetura dos Componentes

### **1. UnitManager (Componente Reutilizado)**
- Implementa o padrão **Singleton**
- Gerencia uma instância única da biblioteca **Pint**
- Fornece o `UnitRegistry()` configurado
- Facilita uso em outros projetos

### **2. ConverterService (Desenvolvimento Próprio)**
- Lógica de conversão isolada
- Não usa `print()` nem `input()`
- Pode ser reaproveitado em:
  - APIs (FastAPI, Flask)
  - Automação de dados
  - Aplicações desktop
  - Outros scripts Python

### **3. CLI com Click**
- Comando `converter`
- Modo interativo (`interativo`)
- Mensagens coloridas (feedback intuitivo)

---

## 📦 Como executar

### **1. Instalar dependências**
```bash
pip install pint click

---

## 📦 Convertendo diretamente
### **2. Executar conversão direta**
```bash
python iConvert.py converter 10 km m

---

## 📦 Modo interatio
### **3. Executar modo interativo**
```bash
python iConvert.py interativo

---

## 📦 Como uar o interativo
### **4. Exemplos de Uso no Modo Interativo**
```bash
iConvert> 10 km m
iConvert> converter 2 hr min
