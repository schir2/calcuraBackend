# Calcura Backend

## Setup

### Create .env in core dore directory


```.dotenv
# Django Secret Key
SECRET_KEY=your-secret-key

# Debug mode (True/False)
DEBUG=True

# Allowed Hosts
ALLOWED_HOSTS=*

# Internal IPs
INTERNAL_IPS=localhost,127.0.0.1

# CORS Whitelist
CORS_ORIGIN_WHITELIST=http://localhost:3000

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS=http://localhost:3000

```

```bash
pip install -r requirements.txt
python manage.py migrate
```