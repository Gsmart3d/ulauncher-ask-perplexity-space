import webbrowser
import subprocess
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction

SPACE_URL = "https://www.perplexity.ai/spaces/tiktok-script-v2-O4iFN2DETmu2cgwU7Ez1gQ"

class PerplexityExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()

        if not query:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Ask TikTok Script Space',
                    description='Tape ta question après le mot-clé',
                    on_enter=OpenUrlAction(SPACE_URL)
                )
            ])

        # Copie la question dans le presse-papier puis ouvre l'espace
        return RenderResultListAction([
            ExtensionResultItem(
                icon='images/icon.png',
                name=f'Question: {query}',
                description='Entrée → Ouvre l\'espace + copie la question (Ctrl+V pour coller)',
                on_enter=CopyToClipboardAction(query)
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name='Ouvrir l\'espace TikTok Script',
                description='Ouvre l\'espace Perplexity',
                on_enter=OpenUrlAction(SPACE_URL)
            )
        ])

if __name__ == '__main__':
    PerplexityExtension().run()
