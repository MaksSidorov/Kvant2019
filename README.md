# Kvantoriada

## Необходимые библитотеки
 + PyQt5
 + dlib
 + keras
 + cv2
 + datetime
 + numpy
 + sqlite3
 + sys
 
## Устройство программы 
 + Исходный код находится в папке src
 + Для запуска программы нужно запутить файл prog.py
 + В файле classes.py находтся виджеты программы
 + В файле functions.py находятся функции для упражнений
 
## Упражнения
 + После нажатия кнопки с Web-камеры пользователя считывается изображение
 + Дальше с помощь библиотеки OpenCV определяем лицо
 + Если лицо обнаружено фиксируем лицивые орентиры, если нет, изображение просто выводится 
 + В случае фиксации лицевых орентиров они подаются в одну из функция файла functions.py
 + Если функция возвращает True, увеличиваем счетчик на 1
 
## Финальная часть
 + После нажатия кнопки с Web-камеры пользователя считывается изображение
 + Дальше с помощь библиотеки OpenCV определяем лицо
 + Если лицо подаем изображение в заранее обученную нейронную сеть, если нет, изображение просто выводится

