import csv
import requests

results = []

with open('Intern.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)

    for row in reader:
        url = row.get('urls')

        if not url:
            continue

        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            print(f"{url} → {status}")

        except requests.exceptions.Timeout:
            status = "Timeout"
            print(f"{url} → Timeout")

        except requests.exceptions.InvalidURL:
            status = "Invalid URL"
            print(f"{url} → Invalid URL")

        except requests.exceptions.ConnectionError:
            status = "Connection Error"
            print(f"{url} → Connection Error")

        except Exception as e:
            status = "Error"
            print(f"{url} → Error: {e}")

        results.append({"url": url, "status": status})


with open('output.csv', 'w', newline='', encoding='utf-8') as out:
    writer = csv.DictWriter(out, fieldnames=["url", "status"])
    writer.writeheader()
    writer.writerows(results)

print("\n Results saved to output.csv")