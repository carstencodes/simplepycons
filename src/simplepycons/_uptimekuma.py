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


class UptimeKumaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uptimekuma"

    @property
    def original_file_name(self) -> "str":
        return "uptimekuma.svg"

    @property
    def title(self) -> "str":
        return "Uptime Kuma"

    @property
    def primary_color(self) -> "str":
        return "#5CDD8B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Uptime Kuma</title>
     <path d="M11.759.955c-4.071 0-7.93 2.265-10.06
 5.774l-.16.263-.116.284c-1.81 4.44-2.188 9.118.621 12.459 2.67 3.174
 6.221 3.328 9.477 3.308 3.256-.02 6.323-.482 8.995-2.032C22.75 19.714
 24 16.917 24
 14.53c0-2.388-.724-4.698-1.882-7.343l-.112-.257-.148-.238C19.683 3.2
 15.83.955 11.758.955Zm0 3.868c2.919 0 5.19 1.305 6.816 3.914 2.076
 4.747 2.076 7.724 0 8.929-3.116 1.808-11.234
 2.359-13.57-.42-1.558-1.853-1.558-4.69 0-8.51 1.584-2.608 3.835-3.913
 6.754-3.913z" />
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
