# Detect New release paper automation

## How to use

1-1. Clone the repository

```cmd
git clone https://github.com/kyunghwanleethebest/paper_auto_detect.git
```

1-2. Make Screen

```cmd
screen -S test
```



2. Make Python Virtual environment

```cmd
# create virtual environment
python -m venv venv

# then activate the environment (Unix)
source venv/bin/activate
```

3. Install the packages 

```cmd
pip install -r requirements.txt
```

4. Make g-mail app token

ref : https://ssrm.co.kr/chatgpt%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EB%B3%B4%EB%82%B4%EA%B8%B0/



5. execute the file

```cmd
python execute.py
```



Put author name in the file execute.py variable **"author_name"**

Put g_mail id & pwd on the command line.



6. escape from screen (Ctrl + a , d)