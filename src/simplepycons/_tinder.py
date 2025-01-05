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


class TinderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tinder"

    @property
    def original_file_name(self) -> "str":
        return "tinder.svg"

    @property
    def title(self) -> "str":
        return "Tinder"

    @property
    def primary_color(self) -> "str":
        return "#FF6B6B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tinder</title>
     <path d="M9.317 9.451c.045.073.123.12.212.12.06 0
 .116-.021.158-.057l.015-.012c.39-.325.741-.66 1.071-1.017 3.209-3.483
 1.335-7.759
 1.32-7.799-.09-.21-.03-.459.15-.594.195-.135.435-.12.615.033 10.875
 10.114 7.995 17.818 7.785 18.337-.87 3.141-4.335 5.414-8.444
 5.53-.138.008-.242.008-.363.008-4.852
 0-8.977-2.989-8.977-6.807v-.06c0-5.297 4.795-10.522
 5.009-10.744.136-.149.345-.195.525-.105.18.076.297.255.291.451-.043
 1.036.167 1.935.631 2.7v.015l.002.001z" />
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
