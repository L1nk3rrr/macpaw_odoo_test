# macpaw_odoo_test Repository
This repository contains a custom module, "account_paid_bills", for Odoo.

## Installation

To include the "macpaw_odoo_test" repository and its modules in your Odoo instance, follow these steps:

1. Clone the repository to your local machine or server: `git clone https://github.com/L1nk3rrr/macpaw_odoo_test`


2. Add a path to your configuration file or cli command:
   `addons_path = /path/to/odoo/addons/,/path/to/macpaw_odoo_test/`


3. Restart your Odoo server for the changes to take effect.
4. Install `account_paid_bills` via apps menu
5. Enjoy!

## Usage
Once the **macpaw_odoo_test** repository is included in your Odoo instance, you can use the `account_paid_bills` module to retrieve paid bills by date range using the **Paid Bills** wizard. Here's how to use it:

1. Log in to your Odoo instance with sufficient access rights (Billing, `account.group_account_invoice`).

2. **Invoicing** -> **Vendors** -> **Paid Bills** to access the functionality.

3. Select **Date From** and **Date To**.
4. Click on the "**View Bills**" button to fetch the paid bills that fall within the specified date range.
5. The results will be displayed on a tree view, showing the relevant vendor bills that have been paid(or paid partialy).