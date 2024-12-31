from flask import Blueprint, request
from flask_restful import Api, Resource
from app.models import Expense
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
import csv
import io
from datetime import datetime

expenses_bp = Blueprint('expenses', __name__)
api = Api(expenses_bp)

class ExpenseList(Resource):
    @jwt_required()
    def get(self):
        """
        Get all expenses for the authenticated user
        """
        user_id = get_jwt_identity()
        expenses = Expense.query.filter_by(user_id=user_id).all()
        return [{
            'id': expense.id,
            'date': expense.date.strftime('%Y-%m-%d'),
            'amount': expense.amount,
            'category': expense.category,
            'notes': expense.notes
        } for expense in expenses], 200

    @jwt_required()
    def post(self):
        data = request.form
        date_str = data.get('date')
        amount = data.get('amount')
        category = data.get('category')
        notes = data.get('notes', '')
        user_id = get_jwt_identity()

        try:
            date = datetime.strptime(date_str, '%d-%m-%Y').date()
        except ValueError:
            return {'message': 'Invalid date format. Use DD-MM-YYYY.'}, 400

        expense = Expense(
            date=date,
            amount=amount,
            category=category,
            notes=notes,
            user_id=user_id
        )
        db.session.add(expense)
        db.session.commit()
        return {'message': 'Expense added successfully'}, 201

class ExpenseUpload(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        if 'file' not in request.files:
            return {'message': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            return {'message': 'No selected file'}, 400
        if file and file.filename.endswith('.csv'):
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream)
            headers = next(csv_input)
            for row in csv_input:
                date_str, amount, category, notes = row
                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d').date()
                    amount = float(amount)
                except ValueError:
                    continue  # Skip invalid rows
                expense = Expense(
                    date=date,
                    amount=amount,
                    category=category,
                    notes=notes,
                    user_id=user_id
                )
                db.session.add(expense)
            db.session.commit()
            return {'message': 'Expenses uploaded successfully'}, 201
        else:
            return {'message': 'Invalid file format. Only CSV is allowed.'}, 400

api.add_resource(ExpenseList, '/')
api.add_resource(ExpenseUpload, '/upload')