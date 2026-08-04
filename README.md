# aqa_study
## Разница между responses и pytest-mock
responses реально проверяет URL/метод запроса — если код обратится не туда, тест упадёт. mocker.patch("requests.Session.request") просто подменяет метод, вернёт мок при любом URL, ничего не проверяя.
## Инструкция для запуска

1. Склонируй репозиторий:
```sh
git https://github.com/YaroslavSoloninin/aqa_study.git
```
```sh
cd aqa_study
```
2. Перейди в нужную ветку проекта
```sh
git checkout feature/week6-requests-mock
```
3. Создай виртуальное окружение 
```sh
python -m venv venv
```
4. Активируй виртуальное окружение
#### Для Windows:
```sh
venv\Scripts\activate
```
#### Для Linux/MacOS:
```sh
source venv/bin/activate
```
5. Установи зависимости
```sh
pip install -r requirements.txt
```
6. Запусти тест
```
pytest
```
