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


class AnycubicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "anycubic"

    @property
    def original_file_name(self) -> "str":
        return "anycubic.svg"

    @property
    def title(self) -> "str":
        return "Anycubic"

    @property
    def primary_color(self) -> "str":
        return "#476695"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Anycubic</title>
     <path d="m6.762.534 8.728 3.481 8.469
 7.449-6.494-.631L6.762.534Zm10.72 10.463 6.518.581-7.826 8.749-8.649
 3.139 9.957-12.469ZM6.592.601l10.699 10.331L7.355 23.44 0 12.465
 6.592.601Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://store.anycubic.com/pages/firmware-sof'''

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
