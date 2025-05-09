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


class BinanceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "binance"

    @property
    def original_file_name(self) -> "str":
        return "binance.svg"

    @property
    def title(self) -> "str":
        return "Binance"

    @property
    def primary_color(self) -> "str":
        return "#F0B90B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Binance</title>
     <path d="M16.624 13.9202l2.7175 2.7154-7.353 7.353-7.353-7.352
 2.7175-2.7164 4.6355 4.6595 4.6356-4.6595zm4.6366-4.6366L24
 12l-2.7154 2.7164L18.5682 12l2.6924-2.7164zm-9.272.001l2.7163
 2.6914-2.7164 2.7174v-.001L9.2721
 12l2.7164-2.7154zm-9.2722-.001L5.4088 12l-2.6914 2.6924L0
 12l2.7164-2.7164zM11.9885.0115l7.353 7.329-2.7174
 2.7154-4.6356-4.6356-4.6355 4.6595-2.7174-2.7154 7.353-7.353z" />
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
