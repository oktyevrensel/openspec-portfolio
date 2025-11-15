from flask import Blueprint, request, jsonify
from .models import Contact, Project, BlogPost
from . import db
from email_validator import validate_email, EmailNotValidError

api_bp = Blueprint('api', __name__)

def success_response(data=None, message="Success"):
    return jsonify({
        'success': True,
        'data': data,
        'message': message
    }), 200

def error_response(message="Error", errors=None, status_code=400):
    return jsonify({
        'success': False,
        'message': message,
        'errors': errors or []
    }), status_code

@api_bp.route('/health', methods=['GET'])
def health_check():
    return success_response({'status': 'healthy', 'version': '1.0.0'})

@api_bp.route('/contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        
        # Validation
        if not data.get('name') or len(data.get('name', '')) < 2:
            return error_response('Name must be at least 2 characters', ['name'])
        
        if not data.get('email'):
            return error_response('Email is required', ['email'])
        
        try:
            validate_email(data['email'])
        except EmailNotValidError:
            return error_response('Invalid email format', ['email'])
        
        if not data.get('message') or len(data.get('message', '')) < 10:
            return error_response('Message must be at least 10 characters', ['message'])
        
        # Create contact
        contact = Contact(
            name=data['name'],
            email=data['email'],
            subject=data.get('subject', ''),
            message=data['message'],
            ip_address=request.remote_addr
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return success_response(
            contact.to_dict(),
            'Thank you! Your message has been sent successfully.'
        ), 201
        
    except Exception as e:
        db.session.rollback()
        return error_response('Failed to submit contact form', [str(e)], 500)

@api_bp.route('/projects', methods=['GET'])
def get_projects():
    try:
        featured_only = request.args.get('featured', '').lower() == 'true'
        
        if featured_only:
            projects = Project.query.filter_by(featured=True).order_by(Project.created_at.desc()).all()
        else:
            projects = Project.query.order_by(Project.created_at.desc()).all()
        
        return success_response([project.to_dict() for project in projects])
    except Exception as e:
        return error_response('Failed to fetch projects', [str(e)], 500)

@api_bp.route('/projects/<slug>', methods=['GET'])
def get_project(slug):
    try:
        project = Project.query.filter_by(slug=slug).first()
        
        if not project:
            return error_response('Project not found', status_code=404)
        
        return success_response(project.to_dict())
    except Exception as e:
        return error_response('Failed to fetch project', [str(e)], 500)

@api_bp.route('/blog', methods=['GET'])
def get_blog_posts():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        category = request.args.get('category')
        tag = request.args.get('tag')
        
        query = BlogPost.query.filter_by(published=True)
        
        if category:
            query = query.filter_by(category=category)
        
        if tag:
            query = query.filter(BlogPost.tags.contains([tag]))
        
        total = query.count()
        posts = query.order_by(BlogPost.published_at.desc()).offset((page - 1) * limit).limit(limit).all()
        
        return success_response({
            'posts': [post.to_dict() for post in posts],
            'total': total,
            'page': page,
            'limit': limit,
            'total_pages': (total + limit - 1) // limit
        })
    except Exception as e:
        return error_response('Failed to fetch blog posts', [str(e)], 500)

@api_bp.route('/blog/<slug>', methods=['GET'])
def get_blog_post(slug):
    try:
        post = BlogPost.query.filter_by(slug=slug, published=True).first()
        
        if not post:
            return error_response('Blog post not found', status_code=404)
        
        return success_response(post.to_dict())
    except Exception as e:
        return error_response('Failed to fetch blog post', [str(e)], 500)
