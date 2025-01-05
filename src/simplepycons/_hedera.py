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


class HederaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hedera"

    @property
    def original_file_name(self) -> "str":
        return "hedera.svg"

    @property
    def title(self) -> "str":
        return "Hedera"

    @property
    def primary_color(self) -> "str":
        return "#222222"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hedera</title>
     <path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24Zm4.9571
 17.3963h-1.5812V14.01H8.6224v3.3777H7.0498V6.6037H8.631v3.3845h6.7535V6.6037h1.5812zm-1.5812-6.2592H8.6224v1.7241h6.7535Z"
 />
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
