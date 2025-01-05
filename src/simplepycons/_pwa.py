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


class PwaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pwa"

    @property
    def original_file_name(self) -> "str":
        return "pwa.svg"

    @property
    def title(self) -> "str":
        return "PWA"

    @property
    def primary_color(self) -> "str":
        return "#5A0FC8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PWA</title>
     <path d="M20.5967 7.482L24
 16.518h-2.5098l-.5816-1.6184h-3.2452l.6933-1.7532h2.0019l-.95-2.6597
 1.1881-3.0047zm-8.111 0l1.7722 5.8393L16.75 7.482h2.4154l-3.6433
 9.036h-2.3833l-1.6395-5.2366-1.7196 5.2366h-2.377l-1.233-2.1161
 1.2144-3.7415 1.342 2.6609 1.9029-5.8393h1.8566zm-8.7453 0c1.0635 0
 1.8713.3055 2.4234.9166a2.647 2.647 0 01.2806.3684l-1.0753
 3.3128-.3847
 1.1854c-.352.1006-.7533.1509-1.204.1509H2.2928v3.102H0V7.482zm-.5816
 1.7532h-.866v2.4276h.8597c.5577 0 .9406-.1194
 1.1485-.3582.1896-.215.2845-.5058.2845-.8724
 0-.364-.1079-.6544-.3235-.8714-.2157-.217-.5834-.3256-1.1032-.3256z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/webmaxru/progressive-web-a'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/webmaxru/progressive-web-a
pps-logo/blob/77744cd5c0a4d484bb3d082c6ac458c44202da03/pwalogo-white.s'''

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
        yield from [
            "Progressive Web Application",
        ]
