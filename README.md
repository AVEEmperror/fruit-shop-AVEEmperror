# Fruit Shop

A fruit shop sells fruits. The exact type of the fruits are stored in the `products.yml` file, which contains the name of a fruit,
its code to be entered at checkout, the unit price in € and the unit (kilograms or items).

Write a program that asks for a customer name and the name of bought products. Then the program repeatedly asks for a product code,
prints a product name and expected unit, and asks for an amount. When the checkout is finished and the purchase summary
(names of the bought products, their quantities, the price rounded to cents, and the total amount to pay) is printed.
Then the procedure is repeated for the next customer.

At the end of the day (ending with a customer named “`END`”) write how many customers were processed, the total money earned and
the name of the customer who paid the most (as well as the amount paid).

## Example

```
Enter the name of the first customer ("END" to end): Joaquim

How many different fruits Joaquim buys? 2

Enter the product code: 01

Joaquim is buying Bananas.
Enter amount [kg]: 1.25

Enter the product code: 02

Joaquim is buying Kiwis.
Enter amount [items]: 2

Joaquim's purchase summary:
Bananas, 1.250 kg: 1.24 EUR
Kiwis, 2.000 items: 2.44 EUR
Total: 3.68 EUR

Enter the next person's name ("END" to end): Jorge

How many different fruits Jorge buys? 1

Enter the product code: 04

Joaquim is buying Peaches.
Enter amount [kg]: 2.2

Jorge's purchase summary:
Peaches, 2.200 kg: 3.85 EUR
Total: 3.85 EUR

Enter the next person's name ("END" to end): END

Processed 2 customers
Joaquim was the one who paid the most: 3.68 EUR
Earned: 7.53 EUR
```

You may use `input` and `print` for user interaction. However, bear in mind that in the future someone may ask you to change
the program to a graphical one. For this reason, all the user interaction must be placed in separate functions, which you will
be able to replace on request.
