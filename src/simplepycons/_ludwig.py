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


class LudwigIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ludwig"

    @property
    def original_file_name(self) -> "str":
        return "ludwig.svg"

    @property
    def title(self) -> "str":
        return "Ludwig"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ludwig</title>
     <path d="M0 0h24v24H0V0Zm13.714
 10.286V3.429h-3.428v10.285H20.57V3.43h-3.428v6.857h-3.429Zm-6.857
 6.857V3.429H3.43V20.57h17.14v-3.428H6.857Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ludwig-ai/ludwig-docs/blob'''

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
