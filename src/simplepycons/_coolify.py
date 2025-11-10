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


class CoolifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coolify"

    @property
    def original_file_name(self) -> "str":
        return "coolify.svg"

    @property
    def title(self) -> "str":
        return "Coolify"

    @property
    def primary_color(self) -> "str":
        return "#6B16ED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coolify</title>
     <path d="M4.364 4.364V0h17.454v4.364zm0 13.09H0V4.365h4.364zm0
 0h17.454v4.364H4.364ZM6.545 6.546v-1.7H22.3V2.182H24v4.363zm0
 0v10.4h-1.7v-10.4ZM3.882 17.936v1.7h-1.7v-1.7ZM24
 24H6.545v-1.7H22.3v-2.664H24Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/coollabsio/coolify/blob/ac
1d98f6035caff10f36fa10508326b4791dec07/public/coolify-logo-monochrome.'''

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
