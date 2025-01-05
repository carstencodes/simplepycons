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


class EricssonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ericsson"

    @property
    def original_file_name(self) -> "str":
        return "ericsson.svg"

    @property
    def title(self) -> "str":
        return "Ericsson"

    @property
    def primary_color(self) -> "str":
        return "#0082F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ericsson</title>
     <path d="M20.76 1.593A2.36 2.36 0 0 0
 19.572.225c-.54-.27-1.188-.336-2.256.02L5.187
 4.29c-1.068.357-1.548.795-1.818 1.338a2.36 2.36 0 0 0 1.059
 3.174c.54.27 1.188.336 2.256-.021l12.129-4.044c1.068-.354 1.548-.795
 1.818-1.338a2.35 2.35 0 0 0 .13-1.806zm0 7.485a2.36 2.36 0 0
 0-1.188-1.368c-.54-.27-1.188-.336-2.256.021L5.187
 11.775c-1.068.357-1.548.795-1.818 1.338a2.36 2.36 0 0 0 1.059
 3.174c.54.27 1.188.336 2.256-.021l12.129-4.041c1.068-.357 1.548-.795
 1.818-1.341a2.35 2.35 0 0 0 .13-1.806zm0 7.488a2.36 2.36 0 0
 0-1.188-1.368c-.54-.27-1.188-.336-2.256.021L5.187
 19.263c-1.068.357-1.548.795-1.818 1.338a2.36 2.36 0 0 0 1.059
 3.174c.54.27 1.188.336 2.256-.02l12.129-4.045c1.068-.354 1.548-.795
 1.818-1.338a2.35 2.35 0 0 0 .13-1.806z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://mediabank.ericsson.net/admin/mb/?h=db'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.ericsson.com/en/newsroom/media-ki'''

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
