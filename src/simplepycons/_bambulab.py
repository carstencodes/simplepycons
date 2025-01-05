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


class BambuLabIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bambulab"

    @property
    def original_file_name(self) -> "str":
        return "bambulab.svg"

    @property
    def title(self) -> "str":
        return "Bambu Lab"

    @property
    def primary_color(self) -> "str":
        return "#00AE42"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bambu Lab</title>
     <path d="M12.662 24V8.959l8.535
 3.369V24zm-9.859-.003v-7.521l8.534-3.371-.001 10.892zM2.803
 0h8.533l.001 11.672-8.534 3.369zm9.859 0h8.535v10.892l-8.535-3.371z"
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
