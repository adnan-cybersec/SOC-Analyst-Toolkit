alerts = [
    "LOW - Failed login",
    "HIGH - Malware detected",
    "MEDIUM - Suspicious login",
    "HIGH - Brute force detected"
]
alerts.append("MEDIUM - Unusual outbound traffic")

backup = alerts[:]

alerts.append("HIGH - Unauthorized access attempt")

print("SOC ALERT MANAGEMENT SYSTEM")
print("---------------------------")

print("Original Alerts:")
for alert in alerts:
	print(alert)

print("Total Alerts:")
print(len(alerts))

print("Backup Alerts:")
for alert in backup:
	print(alert)