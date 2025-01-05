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


class SwrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "swr"

    @property
    def original_file_name(self) -> "str":
        return "swr.svg"

    @property
    def title(self) -> "str":
        return "SWR"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SWR</title>
     <path d="M0 12.187a2.659 2.659 0 0 0 2.648 2.647 2.662 2.662 0 0
 0 2.647-2.646v-.376a1.097 1.097 0 0 1 1.092-1.086c.326 0
 .636.147.844.399h1.712a2.66 2.66 0 0 0-2.558-1.959 2.664 2.664 0 0
 0-2.647 2.647v.374c0 .598-.493 1.09-1.091 1.09a1.096 1.096 0 0
 1-1.09-1.09.314.314 0 0 0-.312-.312H.311a.313.313 0 0
 0-.311.312Zm10.131 2.647a2.664 2.664 0 0 1-2.555-1.96h1.71a1.088
 1.088 0 0 0 1.935-.683v-.379a2.663 2.663 0 0 1 2.648-2.646 2.65 2.65
 0 0 1 2.647 2.591l.008.43a1.097 1.097 0 0 0 1.092 1.086c.326 0
 .636-.146.843-.399h1.712a2.657 2.657 0 0 1-2.556 1.96 2.66 2.66 0 0
 1-2.648-2.646l-.008-.389v-.017a1.096 1.096 0 0 0-1.09-1.059 1.096
 1.096 0 0 0-1.09 1.09v.374a2.663 2.663 0 0 1-2.648
 2.647Zm10.376-3.708a1.09 1.09 0 0 1 1.936.683v.004c0
 .171.14.312.311.312h.935a.313.313 0 0 0 .311-.312 2.663 2.663 0 0
 0-2.648-2.647 2.659 2.659 0 0 0-2.557 1.96h1.712Z" />
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
