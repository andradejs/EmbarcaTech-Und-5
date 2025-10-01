# EmbarcaTech: Unidade 5 - IFPI Pedro II

## 📌 Descrição
Este projeto consiste em um data logger embarcado desenvolvido na placa Labrador 32. Ele utiliza o sensor AHT10 para medir temperatura e umidade relativa do ar, registrando periodicamente esses dados em um cartão microSD. O sistema foi desenvolvido como atividade da Unidade 5 do programa EmbarcaTech.

## 🛠️ Componentes Utilizados
- Placa Labrador 32 (ESP32)
- Sensor AHT10 (I2C – temperatura e umidade)
- Módulo MicroSD

## ⚙️ Funcionalidades
- Leitura de temperatura (°C) e umidade (%) em tempo real.
- Registro contínuo dos dados no cartão microSD.

## 📁 Estrutura dos Arquivos
```
┣ 📄 aht10.py     # Funções para inicializar e ler dados do sensor AHT10
┣ 📄 logger.py    # Classe Logger para salvar logs de execução em arquivo
```

## 📖 Aprendizados
Este projeto permitiu aplicar conceitos de:

- Comunicação I2C (sensor AHT10)
- Comunicação SPI (microSD)
- Manipulação de arquivos em sistemas embarcados
- Estruturação de um data logger simples