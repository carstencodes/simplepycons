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


class CloudflareWorkersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudflareworkers"

    @property
    def original_file_name(self) -> "str":
        return "cloudflareworkers.svg"

    @property
    def title(self) -> "str":
        return "Cloudflare Workers"

    @property
    def primary_color(self) -> "str":
        return "#F38020"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudflare Workers</title>
     <path d="m8.213.063 8.879 12.136-8.67
 11.739h2.476l8.665-11.735-8.89-12.14Zm4.728 0 9.02 11.992-9.018
 11.883h2.496L24 12.656v-1.199L15.434.063ZM7.178 2.02.01 11.398l-.01
 1.2 7.203 9.644 1.238-1.676-6.396-8.556 6.361-8.313Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.cloudflare.com/developer-platform'''

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
