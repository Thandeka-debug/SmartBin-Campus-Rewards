import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.abstract_factory import MobileUIFactory, WebUIFactory


def test_abstract_factory():
    print("\n=== Testing Abstract Factory Pattern ===")
    
    mobile_factory = MobileUIFactory()
    mobile_button = mobile_factory.create_button()
    mobile_dialog = mobile_factory.create_alert_dialog()
    
    assert "mobile" in mobile_button.render().lower()
    assert "mobile" in mobile_dialog.render().lower()
    print("✓ Mobile UI components created")
    
    web_factory = WebUIFactory()
    web_button = web_factory.create_button()
    web_dialog = web_factory.create_alert_dialog()
    
    assert "web" in web_button.render().lower() or "html" in web_button.render().lower()
    assert "web" in web_dialog.render().lower() or "modal" in web_dialog.render().lower()
    print("✓ Web UI components created")
    
    print("✅ Abstract Factory Pattern test passed!\n")


if __name__ == "__main__":
    test_abstract_factory()