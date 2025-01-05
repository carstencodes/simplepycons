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


class EsotericSoftwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "esotericsoftware"

    @property
    def original_file_name(self) -> "str":
        return "esotericsoftware.svg"

    @property
    def title(self) -> "str":
        return "Esoteric Software"

    @property
    def primary_color(self) -> "str":
        return "#3FA9F5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Esoteric Software</title>
     <path d="M23.97 9.88C22.3 2.25 15.71-.68 10.15.13 4.37.97-.62
 5.83.06 13.34c.28 3.08 1.85 5.97 4.17 7.94 2.58 2.2 6.08 3.16 9.39
 2.53.08-.02.14-.1.12-.18
 0-.04-.08-.06-.16-.05-3.18.42-6.51-.65-8.87-2.86a11.222 11.222 0 0
 1-3.48-7.09C.66 6.99 5.42 2.51 10.64 1.97c4.25-.44 8.79 1.91 10.68
 6.76.16.41-.08.81-.5.89-2.92.54-12.51 2.34-14.43
 2.7-.17.03-.32-.08-.32-.26-.12-6.02 5.96-8.55
 10.45-4.79.06.05.26.01.32-.05.03-.03.04-.22-.02-.28-5.39-5.33-13.24-.85-12.8
 6.39.03.44.43.74.85.69l12.33-1.64c0 .08.02.14.02.14.37 6.24-5.86
 8.98-10.43 5.15-.06-.05-.24-.03-.29.03-.02.03-.07.19 0 .25 5.25 5.19
 12.85 1.06 12.81-5.86l3.38-.45c.85-.11 1.47-.91 1.28-1.77Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://esotericsoftware.com/forum/d/25405-sh'''

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
