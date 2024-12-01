from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def get_title_message():
    # Setup the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    message = ""
    

    # Extract the last opponent (adjust the CSS selector accordingly)
    #home = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__first-tn-ed.imso_mh__tnal-cont.imso-tnol > div.imso_mh__tm-nm.imso-medium-font.imso_mh__tm-nm-ew > div > span')
    #home_score = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__scr-sep > div > div > div.imso_mh__l-tm-sc.imso_mh__scr-it.imso-light-font')
    #away = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__second-tn-ed.imso_mh__tnal-cont.imso-tnol > div.imso_mh__tm-nm.imso-medium-font.imso_mh__tm-nm-ew > div > span')  # Example selector
    #away_score = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__scr-sep > div > div > div.imso_mh__r-tm-sc.imso_mh__scr-it.imso-light-font')  # Example selector

    try:
        # Navigate to the FlashScore page for Tottenham's last match
        driver.get("https://www.google.com/search?q=tottenham+latest+score&sca_esv=5b98c83cfd2f6de0&sxsrf=ADLYWIKQ6htOciVchnNw2J5hQxKBTmB3pA%3A1733015108544&ei=RLZLZ8DqIMb67_UPprHVgAc&oq=tottenham+latest&gs_lp=Egxnd3Mtd2l6LXNlcnAiEHRvdHRlbmhhbSBsYXRlc3QqAggBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLAUj9XFCUHFjIO3ACeACQAQCYAWmgAaUMqgEEMTQuM7gBAcgBAPgBAZgCEqAClAyoAhPCAgoQIxiABBgnGIoFwgIFEAAYgATCAgYQABgWGB7CAgcQIxgnGOoCwgITEAAYgAQYQxi0AhiKBRjqAtgBAcICFhAuGIAEGEMYtAIYyAMYigUY6gLYAQHCAhwQLhiABBhDGLQCGMcBGMgDGIoFGOoCGK8B2AEBwgIMECMYgAQYExgnGIoFwgIOEAAYgAQYsQMYgwEYigXCAgoQABiABBhDGIoFwgIPECMYgAQYJxiKBRhGGP0BwgIEEAAYA8ICEBAuGIAEGEMYxwEYigUYrwHCAhkQABiABBiKBRhGGP0BGJcFGIwFGN0E2AEBwgILEAAYgAQYsQMYgwHCAggQLhiABBixA8ICERAuGIAEGLEDGNEDGIMBGMcBwgILEC4YgAQYxwEYrwHCAggQABiABBixA8ICDhAuGIAEGMcBGMsBGK8BwgIIEC4YgAQYywHCAgcQIxiwAxgnwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAhkQLhiABBiwAxhDGMcBGMgDGIoFGK8B2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICBBAjGCfCAgUQLhiABMICChAAGIAEGBQYhwKYAweIBgGQBhG6BgYIARABGAGSBwQxMi42oAem2gE&sclient=gws-wiz-serp")
        #driver.get("https://www.google.com/search?q=arsenal+latest+score&sca_esv=5b98c83cfd2f6de0&sxsrf=ADLYWIJOranX2zJ6sQO-XVVwYEPLZm9TGw%3A1733017710057&ei=bsBLZ4GXA8Cfi-gPz_eCyA4&ved=0ahUKEwiBhv2HuoWKAxXAzwIHHc-7AOkQ4dUDCA8&uact=5&oq=arsenal+latest+score&gs_lp=Egxnd3Mtd2l6LXNlcnAiFGFyc2VuYWwgbGF0ZXN0IHNjb3JlMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB5IlSBQhghYmB5wAngBkAEAmAFdoAGmBaoBATi4AQPIAQD4AQGYAgqgAscFwgIKEAAYsAMY1gQYR8ICDRAuGIAEGLADGEMYigXCAg0QABiABBiwAxhDGIoFwgIIEAAYExgHGB7CAg0QABgTGAcYHhhGGP0BwgIZEAAYExgHGB4YRhj9ARiXBRiMBRjdBNgBAZgDAIgGAZAGCroGBggBEAEYE5IHAjEwoAeyOA&sclient=gws-wiz-serp")
        driver.implicitly_wait(10)
        
        home = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__first-tn-ed.imso_mh__tnal-cont.imso-tnol > div.imso_mh__tm-nm.imso-medium-font.imso_mh__tm-nm-ew > div > span')
        home_score = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__scr-sep > div > div > div.imso_mh__l-tm-sc.imso_mh__scr-it.imso-light-font')
        away = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__second-tn-ed.imso_mh__tnal-cont.imso-tnol > div.imso_mh__tm-nm.imso-medium-font.imso_mh__tm-nm-ew > div > span')  # Example selector
        away_score = driver.find_element(By.CSS_SELECTOR, '#sports-app > div > div:nth-child(3) > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.imso_mh__tm-a-sts > div.imso-ani.imso_mh__tas > div > div.imso_mh__scr-sep > div > div > div.imso_mh__r-tm-sc.imso_mh__scr-it.imso-light-font')  # Example selector

        # Print the extracted text for debugging
        #print(f"Home Team: {home.text}")
        #print(f"Home Score: {home_score.text}")
        #print(f"Away Team: {away.text}")
        #print(f"Away Score: {away_score.text}")

        if home.text == "Tottenham":
            opponent = away.text
        else:
            opponent = home.text

        if (home.text == "Tottenham" and int(home_score.text) > int(away_score.text)) or (away.text == "Tottenham" and int(away_score.text) > int(home_score.text)):
            message = "Congrats Tottenham finally won and you still need a bit of motivation, beeing a Tottenham fan must be hard."
        elif (home.text == "Tottenham" and int(home_score.text) == int(away_score.text)) or (away.text == "Tottenham" and int(away_score.text) == int(home_score.text)):
            message = f"Tottenham draw against {opponent}, you must feel desapointed"
        elif (home.text == "Tottenham" and int(home_score.text) < int(away_score.text)) or (away.text == "Tottenham" and int(away_score.text) < int(home_score.text)):
            message = f"Tottenham was humiliated by {opponent}, take your daily dose of motivational pills"

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    return message

def update_index(result):
    with open('index.html', 'r') as file:
        html_content = file.read()
    
    #Extract the current text inside the dynamic-message div
    current_phrase = re.search(r'<div class="text" id="dynamic_title-message">(.+?)</div>', html_content)
    if current_phrase:
        old_phrase = current_phrase.group(1)
        print(f"Old phrase: {old_phrase}")

    # Replace the old phrase with the new result
    updated_html = html_content.replace(
        f'<div class="text" id="dynamic_title-message">{old_phrase}</div>',
        f'<div class="text" id="dynamic_title-message">{result}</div>')
    
    with open('index.html', 'w') as file:
        file.write(updated_html)


result = get_title_message()
print(result)
update_index(result)



