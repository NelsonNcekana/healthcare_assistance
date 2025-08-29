# 🚀 Deployment Guide

This guide will help you deploy the Healthcare Assistant Chatbot to various platforms.

## 📋 Prerequisites

- Python 3.8+
- Git
- OpenAI API key
- Database (PostgreSQL recommended for production)

## 🌐 Deployment Options

### 1. Heroku Deployment

#### Step 1: Install Heroku CLI
```bash
# macOS
brew install heroku/brew/heroku

# Windows
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 2: Create Heroku App
```bash
heroku create your-app-name
```

#### Step 3: Add PostgreSQL
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

#### Step 4: Set Environment Variables
```bash
heroku config:set OPENAI_API_KEY=your_openai_api_key
heroku config:set SECRET_KEY=your_django_secret_key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

#### Step 5: Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

#### Step 6: Run Migrations
```bash
heroku run python manage.py migrate
heroku run python manage.py create_sample_data
```

### 2. Railway Deployment

#### Step 1: Connect to Railway
1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Create a new project

#### Step 2: Configure Environment Variables
Add these environment variables in Railway dashboard:
- `OPENAI_API_KEY`
- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS`

#### Step 3: Deploy
Railway will automatically deploy your app when you push to GitHub.

### 3. DigitalOcean App Platform

#### Step 1: Create App
1. Go to DigitalOcean App Platform
2. Connect your GitHub repository
3. Select the main branch

#### Step 2: Configure Build Settings
- **Build Command**: `pip install -r requirements.txt`
- **Run Command**: `gunicorn healthcare.wsgi:application`

#### Step 3: Set Environment Variables
Add the required environment variables in the dashboard.

### 4. VPS Deployment (Ubuntu/Debian)

#### Step 1: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv nginx -y

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y
```

#### Step 2: Clone Repository
```bash
git clone https://github.com/yourusername/healthcare-assistant.git
cd healthcare-assistant
```

#### Step 3: Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

#### Step 4: Configure Database
```bash
sudo -u postgres createdb healthcare_db
sudo -u postgres createuser healthcare_user
sudo -u postgres psql -c "ALTER USER healthcare_user PASSWORD 'your_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;"
```

#### Step 5: Configure Django Settings
Update `healthcare/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'healthcare_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address']
```

#### Step 6: Set Up Gunicorn
Create `/etc/systemd/system/healthcare.service`:
```ini
[Unit]
Description=Healthcare Assistant Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/healthcare-assistant
Environment="PATH=/path/to/healthcare-assistant/venv/bin"
ExecStart=/path/to/healthcare-assistant/venv/bin/gunicorn --workers 3 --bind unix:/path/to/healthcare-assistant/healthcare.sock healthcare.wsgi:application

[Install]
WantedBy=multi-user.target
```

#### Step 7: Configure Nginx
Create `/etc/nginx/sites-available/healthcare`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /path/to/healthcare-assistant;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/healthcare-assistant/healthcare.sock;
    }
}
```

#### Step 8: Enable Services
```bash
sudo ln -s /etc/nginx/sites-available/healthcare /etc/nginx/sites-enabled
sudo systemctl start healthcare
sudo systemctl enable healthcare
sudo systemctl restart nginx
```

## 🔧 Production Settings

### Security Considerations
1. **Set DEBUG=False**
2. **Use strong SECRET_KEY**
3. **Configure ALLOWED_HOSTS**
4. **Use HTTPS**
5. **Set up proper database**
6. **Configure static files**

### Performance Optimization
1. **Use PostgreSQL for production**
2. **Configure caching (Redis)**
3. **Optimize static files**
4. **Use CDN for static assets**
5. **Monitor application performance**

## 📊 Monitoring

### Health Checks
- Set up health check endpoints
- Monitor API response times
- Track error rates
- Monitor database performance

### Logging
- Configure proper logging
- Set up log rotation
- Monitor application logs
- Set up error alerting

## 🔒 SSL/HTTPS Setup

### Let's Encrypt (Free)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

### Automatic Renewal
```bash
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 📈 Scaling

### Horizontal Scaling
- Use load balancers
- Deploy multiple instances
- Configure session storage (Redis)
- Use CDN for static files

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Use caching strategies
- Monitor resource usage

## 🆘 Troubleshooting

### Common Issues
1. **Static files not loading**: Check STATIC_ROOT and collectstatic
2. **Database connection errors**: Verify database credentials
3. **Environment variables**: Ensure all required vars are set
4. **Port conflicts**: Check if port 8000 is available

### Debug Commands
```bash
# Check application status
sudo systemctl status healthcare

# View logs
sudo journalctl -u healthcare

# Test database connection
python manage.py dbshell

# Check static files
python manage.py collectstatic --dry-run
```

## 📞 Support

For deployment issues:
1. Check the logs
2. Verify environment variables
3. Test locally first
4. Check platform-specific documentation
