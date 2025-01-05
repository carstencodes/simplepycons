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


class GoogleDataflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googledataflow"

    @property
    def original_file_name(self) -> "str":
        return "googledataflow.svg"

    @property
    def title(self) -> "str":
        return "Google Dataflow"

    @property
    def primary_color(self) -> "str":
        return "#AECBFA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Dataflow</title>
     <path d="M5.856 9.6 3.72 9.564l.036-2.46 6.312-3.516L5.94 1.14
 8.028 0l4.092 2.436h.012L16.284.108h.06l1.992 1.188-4.188 2.352 6.168
 3.684v2.46l-2.124-.036.012-1.284L13.116 5.4l-.024
 2.076-1.224-.012v-.0022l-.84-.0098.024-2.076-5.172 2.94L5.856
 9.6zm12.252 6.072-5.16 2.94.024-2.064-2.064-.024-.024
 2.064-5.1-3.072.012-1.248H3.684v2.4l6.168 3.684 2.0111
 1.1971.005.0149L15.972
 24h.06l2.028-1.14-4.128-2.448-.02.0111.008-.0231
 6.324-3.516.036-2.508-2.148-.024-.024 1.32zM5.664 22.704l1.992
 1.188h.06l4.152-2.328-2.016-1.212-4.188 2.352zm13.68-12.024c-.7555
 0-1.368.6125-1.368 1.368 0 .7555.6125 1.368 1.368 1.368.7556 0
 1.368-.6125 1.368-1.368 0-.7555-.6124-1.368-1.368-1.368zM4.656
 13.224c.7555 0 1.368-.6125 1.368-1.368
 0-.7556-.6125-1.368-1.368-1.368-.7556 0-1.368.6124-1.368 1.368 0
 .7555.6124 1.368 1.368 1.368zm7.416-5.004c-.7555 0-1.368.6125-1.368
 1.368 0 .7556.6125 1.368 1.368 1.368s1.368-.6124
 1.368-1.368c0-.7555-.6125-1.368-1.368-1.368zm-.108 4.812c-.7555
 0-1.368.6125-1.368 1.368s.6125 1.368 1.368 1.368c.7555 0 1.368-.6125
 1.368-1.368s-.6125-1.368-1.368-1.368z" />
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
