"""
Database Migration Script - Add Archive and Notes Features
Run this to update your existing database with new fields
"""

from app import app, db
from models import Task

def migrate_database():
    with app.app_context():
        # Check if columns exist, if not add them
        try:
            # Try to access the columns
            test_task = Task.query.first()
            if test_task:
                _ = test_task.archived
                _ = test_task.notes
            print("✅ Database already has archived and notes columns")
        except Exception as e:
            print("Adding new columns to database...")
            
            # Add columns using raw SQL
            with db.engine.connect() as conn:
                try:
                    conn.execute(db.text("ALTER TABLE task ADD COLUMN archived BOOLEAN DEFAULT 0"))
                    print("✅ Added 'archived' column")
                except:
                    print("⚠️  'archived' column might already exist")
                
                try:
                    conn.execute(db.text("ALTER TABLE task ADD COLUMN notes TEXT"))
                    print("✅ Added 'notes' column")
                except:
                    print("⚠️  'notes' column might already exist")
                
                conn.commit()
            
            print("\n✅ Migration complete!")
            print("Your database is now updated with archive and notes features.")

if __name__ == '__main__':
    print("="*60)
    print("  DATABASE MIGRATION: Archive & Notes Features")
    print("="*60)
    print("\nThis will add 'archived' and 'notes' columns to your tasks.")
    print("Your existing tasks will not be affected.\n")
    
    response = input("Continue with migration? (yes/no): ").strip().lower()
    
    if response == 'yes':
        migrate_database()
    else:
        print("\n❌ Migration cancelled")
