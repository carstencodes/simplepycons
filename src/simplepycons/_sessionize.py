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


class SessionizeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sessionize"

    @property
    def original_file_name(self) -> "str":
        return "sessionize.svg"

    @property
    def title(self) -> "str":
        return "Sessionize"

    @property
    def primary_color(self) -> "str":
        return "#1AB394"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sessionize</title>
     <path d="M12 0c6.628 0 12 5.372 12 12v10c0 1.097-.903 2-2
 2h-7.5l-.001-.169c-.049-2.894-1.347-4.902-3.709-5.96L24
 12l-.32-.109c-2.858-.999-5.251-2.462-7.18-4.391-1.928-1.928-3.392-4.322-4.391-7.181L12
 0 4 18c0 .667.167 1.167.5 1.5.334.334.834.5 1.5.5l.187.001c3.771.04
 5.313 1.295 5.313 3.999H2c-1.097 0-2-.903-2-2V2C0 .903.903 0 2
 0h10Zm7.207 4.793c-.781-.781-1.73-1.097-2.121-.707-.39.39-.074
 1.34.707 2.121.781.781 1.731 1.098
 2.121.707.391-.39.074-1.34-.707-2.121Z" />
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
