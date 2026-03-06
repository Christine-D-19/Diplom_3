from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a[1]")
    FEED_LINK = (By.XPATH, "//p[normalize-space()='Лента заказов']/ancestor::a[1]")

    CONSTRUCTOR_HEADER = (
        By.XPATH,
        "//*[self::h1 or self::h2][contains(normalize-space(),'Соберите бургер')]",
    )

    FIRST_BUN = (
        By.XPATH,
        "(//h2[normalize-space()='Булки']/following::*//a[contains(@href,'/ingredient/')])[1]",
    )
    FIRST_NOT_BUN = (
        By.XPATH,
        "(//h2[normalize-space()='Соусы']/following::*//a[contains(@href,'/ingredient/')])[1]",
    )
    FIRST_NOT_BUN_FALLBACK = (
        By.XPATH,
        "(//h2[normalize-space()='Начинки']/following::*//a[contains(@href,'/ingredient/')])[1]",
    )

    FIRST_INGREDIENT = FIRST_NOT_BUN

    INGREDIENT_COUNTER_IN_CARD = (
        By.XPATH,
        ".//p[contains(@class,'counter') or contains(@class,'Counter')]",
    )

    CONSTRUCTOR_DROPZONE = (
        By.XPATH,
        "//*[contains(@class,'BurgerConstructor')]",
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[.//span[normalize-space()='Войти в аккаунт'] or normalize-space()='Войти в аккаунт']",
    )
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[.//span[normalize-space()='Оформить заказ'] or normalize-space()='Оформить заказ']",
    )

    INGREDIENT_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal') or contains(@class,'Modal')]",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close') or contains(@class,'modal__close')]",
    )

    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal') or contains(@class,'Modal')]",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//p[contains(@class,'digits') or contains(@class,'Digits') or contains(@class,'Modal_modal__title')]",
    )
    