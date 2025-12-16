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


class QltyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qlty"

    @property
    def original_file_name(self) -> "str":
        return "qlty.svg"

    @property
    def title(self) -> "str":
        return "Qlty"

    @property
    def primary_color(self) -> "str":
        return "#66FAEC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qlty</title>
     <path d="M12.453 20.437h10.204V24H12.453Zm2.456-.8
 8.868-9.812L14.897 0l-2.444 2.7 6.437 7.125-6.437 7.124ZM9.102 0 .223
 9.825l8.868 9.814 2.456-2.69L5.11 9.825 11.55 2.7Z" />
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
