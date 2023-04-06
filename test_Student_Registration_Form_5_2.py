from selene.support.shared import browser
from selene import be, have



def test_google_search(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_no_result(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('trdcyt4yfvfjcegkiup').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск не дал результатов по запросу')