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


class ThumbtackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thumbtack"

    @property
    def original_file_name(self) -> "str":
        return "thumbtack.svg"

    @property
    def title(self) -> "str":
        return "Thumbtack"

    @property
    def primary_color(self) -> "str":
        return "#009FD9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thumbtack</title>
     <path d="M6.18 6.38h11.69v2.68H6.17zm7.27 3.8v3.14c0 3.23-.02
 3.74-.14 4.36a7.95 7.95 0 0 1-1.3 2.87c-.03
 0-.78-1.35-.9-1.62-.17-.4-.3-.8-.4-1.25l-.09-.41-.02-5.78.16-.2a3.3
 3.3 0 0 1 2.44-1.1zM12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0
 0 12-12A12 12 0 0 0 12 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.thumbtack.com/press/media-resourc'''

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
