#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
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


class PantheonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pantheon"

    @property
    def original_file_name(self) -> "str":
        return "pantheon.svg"

    @property
    def title(self) -> "str":
        return "Pantheon"

    @property
    def primary_color(self) -> "str":
        return "#FFDC28"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pantheon</title>
     <path d="M7.604 0L9.75 5.171H7.018l.904 2.276h5.535zm4.202
 7.973l.724 1.752h3.09c.066 0 .223-.086.223-.877
 0-.79-.157-.875-.224-.875zm-4.367 0c-.306 0-.474
 0-.612.456-.166.544-.185 1.571-.185 3.57 0 2 .02 3.028.185
 3.572.138.456.306.456.612.456h3.486l-1.727-4.202v.014l-.816-2.116h1.912l.884
 2.119 1.826-.016-1.591-3.853zm5.235 2.1l.724 1.753h2.562c.068 0
 .223-.086.223-.876s-.156-.876-.223-.876zm-3.742.076l2.633
 6.403H8.346L14.297
 24l-2.146-5.172h2.731l-.913-2.276H12.7l-2.634-6.403zm2.374 2.026l.724
 1.752h3.93c.067 0 .223-.086.223-.876s-.155-.876-.223-.876zm.868
 2.1l.723 1.752h2.722c.067 0
 .223-.085.223-.875s-.156-.876-.223-.876zm4.624
 1.2v.511h.103v-.391l.129.391h.096l.125-.391v.391h.107v-.511h-.15l-.127.394-.127-.394zm-.466
 0v.092h.144v.42h.117v-.42h.144v-.092z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://projects.invisionapp.com/boards/8UOJQ'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://projects.invisionapp.com/boards/8UOJQ'''

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
