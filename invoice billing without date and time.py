customer_name=input("Enter Customer Name: ")
num_items=int(input("Enter the number of products purchased: "))
invoice=[]
grand_total=0
sub_total=0
for i in range(num_items):
    print(f"\nItem {i+1}")
    product=input("Item Name: ")
    quantity=int(input("Qty: "))
    price=float(input("Price: "))
    total=quantity*price
    sub_total+=total  
    invoice.append([product,quantity,price,total])
gst=(sub_total*18)/100
grand_total=sub_total+gst

invoice_text="\n"
invoice_text+="===== TECH SHOP =====\n"
invoice_text+=f"Customer: {customer_name}\n"
invoice_text+="\n"
invoice_text+="{:<20}{:<10}{:<10}{:<10}\n".format("Item","Qty","Price","Total")
invoice_text+="-"*50+"\n"
print("invoice",invoice)
for item in invoice:
    invoice_text += "{:<20} {:<10} {:<10} {:<10}\n".format( item[0], item[1], item[2], item[3])
invoice_text+="-"*50+"\n"
invoice_text+=f"Subtotal : Rs.{sub_total}\n"
invoice_text+=f"GST (18%) : Rs.{gst}\n"
invoice_text+=f"Grand Total : Rs.{grand_total}\n"

print(invoice_text)

filename=f"invoice.txt"
with open(filename,"w") as file:
    file.write(invoice_text)
print(f"Invoice saved to {filename}")