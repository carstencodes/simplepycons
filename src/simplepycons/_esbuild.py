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


class EsbuildIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "esbuild"

    @property
    def original_file_name(self) -> "str":
        return "esbuild.svg"

    @property
    def title(self) -> "str":
        return "esbuild"

    @property
    def primary_color(self) -> "str":
        return "#FFCF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>esbuild</title>
     <path d="M12 0A12 12 0 000 12a12 12 0 0012 12 12 12 0 0012-12A12
 12 0 0012 0zM6.718 5.282L13.436 12l-6.718 6.718-2.036-2.036L9.364 12
 4.682 7.318zm7.2 0L20.636 12l-6.718 6.718-2.036-2.036L16.564
 12l-4.682-4.682z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/evanw/esbuild/blob/ac542f9'''

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
