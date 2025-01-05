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


class AirtelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airtel"

    @property
    def original_file_name(self) -> "str":
        return "airtel.svg"

    @property
    def title(self) -> "str":
        return "Airtel"

    @property
    def primary_color(self) -> "str":
        return "#E40000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Airtel</title>
     <path d="M7.137 23.862c.79 0 1.708-.19 2.751-.554 1.55-.538
 2.784-1.281 3.986-2.009l.316-.205a29.733 29.733 0 0 0 3.764-2.72
 16.574 16.574 0 0 0 5.457-7.529c.395-1.138.949-3.384.268-5.487a7.117
 7.117 0 0 0-2.862-3.749c-.158-.126-1.898-1.47-5.203-1.47-3.005 0-6.31
 1.107-9.806 3.32l-.11.08-.317.205a20.133 20.133 0 0 0-2.309
 1.693C1.585 6.813-.091 9.106.004 11.067c.031.79.427 1.534 1.075
 2.008a3.472 3.472 0 0 0 2.214.68c1.803 0 3.765-.948
 5.109-1.74l.253-.157.696-.443.237-.158c1.898-1.234 3.875-2.515
 6.105-3.258a5.255 5.255 0 0 1 1.55-.285 3.163 3.163 0 0 1 .664.08
 2.112 2.112 0 0 1 1.47 1.106c.523 1.012.396 2.61-.316 4.08a17.871
 17.871 0 0 1-4.887 5.836 19.488 19.488 0 0 1-3.194
 2.215l-.095.031a9.634 9.634 0 0
 1-1.471.696l-.08.032-.41.158c-2.23.57-.87-1.329-.87-1.329.474-.537.98-1.028
 1.518-1.502.316-.269.633-.554.933-.854l.064-.063c.395-.38.933-.902.901-1.645-.047-.98-1.075-1.582-2.056-1.613h-.063c-.95
 0-1.819.522-2.404.98a7.27 7.27 0 0 0-1.598 1.74c-.6.901-1.85
 3.226-.632 5.077.49.743 1.313 1.123 2.42 1.123z" />
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
