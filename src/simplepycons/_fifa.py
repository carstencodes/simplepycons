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


class FifaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fifa"

    @property
    def original_file_name(self) -> "str":
        return "fifa.svg"

    @property
    def title(self) -> "str":
        return "FIFA"

    @property
    def primary_color(self) -> "str":
        return "#326295"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FIFA</title>
     <path d="M0
 8.064v7.872h2.486v-2.843h1.728l.671-1.72H2.486V9.775h2.92l.637-1.711zm6.804
 0L6.8 15.936h2.457V8.064zm4.15
 0v7.872h2.484v-2.843h1.726l.677-1.72h-2.403V9.775h2.922L17
 8.064zm7.658 0l-2.83 7.872h2.375l.306-1.058h2.769l.32
 1.058H24l-2.837-7.872zm1.235 2.023l.981 3.277h-1.927z" />
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
