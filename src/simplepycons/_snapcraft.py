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


class SnapcraftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "snapcraft"

    @property
    def original_file_name(self) -> "str":
        return "snapcraft.svg"

    @property
    def title(self) -> "str":
        return "Snapcraft"

    @property
    def primary_color(self) -> "str":
        return "#E95420"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Snapcraft</title>
     <path d="M8.17 11.335a.106.106 0 0 0-.173.022L1.754
 23.466a.105.105 0 0 0
 .032.133c.04.029.101.027.138-.012l8.89-9.11a.107.107 0 0 0
 .005-.144l-2.649-3Zm9.76-3.519L.146.39C.041.346-.047.478.028.56l12.034
 12.874a.11.11 0 0 0 .075.034.102.102 0 0 0 .075-.03L17.96
 7.99a.106.106 0 0 0-.032-.174Zm6.047.547-2.188-4.405a.21.21 0 0
 0-.189-.117h-8.77a.212.212 0 0 0-.08.408l10.96 4.405a.211.211 0 0 0
 .268-.29z" />
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
