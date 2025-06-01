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


class UservoiceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uservoice"

    @property
    def original_file_name(self) -> "str":
        return "uservoice.svg"

    @property
    def title(self) -> "str":
        return "UserVoice"

    @property
    def primary_color(self) -> "str":
        return "#FF6720"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UserVoice</title>
     <path d="m17.449 0-3.892 2.672V16.8c0 1.34-.647 2.527-1.635
 3.253-.937-.768-1.479-1.994-1.479-3.253V16c0-.8-.778-1.6-.778-2.4
 0-.556.376-1.112.606-1.669.11-.219.172-.467.172-.73
 0-.885-.696-1.601-1.556-1.601-.86 0-1.557.716-1.557 1.6 0
 .264.063.512.173.731.23.557.606 1.113.606 1.67 0 .8-.78 1.6-.78
 2.4v.799c0 1.442.429 2.741 1.183
 3.821-1.585-.506-2.738-2.028-2.738-3.821V16c0-.8-.779-1.6-.779-2.4
 0-.556.376-1.112.605-1.669.11-.219.174-.467.174-.73
 0-.885-.698-1.601-1.558-1.601-.86 0-1.556.716-1.556 1.6 0
 .264.063.512.174.731.229.557.604 1.113.604 1.67 0 .8-.778 1.6-.778
 2.4v.799c0 3.97 3.142 7.2 7.005 7.2s7.006-3.23
 7.006-7.2V4.224l.778-.528.778.528V16.64c0 2.653-.778 5.325-3.736 7.2
 3.012 0 6.762-3.48 6.85-7.999V2.671zM4.216.96c-.86 0-1.556.717-1.556
 1.6 0 .884.696 1.6 1.556 1.6s1.557-.716
 1.557-1.6c0-.883-.697-1.6-1.557-1.6zm4.67 0c-.86 0-1.557.717-1.557
 1.6 0 .884.698 1.6 1.558 1.6.86 0 1.556-.716 1.556-1.6
 0-.883-.697-1.6-1.556-1.6zm-4.67 4.32c-.86 0-1.556.717-1.556 1.6s.696
 1.6 1.556 1.6 1.557-.716 1.557-1.6-.697-1.6-1.557-1.6zm4.67 0c-.86
 0-1.557.717-1.557 1.6s.698 1.6 1.558 1.6c.86 0 1.556-.716
 1.556-1.6s-.697-1.6-1.556-1.6z" />
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
