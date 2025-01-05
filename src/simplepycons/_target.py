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


class TargetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "target"

    @property
    def original_file_name(self) -> "str":
        return "target.svg"

    @property
    def title(self) -> "str":
        return "Target"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Target</title>
     <path d="M12.0005 0C18.627 0 24 5.373 24 12.0005 24 18.627 18.627
 24 11.9995 24 5.373 24 0 18.627 0 11.9995 0 5.373 5.373 0 12.0005
 0zm0 19.826a7.8265 7.8265 0 10-.001-15.652C7.7133 4.2246 4.2653
 7.7136 4.2653 12c0 4.2864 3.448 7.7754 7.7342
 7.826h.001zm0-3.9853a3.8402 3.8402 0 110-7.6803c2.1204.0006 3.839
 1.7197 3.839 3.8401s-1.7186 3.8396-3.839 3.8402z" />
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
