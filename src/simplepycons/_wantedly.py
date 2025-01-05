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


class WantedlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wantedly"

    @property
    def original_file_name(self) -> "str":
        return "wantedly.svg"

    @property
    def title(self) -> "str":
        return "Wantedly"

    @property
    def primary_color(self) -> "str":
        return "#21BDDB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wantedly</title>
     <path d="M18.453 14.555c-.171-.111-.658-.764-2.006-3.982a9.192
 9.192 0 0 0-.237-.526l-.274-.664-2.362-5.702H8.85l2.362 5.702 2.362
 5.706 2.181 5.267a.196.196 0 0 0 .362 0l2.373-5.682a.1.1 0 0
 0-.037-.119zm-8.85 0c-.171-.111-.658-.764-2.006-3.982a8.971 8.971 0 0
 0-.236-.525l-.276-.665-2.36-5.702H0l2.362 5.702 2.362 5.706 2.181
 5.267a.196.196 0 0 0 .362 0l2.374-5.682a.098.098 0 0 0-.038-.119ZM24
 6.375a2.851 2.851 0 0 1-2.851 2.852 2.851 2.851 0 0 1-2.852-2.852
 2.851 2.851 0 0 1 2.852-2.851A2.851 2.851 0 0 1 24 6.375Z" />
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
