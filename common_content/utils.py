from .models import SiteConfiguration


def get_site_config():
    """
    :return: Site configuration model
    """
    return SiteConfiguration.get_solo()
