from django import template

register = template.Library()


@register.filter('phone_number_filter')
def phone_number_filter(value):
    new_value = ''
    if value:
        # для узбекский номер

        if len(value) == 9:
            new_value = value[:2] + ' ' + value[2:5] + ' ' + value[5:7] + ' ' + value[7:]
        elif len(value) == 13:
            new_value = value[:4] + ' ' + value[4:6] + ' ' + value[6:9] + ' ' + value[9:11] + ' ' + value[11:]

        #для российский номер

        elif len(value) == 12:
            new_value = value[:2] + ' ' + value[2:5] + ' ' + value[5:8] + ' ' + value[8:10] + ' ' + value[10:]
        elif len(value) == 11:
            new_value = value[:1] + ' ' + value[1:4] + ' ' + value[4:7] + ' ' + value[7:9] + ' ' + value[9:]

    return new_value

