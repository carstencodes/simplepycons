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


class PhotocrowdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "photocrowd"

    @property
    def original_file_name(self) -> "str":
        return "photocrowd.svg"

    @property
    def title(self) -> "str":
        return "Photocrowd"

    @property
    def primary_color(self) -> "str":
        return "#3DAD4B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Photocrowd</title>
     <path d="M2.182 0C.977 0 0 1.058 0 2.364v19.462C0 23.026.977 24
 2.182 24h19.636A2.179 2.179 0 0 0 24 21.826V2.364C24 1.058 23.023 0
 21.818 0zM12 3.49a1.022 1.022 0 1 1 0 2.045 1.022 1.022 0 0 1
 0-2.044zM8.326 4.498a1.022 1.022 0 1 1-.142 2.039 1.022 1.022 0 0 1
 .142-2.04zm7.347 0a1.02 1.02 0 0 1 .955 1.529 1.021 1.021 0 1
 1-.955-1.53zm-10.23 2.74a1.02 1.02 0 1 1 .145 2.037 1.02 1.02 0 0
 1-.145-2.036zm13.113 0a1.02 1.02 0 1 1-.142 2.036 1.02 1.02 0 0 1
 .142-2.035zm-7.497.116a1.021 1.021 0 1 1 .119 2.039 1.021 1.021 0 0
 1-.12-2.04zm3.687.88a1.021 1.021 0 1 1 .001 2.042 1.021 1.021 0 0 1
 0-2.043zm-6.308 1.864a1.02 1.02 0 1 1-.119 2.04 1.02 1.02 0 0 1
 .12-2.04zm3.561.88a1.023 1.023 0 1 1-.001 2.047 1.023 1.023 0 0 1
 .001-2.047zm-7.488.002a1.022 1.022 0 1 1-.001 2.044 1.022 1.022 0 0 1
 0-2.044zm14.977 0a1.02 1.02 0 1 1-.001 2.042 1.02 1.02 0 0 1
 0-2.042zm-3.793.881a1.02 1.02 0 1 1-.119 2.038 1.02 1.02 0 0 1
 .12-2.038zm-6.442 1.866a1.021 1.021 0 1 1-.001 2.042 1.021 1.021 0 0
 1 0-2.042zm3.568.883a1.02 1.02 0 1 1 .12 2.038 1.02 1.02 0 0
 1-.12-2.038zm-7.235.116a1.02 1.02 0 0 1 .44 1.904 1.022 1.022 0 1
 1-.44-1.904zm12.827 0a1.022 1.022 0 1 1 .142 2.038 1.022 1.022 0 0
 1-.142-2.038zm-10.229 2.74a1.021 1.021 0 1 1 .142 2.038 1.021 1.021 0
 0 1-.142-2.038zm7.63 0a1.02 1.02 0 0 1 .44 1.904 1.022 1.022 0 1
 1-.44-1.904zM12 18.463a1.022 1.022 0 1 1 0 2.045 1.022 1.022 0 0 1
 0-2.045z" />
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
