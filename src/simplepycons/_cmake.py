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


class CmakeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cmake"

    @property
    def original_file_name(self) -> "str":
        return "cmake.svg"

    @property
    def title(self) -> "str":
        return "CMake"

    @property
    def primary_color(self) -> "str":
        return "#064F8C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CMake</title>
     <path d="M11.769.066L.067 23.206l12.76-10.843zM23.207
 23.934L7.471 17.587 0 23.934zM24 23.736L12.298.463l1.719
 19.24zM12.893 12.959l-5.025 4.298 5.62 2.248z" />
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
