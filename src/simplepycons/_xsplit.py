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


class XsplitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xsplit"

    @property
    def original_file_name(self) -> "str":
        return "xsplit.svg"

    @property
    def title(self) -> "str":
        return "XSplit"

    @property
    def primary_color(self) -> "str":
        return "#0095DE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>XSplit</title>
     <path d="M24 19.5c-.7-.1-2.5-.3-2.7-.3-.1 0-2.8 2.3-4
 3.399l-.1.101c.1-1.3.3-2.601.399-3.9C11.7 18.1 5.9 17.4 0
 16.7V1.5v-.2H.3C.9 1.4 22.9 3.9 24 4v15.5zm-2.6-2.6V6.2C15.1 5.5 8.7
 4.7 2.4 4v10.6c6.3.8 12.7 1.5 19 2.3z" />
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
