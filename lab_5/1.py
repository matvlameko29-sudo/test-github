def shorten_text(text):
    while '(' in text:
        start = text.find('(')
        end = text.find(')',)
        fragment = text[start:end + 1]
        text = text.replace(fragment, '')

    return ' '.join(text.split())
text = "Падал (куда он там падал) прошлогодний снег"
print(shorten_text(text))