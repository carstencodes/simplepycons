#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class AdobeIllustratorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adobeillustrator"

    @property
    def original_file_name(self) -> "str":
        return "adobeillustrator.svg"

    @property
    def title(self) -> "str":
        return "Adobe Illustrator"

    @property
    def primary_color(self) -> "str":
        return "#FF9A00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Adobe Illustrator</title>
     <path d="M10.53
 10.73c-.1-.31-.19-.61-.29-.92-.1-.31-.19-.6-.27-.89-.08-.28-.15-.54-.22-.78h-.02c-.09.43-.2.86-.34
 1.29-.15.48-.3.98-.46 1.48-.14.51-.29.98-.44
 1.4h2.54c-.06-.211-.14-.46-.23-.721-.09-.269-.18-.559-.27-.859zM19.75.3H4.25C1.9.3
 0 2.2 0 4.55v14.9c0 2.35 1.9 4.25 4.25 4.25h15.5c2.35 0 4.25-1.9
 4.25-4.25V4.55C24 2.2 22.1.3 19.75.3zM14.7
 16.83h-2.091c-.069.01-.139-.04-.159-.11l-.82-2.38H7.91l-.76
 2.35c-.02.09-.1.15-.19.141H5.08c-.11 0-.14-.061-.11-.18L8.19
 7.38c.03-.1.06-.21.1-.33.04-.21.06-.43.06-.65-.01-.05.03-.1.08-.11h2.59c.08
 0 .12.03.13.08l3.65 10.3c.03.109 0 .16-.1.16zm3.4-.15c0
 .11-.039.16-.129.16H16.01c-.1
 0-.15-.061-.15-.16v-7.7c0-.1.041-.14.131-.14h1.98c.09 0
 .129.05.129.14v7.7zm-.209-9.03c-.231.24-.571.37-.911.35-.33.01-.65-.12-.891-.35-.23-.25-.35-.58-.34-.92-.01-.34.12-.66.359-.89.242-.23.562-.35.892-.35.391
 0 .689.12.91.35.22.24.34.56.33.89.01.34-.11.67-.349.92z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://developer.adobe.com/developer-distrib'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
