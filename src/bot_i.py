from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):

        self.not_following_back = []
        self.driver = webdriver.Chrome(
            '/Users/anshul/Documents/Python_bot/chromedriver')
        self.driver.set_window_size(1520,1580)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
            .send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pw)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")\
            .click()
        sleep(4)

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
            .click()

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()

    def get_unfollowers(self):
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span")\
            .click()

        sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]")\
            .click()

        sleep(2)
        following = self._get_names()
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]")\
            .click()
        followers = self._get_names()
        not_following_back = [
            user for user in following if user not in followers]

        print("\n")

        for i in not_following_back:
            print(i)
            print("\n")
        print(len(not_following_back))
        

    def _get_names(self):
        sleep(2)


        SCROLL_PAUSE_TIME = 0.3


        #Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
        # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        sleep(3)

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()

        sleep(2)

        return names


my_bot = InstaBot('lifeofanshul', 'Dubb')
my_bot.get_unfollowers()
print(len(my_bot.not_following_back))
"""
laurierlibrary
wlurecreation
wlu_locus.mus.sci
lauriercriticalthinkers
laurierinnovationsociety
leftrightwlu
goteam2019
mariana.cardonaa
wlufrenchclub
radiolaurier
spc_card
w_bluemystics_wlu
tmlaurier
wlu_rotaract
thefuturebollywood
wlupartylife
canadianpartylife
laurierswimming
wlumindfulnessclub
surolaurier
wlucsa
laurierpsychologysociety
wlunaturalhealth
cplgirls
laurierfootball
realestatewlu
codemasterjii
lauriertutors
thegoldenhackofficial
laurierinsurance
xleratelazaridis
siblaurier
thelinkwlu
enactuslaurier
lauriereconclub
fullsendlaurier
wlu_fossa
wlu.23
error69
sheeksfreaks
thegreattrail
visit_niagara
lalitshokeen1515
nerd_jfpb
punjabimojojojo
canadiancurrydating
cnnbusiness
karo_startup
coolageapp
miltonpubliclibrary
thereadinglamp
goldenspeakersclub
collegefessingcanada
blackberry
blackberrystudentlife
wlu_universityaffairs
nayi_dilli.45
emoboisofindia
briemussell
ria_butera
allielancaster
tech.millionaire
laptop.empire
elusiveprospects
grindfunnel
gaurgopaldas
_beautyremedies
_.shambhala
laurierdatascience
themoneymakingpage
wlu_bookstore
wacampusclubs
laurierwellness
laurierfoodservices
papa_programmer
programmingofficial
ai_basics
codinganddecoding
coding_boy_
geeks_for_geeks
coderhumor
learn.machinelearning
python.coder_
python.hub
ai_machine_learning
programmer.me
cp24breakingnews
wluphi
stefan.bukarica
uwlaurierindianconfessions
uwindianca
singhvijender
startuplaurier
laurieronecard
wluconcourse
wlu_ateam_w
locuswaterloo
recklesswaterloo_
zakirkhan_208
arieshoroscopes
consentisgolden
lifeofpaaji
thesavage_indian
blogto
tube.indian
katrinakaif
teslamotors
zodiac.secrets
goldenhawkcouncil
wlu_firstyearproject
yourstudentsunion
__stupid_pd__
theindianidiot
streetsoftoronto
explorecanada
canada
torontolife
ontariotravel
curiocitytoronto
narcitycanada
bajpayee.manoj
laurierinternational
explorewaterlooregion
waterloo_memes
wluathletics
wilfridlaurieruni
narendramodi
oye.student
varshaa.s15
statistics_maps
dwarkawala
pearlpill
timesnow
pratishthachuphal
sharma_jee_ka_ladka__
lamborghini
marketing.stories
virat.kohli
_shwetzrawat_
sid_artworks
himanshusolanki07
lifestylekingsmotivation
lakshayykaushik
lucrativ.co
billionaire.mindset
rvcjinsta
manvigoell
knitik78
gahlot_kunal_
abhishekahlawat2000
deepak_mla
flevi___25
harshitsaxenahh
yukkttaaa
raman.paradox
sunmeeeeeeet
whyavyanwhy
sharma_jee_ka_ladka_
_boompal_
bhavyakochhar77
"""