"""REST API - TODO Implementation"""
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

class Database:
    """TODO: Database operations"""
    def __init__(self, db_name="items.db"):
        """TODO: Initialize database"""
        pass
    
    def create_table(self):
        """TODO: Create items table"""
        pass
    
    def get_all_items(self):
        """TODO: Get all items"""
        pass
    
    def get_item(self, item_id):
        """TODO: Get item by ID"""
        pass
    
    def create_item(self, name, description, price):
        """TODO: Create new item"""
        pass
    
    def update_item(self, item_id, name, description, price):
        """TODO: Update item"""
        pass
    
    def delete_item(self, item_id):
        """TODO: Delete item"""
        pass

@app.route('/api/items', methods=['GET'])
def get_items():
    """TODO: GET all items"""
    pass

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """TODO: GET item by ID"""
    pass

@app.route('/api/items', methods=['POST'])
def create_item():
    """TODO: POST create item"""
    pass

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """TODO: PUT update item"""
    pass

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """TODO: DELETE item"""
    pass

if __name__ == '__main__':
    app.run(debug=True)
