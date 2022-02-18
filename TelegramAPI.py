"MESAJ GÖNDERME;"
"https://api.telegram.org/bot"
"$token"
"/sendphoto?chat_id="
"$chat_id"
"&text="
"$message"
  
token = "1705788624:AAG2miJoRXmIteB17tLX84QgZVz8vTg-mJY"
chat_id = "@kirmizipatikatest"
message = "Merhaba Kırmızı Patika YouTube!"
messageapi = "https://api.telegram.org/bot"+$token+"/sendmessage?chat_id="+$chat_id+"&text="+$message



"FOTOĞRAF GÖNDERME;"
"Fotoğraf gönderme işlemlerinde, telegram'a indirilebilir bir dosya verilmelidir. Aksi taktirde false değer alırsınız."
~~
"https://api.telegram.org/bot"
"$token"
"/sendphoto?chat_id="
"$chat_id"
"&photo="
"$photo"
 
token = "1705788624:AAG2miJoRXmIteB17tLX84QgZVz8vTg-mJY"
chat_id = "@kirmizipatikatest"
photo = "https://bybug.ml/gallery/webmage.jpg"
messageapi = "https://api.telegram.org/bot"+$token+"/sendphoto?chat_id="+$chat_id+"&photo="+$photo