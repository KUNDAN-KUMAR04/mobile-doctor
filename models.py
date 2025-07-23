from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class Contact(db.Model):
    """Model for storing contact form submissions"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    service_type = db.Column(db.String(100), nullable=False)
    device_model = db.Column(db.String(100), nullable=True)
    issue_description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='new')  # new, contacted, completed
    
    def __repr__(self):
        return f'<Contact {self.name} - {self.service_type}>'


class Review(db.Model):
    """Model for storing customer reviews and ratings"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    review_text = db.Column(db.Text, nullable=False)
    service_type = db.Column(db.String(100), nullable=True)
    device_model = db.Column(db.String(100), nullable=True)
    is_verified = db.Column(db.Boolean, default=False)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Review {self.customer_name} - {self.rating} stars>'


class Service(db.Model):
    """Model for storing service information and pricing"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price_range = db.Column(db.String(50), nullable=True)  # e.g., "₹500-₹2000"
    duration_minutes = db.Column(db.Integer, nullable=True)  # estimated repair time
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Service {self.name}>'


class Device(db.Model):
    """Model for storing supported device information"""
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)  # Apple, Samsung, etc.
    model = db.Column(db.String(100), nullable=False)  # iPhone 13, Galaxy S21, etc.
    is_supported = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Device {self.brand} {self.model}>'


class Appointment(db.Model):
    """Model for storing appointment bookings"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=True)
    preferred_date = db.Column(db.DateTime, nullable=False)
    issue_description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, confirmed, completed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    service = db.relationship('Service', backref=db.backref('appointments', lazy=True))
    device = db.relationship('Device', backref=db.backref('appointments', lazy=True))
    
    def __repr__(self):
        return f'<Appointment {self.customer_name} - {self.preferred_date}>'


class BusinessStats(db.Model):
    """Model for storing and tracking business statistics"""
    id = db.Column(db.Integer, primary_key=True)
    stat_name = db.Column(db.String(50), nullable=False, unique=True)
    stat_value = db.Column(db.Integer, nullable=False, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<BusinessStats {self.stat_name}: {self.stat_value}>'