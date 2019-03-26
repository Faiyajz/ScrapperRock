import csv,time
from requests_html import HTMLSession

csv_file = open('scrappingRock.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(
    ['Brand', 'Year', 'Model', 'Engine', 'Category', 'Sub-Category', 'Manufacturer', 'Part Number', 'Type', 'Price'])

proxies = {
    "https": "https://103.91.128.49:47768",
    "http": "https://103.91.128.49:47768"
}

session = HTMLSession()
url = 'https://www.rockauto.com'
response = session.get(url, proxies=proxies)
print("1")

brands = response.html.find('.navlabellink.nvoffset.nnormal')

for brand in brands[2:3]:
    # print(brand.attrs['href'])
    url = 'https://www.rockauto.com' + brand.attrs['href']
    response = session.get(url, proxies=proxies)
    print("2")
    time.sleep(5)
    years = response.html.find('.navlabellink.nvoffset.nnormal')
    for year in years[1:]: #[1:2]
        # print(year.attrs['href'])
        url = 'https://www.rockauto.com' + year.attrs['href']
        response = session.get(url, proxies=proxies)
        print("3")
        time.sleep(5)
        models = response.html.find('.navlabellink.nvoffset.nnormal')
        for model in models[2:]:  # [2:3]
            # print(model.attrs['href'])
            url = 'https://www.rockauto.com' + model.attrs['href']
            response = session.get(url, proxies=proxies)
            print("4")
            time.sleep(5)
            engines = response.html.find('.navlabellink.nvoffset.nnormal')
            for engine in engines[3:]:  # [3:4]
                # print(engine.attrs['href'])
                url = 'https://www.rockauto.com' + engine.attrs['href']
                response = session.get(url, proxies=proxies)
                print("5")
                time.sleep(5)
                categories = response.html.find('.navlabellink.nvoffset.nnormal')
                for category in categories[4:]:  # [4:5]
                    # print(category.attrs['href'])
                    url = 'https://www.rockauto.com' + category.attrs['href']
                    response = session.get(url, proxies=proxies)
                    print("6")
                    time.sleep(5)
                    subCategories = response.html.find('.navlabellink.nvoffset.nimportant')
                    if len(subCategories) == 0:
                        subCategories = response.html.find('.navlabellink.nvoffset.nnormal')

                    for subCategory in subCategories[5:]:  # [0:1]
                        # print(subCategory.attrs['href'])
                        url = 'https://www.rockauto.com' + subCategory.attrs['href']
                        response = session.get(url, proxies=proxies)
                        print("7")
                        time.sleep(5)
                        manufacturers = response.html.find('.listing-inner')
                        for manufacturer in manufacturers:
                            productManufacturer = manufacturer.find('.listing-final-manufacturer', first=True).text
                            print(productManufacturer)

                            productPartNumber = manufacturer.find('.listing-final-partnumber', first=True).text
                            print(productPartNumber)

                            productType = manufacturer.find('.span-link-underline-remover', first=True)
                            if productType is None:
                                productType = 'N/A'
                                print(productType)
                            else:
                                productType = productType.text
                                print(productType)

                            productPrice = manufacturer.find('.ra-formatted-amount', first=True).text
                            print(productPrice)
                            print("-----------------------")
                            csv_writer.writerow(
                                [brand.text, year.text, model.text, engine.text, category.text, subCategory.text,
                                 productManufacturer, productPartNumber, productType, productPrice])

csv_file.close()
