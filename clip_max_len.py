def clip(text, max_len=50, sign=' '):
    """
    在max_len前面或后面第一个指定符号处截断文本（默认为空格）
    :param text:
    :param max_len:
    :return:
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(sign, 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(sign, max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

a = '12312345 64613212315634641321 354321324'
print(clip(a))