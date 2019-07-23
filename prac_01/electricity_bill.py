TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator 2.0")
tariff = int(input("Which tariff? 11 or 31?"))
if tariff == 11 :
    tariff = TARIFF_11
elif tariff == 31:
    tariff = TARIFF_31
daily_Use = float(input("Enter daily use in kWh: "))
number_Of_Days = int(input("Enter number of billing days: "))
total = tariff  * daily_Use * number_Of_Days
print("Estimated bill: ", total)