total_amount = 90 + 100 + 500

print(f"cart total: {total_amount}")

if total_amount > 999:
  price_after_discount = total_amount * 70/100
  print(f"Pay amount: {price_after_discount}")
elif  499 < total_amount <= 999: #  999 <= price < 499
  price_after_discount = total_amount * 80/100
  print(f"Pay amount: {price_after_discount}")
else:
  print(f"Pay amount: {total_amount}")
