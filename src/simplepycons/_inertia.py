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


class InertiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "inertia"

    @property
    def original_file_name(self) -> "str":
        return "inertia.svg"

    @property
    def title(self) -> "str":
        return "Inertia"

    @property
    def primary_color(self) -> "str":
        return "#9553E9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Inertia</title>
     <path d="M6.901 5.331H0L6.669 12 0 18.669h6.901L13.571 12 6.9
 5.331zm10.43 0H10.43L17.099 12l-6.67 6.669h6.902L24 12l-6.669-6.669z"
 />
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
