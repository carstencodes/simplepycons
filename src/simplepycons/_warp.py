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


class WarpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "warp"

    @property
    def original_file_name(self) -> "str":
        return "warp.svg"

    @property
    def title(self) -> "str":
        return "Warp"

    @property
    def primary_color(self) -> "str":
        return "#01A4FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Warp</title>
     <path d="M12.035 2.723h9.253A2.712 2.712 0 0 1 24
 5.435v10.529a2.712 2.712 0 0 1-2.712 2.713H8.047Zm-1.681 2.6L6.766
 19.677h5.598l-.399 1.6H2.712A2.712 2.712 0 0 1 0 18.565V8.036a2.712
 2.712 0 0 1 2.712-2.712Z" />
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
