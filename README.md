# aqa_study
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
git checkout feature/week4-ui-auth-practice
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
