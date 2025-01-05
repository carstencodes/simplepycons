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


class HtmlFiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "html5"

    @property
    def original_file_name(self) -> "str":
        return "html5.svg"

    @property
    def title(self) -> "str":
        return "HTML5"

    @property
    def primary_color(self) -> "str":
        return "#E34F26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HTML5</title>
     <path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.564-2.438L1.5
 0zm7.031 9.75l-.232-2.718 10.059.003.23-2.622L5.412 4.41l.698
 8.01h9.126l-.326 3.426-2.91.804-2.955-.81-.188-2.11H6.248l.33
 4.171L12 19.351l5.379-1.443.744-8.157H8.531z" />
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
