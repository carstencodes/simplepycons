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


class SharpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sharp"

    @property
    def original_file_name(self) -> "str":
        return "sharp.svg"

    @property
    def title(self) -> "str":
        return "sharp"

    @property
    def primary_color(self) -> "str":
        return "#99CC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>sharp</title>
     <path
 d="M14.2209.0875v5.9613l-3.7433.5012v3.5233l3.7433-.5012v3.5735l3.492-.4672V9.1047L24
 8.2634l-.4631-3.4613-5.824.7794V.0875zM6.287 1.145v5.9618L0
 7.9483l.4634 3.4613 5.8514-.7834 3.4644-.4637V1.145zm3.5198
 9.7185l-3.492.4675v3.578l-6.183.8276.4633 3.4613
 5.8239-.7796v5.4942h3.492v-5.962l3.6114-.4834V13.944l-3.7156.4973zm13.73
 1.7405l-5.824.779-3.492.4673v9.0179h3.492v-5.9618L24 16.0652Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/lovell/sharp/blob/315f519e'''

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
