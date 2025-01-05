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


class DiagramsdotnetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "diagramsdotnet"

    @property
    def original_file_name(self) -> "str":
        return "diagramsdotnet.svg"

    @property
    def title(self) -> "str":
        return "diagrams.net"

    @property
    def primary_color(self) -> "str":
        return "#F08705"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>diagrams.net</title>
     <path d="M19.69 13.419h-2.527l-2.667-4.555a1.292 1.292 0
 001.035-1.28V4.16c0-.725-.576-1.312-1.302-1.312H9.771c-.726
 0-1.312.576-1.312 1.301v3.435c0 .619.426 1.152 1.034 1.28l-2.666
 4.555H4.309c-.725 0-1.312.576-1.312 1.301v3.435c0 .725.576 1.312
 1.302 1.312h4.458c.726 0 1.312-.576
 1.312-1.302v-3.434c0-.726-.576-1.312-1.301-1.312h-.437l2.645-4.523h2.059l2.656
 4.523h-.438c-.725 0-1.312.576-1.312 1.301v3.435c0 .725.576 1.312
 1.302 1.312H19.7c.726 0 1.312-.576
 1.312-1.302v-3.434c0-.726-.576-1.312-1.301-1.312zM24 22.976c0
 .565-.459 1.024-1.013 1.024H1.024A1.022 1.022 0 010 22.987V1.024C0
 .459.459 0 1.013 0h21.963C23.541 0 24 .459 24 1.013z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jgraph/drawio/blob/4743eba'''

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
        yield from [
            "draw.io",
        ]
