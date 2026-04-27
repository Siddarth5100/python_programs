'''
Q1. Python — Dictionary + Iteration (Frappe context)
A Frappe site has Sales Invoice and Payment records. Write a program that:
Uses the payments list to calculate how much each customer has already paid
Subtracts paid amount from each invoice's grand_total to find remaining balance per customer
Classifies each customer as "Fully Paid", "Partial", or "No Payment" based on whether they've paid everything, something, or nothing
Build a dictionary with customer name as key and a dict of billed, paid, remaining, status as value
Print only "Partial" and "No Payment" customers, sorted by remaining balance descending
'''

invoices = [
   {"name": "SINV-001", "customer": "Lakshmi Textiles", "grand_total": 25000},
   {"name": "SINV-002", "customer": "KPR Mills",        "grand_total": 40000},
   {"name": "SINV-003", "customer": "Lakshmi Textiles", "grand_total": 30000},
   {"name": "SINV-004", "customer": "Premier Mills",    "grand_total": 60000},
   {"name": "SINV-005", "customer": "KPR Mills",        "grand_total": 50000},
   {"name": "SINV-006", "customer": "Sangam Exports",   "grand_total": 20000},
]

payments = [
   {"customer": "Lakshmi Textiles", "amount": 25000},
   {"customer": "Lakshmi Textiles", "amount": 10000},
   {"customer": "KPR Mills",        "amount": 90000},
   {"customer": "Premier Mills",    "amount": 30000},
]


# Expected output:

'''
{
 "Premier Mills": {
   "billed": 60000, "paid": 30000, "remaining": 30000, "status": "Partial"
 },
"Lakshmi Textiles": {
   "billed": 55000, "paid": 35000, "remaining": 20000, "status": "Partial"
 },
 "Sangam Exports": {
   "billed": 20000, "paid": 0, "remaining": 20000, "status": "No Payment"
 }
}
'''

overall_report = {}
total_billed = 0 
total_paid = 0
total_remaining = 0
status = ["Fully Paid", "Partial", "No Payment"]


for name in invoices:
    if not name["customer"] in overall_report:
        overall_report[name["customer"]] = {}    
        overall_report[name["customer"]]["billed"] = 0
        overall_report[name["customer"]]["paid"] = 0
        overall_report[name["customer"]]["remaining"] = 0
        overall_report[name["customer"]]["status"] = "NA"



print(overall_report)