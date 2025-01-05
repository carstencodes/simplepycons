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


class ChaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chase"

    @property
    def original_file_name(self) -> "str":
        return "chase.svg"

    @property
    def title(self) -> "str":
        return "Chase"

    @property
    def primary_color(self) -> "str":
        return "#117ACA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chase</title>
     <path d="M0 15.415c0 .468.38.85.848.85h5.937V.575L0
 7.72v7.695m15.416 8.582c.467 0 .846-.38.846-.849v-5.937H.573l7.146
 6.785h7.697M24 8.587a.844.844 0 0
 0-.847-.846h-5.938V23.43l6.782-7.148L24 8.586M8.585.003a.847.847 0 0
 0-.847.847v5.94h15.688L16.282.003H8.585Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Chase'''

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
