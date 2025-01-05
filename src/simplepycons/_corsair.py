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


class CorsairIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "corsair"

    @property
    def original_file_name(self) -> "str":
        return "corsair.svg"

    @property
    def title(self) -> "str":
        return "Corsair"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Corsair</title>
     <path d="M13.072.412s1.913 3.881 1.563 5.5c0 0 4.987 1.612 5.54
 4.272 0 0 2.73-3.594-7.103-9.772zM7.908 4.067s1.678 2.625 1.417
 4.35l2.818 1.067a17.56 17.56 0 0 0-.991-3.248zm3.784.691a14.162
 14.162 0 0 1 .163 13.794 17.702 17.702 0 0 0
 .594-6.585c-.017-.186-.031-.368-.053-.55L6.908 7.759a14.13 14.13 0 0
 1 1.133 4.465 14.02 14.02 0 0 1-1.305 7.347 17.75 17.75 0 0 0
 .442-5.988.92.92 0 0 1-.022-.243l-5.133-2.726a11.639 11.639 0 0 1
 1.075 3.93A11.785 11.785 0 0 1 0 23.587c21.91-9.29 22.795-3.173
 22.795-3.173s1.656-2.164 1.085-4.51C23.128 12.79 11.692 4.759 11.692
 4.759zM3.04 7.245s1.629 2.09 1.363 3.815l2.567.637a20.357 20.357 0 0
 0-.863-2.788z" />
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
