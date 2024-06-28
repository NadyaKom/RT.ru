class RegPageLoc:
    LOCATOR_REG_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_BUTTON_REGISTRATION = (By.NAME, 'register')
    LOCATOR_REGISTRATION_CODE_FIELD = (By.CLASS_NAME, 'card-container__title')

    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_INPUT_FIELD = (By.XPATH, '//input[contains(@class, "rt-input__input")]')
