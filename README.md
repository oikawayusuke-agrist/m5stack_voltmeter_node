# m5stack_voltmeter_node

[document](https://docs.m5stack.com/#/en/unit/vmeter)  
   id 0x49  
   16-bit ADC conversion  
   0x53は絶対使うな、工場出荷時のきゃりぶれーしょん  
  
   $ sudo i2cdetect -y -r 1  

   reg_addr  
   getVoltage()  
    getConversion()  
     i2cReadU16(_ads1115_addr, ADS1115_RA_CONVERSION, &value);  
      i2cReadBytes(addr, reg_addr, read_buf, 2);  

   reg_addr : ADS1115_RA_CONVERSION 0x00  
   write(reg_addr)  
   requestFrom(addr, (uint8_t)len)  
   参考資料  
   - [温湿度センサAM2320をRaspberry Pi 3で使用する](http://wizqro.net/%E6%B8%A9%E6%B9%BF%E5%BA%A6%E3%82%BB%E3%83%B3%E3%82%B5am2320%E3%82%92raspberry-pi-3%E3%81%A7%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B/)  
   - [Raspberry Pi で湿度センサーを動かそう！](https://www.indetail.co.jp/blog/13008/)
   - [Arduino 入門　I2C通信編 p9](https://monolizm.com/sab/pdf/%E7%AC%AC16%E5%9B%9E_%E3%83%97%E3%83%AC%E3%82%BC%E3%83%B3%E8%B3%87%E6%96%99(IC2%E9%80%9A%E4%BF%A1%E7%B7%A8).pdf)i2cの読み取りを理解するのに八頭がわかりやすかった。  
   - [ADS1115 P18-21]](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ADS1115.PDF) データシートさえ読んでればなんとかなる。  
  
   133 : 10000101  
   131 : 10000011  
       : 10001001  
   133 : 10000100  
   131 : 10000011  
   1000010010000011 : 8483  
  
   1000010110000011  
   1000010110000011  
   34179 * 2 = 68358  
  
   レジスタアドレス  
   コンフィグアドレス：0b01  
