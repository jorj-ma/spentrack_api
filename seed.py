from app import create_app, db
from app.models import Category

def seed_data():
    app=create_app()
    with app.app_context():
        categories = [
            "Food and Groceries", "Housing", "Healthcare", "Education",
            "Transportation", "Utilities", "Shopping", "Communication",
            "Savings", "Personal Care", "Entertainment", "Miscellaneous"
        ]

        print("Seeding database...")
        for name in categories:
            if not Category.query.filter_by(name=name).first():
                category = Category(name=name)
                db.session.add(category)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()