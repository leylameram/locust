@task
def search(self):
    search_key_list = ['telefon', 'bilgisayar']
    search_key = random.choice(search_key_list)
    response = self.client.get("https://www.gittigidiyor.com/arama/?k=" + search_key + "")

    pq = BeautifulSoup(response.content, "html.parser")
    for link in pq.find_all("ul", attrs={"class": "catalog-view clearfix products-container"}):
        list.append(link.li.a["href"])

    global product_link
    product_link = random.choice(list)
