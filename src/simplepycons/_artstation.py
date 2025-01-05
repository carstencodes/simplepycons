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


class ArtstationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "artstation"

    @property
    def original_file_name(self) -> "str":
        return "artstation.svg"

    @property
    def title(self) -> "str":
        return "ArtStation"

    @property
    def primary_color(self) -> "str":
        return "#13AFF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ArtStation</title>
     <path d="M0 17.723l2.027 3.505h.001a2.424 2.424 0 0 0 2.164
 1.333h13.457l-2.792-4.838H0zm24
 .025c0-.484-.143-.935-.388-1.314L15.728 2.728a2.424 2.424 0 0
 0-2.142-1.289H9.419L21.598
 22.54l1.92-3.325c.378-.637.482-.919.482-1.467zm-11.129-3.462L7.428
 4.858l-5.444 9.428h10.887z" />
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
