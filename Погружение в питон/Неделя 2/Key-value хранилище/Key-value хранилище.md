На этой неделе мы с вами реализуем собственное key-values хранилище. Данные будут сохраняться в файле storage.data. Добавление новых данных в хранилище и получение текущих значений осуществляется с помощью утилиты командной строки storage.py. Пример работы утилиты:  

Сохранение значения value по ключу key_name:  

```
$ storage.py --key key_name --val value
```
Получение значения по ключу key_name: 
```
$ storage.py --key key_name```

```
Вашей задачей будет написать реализацию утилитыstorage.py.

Утилита может вызваться со следующими параметрами:

--key <имя ключа> , где <имя ключа> - ключ по которому сохраняются/получаются значения

--val <значение>, где <значение> - сохраняемое значение.

Если при запуске утилиты переданы оба ключа, происходит добавление переданного значения по ключу и сохранение данных в файле. Если передано только имя ключа, происходит чтение файла хранилища и вывод на печать значений, которые были сохранены по данному ключу.  Обратите внимание, что значения по одному ключу не перезаписываются, а добавляются к уже сохраненным. Другими словами - по одному ключу могут храниться несколько значений. При выводе на печать, значения выводятся в порядке их добавления в хранилище. Формат вывода на печать для нескольких значений:  
```value_1, value_2```
Обратите внимание на пробел после запятой. Если значений по ключу не было найдено, выведите пустую строку или None.

Для работы с аргументами командной строки используйте модуль argparse. Хранить данные в файле мы рекомендуем в формате JSON с помощью использования модуля стандартной библиотеки  json. Прежде чем отправлять ваше решение на проверку, протестируйте работу вашей утилиты на добавление нескольких ключей и разных значений.
### Решение :
```
import os
import tempfile
import argparse
import json
import pickle

parser = argparse.ArgumentParser()

parser.add_argument('--key', dest="key")
parser.add_argument('--val', dest="val")

args = parser.parse_args()
key = str(args.key)
val = str(args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'wb+') as tf:
    if key != "None":
        if val != "None":
            if (os.stat(storage_path).st_size != 0) and (tf.read() != b""):
                data_new = pickle.load(tf)
                if key in data_new:
                    data_new[key].append(val)
                else:
                    data_new[key] = list()
                    data_new[key].append(val)
                    pickle.dump(data_new, tf)
            else:
                template = {str(key): [str(val)]}
                print(template)
                pickle.dump(template, tf)
        else:
            if (os.stat(storage_path).st_size != 0) and (tf.read() != b""):
                data_new = pickle.load(tf)
                print(data_new)
                if key in data_new:
                    for i in data_new[key]:
                        print(data_new)

        print(tf.read())
