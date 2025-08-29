# 🏥 Healthcare Assistant Chatbot

An AI-powered healthcare chatbot built with Django and OpenAI, designed to provide health information, symptom guidance, and patient support.

## 🌟 Features

### 🤖 AI-Powered Chat Interface
- **Intelligent Health Conversations**: Powered by OpenAI's GPT-4o-mini model
- **Contextual Responses**: Maintains conversation history for better interactions
- **Health-Focused**: Specialized in healthcare topics and medical information
- **Educational Content**: Provides accurate, educational health information

### 📊 Comprehensive Dashboard
- **Health Logs**: Track symptoms, medications, appointments, and more
- **Medication Reminders**: Manage medication schedules and dosages
- **Vital Signs Tracking**: Monitor blood pressure, heart rate, temperature, etc.
- **Statistics Overview**: Visual representation of health data

### 💾 Data Management
- **Session-Based Chat History**: Persistent conversations across sessions
- **Database Models**: Structured data storage for health information
- **Sample Data**: Pre-populated with realistic healthcare data for demonstration

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Django 5.2.5 |
| **AI/ML** | OpenAI GPT-4o-mini API |
| **Database** | SQLite (development) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Icons** | Font Awesome 6.4.0 |
| **Environment** | Python 3.13, Virtual Environment |

## 📁 Project Structure

```
healthcare_assist/
├── healthcare/                 # Django project
│   ├── chatbot/               # Main app
│   │   ├── models.py          # Database models
│   │   ├── views.py           # Business logic
│   │   ├── urls.py            # URL routing
│   │   ├── templates/         # HTML templates
│   │   ├── static/            # CSS, JS, images
│   │   └── management/        # Custom commands
│   ├── settings.py            # Django settings
│   └── urls.py                # Main URL config
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management
├── .env                       # Environment variables
└── README.md                  # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- OpenAI API key
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/healthcare-assistant.git
cd healthcare-assistant
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

### Step 5: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py create_sample_data
```

### Step 6: Run the Application
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📱 Usage

### Chat Interface
1. Navigate to the main page
2. Type your health-related question
3. Receive AI-powered responses
4. View conversation history
5. Clear chat when needed

### Dashboard
1. Visit `/dashboard/` to see health overview
2. View recent health logs
3. Check medication reminders
4. Monitor vital signs
5. Access statistics

## 🔧 Key Features Implementation

### AI Integration
- **OpenAI API**: Seamless integration with GPT-4o-mini
- **Error Handling**: Comprehensive exception management
- **Rate Limiting**: Optimized API calls for cost efficiency
- **Context Management**: Maintains conversation context

### Database Design
- **HealthLog Model**: Flexible health tracking
- **MedicationReminder Model**: Medication management
- **VitalSign Model**: Vital signs monitoring
- **User Relationships**: Scalable for multi-user support

### Frontend Design
- **Responsive Layout**: Works on all device sizes
- **Modern UI**: Clean, professional design
- **Interactive Elements**: Smooth user experience
- **Accessibility**: User-friendly interface

## 🎯 Portfolio Highlights

### Technical Skills Demonstrated
- **Django Development**: Full-stack web application
- **API Integration**: Third-party service integration
- **Database Design**: Complex data modeling
- **Frontend Development**: Modern UI/UX design
- **Error Handling**: Robust application architecture
- **Environment Management**: Production-ready setup

### Problem-Solving
- **Healthcare Domain**: Real-world application
- **AI Integration**: Modern technology implementation
- **User Experience**: Intuitive interface design
- **Data Management**: Efficient information handling

### Code Quality
- **PEP 8 Compliance**: Clean, readable code
- **Modular Design**: Well-organized structure
- **Documentation**: Comprehensive comments
- **Best Practices**: Industry-standard implementation

## 🔒 Security & Privacy

- **Environment Variables**: Secure API key management
- **Input Validation**: Protected against malicious input
- **Session Management**: Secure user sessions
- **Data Protection**: Privacy-focused design

## 🚀 Deployment Ready

The application is structured for easy deployment:
- **Environment Configuration**: Production-ready settings
- **Static Files**: Optimized for deployment
- **Database Migration**: Easy database setup
- **Documentation**: Clear deployment instructions

## 📈 Future Enhancements

- [ ] User authentication system
- [ ] Multi-language support
- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Integration with health devices
- [ ] Telemedicine features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Portfolio: [Your Portfolio](https://yourportfolio.com)

## 🙏 Acknowledgments

- OpenAI for providing the AI capabilities
- Django community for the excellent framework
- Bootstrap team for the UI components
- Font Awesome for the beautiful icons

---

**Note**: This is a demonstration project. For actual medical advice, please consult healthcare professionals.
