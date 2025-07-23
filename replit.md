# Mobile Doctor Hyderabad - Web Application

## Overview

This is a Flask-based web application for Mobile Doctor Hyderabad, a mobile phone repair service business. The application serves as a landing page/website to showcase the business's services, location, and contact information. It's designed as a simple, static website with SEO optimization for local search visibility.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **Static Content**: HTML templates with embedded CSS and JavaScript
- **SEO Optimization**: Structured data markup using JSON-LD schema for local business with star ratings
- **Responsive Design**: Mobile-first approach with viewport meta tags

### Backend Architecture
- **Framework**: Flask (Python micro-framework)
- **Database**: PostgreSQL with Flask-SQLAlchemy ORM
- **Application Structure**: Modular application with separate models and routes
- **Session Management**: Flask sessions with configurable secret key
- **API Endpoints**: RESTful endpoints for stats and reviews
- **Deployment**: Configured for host '0.0.0.0' on port 5000

### Database Architecture
- **ORM**: SQLAlchemy with Flask-SQLAlchemy extension
- **Models**: Contact, Review, Service, Device, Appointment, BusinessStats
- **Features**: Contact form submissions, customer reviews, appointment booking, business analytics
- **Data Integrity**: Foreign key relationships and data validation

## Key Components

### Core Application Files
- `app.py`: Main Flask application with route definitions and database integration
- `main.py`: Application entry point (imports from app.py)
- `models.py`: Database models (Contact, Review, Service, Device, Appointment, BusinessStats)
- `templates/index.html`: Main landing page template with dynamic content support

### Business Logic
- Multi-route application with database-driven content
- Contact form submission and management
- Customer review system with moderation
- Appointment booking system
- Business statistics tracking
- API endpoints for data access

### SEO and Marketing Features
- Google AdSense integration
- Structured data markup for local business
- Multi-language keywords (English, Telugu, Hindi)
- Meta descriptions and keywords optimization

## Data Flow

1. **Request Handling**: Flask receives HTTP requests on multiple routes ('/', '/contact', '/review', '/appointment')
2. **Database Operations**: SQLAlchemy handles database queries and data persistence
3. **Template Rendering**: Jinja2 renders templates with dynamic data from the database
4. **Form Processing**: Contact forms, reviews, and appointments are processed and stored
5. **API Responses**: RESTful endpoints serve JSON data for statistics and reviews
6. **Response Delivery**: Dynamic HTML content with real-time data is served to the client

### Database Tables
- **contact**: Store customer inquiries and service requests
- **review**: Manage customer reviews with ratings and moderation
- **service**: Catalog of available repair services with pricing
- **device**: Supported device models and brands
- **appointment**: Track scheduled repair appointments
- **business_stats**: Store key business metrics for display

## External Dependencies

### Python Dependencies
- Flask web framework
- Flask-SQLAlchemy ORM
- psycopg2-binary (PostgreSQL adapter)
- email-validator (for form validation)
- gunicorn (WSGI server)
- Standard library modules (os, datetime)

### Third-Party Services
- Google AdSense (ca-pub-2488763930939291)
- Google Structured Data for business listings

### Environment Variables
- `SESSION_SECRET`: Configurable session secret key (defaults to "default_secret_key")

## Deployment Strategy

### Development Configuration
- Debug mode enabled
- Binds to all interfaces (0.0.0.0)
- Runs on port 5000
- Environment-based configuration for session secrets

### Production Considerations
- Session secret should be set via environment variable
- Debug mode should be disabled
- Consider using a production WSGI server
- Static assets could be served by a reverse proxy

### Hosting Requirements
- Python 3.x environment
- Flask framework support
- Environment variable configuration capability
- Port 5000 availability (or configurable port)

## Technical Notes

The application is intentionally simple, focusing on presenting business information rather than complex functionality. The structured data markup suggests this is optimized for local SEO and Google Business listings. The multilingual keywords indicate targeting of diverse linguistic communities in Hyderabad.

Future enhancements might include:
- Contact form functionality
- Service booking system
- Customer testimonials
- Gallery of repair work
- Blog/news section