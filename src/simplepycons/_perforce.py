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


class PerforceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "perforce"

    @property
    def original_file_name(self) -> "str":
        return "perforce.svg"

    @property
    def title(self) -> "str":
        return "Perforce"

    @property
    def primary_color(self) -> "str":
        return "#4C00FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Perforce</title>
     <path d="m7.386 14.957 2.279-1.316-.576-.333A1.48 1.48 0 0 1
 8.334 12c0-.262.073-.915.755-1.308l10.31-5.953a1.49 1.49 0 0 1 1.51
 0c.228.13.755.52.755 1.308v11.906c0 .788-.527 1.178-.754
 1.308s-.828.393-1.51 0l-2.732-1.577-2.334 1.348 3.899 2.251a3.81 3.81
 0 0 0 3.845 0A3.81 3.81 0 0 0 24 17.953V6.047a3.81 3.81 0 0
 0-1.922-3.33 3.83 3.83 0 0 0-1.923-.52c-.66 0-1.32.173-1.922.52L7.923
 8.67A3.81 3.81 0 0 0 6 12c0 1.17.51 2.234 1.386
 2.956zm9.228-5.913-2.279 1.316.576.333c.682.393.755 1.046.755 1.308 0
 .263-.073.915-.755 1.308l-10.31 5.954a1.49 1.49 0 0 1-1.51 0 1.48
 1.48 0 0 1-.755-1.308V6.047c0-.788.527-1.178.754-1.308s.828-.393 1.51
 0l2.732 1.577 2.334-1.348-3.899-2.251a3.81 3.81 0 0 0-3.845 0A3.81
 3.81 0 0 0 0 6.047v11.906c0 1.39.72 2.635 1.922 3.33a3.83 3.83 0 0 0
 1.923.52c.66 0 1.32-.173 1.922-.52l10.31-5.953A3.81 3.81 0 0 0 18
 12c0-1.17-.51-2.234-1.386-2.956" />
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
