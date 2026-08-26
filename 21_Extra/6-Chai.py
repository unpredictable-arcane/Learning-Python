chai_type = "Adrak chai"
customer_name = "Anuj"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:4]}")
print(f"Last word: {chai_description[7:]}")
print(f"Last word: {chai_description[::-1]}")

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")

print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")

decoded_label = ecoded_label.decode("utf-8")

print(f"Decoded label: {decoded_label}")