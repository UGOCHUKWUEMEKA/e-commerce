# e-commerce
# E-Commerce Project

## Overview
This project is a full-featured e-commerce platform built using Django. It allows vendors to manage their products, buyers to browse and purchase items, and administrators to oversee the marketplace. The system provides authentication, product management, shopping cart functionality, order processing, and wishlist management.

## Features
### User Accounts
- User registration with email verification
- Secure authentication with JWT or session-based login
- Profile management with update functionalities
- Password reset and change options

### Product Management
- Vendors can create, update, and delete products
- Products categorized with filtering and search capabilities
- Image upload support for product listings
- Stock and inventory management

### Shopping Cart & Orders
- Users can add/remove products from the cart
- Real-time cart updates and checkout functionality
- Order placement with status tracking (Pending, Processing, Shipped, Delivered)
- Integration with payment gateways for transactions

### Wishlist
- Users can add products to their wishlist
- Wishlist persists for future visits
- Easy add-to-cart from wishlist

### Vendor Management
- Vendors can register and manage their stores
- Dashboard for tracking product performance and sales
- Order management and fulfillment tracking

### Administrator Dashboard
- User and vendor management
- Product approval workflow
- Order and sales analytics dashboard

## Project Structure
```
accounts/        # User authentication and profile management
cart/            # Shopping cart functionality
orders/          # Order processing and history
products/        # Product management and categories
vendors/         # Vendor-specific features and storefront management
wishlist/        # Wishlist functionality
ecommerce_project/  # Project settings and configurations
manage.py        # Django management script
db.sqlite3       # SQLite database file
requirements.txt  # Project dependencies
```

## Installation & Setup
### Prerequisites
- Python 3.8+
- Django 4.0+
- Virtual environment (recommended)
- PostgreSQL or MySQL (Optional for production use)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ecommerce_project.git
   cd ecommerce_project
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the application:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## API Endpoints
| Endpoint                  | Method | Description |
|---------------------------|--------|-------------|
| /api/products/            | GET    | List all products |
| /api/products/<id>/       | GET    | Get product details |
| /api/cart/                | GET    | View cart |
| /api/cart/add/            | POST   | Add item to cart |
| /api/orders/              | GET    | List user orders |
| /api/orders/<id>/         | GET    | View order details |
| /api/orders/create/       | POST   | Place a new order |
| /api/wishlist/            | GET    | View wishlist |
| /api/wishlist/add/        | POST   | Add item to wishlist |

## Contribution
Feel free to contribute by submitting issues or pull requests. To contribute:
1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## Deployment
For production use, consider deploying with:
- **Gunicorn & Nginx** for better performance
- **PostgreSQL** as the database instead of SQLite
- **Docker & Docker Compose** for containerization
- **CI/CD pipelines** for automated deployments

## License
This project is licensed under the MIT License.

