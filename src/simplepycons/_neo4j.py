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


class NeoFourJIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "neo4j"

    @property
    def original_file_name(self) -> "str":
        return "neo4j.svg"

    @property
    def title(self) -> "str":
        return "Neo4j"

    @property
    def primary_color(self) -> "str":
        return "#4581C3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Neo4j</title>
     <path d="M9.629 13.227c-.593 0-1.139.2-1.58.533l-2.892-1.976a2.61
 2.61 0 0 0 .101-.711 2.633 2.633 0 0 0-2.629-2.629A2.632 2.632 0 0 0
 0 11.073a2.632 2.632 0 0 0 2.629 2.629c.593 0 1.139-.2 1.579-.533L7.1
 15.145c-.063.226-.1.465-.1.711 0 .247.037.484.1.711l-2.892
 1.976a2.608 2.608 0 0 0-1.579-.533A2.632 2.632 0 0 0 0 20.639a2.632
 2.632 0 0 0 2.629 2.629 2.632 2.632 0 0 0
 2.629-2.629c0-.247-.037-.485-.101-.711l2.892-1.976c.441.333.987.533
 1.58.533a2.633 2.633 0 0 0
 2.629-2.629c0-1.45-1.18-2.629-2.629-2.629ZM16.112.732c-4.72 0-7.888
 2.748-7.888 8.082v3.802a3.525 3.525 0 0 1 3.071.008v-3.81c0-3.459
 1.907-5.237 4.817-5.237s4.817 1.778 4.817 5.237v8.309H24V8.814C24
 3.448 20.832.732 16.112.732Z" />
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
