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


class DocsdotrsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "docsdotrs"

    @property
    def original_file_name(self) -> "str":
        return "docsdotrs.svg"

    @property
    def title(self) -> "str":
        return "Docs.rs"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Docs.rs</title>
     <path d="m22.903 11.728-4.528-1.697V4.945a1.69 1.69 0 0
 0-1.097-1.58l-4.687-1.757a1.668 1.668 0 0 0-1.186 0L6.717 3.366a1.687
 1.687 0 0 0-1.097 1.58v5.085l-4.528 1.697A1.69 1.69 0 0 0 0
 13.308v5.16c0 .638.36 1.224.933 1.51l4.687 2.344a1.68 1.68 0 0 0 1.51
 0L12 19.884l4.87 2.438a1.68 1.68 0 0 0 1.51 0l4.687-2.344a1.69 1.69 0
 0 0 .933-1.51v-5.16c0-.703-.436-1.331-1.097-1.58zm-6.122-1.66-3.984
 1.496V8.367l3.984-1.734zM7.22 4.88 12 3.09l4.781 1.79v.028L12
 6.848l-4.781-1.94Zm3.937 13.645-3.984
 1.992V16.81l3.984-1.818zm0-5.25-4.781
 1.94-4.781-1.94v-.028l4.781-1.79 4.781 1.79zm11.25 5.25-3.984
 1.992V16.81l3.984-1.818zm0-5.25-4.781
 1.94-4.781-1.94v-.028l4.781-1.79 4.781 1.79z" />
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
