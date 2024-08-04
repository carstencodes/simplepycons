#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class ElloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ello"

    @property
    def original_file_name(self) -> "str":
        return "ello.svg"

    @property
    def title(self) -> "str":
        return "Ello"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ello</title>
     <path d="M12 0C5.377 0 0 5.377 0 12s5.377 12 12 12 12-5.377
 12-12S18.623 0 12 0zm6.96 13.8c-.8 3.16-3.68 5.4-6.96
 5.4s-6.16-2.24-6.96-5.4c-.08-.36.12-.76.48-.84s.76.12.84.48c.68 2.56
 3 4.36 5.64 4.36 2.64 0 4.96-1.8
 5.64-4.36.08-.36.48-.6.84-.48.36.08.6.48.48.84z" />
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
