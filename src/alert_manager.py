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
print(alerts)

print("Total Alerts:")
print(len(alerts))

print("Backup Alerts:")
print(backup)



