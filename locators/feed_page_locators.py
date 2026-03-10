from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_HEADER = (
        By.XPATH,
        "//*[contains(@class,'OrderFeed') or contains(@class,'orderFeed')]",
    )

    IN_PROGRESS_SECTION = (
        By.XPATH,
        "//*[contains(normalize-space(),'В работе')]/ancestor::*[self::section or self::div][1]",
    )
    IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//*[contains(normalize-space(),'В работе')]/ancestor::*[self::section or self::div][1]"
        "//li//p[contains(@class,'digits') or contains(@class,'Digits')]",
    )

    TOTAL_DONE = (
        By.XPATH,
        "//*[contains(normalize-space(),'Выполнено за все время')]/following-sibling::*[1]",
    )
    TODAY_DONE = (
        By.XPATH,
        "//*[contains(normalize-space(),'Выполнено за сегодня')]/following-sibling::*[1]",
    )
    