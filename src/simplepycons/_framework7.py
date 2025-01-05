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


class FrameworkSevenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "framework7"

    @property
    def original_file_name(self) -> "str":
        return "framework7.svg"

    @property
    def title(self) -> "str":
        return "Framework7"

    @property
    def primary_color(self) -> "str":
        return "#EE350F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Framework7</title>
     <path d="M0 12a11.95 11.95 0 012.713-7.6h18.574L8.037 23.33C3.358
 21.694 0 17.24 0 12zm22.271-6.208A11.944 11.944 0 0124 12c0
 6.627-5.373 12-12 12-.794 0-1.57-.077-2.32-.224zM4.295 2.8A11.952
 11.952 0 0112 0c2.933 0 5.62 1.052 7.705 2.8z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/framework7io/framework7-we'''

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
