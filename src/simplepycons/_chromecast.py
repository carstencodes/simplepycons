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


class ChromecastIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chromecast"

    @property
    def original_file_name(self) -> "str":
        return "chromecast.svg"

    @property
    def title(self) -> "str":
        return "Chromecast"

    @property
    def primary_color(self) -> "str":
        return "#999999"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chromecast</title>
     <path d="M0
 18.5455v3.2727h3.2727c0-1.811-1.4618-3.2727-3.2727-3.2727zm0-4.3637v2.1818c3.011
 0 5.4545 2.4437 5.4545
 5.4546h2.1819c0-4.2218-3.4146-7.6364-7.6364-7.6364zm0-4.3636V12c5.4218
 0 9.8182 4.3964 9.8182
 9.8182H12c0-6.6327-5.3782-12-12-12zm21.8182-7.6364H2.1818C.9818
 2.1818 0 3.1636 0
 4.3636v3.2728h2.1818V4.3636h19.6364v15.2728h-7.6364v2.1818h7.6364c1.2
 0 2.1818-.9818
 2.1818-2.1818V4.3636c0-1.2-.9818-2.1818-2.1818-2.1818Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.google.com/intl/en_us/chromecast/'''

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
            "Google Cast",
        ]
