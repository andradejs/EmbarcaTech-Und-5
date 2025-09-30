from periphery import I2C
import time

I2C_BUS = "/dev/i2c-2"  # Ajuste conforme necessário
I2C_ADDRESS = 0x38   # Endereço I2C do AHT10

i2c = I2C(I2C_BUS)

def aht10_init():
    """Inicializa o sensor AHT10."""
    # Comando para inicializar o AHT10
    init_command = [0xE1]
    # Envia comando de inicialização
    i2c.transfer (I2C_ADDRESS, [I2C.Message(init_command)])
    # Aguarde 20ms para estabilização
    time.sleep(0.04)


def aht10_read():
    """Lê temperatura e umidade do sensor AHT10."""
    # Envia comando para iniciar medição
    measure_command = [0xAC, 0x33, 0x00]
    i2c.transfer(I2C_ADDRESS, [I2C.Message(measure_command)])
    time.sleep(0.08) # Aguarde 80ms para conversão

     # Lê os 6 bytes de dados do sensor
    read_message = I2C.Message(bytearray(6), read=True)
    i2c.transfer(I2C_ADDRESS, [read_message])
    data = read_message.data

    """Data registra os 5 bytes
    Bytes 1, 2 e a primeira metade do 3- humidade
    Segunda metade do 3, 4 e 5 temperatura;"""
    humidity_raw = ((data[1] << 16) | (data[2] << 8) | data[3]) >> 4
    temperature_raw = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]

    # Calcula umidade e temperatura reais
    humidity = (humidity_raw / 1048576) * 100 # Em percentual
    temperature = (temperature_raw / 1048576) * 200 - 50 # Em °C
    return temperature, humidity