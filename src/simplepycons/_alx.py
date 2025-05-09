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


class AlxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alx"

    @property
    def original_file_name(self) -> "str":
        return "alx.svg"

    @property
    def title(self) -> "str":
        return "ALX"

    @property
    def primary_color(self) -> "str":
        return "#002B56"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ALX</title>
     <path d="m13.732 5.879-2.903 1.299V18.12h2.903V5.879Zm3.219
 1.436c-.361.36-1.59 1.587-1.977 1.978.839.851 1.684 1.696 2.527
 2.543l-2.529 2.529 1.978 1.978c.844-.842 1.686-1.686
 2.529-2.529l2.543 2.529c.66-.659 1.319-1.319
 1.978-1.98-.848-.841-1.695-1.684-2.543-2.527L24
 9.293l-1.978-1.978-2.543 2.543-2.528-2.543ZM6.157 9.271v.382C3.256
 8.379.002 10.503 0 13.671c.001 3.169 3.256 5.293 6.157
 4.018v.431H9.06V9.271H6.157ZM4.39 11.902c.978 0 1.718.741 1.767
 1.674v.19a1.77 1.77 0 0 1-1.767 1.675c-.946
 0-1.77-.792-1.77-1.77s.792-1.77 1.77-1.77v.001Z" />
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
