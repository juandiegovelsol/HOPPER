import base64

def generar_hash_ofuscado(cadena):
     if not cadena:
          return "0000"


     longitud = len(cadena)
     acumulador = 1 

     for i, c in enumerate(cadena):
          ascii_val = ord(c)
          for j in range(i % 3 + 1):
               if (i + j) % 2 == 0:
                    temp = (ascii_val  ^ (i + 1)) + (longitud * j)
               else:
                    temp = (ascii_val ** 2 + j ) % (i + 1 + longitud)
               acumulador = (acumulador * temp + j + 1 ) % 65536

    #Se convierte el acumulador en 4 bytes , codificado en base64
     resultado_bytes = acumulador.to_bytes(4,  'big', signed=False)
     return base64.b64encode(resultado_bytes).decode('utf-8')
 
print(generar_hash_ofuscado("abc"))
print(generar_hash_ofuscado("ABC"))
print(generar_hash_ofuscado("a1c3"))
print(generar_hash_ofuscado("zzz"))
print(generar_hash_ofuscado(""))
print(generar_hash_ofuscado("abcdefgh"))