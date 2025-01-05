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


class SuiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sui"

    @property
    def original_file_name(self) -> "str":
        return "sui.svg"

    @property
    def title(self) -> "str":
        return "Sui"

    @property
    def primary_color(self) -> "str":
        return "#4DA2FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sui</title>
     <path d="M17.636 10.009a7.16 7.16 0 0 1 1.565 4.474 7.2 7.2 0 0
 1-1.608 4.53l-.087.106-.023-.135a7 7 0 0
 0-.07-.349c-.502-2.21-2.142-4.106-4.84-5.642-1.823-1.034-2.866-2.278-3.14-3.693-.177-.915-.046-1.834.209-2.62.254-.787.631-1.446.953-1.843l1.05-1.284a.46.46
 0 0 1 .713 0l5.28 6.456zm1.66-1.283L12.26.123a.336.336 0 0 0-.52
 0L4.704 8.726l-.023.029a9.33 9.33 0 0 0-2.07 5.872C2.612 19.803 6.816
 24 12 24s9.388-4.197 9.388-9.373a9.32 9.32 0 0 0-2.07-5.871zM6.389
 9.981l.63-.77.018.142q.023.17.055.34c.408 2.136 1.862 3.917 4.294
 5.297 2.114 1.203 3.345 2.586 3.7 4.103a5.3 5.3 0 0 1 .109
 1.801l-.004.034-.03.014A7.2 7.2 0 0 1 12 21.67c-3.976
 0-7.2-3.218-7.2-7.188 0-1.705.594-3.27 1.587-4.503z" />
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
