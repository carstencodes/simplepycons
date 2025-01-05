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


class SourcetreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sourcetree"

    @property
    def original_file_name(self) -> "str":
        return "sourcetree.svg"

    @property
    def title(self) -> "str":
        return "Sourcetree"

    @property
    def primary_color(self) -> "str":
        return "#0052CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sourcetree</title>
     <path d="M11.999 0C6.756 0 2.474 4.245 2.474 9.525c0 4.21 2.769
 7.792 6.572 9.047v4.764c0 .37.295.664.664.664h4.506a.661.661 0 0 0
 .664-.664v-4.764c.025-.008.049-.019.074-.027v.064c3.694-1.22
 6.412-4.634
 6.565-8.687.005-.124.007-.25.007-.375v-.022c0-.152-.006-.304-.013-.455C21.275
 4.037 17.125 0 11.999 0Zm0 6.352a3.214 3.214 0 0 1 2.664
 5.005v.002A3.218 3.218 0 0 1 12 12.775a3.212 3.212 0 0 1 0-6.424z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://atlassian.design/resources/logo-libra'''

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
