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


class ShanghaiMetroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shanghaimetro"

    @property
    def original_file_name(self) -> "str":
        return "shanghaimetro.svg"

    @property
    def title(self) -> "str":
        return "Shanghai Metro"

    @property
    def primary_color(self) -> "str":
        return "#EC1C24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shanghai Metro</title>
     <path d="M20.383 11.664h-1.716l-3.432-4.487-3.073 3.606L9.31
 7.177l-3.513 4.487H3.63c.185-4.464 3.872-8.047 8.383-8.047 3.953 0
 7.27 2.748 8.15 6.424h3.687C22.91 4.359 17.96.01 12 .01c-6.632 0-12
 5.369-12 12 0 1.102.15 2.169.429 3.177h6.516l2.412-2.55 2.805 3.478
 2.945-3.502 1.902 2.61h2.69c-1.287 2.967-4.256 5.495-7.699 5.495-2.84
 0-5.357-1.681-6.875-3.942H.997C2.852 21.02 7.072 23.988 12
 23.988c6.632 0 12-5.368 12-12 0-.116 0-.231-.012-.347l-3.605.023Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Shanghai_M'''

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
