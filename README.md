Workshifts XML
================
Тестовое задание для 2GIS
Скрипт для вычисления общего времени пребывания людей за каждое число

#### Сборка и запуск
```docker build workshifts -t workshifts
docker run -v /path/to/xml_file:/workshift.xml workshifts --xml_path="/workshift.xml"
или с аргументами
docker run -v /path/to/xml_file:/workshift.xml workshifts --xml_path="/workshift.xml" --start_date=02-03-2011 --end_date=05-03-2011 --logins="b.testobject,a.stepanova, i.ivanov"
```
Где /path/to/xml_file - путь до XML файла со схемами для передачи его по тому. Аргументы не обязательны

#### Тесты
Лежат в папке scripts/tests. Запускать либо перед сборкой, либо внутри сборки (лучше первый вариант)
```
docker run -v /home/ubuntu/test_workshifts.xml:/workshift.xml -it --entrypoint /bin/bash workshifts
python -m pytest tests
```

#### Аргументы
- xml_path (обязателен) - Путь до XML-файла со сменами
- start_date (не обязателен) - Начальный срез смен, по которому будет идти поиск в файле
- end_date (не обязателен) - Конечный срез смен, по которому будет идти поиск
- logins (не обязателен) - Список логинов через запятую, допускаются запятые между логинами
