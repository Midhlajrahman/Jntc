from django import template

register = template.Library()


@register.filter
def highlight_word(value, words):
    if not words:
        return value

    try:
        value.index(words)
        value = value.split(words)
        value = f'<span class="blue_color">{words}</span>'.join(value)
        return value
    except Exception:
        words = words.split()
        for word in words:
            value = value.split(word)
            value = f'<span class="blue_color">{word}</span>'.join(value)
        return value
