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


class KlarnaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "klarna"

    @property
    def original_file_name(self) -> "str":
        return "klarna.svg"

    @property
    def title(self) -> "str":
        return "Klarna"

    @property
    def primary_color(self) -> "str":
        return "#FFB3C7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Klarna</title>
     <path d="M4.592 2v20H0V2h4.592zm11.46 0c0 4.194-1.583 8.105-4.415
 11.068l-.278.283L17.702 22h-5.668l-6.893-9.4 1.779-1.332c2.858-2.14
 4.535-5.378 4.637-8.924L11.562 2h4.49zM21.5 17a2.5 2.5 0 110 5 2.5
 2.5 0 010-5z" />
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
