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


class AppleArcadeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "applearcade"

    @property
    def original_file_name(self) -> "str":
        return "applearcade.svg"

    @property
    def title(self) -> "str":
        return "Apple Arcade"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apple Arcade</title>
     <path d="M.198 18.24a.966.966 0 0
 1-.194-.571v-.955s0-.571.563-.313c0 0 6.919 3.135 8.033 3.626a7.832
 7.832 0 0 0 3.408.729 8.216 8.216 0 0 0
 3.396-.729l8.037-3.626c.559-.258.559.313.559.313v.955a1.038 1.038 0 0
 1-.198.575c-.19.258-.515.539-1.411.959-.713.337-6.23 2.818-6.995
 3.17a8.008 8.008 0 0 1-3.4.729 8.336 8.336 0 0
 1-3.82-.927c-1.435-.65-5.849-2.631-6.567-2.972-.9-.428-1.153-.654-1.411-.963zm1.411-5.973l6.987-3.17a7.975
 7.975 0 0 1 2.164-.634v5.707c0 .396.571.697 1.236.697s1.141-.313
 1.141-.697V8.479c.778.105 1.54.313 2.263.618l6.987 3.17c.579.273
 1.609.761 1.609 1.538s-1.011 1.236-1.609 1.53l-6.987 3.17a8.2 8.2 0 0
 1-3.396.729 7.832 7.832 0 0 1-3.408-.729l-6.987-3.17C1.011 15.042 0
 14.574 0 13.801s1.03-1.264 1.609-1.534zm1.807 2.247c.77.396 1.683.396
 2.453 0 .682-.396.686-1.026 0-1.419a2.705 2.705 0 0 0-2.453
 0c-.68.392-.666 1.02 0 1.419zM12 7.595a3.35 3.35 0 1 1
 3.349-3.351v.003c0 1.849-1.5 3.348-3.349 3.348z" />
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
