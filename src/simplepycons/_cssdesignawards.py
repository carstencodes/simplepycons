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


class CssDesignAwardsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cssdesignawards"

    @property
    def original_file_name(self) -> "str":
        return "cssdesignawards.svg"

    @property
    def title(self) -> "str":
        return "CSS Design Awards"

    @property
    def primary_color(self) -> "str":
        return "#280FEE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CSS Design Awards</title>
     <path d="m7.46.93-7.46 7.38 3.73 3.73 3.74 3.65 3.73 3.65
 3.74-3.65-7.47-7.38 7.47-7.4zm5.33 3.73-3.67 3.65 7.39 7.38-7.46
 7.4h7.46l3.76-3.66 3.73-3.73-3.73-3.65-3.74-3.73z" />
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
