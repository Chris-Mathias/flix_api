# Flix API

Esta API foi desenvolvida para fins de estudo, baseada em um curso de Django. O objetivo é praticar conceitos de desenvolvimento backend, APIs RESTful e deploy em ambientes de produção.

## Funcionalidades

- CRUD de recursos (exemplo: filmes, séries, usuários)
- Autenticação de usuários
- Endpoints RESTful
- Documentação automática via DRF

## Tecnologias

- Python 3.x
- Django
- Django REST Framework
- SQLite

## Como rodar localmente

```bash
git clone https://github.com/Chris-Mathias/flix_api.git
cd flix_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deploy em VPS (Ubuntu)

1. **Clone o projeto e configure o ambiente:**
    ```bash
    sudo apt update
    sudo apt install python3-pip python3-venv git
    git clone https://github.com/Chris-Mathias/flix_api.git
    cd flix_api
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Configure variáveis de ambiente e banco de dados.**

3. **Aplique as migrações:**
    ```bash
    python manage.py migrate
    ```

4. **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

5. **Configure o Gunicorn:**
    ```bash
    pip install gunicorn
    gunicorn flix_api.wsgi:application --bind 0.0.0.0:8000
    ```

6. **(Opcional) Configure o Nginx como proxy reverso.**

7. **Acesse sua API pelo IP da VPS na porta configurada.**

---

> **Nota:** Lembre-se de configurar as variáveis de ambiente sensíveis (SECRET_KEY, DEBUG, ALLOWED_HOSTS) e considerar o uso de um banco de dados de produção (como PostgreSQL).
