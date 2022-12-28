from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = 'https://br.betano.com/sport/futebol/jogos-de-hoje/'
path = '/home/enacom/Downloads/chromedriver_linux64/chromedriver' #introduce your file's path inside '...'

driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(1) #add implicit wait, if necessary
close_add = driver.find_element(By.CSS_SELECTOR, '#landing-page-modal > div > div.sb-modal__close > button > svg')
close_add.click()
accept_cookies = driver.find_element(By.CSS_SELECTOR, 'body > div.root-wrapper.root-wrapper--handheld.upcoming24h-route-page > div > section.main-content-wrapper > div.sticky-notification.sticky-notification--bottom > div > div.sticky-notification__actions-container > button:nth-child(2)')
accept_cookies.click()
time.sleep(1)


teams = []
x12 = [] #3-way
odds_events = []

#select only upcoming matches box
# box = driver.find_element(By.CSS_SELECTOR, 'body > div.root-wrapper.root-wrapper--handheld.upcoming24h-route-page > div > section.main-content-wrapper > div.grid__row.main-content-wrapper__content > div.grid__column.grid__column--fluid.grid__column__main-content > section > div.league-page')
league_page = driver.find_elements(By.CLASS_NAME, 'events-list__grid')[0]
events = league_page.find_elements(By.CLASS_NAME, 'events-list__grid__event')[0]
info = events.find_elements(By.CLASS_NAME, 'events-list__grid__info')[0]
box = info.find_elements(By.CLASS_NAME, 'events-list__grid__info__main__participants__participant-name')
print(len(box))
time.sleep(2)

# <a href="/odds/swetes-fc-sap-fc/30451441/" class="GTM-event-link events-list__grid__info__main" title="Antígua e Barbuda - Premier League"><div class="events-list__grid__info__main__row"><div class="events-list__grid__info__main__participants"><div class="events-list__grid__info__main__participants__participant"><span class="events-list__grid__info__main__participants__participant-name"><!---->
#                   Swetes FC
#                   <!----></span> <!----></div><div class="events-list__grid__info__main__participants__participant"><span class="events-list__grid__info__main__participants__participant-name"><!---->
#                   Sap FC
#                   <!----></span> <!----></div> <!----></div> <div class="events-list__grid__info__main__actions"><span class="event-icons tw-m-0 tw-ml-[6px]"><!----> <!----> <!----> <!----> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" svg-inline="" role="presentation" focusable="false" tabindex="-1" class="tw-text-n-48-slate tw-m-0 tw-ml-[6px] tw-fill-current kz-icon-sxs has-tooltip" data-original-title="null"><path d="M2.667 1.333c-.737 0-1.334.597-1.334 1.334v10.666c0 .737.597 1.334 1.334 1.334h10.666c.737 0 1.334-.597 1.334-1.334V2.667c0-.737-.597-1.334-1.334-1.334H2.667zm4.666 3c0-.184.15-.333.334-.333h1C8.85 4 9 4.15 9 4.333V12H7.333V4.333zM4.333 7c0-.184.15-.333.334-.333h1C5.85 6.667 6 6.816 6 7v5H4.333V7zm6 2c0-.184.15-.333.334-.333h1c.184 0 .333.149.333.333v3h-1.667V9z" clip-rule="evenodd"></path></svg> <!----> <!----> <!----></span> <!----></div></div> <!----></a>

# <div class="events-list__grid__info__main__participants"><div class="events-list__grid__info__main__participants__participant"><span class="events-list__grid__info__main__participants__participant-name"><!---->
#                   Swetes FC
#                   <!----></span> <!----></div><div class="events-list__grid__info__main__participants__participant"><span class="events-list__grid__info__main__participants__participant-name"><!---->
#                   Sap FC
#                   <!----></span> <!----></div> <!----></div>