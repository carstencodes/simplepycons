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


class SteemitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "steemit"

    @property
    def original_file_name(self) -> "str":
        return "steemit.svg"

    @property
    def title(self) -> "str":
        return "Steemit"

    @property
    def primary_color(self) -> "str":
        return "#06D6A9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Steemit</title>
     <path d="M20.982 7.246c-1-1-2.163-1.73-3.4-2.202.721-2.12
 3.277-2.892 3.277-2.892S14.895-.944 8.31.29C6.114.64 4.008 1.988
 2.468 3.768a9.152 9.152 0 0 0 .991 12.984c.598.512 1.934 1.308 1.958
 1.349-.876 2.226-3.678 2.835-3.678 2.835s3.703 2.316 8.676
 2.917c1.319.163 2.72.204 4.17.05 2.302-.188 4.596-1.406
 6.34-3.12a9.525 9.525 0 0 0 .058-13.538zm-1.704 12.058c-1.41
 1.382-3.515 2.26-5.137
 2.381-1.147.114-2.376.13-3.555-.016-1.737-.212-2.99-.69-4.22-1.154.623-.601
 1.246-1.43 1.5-2.145a1.652 1.652 0 0 0-.05-1.308 6.995 6.995 0 0 1
 1.426-8.077 7.196 7.196 0 0 1 5.931-1.99 7.142 7.142 0 0 1 4.228
 2.047c2.785 2.795 2.687 7.524-.123 10.262z" />
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
