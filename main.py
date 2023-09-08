"""
PLAYWRIGHT AUTOMATION
"""
from typing import Any, Literal, List
from playwright.sync_api import sync_playwright, Locator
from pyperclip import copy
from tools import capture_output, loop_iterable


class PLAYWRIGHT: # TODO: IMPLEMENT THIS CODE TO MY PACKAGE
    def __init__(self, url, browser:str=Literal['chromium', 'firefox', 'webkit'], headless:bool=True, timeout:int=None, **k):
        self.url = url
        self.elements = None
        self.p = sync_playwright().start()
        self.browser = browser
        self.headless = headless
        match self.browser:
            case 'chromium':
                self.browser = self.p.chromium.launch(headless=headless, timeout=timeout, **k)
            case 'firefox':
                self.browser = self.p.firefox.launch(headless=headless, timeout=timeout, **k)
            case 'webkit':
                self.browser = self.p.webkit.launch(headless=headless, timeout=timeout, **k)
        self.page = self.browser.new_page()
        self.page.goto(self.url)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return {
            'url' : self.url,
            'browser' : self.browser,
            'elements' : self.elements
        }

    def innerText(self) -> list[str]:
        """
        Returns the text within the elements found
        """
        return self.elements.all_inner_texts()
    
    def innerContent(self) -> list[str]:
        return self.elements.all_text_contents()
    
    def SEND_KEYS(self, keys:str=''):
        try:
            return self.elements.fill(keys)
        except:
            if not self.headless:
                return self.type(keys)
            else:
                pass
        return self
    
    def CLICK(self, click_count:int=None, delay:float=None, **k):
        return self.elements.click(click_count=click_count, delay=delay, **k)

    def CHECK(self, force:bool=None, **k):
        return self.elements.check(force=force, **k)
    
    def ALL(self):
        """
        **Usage**

        for li in await page.get_by_role('listitem').all():
        await li.click();
        for li in page.get_by_role('listitem').all():
        li.click();
        """
        return self.elements.all()
    
    def DOUBLE_CLICK(self, modifiers:List[Literal['Alt','Control','Meta','Shift']]=None, **k):
        return self.elements.dblclick(modifiers=modifiers, **k)
    
    def CLEAR(self, force:bool=None, **k):
        """
        Clear the input field
        """
        return self.elements.clear(force=force, **k)

    def DRAG_TO(self, target:Locator, force:bool=None, **k):
        self.elements.drag_to(target=target, force=force, **k)

    def FILTER(self, has_text:str=None, has:str=None, has_not_text:bool=None, has_not:str=None):
        self.elements.filter(has=has, has_not=has_not, has_not_text=has_not_text, has_text=has_text)
        return self
    
    def test(self):
        ... # TODO I still gotta implement the other methods

    def FIND_ELEMENT_BY_XPATH(self, xpath:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None):
        self.elements = self.page.locator(xpath, has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self
        
    def FIND_ELEMENT_BY_CLASS_NAME(self, class_name:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None): # NOTE can probably optimize this
        self.elements = self.page.locator(f'//*[@class="{class_name}"]', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self
        
    def FIND_ELEMENT_BY_CSS_SELECTOR(self, css_selector:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None):
        self.elements = self.page.locator(f'css={css_selector}', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self
        
    def FIND_ELEMENT_BY_ID(self, Id:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None):
        try:
            self.elements = self.page.locator(f'#{Id}', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        except:
            self.elements = self.page.locator(f'xpath=//[@id="{Id}"]', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self

    def FIND_ELEMENT_BY_LINK_TEXT(self, link_text:str):
        self.elements = self.page.get_by_role('link',name=link_text)
        return self
        
    def FIND_ELEMENT_BY_NAME(self, name:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None):
        self.elements = self.page.locator(f'xpath=//*[@name="{name}"]', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self
        
    def FIND_ELEMENT_BY_PARTIAL_LINK_TEXT(self, partial_link_text:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None):
        self.elements = self.page.locator(f'xpath=//*/a[text()="{partial_link_text}"]', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self
        
    def FIND_ELEMENT_BY_TAG_NAME(self, tag_name:str, *, has_text:str=None, has:str=None, has_not:str=None, has_not_text:str=None):
        self.elements = self.page.locator(f'xpath=//*/{tag_name}', has_text=has_text, has=has, has_not=has_not, has_not_text=has_not_text)
        return self

    def STOP(self) -> None:
        self.browser.close()
        self.p.stop()

if __name__ == '__main__':
    attributes: list[str] = 'xpath class_name css_selector Id link_text name partial_link_text tag_name'.split()
    play = PLAYWRIGHT('https://books.toscrape.com', 'chromium')
    play.FIND_ELEMENT_BY_XPATH('//h3/a')
    with open('info.txt','w') as file:
        data = capture_output(play.test, True)
        file.write(data)