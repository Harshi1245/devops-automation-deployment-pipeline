@echo off
echo Running code quality checks...
python -m flake8 app.py test_app.py
if errorlevel 1 exit /b 1

echo Running automated tests...
python -m pytest -v
if errorlevel 1 exit /b 1

echo All validation checks passed!