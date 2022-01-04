from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://footballteam.pl')

browser.find_element_by_xpath('//*[@id="buttons"]/div/button[1]').click()
browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[1]/div[1]').click()
username = browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[2]/div/form/div[1]/input')
password = browser.find_element_by_xpath('//*[@id="modal-login"]/div/div/div[2]/div/form/div[2]/input')
username.send_keys('granat29@vp.pl')
password.send_keys('qwerty123')
browser.find_element_by_xpath('//*[@id="btn-login"]').click()

browser.maximize_window()
browser.implicitly_wait(5)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/aside/ul/li[3]/a').click()


gra_ofensywna =     '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[2]/div/div[2]'
gra_defensywna =    '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[3]/div/div[2]'
rozgrywanie =       '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[4]/div/div[2]'
kondycja =          '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[5]/div/div[2]'
czytanie_gry =      '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[6]/div/div[2]'
pressing =          '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[2]'
stale_fragmenty =   '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[2]'
skutecznosc =       '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[9]/div/div[2]'


strzaly = wslizgi = kreatywnosc = wydolnosc = sprint = zwinnosc = rzuty_wolne = celnosc =                                   '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[2]/div[2]'
drybling = przewidywanie = dosrodkowania = wytrzymalosc = skocznosc = agresja = rzuty_karne = precyzja =                    '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[3]/div[2]'
atak = wznawianie_gry = przeglad_pola = regeneracja = _6_zmysl = przyspieszenie = rzuty_rozne = gra_z_kontry =              '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[4]/div[2]'
balans = opanowanie = przetrzymanie = oszczedzanie_energii = pulapki_offsidowe = poswiecenie = kontrola_pilki = technika =  '/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div[5]/div[2]'


def train_skill(xpath):
    bttn_xpath = xpath + '/button'
    skill = browser.find_element_by_xpath(xpath)
    action = ActionChains(browser).move_to_element(skill)
    action.perform()
    bttn = browser.find_element_by_xpath(bttn_xpath)
    browser.execute_script("arguments[0].click();", bttn)


def training(name_training1, num_of_training1, name_training2, num_of_training2):
    training1_counter = 0
    training2_counter = 0
    while training1_counter < num_of_training1 or training2_counter < num_of_training2:
        if training1_counter < num_of_training1:
            try:
                train_skill(name_training1)
                training1_counter += 1
            except:
                pass
        if training2_counter < num_of_training2:
            try:
                train_skill(name_training2)
                training2_counter += 1
            except:
                pass


if __name__ == '__main__':
    #train_skill(kondycja)
    training(kreatywnosc, 2000, przeglad_pola, 2000)
