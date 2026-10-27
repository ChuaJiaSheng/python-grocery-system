# Python Grocery Ordering System

A terminal application for browsing groceries, building a shopping cart, and calculating a bill. Developed as EGE151 group coursework, it demonstrates Python dictionaries, sorting, input handling, and a menu-driven application.

**Stack:** Python 3 · standard library · in-memory data

## Features

- Browse the product catalogue by category, alphabetical order, or ascending price.
- Select quantities, view the cart, and remove an item.
- Calculate a 10% discount for a discount-card holder.
- Apply the coursework's historical **7% GST** after any discount.
- Display an itemised receipt and simulate payment confirmation.

## Run

From the repository root:

```sh
python src/main.py
```

No package installation or database is required. Use a terminal with interactive input. The program starts immediately when the script runs; it is not designed as an importable library.

## Example workflow

1. Choose **View Menu/Place Orders**.
2. Choose a sorting method, then enter the displayed item number and quantity.
3. Return to the main menu to inspect or edit the cart.
4. Select **Payment/Check Out** and answer the discount-card question.
5. Review the bill and confirm the simulated payment.

For example, a $10.00 subtotal becomes $9.00 after the 10% discount, then $9.63 with the preserved 7% GST calculation. These are the original assignment rules, not a current retail tax configuration.

## Source guide

| File or function | Responsibility |
| --- | --- |
| [src/main.py](src/main.py) | Catalogue, cart, menus, calculations, and checkout |
| `sort_category`, `sort_alphabetical`, `sort_price` | Build the three catalogue views |
| `view_order`, `remove_orders` | Display and edit the cart |
| `check_out`, `display_receipt`, `payment` | Calculate the bill and show the simulated checkout |

## Coursework limitations

The cart is lost when the process ends. Adding the same product again replaces that product's existing cart entry rather than accumulating its quantity. Quantity validation and navigation are basic; several menus call other menus recursively. No real payment, online ordering, stock control, or user accounts are implemented.

## Team

- **Chua Jia Sheng:** primary programming, code fixes, report sections, and presentation.
- **Thaddeus Leow:** flowchart, programming support, task coordination, testing, and presentation.
- **Bryant Lew:** programming support, report, testing, and presentation.

Thanks to Yu Cheng, Pyie Sone, and Mr Koh for assistance and feedback.
