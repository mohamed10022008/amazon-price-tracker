from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.com/Headset-Microphone-Headphones-Surround-Playstation/dp/B09H74FXNW/ref=sr" \
      "_1_8?keywords=gamin"\
      "g+headsets&pd_rd_r=397d0cd6-0c01-4af8-a1fc-fb47dc6ecdff&pd_rd_w=agcde&pd_rd_wg=0HQkv&pf_" \
      "rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=S5CJRYE0NYWFFV1HQR95&qid=1653684108&sr=8-8"

hdr = {
    "Accept-Language": "fr-FR;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

# request:
response = requests.get(url, headers=hdr)
code_page = response.text

# beautiful soup
bs = BeautifulSoup(code_page, "html.parser")
price = bs.find("span", class_="a-offscreen")
price_text = price.get_text()
price_float = price_text.split("$")[1]
price_as_float = float(price_float)
product_name = bs.find("h1", class_="a-size-large product-title-word-break").get_text()

price_buy = 356.0
# print(price_as_float) 😎😎 it works
# smtp

if price_as_float < price_buy:
    message = f"{product_name} is now {price_text}"
    # print(message)
    with smtplib.SMTP("Smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("pythond450@gmail.com", "mohamed123456789")
        connection.sendmail(
            from_addr="pythond450@gmail.com",
            to_addrs="pythond450@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
