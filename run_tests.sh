#!/bin/bash
pytest || true

cp categories.json reports/allure/

if [ -d "allure-report/history" ]; then
    cp -r allure-report/history/ reports/allure/history/
fi

allure generate reports/allure -o allure-report --clean
