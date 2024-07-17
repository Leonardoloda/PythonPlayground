class Messenger:
    STOCK_PATTERN = "[STOCK]"
    DIFF_PATTERN = "[DIFF]"
    HEADLINE_PATTERN = "[HEADLINE]"
    BRIEF_PATTERN = "[BRIEF]"

    TEMPLATE = f"""
    {STOCK_PATTERN}: {DIFF_PATTERN}
    Headline: {HEADLINE_PATTERN}
    Brief: {BRIEF_PATTERN}
    """

    def __init__(self):
        pass

    def format_diff(self, diff: float):
        if diff > 0:
            return f"🔺{diff:.2f}%"

        if diff < 0:
            return f"🔻{diff:.2f}%"

    def create_message(self, stock: str, diff: float, headline: str, brief: str):
        message_with_stock = self.TEMPLATE.replace(self.STOCK_PATTERN, stock)
        message_with_diff = message_with_stock.replace(self.DIFF_PATTERN, self.format_diff(diff))
        message_with_headline = message_with_diff.replace(self.HEADLINE_PATTERN, headline)
        message = message_with_headline.replace(self.BRIEF_PATTERN, brief)

        return message
