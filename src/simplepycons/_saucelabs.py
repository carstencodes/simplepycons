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


class SauceLabsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "saucelabs"

    @property
    def original_file_name(self) -> "str":
        return "saucelabs.svg"

    @property
    def title(self) -> "str":
        return "Sauce Labs"

    @property
    def primary_color(self) -> "str":
        return "#3DDC91"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sauce Labs</title>
     <path d="M23.4337
 7.344c-.5641-.7664-1.469-1.2197-2.4343-1.2197H13.999L11.9993
 12h4.8377l-1.9998 5.8755H9.9995l-1.9997 5.8755h9.0001c1.2912 0
 2.438-.8086 2.8466-2.0088L23.846
 9.9922c.3049-.8957.1518-1.8807-.4123-2.647Zm-13.434
 4.655H7.1618l1.9997-5.8756h4.8378l2.001-5.8743H7c-1.2912
 0-2.438.8086-2.8466 2.0089L.154 14.0079c-.3049.8956-.1518 1.8807.4123
 2.647.5641.7663 1.469 1.2196 2.4343
 1.2196h7.0004l1.9998-5.8755H10.001z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
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
