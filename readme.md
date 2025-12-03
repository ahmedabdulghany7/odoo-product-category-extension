# Real Estate – Product Category Website Address Extension

This Odoo 18 module adds a custom text field (250 chars) to the Product Category form inside:

Inventory → Configuration → Product Categories

The new field is labeled “Website Address”, allowing users to store any location URL or descriptive text related to the category.

## Features

- Adds a new Char field (`location_address`) to the `product.category` model.  
- Field length: **250 characters**.  
- Appears **under the Parent Category** field on the form view.  
- Adds the field to the **tree (list) view** for better visibility.  
- Fully compatible with **Odoo 18**.  
- Simple, modular, and easy to extend.


## Installation

1. Copy the module folder into:  
   `/odoo/addons/`

2. Restart the Odoo server:  
   `sudo systemctl restart odoo`

3. Activate **Developer Mode**.

4. Go to:  
   `Apps → Update Apps List`

5. Search for **Real Estate** and install it.

## Usage

1. Navigate to:  
   `Inventory → Configuration → Product Categories`

2. Open any category or create a new one.  

3. You will see a field named **Website Address** below the “Parent Category” field.  

4. Enter any text or link (up to 250 characters).  

5. The value also shows in the list/tree view for quick reference.


## Module Structure

```
app_one/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── product_category.py
├── views/
│  └── product_category_views.xml
└── security/
    └── ir.model.access.csv

```

## Configuration

### Database Setup

The module expects the following PostgreSQL configuration:

- **Host**: localhost
- **Port**: 5432
- **Database User**: odoo18
- **Database Password**: odoo18

Update your `odoo.conf` file with appropriate credentials for your environment.


## Author

**Ahmed Abdulghany**

## License

LGPL-3

## Version

18.0.1.0.0

## Support

For issues, questions, or contributions, please contact the module author.

---

**Note**: This module is designed specifically for Odoo 18.0 and may require modifications for compatibility with other versions.