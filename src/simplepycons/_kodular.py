#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class KodularIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kodular"

    @property
    def original_file_name(self) -> "str":
        return "kodular.svg"

    @property
    def title(self) -> "str":
        return "Kodular"

    @property
    def primary_color(self) -> "str":
        return "#4527A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kodular</title>
     <path d="M3.612 0a5.6 5.6 0 0 1 5.6 5.6v4.934l2.44-2.44a4.48 4.48
 0 0 1 6.336 0l-6.095 6.096 8.495 8.495a4.48 4.48 0 0 1-6.336
 0l-4.84-4.84V24a5.6 5.6 0 0 1-5.6-5.6Z" />
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
