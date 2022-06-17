"""
Вспомогательные методы для форм
"""


def get_form_controls_class( form_control_class: str = '' ) -> str:
    """
    Получить имена классов для компонентов формы

    :param form_control_class: дополнительный класс
    :return: классы стилей bootstrap
    """
    return f'form-control form-control-sm {form_control_class}'


def get_form_control_helper( help_text: str, custom_class: str = '' ) -> str:
    """
    Получить вспомогательный текст для компонента формы, обернутый в <small> с заготовленными классами
    
    :param help_text: текст, который в дальнейшем будет распечатан
    :param custom_class: дополнительный класс
    :return: подписи к компонентам формы
    """
    return f'<small class="form-text text-muted {custom_class}">{help_text}</small>'
