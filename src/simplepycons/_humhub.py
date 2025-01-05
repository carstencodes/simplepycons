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


class HumhubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "humhub"

    @property
    def original_file_name(self) -> "str":
        return "humhub.svg"

    @property
    def title(self) -> "str":
        return "HumHub"

    @property
    def primary_color(self) -> "str":
        return "#1B8291"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HumHub</title>
     <path d="M23.709
 7.7807c.1014-1.6778-.888-3.2298-2.4515-3.8452L11.9448.2695c-1.5655-.616-3.3488-.152-4.418
 1.1463l-6.36 7.731C.0988 10.4444-.01 12.2912.8934 13.7087l5.387
 8.4632c.9035 1.4175 2.6273 2.1289 4.2557
 1.7076l9.6853-2.5096c1.627-.4213 2.7889-1.88
 2.8903-3.5591l.0879-2.1924s.1657-1.3038-1.3694-1.3255c-1.1307-.0149-.9867.9616-1.9753
 1.5676-.7933.4862-3.3583.7263-4.0237-1.93 0 0-.7784-2.3331.704-4.4944
 1.481-2.1613 3.1675-1.0124 3.8255-.0967 1.3099 1.8238 3.252.9866
 3.2386-.3828z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/humhub/documentation/blob/'''

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
