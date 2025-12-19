# Лабораторная работа №6
## Обучение нейронной сети PointNet++ для семантической сегментации облака точек
В файле "lab6.ipynb" содержится ход работы (на ноутбуке с GPU RTX 5050 8 GB) и результаты ЛР №6.

Для запуска Jupyter-ноутбука потребуются Python 3.11.9, Jupyter Notebook и зависимости, указанные в файле "lab6.ipynb".

Для запуска в Ubuntu (или WSL) выполните:
```
sudo apt update
```
```
sudo apt install build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
```
sudo apt update && sudo apt upgrade -y
```
```
sudo apt install software-properties-common -y 'pyenv'
```
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
```
source ~/.bashrc
```
```
pyenv install 3.11.9
```
После установки Python:
```
pip install jupyter
```