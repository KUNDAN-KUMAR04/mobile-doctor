import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

# configure the database
database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable not set")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the app with the extension
db.init_app(app)

# Import models and create tables
with app.app_context():
    import models
    db.create_all()

@app.route('/')
def index():
    # Get recent reviews for display
    recent_reviews = models.Review.query.filter_by(is_published=True).order_by(models.Review.created_at.desc()).limit(5).all()
    
    # Get business stats
    stats = {}
    business_stats = models.BusinessStats.query.all()
    for stat in business_stats:
        stats[stat.stat_name] = stat.stat_value
    
    return render_template('index.html', reviews=recent_reviews, stats=stats)


@app.route('/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submissions"""
    try:
        contact = models.Contact(
            name=request.form.get('name'),
            phone=request.form.get('phone'),
            email=request.form.get('email', ''),
            service_type=request.form.get('service_type'),
            device_model=request.form.get('device_model', ''),
            issue_description=request.form.get('issue_description')
        )
        
        db.session.add(contact)
        db.session.commit()
        
        flash('Thank you for contacting us! We will get back to you soon.', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        db.session.rollback()
        flash('Sorry, there was an error submitting your request. Please try again.', 'error')
        return redirect(url_for('index'))


@app.route('/review', methods=['POST'])
def submit_review():
    """Handle review submissions"""
    try:
        review = models.Review(
            customer_name=request.form.get('customer_name'),
            rating=int(request.form.get('rating')),
            review_text=request.form.get('review_text'),
            service_type=request.form.get('service_type', ''),
            device_model=request.form.get('device_model', '')
        )
        
        db.session.add(review)
        db.session.commit()
        
        flash('Thank you for your review! It will be published after verification.', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        db.session.rollback()
        flash('Sorry, there was an error submitting your review. Please try again.', 'error')
        return redirect(url_for('index'))


@app.route('/appointment', methods=['POST'])
def book_appointment():
    """Handle appointment booking"""
    try:
        appointment = models.Appointment(
            customer_name=request.form.get('customer_name'),
            phone=request.form.get('phone'),
            email=request.form.get('email', ''),
            service_id=int(request.form.get('service_id')),
            device_id=request.form.get('device_id') and int(request.form.get('device_id')),
            preferred_date=datetime.strptime(request.form.get('preferred_date'), '%Y-%m-%dT%H:%M'),
            issue_description=request.form.get('issue_description', '')
        )
        
        db.session.add(appointment)
        db.session.commit()
        
        flash('Your appointment has been booked! We will confirm the time with you soon.', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        db.session.rollback()
        flash('Sorry, there was an error booking your appointment. Please try again.', 'error')
        return redirect(url_for('index'))


@app.route('/api/stats')
def get_stats():
    """API endpoint to get current business statistics"""
    stats = {}
    business_stats = models.BusinessStats.query.all()
    for stat in business_stats:
        stats[stat.stat_name] = stat.stat_value
    
    # Default stats if none exist
    if not stats:
        stats = {
            'repairs_completed': 2847,
            'happy_customers': 2156,
            'years_experience': 12,
            'success_rate': 98
        }
    
    return jsonify(stats)


@app.route('/api/reviews')
def get_reviews():
    """API endpoint to get published reviews"""
    reviews = models.Review.query.filter_by(is_published=True).order_by(models.Review.created_at.desc()).all()
    review_data = []
    
    for review in reviews:
        review_data.append({
            'customer_name': review.customer_name,
            'rating': review.rating,
            'review_text': review.review_text,
            'service_type': review.service_type or '',
            'device_model': review.device_model or '',
            'created_at': review.created_at.isoformat() if review.created_at else ''
        })
    
    return jsonify(review_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
