# Python – Pizza Restaurant POS

Command-line POS system for a pizza restaurant. Takes orders, applies student discounts (if applicable), handles delivery vs. pickup (with tip and delivery fee logic), calculates HST, and writes a formatted receipt to disk.

## Features
- **Menu of 6 items**: Cheese, Pepperoni, Hawaiian, Canadian, Deluxe, Vegetarian  
- **Student discount**: 10% off subtotal  
- **Delivery options**: Tip prompt (5%, 10%, 15%) and $5 delivery fee if subtotal < $30 (waived otherwise)  
- **Tax**: HST at 13%  
- **Receipt output**: Prints to console and saves to a text file (`amazingEatsReciept.txt`)  
- **Branding**: Banner and messages for *Arnold’s Amazing Eats!*  

## How It Works
1. Enter customer details  
2. Add pizzas and quantities  
3. Choose **delivery** or **pickup**  
4. (Delivery only) Choose **tip amount** (5%, 10%, or 15%)  
5. Program calculates totals, applies discounts/fees, and generates a receipt  

The receipt is displayed in the console and saved as **`amazingEatsReciept.txt`** in the current folder.  

## Quick Start
```bash
# Run the program
python src/pos.py
