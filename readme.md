
# 📡 EmbarcaTech: Unidade 5 - IFPI Pedro II

## 📌 Descrição
Este projeto consiste em um **data logger embarcado** desenvolvido na placa **Labrador 32 (ESP32)**.  
Ele utiliza o sensor **AHT10** para medir temperatura e umidade relativa do ar, registrando periodicamente esses dados em um cartão **microSD**.  

O sistema foi desenvolvido como atividade da Unidade 5 do programa **EmbarcaTech - IFPI Pedro II**.

---

## 🛠️ Componentes Utilizados
- 🔌 **Placa Labrador 32**
- 🌡️ **Sensor AHT10** (I2C – temperatura e umidade)
- 💾 **Módulo MicroSD**

---

## ⚡ Funcionalidades
- 📊 Leitura de **temperatura (°C)** e **umidade (%)** em tempo real.  
- 💾 Registro contínuo dos dados no cartão **microSD**.  

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório
```bash
git clone https://github.com/valdomg/EmbarcaTech-Und-5.git
cd EmbarcaTech-Und-5
````

### 2. Criar ambiente virtual (venv)

```bash
python3 -m venv .venv
```

### 3. Ativar o ambiente virtual

* **Linux**

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

Com o ambiente ativo, rode:

```bash
pip install -r requirements.txt
```

#### 📂 Configuração do cartão microSD da Labrador

Após ativar a `venv`, configure o cartão microSD:

```bash
# Criar o ponto de montagem
sudo mkdir -p /mnt/sdcard

# Montar o SDCard com permissão de escrita temporária
sudo mount -o uid=$(id -u),gid=$(id -g) /dev/mmcblk0p1 /mnt/sdcard

# Criar a pasta de logs
mkdir /mnt/sdcard/logs
````

> ⚠️ **Importante:** no código, utilize o caminho `/mnt/sdcard/logs` no construtor da classe `Logger`.

Exemplo:

```python
from logger import Logger

log = Logger("/mnt/sdcard/logs")
```

### 5. Executar a aplicação

* **Linux**
```bash
python3 main.py
```

### 6. Sair do ambiente virtual

* **Linux**
```bash
deactivate
```
---

## 📁 Estrutura dos Arquivos

```
┣ 📄 aht10.py     # Funções para inicializar e ler dados do sensor AHT10
┣ 📄 logger.py    # Classe Logger para salvar logs de execução em arquivo
┣ 📄 main.py      # Arquivo principal para executar a aplicação
┣ 📄 requirements.txt  # Dependências do projeto
```

---
## 📖 Aprendizados

Este projeto permitiu aplicar conceitos de:

* 🔌 **Comunicação I2C** (sensor AHT10)
* 💾 **Comunicação SPI** (microSD)
* 🗂️ **Manipulação de arquivos em sistemas embarcados**
* 🛠️ **Estruturação de um data logger simples**
---



## 📄 Licença

Este projeto está sob a licença **MIT**.
Sinta-se livre para usar e modificar conforme necessário.

