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


class MakeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "make"

    @property
    def original_file_name(self) -> "str":
        return "make.svg"

    @property
    def title(self) -> "str":
        return "Make"

    @property
    def primary_color(self) -> "str":
        return "#6D00CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Make</title>
     <path d="M13.38 3.498c-.27 0-.511.19-.566.465L9.85
 18.986a.578.578 0 0 0 .453.678l4.095.826a.58.58 0 0 0
 .682-.455l2.963-15.021a.578.578 0 0 0-.453-.678l-4.096-.826a.589.589
 0 0 0-.113-.012zm-5.876.098a.576.576 0 0 0-.516.318L.062
 17.697a.575.575 0 0 0 .256.774l3.733 1.877a.578.578 0 0 0
 .775-.258l6.926-13.781a.577.577 0 0 0-.256-.776L7.762 3.658a.571.571
 0 0 0-.258-.062zm11.74.115a.576.576 0 0 0-.576.576v15.426c0
 .318.258.578.576.578h4.178a.58.58 0 0 0 .578-.578V4.287a.578.578 0 0
 0-.578-.576Z" />
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
