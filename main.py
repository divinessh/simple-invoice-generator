# Created by Divinessh

def generate_invoice():
    print("\n****SIMPLE INVOICE GENERATOR****\n")
    customer_name = input("Customer Name: ")
    date = input("Date (DD/MM/YYYY): ")

    items = []
    while True:
        item = input("Enter item name (or type 'complete' to finish): ")
        if item.lower() == 'complete':
            break
        price = float(input(f"Enter price for '{item}': RM "))
        quantity = int(input(f"Enter quantity for '{item}': "))
        items.append((item, price, quantity))

    subtotal = sum(price * qty for _, price, qty in items)
    tax_rate = 0.06  # 6% SST
    tax = subtotal * tax_rate
    total = subtotal + tax

    invoice_lines = [
        "\n****INVOICE****",
        f"Customer: {customer_name}",
        f"Date: {date}\n",
        f"{'Item':20}{'Price (RM)':>12}{'Qty':>6}{'Total (RM)':>14}"
    ]

    for item, price, qty in items:
        line_total = price * qty
        invoice_lines.append(f"{item:20}{price:12.2f}{qty:6}{line_total:14.2f}")

    invoice_lines += [
        "\n",
        f"Subtotal: RM{subtotal:.2f}",
        f"Tax (6%): RM{tax:.2f}",
        f"Total: RM{total:.2f}",
        "\nThank you for your purchase!"
    ]

    with open("invoice.txt", "w") as f:
        for line in invoice_lines:
            f.write(line + "\n")

    print("\nInvoice generated successfully as 'invoice.txt'.")

if __name__ == "__main__":
    generate_invoice()
