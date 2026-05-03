"""
ABSTRACT FACTORY PATTERN
Use case: Create families of related UI components (Mobile vs Web)
"""

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def on_click(self) -> str:
        pass


class AlertDialog(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def show(self, message: str) -> str:
        pass


class MobileButton(Button):
    def render(self) -> str:
        return "  Rendering a mobile-friendly touch button"
    
    def on_click(self) -> str:
        return "  Mobile button tapped - event triggered"


class MobileAlertDialog(AlertDialog):
    def render(self) -> str:
        return "  Rendering a bottom-sheet alert dialog for mobile"
    
    def show(self, message: str) -> str:
        return f"  Mobile alert showing: {message}"


class WebButton(Button):
    def render(self) -> str:
        return "  Rendering an HTML/CSS button"
    
    def on_click(self) -> str:
        return "  Web button clicked - JavaScript event fired"


class WebAlertDialog(AlertDialog):
    def render(self) -> str:
        return "  Rendering a modal dialog for web"
    
    def show(self, message: str) -> str:
        return f"  Web alert showing: {message}"


class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_alert_dialog(self) -> AlertDialog:
        pass


class MobileUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MobileButton()
    
    def create_alert_dialog(self) -> AlertDialog:
        return MobileAlertDialog()


class WebUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WebButton()
    
    def create_alert_dialog(self) -> AlertDialog:
        return WebAlertDialog()


def render_ui(factory: UIFactory) -> None:
    button = factory.create_button()
    dialog = factory.create_alert_dialog()
    
    print(button.render())
    print(button.on_click())
    print(dialog.render())
    print(dialog.show("Bin is 95% full!"))


if __name__ == "__main__":
    print("=== Abstract Factory Pattern Demo ===")
    
    print("\n--- Mobile UI ---")
    render_ui(MobileUIFactory())
    
    print("\n--- Web UI ---")
    render_ui(WebUIFactory())
    
    print("\n✅ Abstract Factory Pattern works!")