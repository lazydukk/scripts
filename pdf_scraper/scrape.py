import requests


def scrape_pages(start, end):
    for i in range(start, end + 1):
        url = f"https://drive.apluseducation.lk/pdf/pdf/PDF/AJ/2025/MS/2025-{i}.pdf"
        response = requests.get(url, verify=False)

        # Save the content to a file
        with open(f"data/{i}.pdf", "wb") as file:
            file.write(response.content)
            file.close()
        print(f"File downloaded: {i}")

        # Sleep for a random interval between 2 and 60 seconds
        # time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    scrape_pages(1, 54)
