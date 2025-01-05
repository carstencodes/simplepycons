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


class PlatformioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "platformio"

    @property
    def original_file_name(self) -> "str":
        return "platformio.svg"

    @property
    def title(self) -> "str":
        return "PlatformIO"

    @property
    def primary_color(self) -> "str":
        return "#F5822A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlatformIO</title>
     <path d="M12 23.992c1.25.211 7.051-3.743
 9.113-8.217.253-.686.61-1.198.746-2.5.21-2.016-.41-3.912-1.59-5.419-.987-1.163-2.305-2.004-3.88-2.532l.683-2.583a1.371
 1.371 0 1 0-.76-.189L15.64 5.1c-1.109-.288-2.328-.437-3.64-.444m5.978
 11.667c-1.548 1.346-2.525 1.488-3.045
 1.467-.274-.034-.75-.558-.919-1.104-.188-.612-.28-1.282-.273-2.2-.199-2.476
 1.465-5.624 3.937-6.041 1.003-.186 2.39.493 2.889 2.088.506
 1.422-.645 4.147-2.589 5.79zM12
 4.656c-1.315.007-2.538.156-3.65.447l-.675-2.56A1.37 1.37 0 0 0 6.962
 0a1.372 1.372 0 0 0-.044 2.742L7.6 5.328c-1.57.528-2.885 1.367-3.871
 2.528-1.179 1.507-1.8 3.403-1.588 5.419.136 1.302.492 1.814.745 2.5
 2.062 4.474 7.862 8.428 9.113 8.217m-1.507-9.507c.007.92-.086
 1.589-.274 2.201-.167.546-.644 1.07-.918
 1.104-.52.021-1.498-.121-3.045-1.467-1.944-1.643-3.095-4.368-2.589-5.79.5-1.595
 1.886-2.274 2.889-2.088 2.471.417 4.136 3.565 3.937
 6.04zm6.45-2.19a1.24 1.24 0 1 0 0 2.48 1.24 1.24 0 0 0 0-2.48zm.416
 1.149a.325.325 0 1 1 0-.65.325.325 0 0 1 0 .65zM7.25 12.294a1.24 1.24
 0 1 0 0 2.48 1.24 1.24 0 0 0 0-2.48zm-.418 1.15a.325.325 0 1 1
 0-.65.325.325 0 0 1 0 .65z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://piolabs.com/legal/trademarks.html#use'''
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
