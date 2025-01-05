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


class TrelloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trello"

    @property
    def original_file_name(self) -> "str":
        return "trello.svg"

    @property
    def title(self) -> "str":
        return "Trello"

    @property
    def primary_color(self) -> "str":
        return "#0052CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trello</title>
     <path d="M21.147 0H2.853A2.86 2.86 0 000 2.853v18.294A2.86 2.86 0
 002.853 24h18.294A2.86 2.86 0 0024 21.147V2.853A2.86 2.86 0 0021.147
 0zM10.34 17.287a.953.953 0 01-.953.953h-4a.954.954 0
 01-.954-.953V5.38a.953.953 0 01.954-.953h4a.954.954 0
 01.953.953zm9.233-5.467a.944.944 0 01-.953.947h-4a.947.947 0
 01-.953-.947V5.38a.953.953 0 01.953-.953h4a.954.954 0 01.953.953z" />
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
