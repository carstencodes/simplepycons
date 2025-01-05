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


class ReasonStudiosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reasonstudios"

    @property
    def original_file_name(self) -> "str":
        return "reasonstudios.svg"

    @property
    def title(self) -> "str":
        return "Reason Studios"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Reason Studios</title>
     <path d="M2.49 5.114l8.3-4.79a2.421 2.421 0 012.39-.017l.03.017
 8.299 4.79c.74.427 1.2 1.212 1.211 2.065V16.79c0 .854-.451
 1.645-1.184 2.08l-.027.016-8.299 4.79a2.42 2.42 0
 01-2.39.017l-.03-.017-8.3-4.79a2.421 2.421 0
 01-1.21-2.065V7.21c0-.855.45-1.645 1.184-2.08l.026-.016 8.3-4.79zM12
 4.026L5.092 8.013v7.974L12 19.974V12l6.908-3.987z" />
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
