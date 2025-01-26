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


class LangflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "langflow"

    @property
    def original_file_name(self) -> "str":
        return "langflow.svg"

    @property
    def title(self) -> "str":
        return "Langflow"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Langflow</title>
     <path d="M9.755 1.52h-.001c-.31 0-.608.124-.828.343L4.037
 6.752a1.17 1.17 0 0 1-.827.343H1.17A1.17 1.17 0 0 0 0 8.295l.052
 1.984a1.17 1.17 0 0 0 1.17 1.14h2.37c.31 0
 .607-.124.827-.344l4.93-4.93c.22-.22.517-.343.827-.343h2.874a1.17
 1.17 0 0 0 1.17-1.17V2.69a1.17 1.17 0 0 0-1.17-1.17zm9.78 2.503c-.31
 0-.608.123-.828.343l-4.889 4.889a1.17 1.17 0 0 1-.827.342h-2.756c-.31
 0-.608.124-.827.344L4.15 15.197a1.17 1.17 0 0 1-.827.343H1.32a1.17
 1.17 0 0 0-1.17 1.17v1.996c0 .646.524 1.17 1.17 1.17h2.017c.302 0
 .592-.116.81-.325l5.535-5.304a1.17 1.17 0 0 1 .81-.326h2.88c.31 0
 .607-.123.827-.342l4.93-4.93c.22-.22.517-.344.827-.344h2.873A1.17
 1.17 0 0 0 24 7.135V5.193a1.17 1.17 0 0 0-1.17-1.17h-3.294zm0
 8.559c-.31 0-.608.123-.828.343l-4.889 4.889a1.17 1.17 0 0
 1-.827.343h-2.04a1.17 1.17 0 0 0-1.17 1.2l.052 1.984a1.17 1.17 0 0 0
 1.17 1.14h2.37c.31 0
 .607-.124.827-.343l4.93-4.93c.22-.22.517-.343.827-.343h2.873a1.17
 1.17 0 0 0 1.17-1.17v-1.943a1.17 1.17 0 0 0-1.17-1.17h-3.294Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/langflow-ai/langflow/blob/
a5f5f3e3e30ee1740b696e3ad1823287ba27870c/docs/static/img/langflow-icon'''

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
