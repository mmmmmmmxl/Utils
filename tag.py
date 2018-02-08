#coding: utf-8


def tag(name, *content, cls=None, **attrs):
    """
    To generate HTML Tag with prototype
    :param name:
    :param cls:
    :param content:
    :param attrs:
    :return:
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


#How to Call this method
print(tag('br'))
# <br />
print(tag('p', 'hello'))
# <p>hello</p>
print(tag('p', 'hello', 'world'))
# <p>hello</p>
# <p>world</p>
print(tag('p', 'hello', id=33))
# <p id="33">hello</p>
print(tag('p', 'hello', 'world', cls='sidebar'))
# <p class="sidebar">hello</p>
# <p class="sidebar">world</p>
my_tag = {"name": "img", "title": "Sunset Boulevard",
          "src": "sunset.jpg", "cls": "framed"}
print(tag(**my_tag))
# <img class="framed" src="sunset.jpg" title="Sunset Boulevard" />