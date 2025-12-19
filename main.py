import webbrowser
import pyperclip
import time
import pyautogui
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

SPACE_URL = "https://www.perplexity.ai/spaces/tiktok-script-v2-O4iFN2DETmu2cgwU7Ez1gQ"

class PerplexityExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()

        if not query:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Ask TikTok Script Space',
                    description='Tape ta question',
                    on_enter=ExtensionCustomAction({'action': 'open', 'query': ''})
                )
            ])

        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name=f'{query}',
                description='Entrée pour poser dans ton espace',
                on_enter=ExtensionCustomAction({'action': 'search', 'query': query})
            )
        ])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        
        if data['action'] == 'search':
            query = data['query']
            
            # Copie la question dans le presse-papier
            pyperclip.copy(query)
            
            # Ouvre l'espace
            webbrowser.open(SPACE_URL)
            
            # Attend le chargement
            time.sleep(3)
            
            # Clique au centre de l'écran
            screen_width, screen_height = pyautogui.size()
            pyautogui.click(screen_width // 2, screen_height // 2)
            
            # Attend un peu
            time.sleep(0.5)
            
            # Ctrl+V pour coller
            pyautogui.hotkey('ctrl', 'v')
            
            # Entrée pour envoyer
            time.sleep(0.3)
            pyautogui.press('enter')

if __name__ == '__main__':
    PerplexityExtension().run()
