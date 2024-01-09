from bs4 import BeautifulSoup
from locust import HttpUser, task, constant, TaskSet    #http istekleri gösdermek için eklenir
from locust.exception import RescheduleTask
import random

def getSearchdata():
    data =['ayakkabı', 'telefon']

    return data[random.randint(0, (len(data)-1))]



class LocustFile(TaskSet):
    wait_time = constant(1)   #her istekten sonra belli bir bekleme süresi koymak istersek sabit için constant kullanılır ya da
                              # between(0.5, 2.5) dersek bu aralıklarda atar requestleri .


    @task
    def get_users(self):
    #@task  #bu userın görev olarak algılanması için buraya tag eklemeliyiz
        #with self.client.get("/", name="Post Search") as response: # buraya istek gönder ve response değişkenine at
        #    print(response.status_code())

        #with self.client.get("/", name="first page") as response:
        #     print(response)
        #self.client.get("/config.json", name="ConfigJson")
        #self.client.get("https://api.n11.com/entries", name="Entries", verify=False)
        #self.client.get("/prod.html", name="ProdHtml")
        #with self.client.post("arama", name="POST_View", json={"text":"deneme"}) as response:
        #    if response.status_code == 400:
        #        print(response)
        #self.client.post("https://api.demoblaze.com/addtocart", name="POST_AddToCart", json={"id":"e83fcc75-801e-53ff-e9f1-bf470cf1a2d4","cookie":"user=d408a36d-88c4-396f-4dcb-8811ad9ff028","prod_id":"1","flag":"false"}, verify=False)

        #random_text = self.client.post("arama", json={"searchData": "sdjnsdjds"})
        with self.client.get("/", name="Search", catch_response=True) as response:   #succes ile bu requestin success döndüğünü söylicem ama
            if response.status_code == 200:                                   # catch_response ture yazmazsak bunu kullanamayız
                print(response.status_code)
    @task
    def get_n11(self):
        random_text = self.getSearchdata()
        with self.client.get("/arama", params={"q": random_text}, name="Get Search Key" +random_text+ "for search bar", catch_response=True) as searchresponse:   #succes ile bu requestin success döndüğünü söylicem ama                                   # catch_response ture yazmazsak bunu kullanamayız
                print(searchresponse)

class UserBehavior(HttpUser):
    task_set = LocustFile
    min_wait = 50000
    max_wait = 90000
    host = "https://www.n11.com/"
